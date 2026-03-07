import tkinter
from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    if timer:
        window.after_cancel(timer)
    start_button.config(state="normal")
    canvas.itemconfig(timer_text, text="00:00")
    text_label.config(text="TIMER", fg=GREEN)
    tik_label.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
reps = 0

def start_timer():
    start_button.config(state="disabled")
    global reps
    reps +=1

    work_sec = WORK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_sec)
        text_label.config(text="Break", fg=RED)

    elif reps % 2 == 0:
        count_down(short_sec)
        text_label.config(text="Break", fg=PINK)

    else:
        count_down(work_sec)
        text_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = count // 60
    seconds = count % 60

    time_str = f"{minutes:02}:{seconds:02}"
    canvas.itemconfig(timer_text, text=time_str)

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()

        window.attributes('-topmost', True)
        window.attributes('-topmost', False)

        marks = ""
        work_sessions = reps // 2
        for _ in range(work_sessions):
            marks += "✔"
        tik_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.configure(background=YELLOW)
window.configure(padx=100, pady=100)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness= 0)
bg = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image= bg)

timer_text = canvas.create_text(100,112,text="00:00",font=(FONT_NAME, 35, "bold"),fill=YELLOW)
canvas.grid(row=2, column=1)

text_label = Label(window, text="TIMER",font=(FONT_NAME , 30 ,"bold"),bg=YELLOW,fg=GREEN)
text_label.grid(row=1, column=1)

tik_label = Label(window, text="", font=(FONT_NAME, 15, "bold"), bg=YELLOW, fg=GREEN)
tik_label.grid(row=4, column=1)

start_button = Button(text= "Start", command=start_timer)
start_button.grid(row=3, column=0)

reset_button = Button(text= "Reset", command=reset_timer)
reset_button.grid(row=3, column=2)

window.mainloop()