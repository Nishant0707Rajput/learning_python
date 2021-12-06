import tkinter as tk
from tkinter import ttk

root = tk.Tk()

main = ttk.Frame(root)
main.pack(side="left", fill="both", expand="True")

main_2 = ttk.Frame(root)
main_2.pack(side="left", fill="both", expand="True")

tk.Label(main, text="Label top", bg="red", fg="black").pack(side="top", expand="True", fill="both")
tk.Label(main, text="Label top", bg="blue", fg="black").pack(side="top", expand="True", fill="both")
tk.Label(main_2, text="Label left", bg="violet", fg="black").pack(side="top", expand="True", fill="both")
tk.Label(main_2, text="Label left", bg="purple", fg="black").pack(side="top", expand="True", fill="both")

root.mainloop()