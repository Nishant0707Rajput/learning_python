import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from windows import dpi_func

dpi_func()

root = tk.Tk()

root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Examples")
current_val = tk.DoubleVar()


def handle_scale_change(event):
    print(scale.get())

scale = ttk.Scale(
    root,
    orient="horizontal",
    from_=0,
    to=10,
    variable=current_val,
    command=handle_scale_change
)
scale.pack(fill="x")
scale["state"] = "normal"   #disabled
root.mainloop()
print(current_val.get())