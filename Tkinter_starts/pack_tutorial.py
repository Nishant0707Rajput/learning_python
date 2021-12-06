import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x400")

rectangle_1 = tk.Label(root, text="Rectangle 1", bg="red", fg="black")
rectangle_1.pack(side="left",ipadx=10, ipady=10, fill="both", expand=True)

rectangle_2 = tk.Label(root, text="Rectangle 2", bg="green", fg="black")
rectangle_2.pack(ipadx=10, ipady=10, fill="both", expand=True)


rectangle_1 = tk.Label(root, text="Rectangle 1", bg="purple", fg="black")
rectangle_1.pack(side="left",ipadx=10, ipady=10, fill="both", expand=True)

root.mainloop()