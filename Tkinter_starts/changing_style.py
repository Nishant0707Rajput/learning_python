import tkinter as tk
from tkinter import ttk


root = tk.Tk()

style = ttk.Style(root)
name = ttk.Label(root, text="Hello, world!")
name.pack()
# print(name.winfo_class())
# style.configure("TLabel", font=("Segoe UI", 32))

print(style.layout("TLabel"))

print(style.element_options("Label.border"))
print(style.element_options("Label.padding"))
print(style.element_options("Label.label"))

print(style.lookup("TLabel", "font"))
print(style.lookup("TLabel", "foreground"))
print(style.lookup("TLabel", "compound"))

style.theme_use("clam")

print(style.layout("TLabel"))

print(style.element_options("Label.border"))
print(style.element_options("Label.padding"))
print(style.element_options("Label.label"))

print(style.lookup("TLabel", "font"))
print(style.lookup("TLabel", "foreground"))
print(style.lookup("TLabel", "compound"))

style.configure("TLabel", bordercolour="#f00")
style.configure("TLabel", borderwidth=20)
style.configure("TLabel", relief="solid")


root.mainloop()