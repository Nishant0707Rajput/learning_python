import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from windows import dpi_func

dpi_func()

root = tk.Tk()

root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Examples")

label = ttk.Label(root, text="Hello World!", padding=20)
label.config(font=("Baskerville Old Face", 20))
label.pack()

ttk.Separator().pack(fill="x")

label_1 = ttk.Label(root, padding=10, text="Line after separator")
label_1.pack()

root.mainloop()