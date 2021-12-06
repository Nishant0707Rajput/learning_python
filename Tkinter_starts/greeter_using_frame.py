import tkinter as tk
from tkinter import ttk


def Greet():
    if user_name.get():
        print(f"Hello {user_name.get()}")
        return
    print("Please type the name:::")


root = tk.Tk()
root.title("Greeter")
user_name = tk.StringVar()

style = ttk.Style(root)
print(style.theme_names())
print(style.theme_use())

frame_1 = ttk.Frame(root, padding=(10, 20, 10, 0))
frame_1.pack(fill="both")


name_label = ttk.Label(frame_1, text="Name: ")
name_label.pack(side="left", padx=(0, 10))
name_entry = ttk.Entry(frame_1, textvariable=user_name)
name_entry.pack(side="left", padx=(0, 10),fill="x",expand=True)
name_entry.focus()
# print(user_name)

frame_2 = ttk.Frame(root, padding=(0, 10))
frame_2.pack(fill="both")

greet_button = ttk.Button(frame_2, text="Greet", command=Greet)
greet_button.pack(side="left", fill="x", expand=True)

quit_button = ttk.Button(frame_2, text="QUIT", command=root.destroy)
quit_button.pack(side="right", fill="x", expand=True)

root.mainloop()
# print(str(user_name.get()))