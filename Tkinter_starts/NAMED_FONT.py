import tkinter as tk
from tkinter import ttk
import tkinter.font as font

root = tk.Tk()

style = ttk.Style(root)


warning_label_font = font.Font(family="Helvetica", size=14, weight="bold")
# Helvetica, Courier, Time are common in every system

print(*font.families(), sep="\n")
# another_button_font = font.Font(family="Baskerville Old Face", size=8,)
style.configure("CustomButton.TButton", font=("Baskerville Old Face", 20 ))
name = ttk.Label(root, text="Hello World!", font=warning_label_font)
entry = ttk.Entry(root, width=20)
button = ttk.Button(root, text="Press me", style="CustomButton.TButton")
name.pack()
entry.pack()
button.pack()
root.mainloop()
