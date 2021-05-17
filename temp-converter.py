from tkinter import *

myframe = Tk()
myframe.geometry("700x500")
myframe.title("Temperature Converter")
myframe.config(bg="turquoise")

cel = StringVar()
fahren = StringVar()
result = StringVar()


def convert_c():
    cel = int(celsius_3.get())
    fahren = (cel * 9 / 5) + 32
    return result.set(fahren)


def convert_f():
    fahren = int(fahrenheit_3.get())
    cel = (fahren - 32) * 5 / 9
    return result.set(cel)


def activate_celsius():
    celsius_3.config(state='normal')
    fahrenheit_3.config(state="normal")
    fahrenheit_3.delete(0, END)
    fahrenheit_3.config(state='readonly')


def activate_fahrenheit():
    celsius_3.config(state="normal")
    celsius_3.delete(0, END)
    celsius_3.config(state='readonly')
    fahrenheit_3.config(state='normal')


def clear_entries():
    celsius_3.delete(0, END)
    fahrenheit_3.delete(0, END)
    answer.delete(0, END)


def exit_program():
    myframe.destroy()


celsius_1 = Button(myframe, text="Activate Celsius - Fahrenheit", command=activate_celsius)
celsius_1.place(x=10, y=20)
fahrenheit_1 = Button(myframe, text="Activate Fahrenheit - Celsius", command=activate_fahrenheit)
fahrenheit_1.place(x=470, y=20)

celsius_2 = Label(myframe, text="Celsius to Fahrenheit", bg="turquoise")
celsius_2.place(x=50, y=60)
celsius_3 = Entry(myframe, state='readonly', textvariable=cel)
celsius_3.place(x=40, y=90)

fahrenheit_2 = Label(myframe, text="Fahrenheit to Celsius", bg="turquoise")
fahrenheit_2.place(x=500, y=60)
fahrenheit_3 = Entry(myframe, state='readonly', textvariable=fahren)
fahrenheit_3.place(x=490, y=90)

calc = Button(myframe, text="Calculate Celsius", command=convert_f)
calc.place(x=550, y=350)
calc_2 = Button(myframe, text="Calculate Fahrenheit", command=convert_c)
calc_2.place(x=10, y=350)
clear = Button(myframe, text="Clear", command=clear_entries)
clear.place(x=300, y=350)
exit_1 = Button(myframe, text="Exit Program", command=exit_program)
exit_1.place(x=550, y=460)
answer = Entry(myframe, textvariable=result, state="readonly", bg="lawn green")
answer.place(x=250, y=250)

myframe.mainloop()
