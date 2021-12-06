class Device:

    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r} connected by {self.connected_by!r}"

    def disconnected(self):
        self.connected = False
        print("Disconnected")


class Printer(Device):

    def __init__(self, name, connected_by, capacity) -> object:
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()}, {self.remaining_pages} pages remaining"

    def print_info(self, pages):
        if not self.connected:
            print("Your printer is not connected.")
            return
        print(f"Printing {pages}")
        self.remaining_pages -= pages


printer = Printer("PRINTER", "USB", 500)
print(printer)
printer.print_info(25)
print(printer)
printer.disconnected()
printer.print_info(23)



# printer = Device("Printer", "USB")
# print(printer)
# printer.disconnected()




