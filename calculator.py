import tkinter as tk

def press_key(key):
    if key == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif key == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, key)

# Create main window
app = tk.Tk()
app.title("Compact Calculator")

# Set window size dynamically
button_width = 60  # Width of each button in pixels
button_height = 40  # Height of each button in pixels
app.geometry(f"{button_width * 4 + 20}x{button_height * 5 + 40}")

# Entry widget
entry = tk.Entry(app, font=("Arial", 16), borderwidth=2, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

# Button labels
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

# Add buttons to the grid
for idx, button in enumerate(buttons):
    row, col = divmod(idx, 4)
    tk.Button(
        app,
        text=button,
        font=("Arial", 14),
        command=lambda b=button: press_key(b)
    ).grid(row=row + 1, column=col, sticky="nsew", padx=2, pady=2)

# Adjust row and column weights for even resizing
for i in range(4):
    app.grid_columnconfigure(i, weight=1)
for i in range(5):
    app.grid_rowconfigure(i, weight=1)

# Run the application
app.mainloop()
