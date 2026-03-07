import tkinter
from tkinter import *

def calculate():
    ml = float(miles_input.get())
    km = ml*1.6093
    equals_label.config(text = round(km))


window = tkinter.Tk()
window.title("Miles to Km Converter")
window.config(padx=30, pady=30)

miles_input = Entry(window, width = 10)
miles_input.grid(column = 1, row = 0)

miles_label = Label(window,text = "Miles")
miles_label.grid(column = 2, row = 0)

equals_label = Label(window,text = "0")
equals_label.grid(column = 1, row = 1)

is_equal_label = Label(window,text = "is equal to")
is_equal_label.grid(column = 0, row = 1)

km_label = Label(window,text = "Km")
km_label.grid(column = 2, row = 1)

calculate_button = Button(text = "Calculate", command = calculate)
calculate_button.grid(column = 1, row = 2)













window.mainloop()