import tkinter as tk
from tkinter import ttk
import tkinter.font as font

root = tk.Tk()

style = ttk.Style(root)
style.configure("CustomButton.TButton", font=("Segoe UI", 10))

font.nametofont("TkDefaultFont").configure(size=15) #--------->To change entry field font
font.nametofont("TkTextFont").configure(size=15)  #--------->To change entry field font
style.configure("CustomButton.TButton", font=("Segoe UI", 10)) #------>specific element font change

name = ttk.Label(root, text="Hello World!")
entry = ttk.Entry(root, width=20)
button = ttk.Button(root, text="Press me", style="CustomButton.TButton")
name.pack()
entry.pack()
button.pack()
root.mainloop()
