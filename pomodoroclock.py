import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class PomodoroClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Clock with AI Avatar")

        # Default time intervals (in seconds)
        self.work_time = 25 * 60  # 25 minutes
        self.short_break = 5 * 60  # 5 minutes
        self.long_break = 15 * 60  # 15 minutes
        self.current_time = self.work_time
        self.cycles_completed = 0
        self.running = False

        # Load avatar image
        self.avatar_image = Image.open("C:\\Users\\Shreya\\Desktop\\avatar.png")
        self.avatar_image = self.avatar_image.resize((100, 100), Image.ANTIALIAS)
        self.avatar_photo = ImageTk.PhotoImage(self.avatar_image)

        # UI Elements
        self.canvas = tk.Canvas(root, width=300, height=300, bg="white")
        self.canvas.pack()

        self.avatar_label = tk.Label(root, image=self.avatar_photo, bg="white")
        self.avatar_label.pack()

        self.message_label = tk.Label(root, text="Let's get to work!", font=("Helvetica", 14), bg="white")
        self.message_label.pack()

        self.time_label = tk.Label(root, text="25:00", font=("Helvetica", 24))
        self.time_label.pack()

        self.start_button = tk.Button(root, text="Start", command=self.start_timer)
        self.start_button.pack()

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_timer)
        self.reset_button.pack()

        self.customize_button = tk.Button(root, text="Customize Time", command=self.customize_intervals)
        self.customize_button.pack()

        self.draw_clock()

    def draw_clock(self):
        self.canvas.delete("all")

        # Draw clock face
        self.canvas.create_oval(50, 50, 250, 250, fill="#F5F5F5", outline="#333")
        for i in range(12):
            angle = math.radians(i * 30)
            x1 = 150 + 90 * math.sin(angle)
            y1 = 150 - 90 * math.cos(angle)
            x2 = 150 + 100 * math.sin(angle)
            y2 = 150 - 100 * math.cos(angle)
            self.canvas.create_line(x1, y1, x2, y2, fill="black", width=2)

        # Calculate hand positions
        minutes_remaining = self.current_time // 60
        seconds_remaining = self.current_time % 60

        # Minute hand
        minute_angle = math.radians((minutes_remaining % 60) * 6 - 90)
        minute_x = 150 + 80 * math.cos(minute_angle)
        minute_y = 150 + 80 * math.sin(minute_angle)
        self.canvas.create_line(150, 150, minute_x, minute_y, fill="blue", width=4)

        # Second hand
        second_angle = math.radians(seconds_remaining * 6 - 90)
        second_x = 150 + 90 * math.cos(second_angle)
        second_y = 150 + 90 * math.sin(second_angle)
        self.canvas.create_line(150, 150, second_x, second_y, fill="red", width=2)

        # Center
        self.canvas.create_oval(145, 145, 155, 155, fill="black")

    def update_timer(self):
        if self.running and self.current_time > 0:
            self.current_time -= 1
            minutes, seconds = divmod(self.current_time, 60)
            self.time_label.config(text=f"{minutes:02}:{seconds:02}")
            self.update_avatar_message()
            self.draw_clock()
            self.root.after(1000, self.update_timer)
        elif self.current_time == 0:
            self.running = False
            self.cycles_completed += 1
            messagebox.showinfo(
                "Time's up!",
                "Time to take a break!" if self.cycles_completed % 4 else "Long break!",
            )
            self.start_next_session()

    def update_avatar_message(self):
        if self.current_time > 0:
            self.message_label.config(text="Keep going! You're doing great!")
        else:
            self.message_label.config(text="Time's up! Take a break!")

    def start_timer(self):
        if not self.running:
            self.running = True
            self.update_timer()

    def reset_timer(self):
        self.running = False
        self.current_time = self.work_time
        self.time_label.config(text="25:00")
        self.message_label.config(text="Let's get to work!")
        self.draw_clock()

    def start_next_session(self):
        if self.cycles_completed % 4 == 0:
            self.current_time = self.long_break
            self.message_label.config(text="Take a long break!")
        elif self.cycles_completed % 2 == 0:
            self.current_time = self.work_time
            self.message_label.config(text="Time to get back to work!")
        else:
            self.current_time = self.short_break
            self.message_label.config(text="Take a short break!")
        self.update_timer()

    def customize_intervals(self):
        customize_window = tk.Toplevel(self.root)
        customize_window.title("Customize Intervals")

        tk.Label(customize_window, text="Work Time (minutes):").grid(row=0, column=0)
        work_entry = tk.Entry(customize_window)
        work_entry.grid(row=0, column=1)

        tk.Label(customize_window, text="Short Break (minutes):").grid(row=1, column=0)
        short_entry = tk.Entry(customize_window)
        short_entry.grid(row=1, column=1)

        tk.Label(customize_window, text="Long Break (minutes):").grid(row=2, column=0)
        long_entry = tk.Entry(customize_window)
        long_entry.grid(row=2, column=1)

        def save_intervals():
            try:
                self.work_time = int(work_entry.get()) * 60
                self.short_break = int(short_entry.get()) * 60
                self.long_break = int(long_entry.get()) * 60
                self.reset_timer()
                customize_window.destroy()
            except ValueError:
                messagebox.showerror("Invalid input", "Please enter valid numbers.")

        tk.Button(customize_window, text="Save", command=save_intervals).grid(row=3, column=0, columnspan=2)

# Run the app
root = tk.Tk()
app = PomodoroClock(root)
root.mainloop()
