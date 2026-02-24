from turtle import Screen, Turtle
from create_bar import Bar
from the_ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Bar((350, 0))
l_paddle = Bar((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

tim = Turtle()
tim.color("white")
tim.hideturtle()
tim.penup()
tim.goto(0, 350)
tim.speed("fastest")
tim.right(90)
tim.pendown()
for _ in range(35):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

screen.listen()

screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

move_speed = 0.1

game_is_on = True
while game_is_on:
    time.sleep(move_speed)
    screen.update()
    ball.move()

    # 1. Έλεγχος για σύγκρουση με τα paddles (ΕΠΙΤΑΧΥΝΣΗ)
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
        move_speed *= 0.9

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # 2. Έλεγχος για πόντο Δεξιά (REFRESH)
    if ball.xcor() > 380:
        ball.reset_pos()
        move_speed = 0.1
        scoreboard.left_point()

    # 3. Έλεγχος για πόντο Αριστερά (REFRESH)
    if ball.xcor() < -380:
        ball.reset_pos()
        move_speed = 0.1
        scoreboard.right_point()

screen.exitonclick()