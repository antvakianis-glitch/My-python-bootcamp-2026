import csv
import tkinter
from tkinter import *
from tkinter import messagebox
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
flip_timer = None

current_card = {}

try:

    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/german_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")

def next_card():
    global flip_timer, current_card
    if flip_timer:
        window.after_cancel(flip_timer)

    current_card = random.choice(to_learn)

    canvas.itemconfig(card_title, text="German", fill="black")
    canvas.itemconfig(card_word, text=current_card["German"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front_img)

    flip_timer = window.after(5000, func=flip_card)

def is_known():
    to_learn.remove(current_card)

    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("data/words_to_learn.csv", index=False)

    if len(to_learn) == 0:
        messagebox.showinfo(message="Well done, no more words to learn")
        window.destroy()
    else:
        next_card()

def reset():
    global to_learn
    try:
        original_data = pandas.read_csv("./data/german_words.csv")
    except FileNotFoundError:
        messagebox.showinfo(title="File not found", message="Data file doesnt exist")
    else:
        to_learn = original_data.to_dict(orient="records")
        new_data = pandas.DataFrame(to_learn)
        new_data.to_csv("data/words_to_learn.csv", index=False)

        next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526,highlightthickness=0)
canvas.config(bg=BACKGROUND_COLOR)

card_back_img = PhotoImage(file="./images/card_back.png")

card_front_img = PhotoImage(file="./images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)

card_title = canvas.create_text(400, 150, text="German", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image,command=next_card,highlightthickness=0,bd=0)
wrong_button.config(background=BACKGROUND_COLOR)
wrong_button.grid(row=1, column=0)

correct_image = PhotoImage(file="./images/right.png")
correct_button = Button(image=correct_image,command=is_known, highlightthickness=0,bd=0)
correct_button.config(background=BACKGROUND_COLOR)
correct_button.grid(row=1, column=1)

reset_image = PhotoImage(file="./images/reset.png")
reset_button = Button(image=reset_image,command= reset,highlightthickness=0,bd=0)
reset_button.config(background=BACKGROUND_COLOR)
reset_button.grid(row=1, column=0,columnspan=2)

next_card()

window.mainloop()