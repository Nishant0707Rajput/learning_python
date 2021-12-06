def dpi_func():
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)