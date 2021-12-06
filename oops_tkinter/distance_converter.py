import tkinter as tk
from tkinter import ttk
from windows import dpi_func
import tkinter.font as font

dpi_func()


class DistanceConverter(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Distance Converter")
        self.frames = dict()

        container = ttk.Frame(self)
        container.grid(padx=60, pady=30, sticky="EW")

        for FrameClass in (MetresToFeet, FeetToMeter):
            frame = FrameClass(container, self)
            self.frames[FrameClass] = frame
            frame.grid(row=0, column=0, sticky="NSWE")

        self.show_frame(MetresToFeet)

    def show_frame(self, container):
        frame = self.frames[container]
        self.bind("<Return>", frame.calculate)
        self.bind("<KP_Enter>", frame.calculate)
        frame.tkraise()


class MetresToFeet(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)

        self.metres_value = tk.StringVar()
        self.feet_value = tk.StringVar(value="Feet Shown Here")

        metres_label = ttk.Label(self, text="Metres:")
        metres_input = ttk.Entry(self, width=10, textvariable=self.metres_value, font=("Baskerville Old Face", 15))
        feet_label = ttk.Label(self, text="Feet:")
        feet_display = ttk.Label(self, text="Feet shown here", textvariable=self.feet_value)
        calc_button = ttk.Button(self, text="Calculate", command=self.calculate)
        switch_page_button = ttk.Button(self,
                                        text="Switch to feet conversion",
                                        command=lambda: controller.show_frame(FeetToMeter))
        metres_label.grid(row=0, column=0, sticky="W")
        metres_input.grid(row=0, column=1, sticky="EW")
        metres_input.focus()

        feet_label.grid(column=0, row=1, sticky="W")
        feet_display.grid(column=1, row=1, sticky="EW")

        calc_button.grid(column=0, row=2, columnspan=2, sticky="EW")
        switch_page_button.grid(column=0, row=3, columnspan=2, sticky="EW")
        for child in self.winfo_children():
            child.grid_configure(padx=15, pady=15)

    def calculate(self, *args):
        try:
            metres = float(self.metres_value.get())
            feet = metres * 3.28084
            # print(f"{metres} metres is equal to {feet:.3f} feet.")
            self.feet_value.set(f"{feet:.3f}")
        except ValueError:
            pass


class FeetToMeter(ttk.Frame):
    def __init__(self, container,controller, **kwargs):
        super().__init__(container, **kwargs)

        self.metres_value = tk.StringVar(value="Metres Shown Here")
        self.feet_value = tk.StringVar()

        feet_label = ttk.Label(self, text="Feet:")
        feet_input = ttk.Entry(self, width=10, textvariable=self.feet_value, font=("Baskerville Old Face", 15))
        metres_label = ttk.Label(self, text="Metre:")
        metres_display = ttk.Label(self, text="Metre shown here", textvariable=self.metres_value)
        calc_button = ttk.Button(self, text="Calculate", command=self.calculate)
        switch_page_button = ttk.Button(self,
                                        text="Switch to metre conversion",
                                        command=lambda: controller.show_frame(MetresToFeet))

        feet_label.grid(row=0, column=0, sticky="W")
        feet_input.grid(row=0, column=1, sticky="EW")
        feet_input.focus()

        metres_label.grid(row=1, column=0, sticky="W")
        metres_display.grid(row=1, column=1, sticky="EW")
        switch_page_button.grid(column=0, row=3, columnspan=2, sticky="EW")
        calc_button.grid(column=0, row=2, columnspan=2, sticky="EW")
        for child in self.winfo_children():
            child.grid_configure(padx=15, pady=15)

    def calculate(self, *args):
        try:
            feet = float(self.feet_value.get())
            metres = feet / 3.28084
            # print(f"{metres} metres is equal to {feet:.3f} feet.")
            self.metres_value.set(f"{metres:.3f}")
        except ValueError:
            pass


root = DistanceConverter()
font.nametofont("TkDefaultFont").config(size=15)

root.columnconfigure(0, weight=1)

root.mainloop()
