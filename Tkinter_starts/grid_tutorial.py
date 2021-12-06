import tkinter as tk
from tkinter import ttk
from ctypes import windll
from PIL import Image,ImageTk
windll.shcore.SetProcessDpiAwareness(1)


def Greet():
    if user_name.get():
        print(f"Hello {user_name.get()}")
        return
    print("Please type the name:::")


root = tk.Tk()
root.title("Greeter")
user_name = tk.StringVar()
root.columnconfigure(0, weight=1)
frame_1 = ttk.Frame(root, padding=(10, 20, 10, 0))
frame_1.grid(row=0, column=0, sticky="EW")


name_label = ttk.Label(frame_1, text="Name: ")
name_label.grid(row=0, column=0, padx=(0,10))
name_entry = ttk.Entry(frame_1, textvariable=user_name)
name_entry.grid(row=0, column=1)
name_entry.focus()
# print(user_name)

frame_2 = ttk.Frame(root, padding=(0, 10))
frame_2.grid(row=1,column=0,sticky="EW")
frame_2.columnconfigure((0,1), weight=1)

greet_button = ttk.Button(frame_2, text="Greet", command=Greet)
greet_button.grid(row=0, column=0,sticky="EW")
quit_button = ttk.Button(frame_2, text="QUIT", command=root.destroy)
quit_button.grid(row=0, column=1,sticky="EW")

root.mainloop()
# print(str(user_name.get()))