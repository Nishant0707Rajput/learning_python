import tkinter as tk
from tkinter import ttk
from windows import dpi_func
import numpy as np
import tkinter.font as font
from PIL import Image, ImageTk

dpi_func()

root = tk.Tk()
root.geometry("1000x900")
root.resizable(False, False)
root.title("Matrix Solution")
font.nametofont("TkDefaultFont").config(size=8)
root.columnconfigure(0, weight=1)

new_frame = ttk.Frame(root, padding=(10, 0))
new_frame.grid(row=0, column=0)

image = Image.open("Capture.PNG").resize((750,450))
photo = ImageTk.PhotoImage(image)
label = ttk.Label(new_frame, image=photo, padding=5, compound="top")
label.grid(row=0, column=0)
image_2 = Image.open("Capture_2.PNG").resize((250, 175))
photo_2 = ImageTk.PhotoImage(image_2)
label_2 = ttk.Label(new_frame, image=photo_2, padding=5, compound="top")
label_2.grid(row=1, column=0, sticky="W")

main = ttk.Frame(root, padding=(10, 0))
main.grid(row=1, column=0)

Variable_values = tk.StringVar()
Voltage_values = tk.StringVar()
Current_Values = tk.StringVar(value="Current Values Shown Here")


def calculate_feet(*args):
    try:
        Variable = Variable_values.get()
        Voltages = Voltage_values.get()
        R = np.matrix(Variable)
        V = np.matrix(Voltages)
        I = np.linalg.inv(R) * V
        I = I.tolist()
        # print(f"{metres} metres is equal to {feet:.3f} feet.")
        Current_Values.set(f"{I}")
    except ValueError:
        Current_Values.set(f"Either solution doesn't exist or" 
                           " Please fill the values according to the Given Format")


Variable_label = ttk.Label(main, text="Variables:")
Variable_input = ttk.Entry(main, width=50, textvariable=Variable_values,font=("Baskerville Old Face", 10))

Voltage_label = ttk.Label(main, text="Voltages:")
Voltage_input = ttk.Entry(main, width=25, textvariable=Voltage_values,font=("Baskerville Old Face", 10))

Current_label = ttk.Label(main, text="Currents:")
Current_display = ttk.Label(main, text="Current Values shown here", textvariable=Current_Values)
calc_button = ttk.Button(main, text="Calculate", command=calculate_feet)

Variable_label.grid(row=0, column=0, sticky="W")
Variable_input.grid(row=0, column=1, sticky="EW")
Variable_input.focus()

Voltage_label.grid(row=1, column=0, sticky="W")
Voltage_input.grid(row=1, column=1, sticky="EW")
Voltage_input.focus()

Current_label.grid(column=0, row=2, sticky="W")
Current_display.grid(column=1, row=2, sticky="EW")

calc_button.grid(column=0, row=3, columnspan=2)

for child in main.winfo_children():
    child.grid_configure(padx=10, pady=10)

root.bind("<Return>", calculate_feet)
root.bind("<KP_Enter>", calculate_feet)
root.mainloop()