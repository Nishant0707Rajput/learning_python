import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from windows import dpi_func

dpi_func()

root = tk.Tk()

root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Examples")

initial_val = tk.IntVar(value=20)
spin_box = ttk.Spinbox(
    root,
    from_=1,
    to=30,
    #values =(5, 10 , 15, 20, 25, 30)
    textvariable=initial_val,
    wrap=True
)
spin_box.pack()
root.mainloop()