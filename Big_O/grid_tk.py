import tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

# tkinter._test()
main_window = tkinter.Tk()
main_window.title("title-WELCOME TO TKINTER")
main_window.geometry("1200x768")

label = tkinter.Label(main_window, text="Label-EXAMPLE", borderwidth=9, relief='raised')
label.grid(row=0, column=0)

leftframe = tkinter.Frame(main_window)
leftframe.grid(row=1, column=1)

rightframe = tkinter.Frame(main_window, borderwidth=1)
rightframe.grid(row=1, column=2, sticky='n')

canvas = tkinter.Canvas(leftframe, relief='raised', borderwidth=7, bg='red')
canvas.grid(row=0, column=0)

button1 = tkinter.Button(rightframe, text='button1', bg='green')
button2 = tkinter.Button(rightframe, text='button2')
button3 = tkinter.Button(rightframe, text='button3')
button2.grid(row=0, column=0)
button1.grid(row=1, column=0)
button3.grid(row=2, column=0)

main_window.mainloop()