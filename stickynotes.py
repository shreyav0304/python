import tkinter as tk
from tkinter import colorchooser, font
import os
import json

# Directory to save notes
NOTES_DIR = "sticky_notes"
if not os.path.exists(NOTES_DIR):
    os.makedirs(NOTES_DIR)

# Predefined color palette
COLOR_PALETTE = ["lightyellow", "lightblue", "lightgreen", "lightpink", "lavender", "lightgray", "peachpuff"]

# Function to save the content of a note
def save_note(note_id, content, color, position):
    note_data = {
        "content": content,
        "color": color,
        "position": position
    }
    with open(os.path.join(NOTES_DIR, f"note_{note_id}.json"), "w") as f:
        json.dump(note_data, f)

# Function to load existing notes
def load_notes():
    for filename in os.listdir(NOTES_DIR):
        if filename.endswith(".json"):
            note_id = int(filename.split("_")[1].split(".")[0])
            with open(os.path.join(NOTES_DIR, filename), "r") as f:
                note_data = json.load(f)
            create_note(note_id, note_data["content"], note_data["color"], note_data["position"])

# Function to create a new sticky note
def create_note(note_id=None, content="", color="lightyellow", position=None):
    # Generate a unique note ID if not provided
    if note_id is None:
        note_id = max(notes.keys(), default=0) + 1

    # Create a new note window
    note = tk.Toplevel()
    note.geometry("200x200")
    note.title(f"Sticky Note {note_id}")
    note.config(bg=color)

    if position:
        note.geometry(f"+{position[0]}+{position[1]}")

    # Enable dragging of the note
    def start_drag(event):
        note.x = event.x
        note.y = event.y

    def drag(event):
        x = note.winfo_x() + event.x - note.x
        y = note.winfo_y() + event.y - note.y
        note.geometry(f"+{x}+{y}")

    note.bind("<Button-1>", start_drag)
    note.bind("<B1-Motion>", drag)

    # Add a text widget for note content
    text = tk.Text(note, wrap=tk.WORD, font=("Arial", 12), bg=color)
    text.insert(tk.END, content)
    text.pack(expand=True, fill=tk.BOTH)

    # Add a color picker button
    def change_color():
        # Create a small color palette window
        palette_window = tk.Toplevel(note)
        palette_window.title("Choose a Color")
        palette_window.geometry("250x100")
        palette_window.resizable(False, False)

        # Add buttons for each predefined color
        for c in COLOR_PALETTE:
            tk.Button(
                palette_window, 
                bg=c, 
                width=4, 
                height=2, 
                command=lambda col=c: apply_color(col)
            ).pack(side=tk.LEFT, padx=5, pady=5)

        # Apply the selected color
        def apply_color(selected_color):
            text.config(bg=selected_color)
            note.config(bg=selected_color)
            notes[note_id]["color"] = selected_color
            palette_window.destroy()

    color_btn = tk.Button(note, text="Color", command=change_color, font=("Arial", 10))
    color_btn.pack(side=tk.LEFT, padx=5, pady=5)

    # Add a font size button
    def change_font_size():
        size_window = tk.Toplevel(note)
        size_window.title("Font Size")
        size_window.geometry("200x100")
        size_window.resizable(False, False)

        tk.Label(size_window, text="Font Size:").pack(pady=5)
        size_entry = tk.Entry(size_window)
        size_entry.pack(pady=5)

        def apply_size():
            try:
                new_size = int(size_entry.get())
                text.config(font=("Arial", new_size))
                size_window.destroy()
            except ValueError:
                pass

        tk.Button(size_window, text="Apply", command=apply_size).pack(pady=5)

    font_btn = tk.Button(note, text="Font Size", command=change_font_size, font=("Arial", 10))
    font_btn.pack(side=tk.LEFT, padx=5, pady=5)

    # Add a close button
    def close_note():
        save_note(note_id, text.get("1.0", tk.END).strip(), text.cget("bg"), (note.winfo_x(), note.winfo_y()))
        del notes[note_id]
        note.destroy()

    close_btn = tk.Button(note, text="Close", command=close_note, font=("Arial", 10))
    close_btn.pack(side=tk.RIGHT, padx=5, pady=5)

    # Add a delete button
    def delete_note():
        if os.path.exists(os.path.join(NOTES_DIR, f"note_{note_id}.json")):
            os.remove(os.path.join(NOTES_DIR, f"note_{note_id}.json"))
        del notes[note_id]
        note.destroy()

    delete_btn = tk.Button(note, text="Delete", command=delete_note, font=("Arial", 10))
    delete_btn.pack(side=tk.RIGHT, padx=5, pady=5)

    # Save note reference
    notes[note_id] = {"window": note, "text": text, "color": color}

# Main application
app = tk.Tk()
app.title("Sticky Notes")
app.geometry("500x400")
app.resizable(False, False)

# Track notes
notes = {}

# Create frame for layout (settings & note creation)
frame = tk.Frame(app)
frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

# Taskbar-like Settings Panel
settings_frame = tk.Frame(app, bg="lightgray", height=40)
settings_frame.pack(fill=tk.X)

# Add default color button in settings
def set_default_color():
    color = colorchooser.askcolor()[1]  # Get color from color chooser
    if color:
        default_color_btn.config(bg=color)
        global default_note_color
        default_note_color = color

default_color_btn = tk.Button(settings_frame, text="Default Color", command=set_default_color, font=("Arial", 12))
default_color_btn.pack(side=tk.LEFT, padx=10)

# Set default color variable
default_note_color = "lightyellow"  # Initial default color

# Create a button to create new notes
create_btn = tk.Button(frame, text="New Note", command=create_note, font=("Arial", 14))
create_btn.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

# Load existing notes on startup
load_notes()

# Run the application
app.mainloop()