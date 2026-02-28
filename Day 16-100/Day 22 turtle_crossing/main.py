from turtle import Turtle, Screen
import time
from car_manager import CarManager
from scoreboard import Scoreboard

tim = Turtle()
tim.shape("turtle")
tim.color("black")
tim.penup()
tim.goto(0, -280)
tim.setheading(90)

def go_up():
    new_y = tim.ycor() + 10
    if new_y < 300:
        tim.goto(0, new_y)

def go_down():
    new_y = tim.ycor() - 10
    if new_y > -290:
        tim.goto(0, new_y)

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.tracer(0)

difficulty = screen.textinput("Turtle Crossing", "Choose difficulty (easy/medium/hard): ")

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

if difficulty and difficulty.lower() == "easy":
    car_frequency = 10
elif difficulty and difficulty.lower() == "medium":
    car_frequency = 6
else:
    car_frequency = 4

scoreboard = Scoreboard()
car_manager = CarManager()

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car(car_frequency)
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(tim) < 20:
            is_game_on = False
            scoreboard.game_over()
            break

    if tim.ycor() > 280:
        tim.goto(0, -280)
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()