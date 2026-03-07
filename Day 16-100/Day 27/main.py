import tkinter
from tkinter import *

window = tkinter.Tk()

window.title("My first GUI Program")
window.minsize(width=500, height=400)

my_label = tkinter.Label(text="I am a label", font=("Arial", 18, "bold"))
my_label.pack()

my_label["text"] = "New label"
my_label.config(text = "New label")
my_label.grid(column = 0, row = 0)


def button_click():
    my_label.config(text = input.get())


button = Button(text = "Click me", command=button_click)
button.grid(column = 1, row = 1)

new_button = Button(text = "Click me", command=button_click)
new_button.grid(column = 2, row = 0)

input = Entry(width=10)
input.grid(column = 3, row = 2)
print(input.get())

window.mainloop()

