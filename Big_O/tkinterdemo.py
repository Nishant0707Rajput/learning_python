import tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

# tkinter._test()
main_window = tkinter.Tk()

main_window.title("title-WELCOME TO TKINTER")
main_window.geometry("1200x768")

label = tkinter.Label(main_window, text="Label-EXAMPLE", borderwidth=9, relief='raised')
label.pack(side="top")

leftframe = tkinter.Frame(main_window)
leftframe.pack(side='left', anchor='n', fill=tkinter.Y,expand=True)

rightframe = tkinter.Frame(main_window,borderwidth=1)
rightframe.pack(side='right', anchor='n', expand=True)

canvas = tkinter.Canvas(leftframe, relief='raised', borderwidth=7, bg='red')
canvas.pack(side="bottom")

button1 = tkinter.Button(rightframe, text='button1')
button2 = tkinter.Button(rightframe, text='button2')
button3 = tkinter.Button(rightframe, text='button3')
button2.pack(side='top')
button1.pack(side='top')
button3.pack(side='top')

main_window.mainloop()