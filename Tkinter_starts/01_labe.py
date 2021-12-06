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
image = Image.open("nishant_sign_english.jpg").resize((85, 45))
photo = ImageTk.PhotoImage(image)
label = ttk.Label(root, text="Image with Text", image=photo, padding=5, compound="top")
label.pack()
# label["image"] = new_image                         to change image
a_var = tk.StringVar()
label_1 = ttk.Label(root, padding=10, textvariable=a_var)
label_1.pack()
a_var.set("Hello text called by a_var")
root.mainloop()