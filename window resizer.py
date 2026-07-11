import tkinter as tk
from tkinter import *


class WindowResizer:

    def __init__(self, root):
        self.root = root
        self.root.title("Smart Window Resizer")
        self.root.geometry("700x500")
        self.root.configure(bg="#1E1E2F")
        self.root.resizable(False, False)

        self.default_width = 700
        self.default_height = 500

        style = ttk.Style()
        style.theme_use("clam")

        style.configure("TButton", font=("Segoe UI", 11, "bold"), padding=8)

        style.configure("TEntry",font=("Segoe UI", 11))

        self.create_widgets()

        self.root.bind("<Return>", lambda e: self.resize_window())
        

    def create_widgets(self):

        title = tk.Label(self.root, text="Smart Window Resizer",font=("Segoe UI", 22, "bold"), fg="white", bg="#1E1E2F")
        title.pack(pady=20)

        info = tk.Label(
            self.root,
            text="Resize your window instantly!",
            font=("Segoe UI", 11),
            fg="lightgray",
            bg="#1E1E2F"
        )
        info.pack()

        frame = tk.Frame(self.root, bg="#1E1E2F")
        frame.pack(pady=20)

        tk.Label(frame, text="Width", fg="white", bg="#1E1E2F", font=("Segoe UI", 11)).grid(row=0, column=0, padx=10, pady=10)

        self.width_entry = ttk.Entry(frame, width=15)
        self.width_entry.grid(row=0, column=1)

        tk.Label(frame, text="Height", fg="white", bg="#1E1E2F", font=("Segoe UI", 11)).grid(row=1, column=0, padx=10, pady=10)

        self.height_entry = ttk.Entry(frame, width=15)
        self.height_entry.grid(row=1, column=1)

        button_frame = tk.Frame(self.root, bg="#1E1E2F")
        button_frame.pack(pady=10)

        ttk.Button(button_frame, text="Resize", command=self.resize_window).grid(row=0, column=0, padx=10)

        ttk.Button(button_frame,text="Reset",command=self.reset_window).grid(row=0, column=1, padx=10)

        ttk.Button(button_frame,text="Center", command=self.center_window).grid(row=0, column=2, padx=10)

        preset_frame = tk.LabelFrame(self.root, text="Quick Presets", bg="#1E1E2F", fg="white", font=("Segoe UI", 11))

        preset_frame.pack(pady=15)

        presets = [("Small", 400, 300),("Medium", 800, 600),("Large", 1200, 800),("HD", 1366, 768)]

        for i, (text, w, h) in enumerate(presets):
            ttk.Button(preset_frame,text=text,command=lambda x=w, y=h: self.apply_preset(x, y)).grid(row=0, column=i, padx=8, pady=10)

        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()

        self.screen_label = tk.Label(
            self.root,
            text=f"🖥 Screen Resolution : {screen_w} x {screen_h}",fg="#6EEB83",bg="#1E1E2F", font=("Segoe UI", 10) )

        self.screen_label.pack()

        self.status = tk.Label(
            self.root,
            text="Ready",fg="cyan",bg="#1E1E2F",font=("Segoe UI", 10, "bold") )

        self.status.pack(pady=15)

    
    def resize_window(self):

        try:
            width = int(self.width_entry.get())
            height = int(self.height_entry.get())

            if width <= 0 or height <= 0:
                raise ValueError

            self.root.geometry(f"{width}x{height}")
            self.status.config(text=f"Window resized to {width} x {height}",fg="#6EEB83")

        except ValueError:
            messagebox.showerror("Invalid Input","Please enter positive integers only.")
            self.status.config( text="Invalid Input", fg="red")

    
    def apply_preset(self, width, height):

        self.width_entry.delete(0, tk.END)
        self.height_entry.delete(0, tk.END)
        self.width_entry.insert(0, width)
        self.height_entry.insert(0, height)
        self.resize_window()

    
    def reset_window(self):

        self.root.geometry( f"{self.default_width}x{self.default_height}")
        self.status.config(text="Reset to Default",fg="orange")

    
    def center_window(self):

        self.root.update_idletasks()

        width = self.root.winfo_width()
        height = self.root.winfo_height()

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))

        self.root.geometry(f"{width}x{height}+{x}+{y}")

        self.status.config(text="Window Centered",fg="cyan" )


root = tk.Tk()

WindowResizer(root)

root.mainloop()
