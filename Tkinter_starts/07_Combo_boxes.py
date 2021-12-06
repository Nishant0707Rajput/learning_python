import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from windows import dpi_func

dpi_func()

root = tk.Tk()

root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Examples")

selected_weekday = tk.StringVar()
weekday = ttk.Combobox(root,textvariable=selected_weekday)
weekday["values"] = ("MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY")
weekday["state"] = "readonly"   #normal


def handle_selection(event):
    print("Today is", selected_weekday.get())
    print("But we are going to change it to Wednesday")
    selected_weekday.set("WEDNESDAY")
    print(weekday.current())


weekday.bind("<<ComboboxSelected>>",handle_selection)

weekday.pack()
root.mainloop()
print(selected_weekday.get(), "was elected")