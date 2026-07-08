import tkinter as tk
from tkinter import Tk, messagebox 

def resize_window():
    try:
        width = int(width_entry.get())
        height = int(height_entry.get())

        if width <= 0 or height <= 0:
            raise ValueError

        root.geometry(f"{width}x{height}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter positive integer values for width and height.")

# Main Window
root = Tk()
root.title("Window Resizer GUI")
root.geometry("400x200")

# Title Label
title_label = tk.Label(root, text="Window Resizer GUI", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

width_frame = tk.Frame(root)
width_frame.pack(pady=5)

tk.Label(width_frame, text="Window Width:").pack(side=tk.LEFT, padx=5)
width_entry = tk.Entry(width_frame, width=10)
width_entry.pack(side=tk.LEFT)

height_frame = tk.Frame(root)
height_frame.pack(pady=5)

tk.Label(height_frame, text="Window Height:").pack(side=tk.LEFT, padx=5)
height_entry = tk.Entry(height_frame, width=10)
height_entry.pack(side=tk.LEFT)

# Resize Button
resize_button = tk.Button(root, text="Resize Window", command=resize_window)
resize_button.pack(pady=20)

root.mainloop()