from turtle import Turtle, Screen
import pandas
from timer import Countdown

screen = Screen()
screen.setup(width=725, height=491)
screen.bgpic("blank_states_img.gif")
screen.title("U.S. States Game")

t = Turtle()
t.hideturtle()
t.penup()

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
missing_states = []

timer = Countdown()
timer.update_timer()

while len(guessed_states) < len(all_states):
    if timer.time_left <= 0:
        t.goto(0,0)
        t.write("Your time is up", align="center", font=("Courier", 16, "bold"))
        break

    answer = screen.textinput(f"{len(guessed_states)}/50 States", "What's another State name?")

    if answer is None or answer.title() == "Exit":
        timer.is_paused = True
        break

    user_answer = answer.title()

    if user_answer in all_states and user_answer not in guessed_states:
        guessed_states.append(user_answer)
        state_data = data[data.state == user_answer]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(user_answer)

    if len(guessed_states) == len(all_states):
        timer.is_paused = True
        t.goto(0,0)
        t.write("Super you found all states in time", align="center", font=("Courier", 16, "bold"))
        break

missing_states = [state for state in all_states if state not in guessed_states]
if len(missing_states) > 0:
    pandas.DataFrame(missing_states).to_csv("states_to_learn.csv")

screen.mainloop()
