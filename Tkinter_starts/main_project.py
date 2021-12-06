import tkinter as tk
from tkinter import ttk
from windows import dpi_func
import tkinter.font as font


dpi_func()

root = tk.Tk()
root.title("Distance Converter")
font.nametofont("TkDefaultFont").config(size=15)

root.columnconfigure(0, weight=1)
main = ttk.Frame(root, padding=(30, 15))
main.grid()

metres_value = tk.StringVar()
feet_value = tk.StringVar(value="Feet Shown Here")


def calculate_feet(*args):
    try:
        metres = float(metres_value.get())
        feet = metres * 3.28084
        # print(f"{metres} metres is equal to {feet:.3f} feet.")
        feet_value.set(f"{feet:.3f}")
    except ValueError:
        pass


metres_label = ttk.Label(main, text="Metres:")
metres_input = ttk.Entry(main, width=10, textvariable=metres_value, font=("Baskerville Old Face", 15))
feet_label = ttk.Label(main, text="Feet:")
feet_display = ttk.Label(main, text="Feet shown here", textvariable=feet_value)
calc_button = ttk.Button(main, text="Calculate", command=calculate_feet)

metres_label.grid(row=0, column=0, sticky="W")
metres_input.grid(row=0, column=1, sticky="EW")
metres_input.focus()

feet_label.grid(column=0, row=1, sticky="W")
feet_display.grid(column=1, row=1, sticky="EW")

calc_button.grid(column=0, row=2, columnspan=2)

for child in main.winfo_children():
    child.grid_configure(padx=15, pady=15)

root.bind("<Return>", calculate_feet)
root.bind("<KP_Enter>", calculate_feet)
root.mainloop()