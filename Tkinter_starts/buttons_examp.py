import tkinter as tk
from tkinter import ttk


def Greet():
    if user_name.get():
        print(f"Hello {user_name.get()}")
        return
    print("Please type the name:::")



root = tk.Tk()
user_name = tk.StringVar()

name_label = ttk.Label(root, text="Name: ")
name_label.pack(side="left", padx=(0, 10))
name_entry = ttk.Entry(root, width=20, textvariable=user_name)
name_entry.pack(side="left", padx=(0, 10))
name_entry.focus()
# print(user_name)

greet_button = ttk.Button(text="Greet", command=Greet)
greet_button.pack(side="left")

quit_button = ttk.Button(text="QUIT", command=root.destroy)
quit_button.pack(side="right")

root.mainloop()
# print(str(user_name.get()))