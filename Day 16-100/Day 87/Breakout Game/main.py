import time
import turtle
from paddle import Paddle
from ball import Ball
from bricks import Bricks
from scoreboard import Scoreboard

game_is_on = True
is_paused = False
bricks_broken_counter = 0

window = turtle.Screen()
window.bgcolor("black")
window.title("Breakout Game")
window.colormode(255)
window.tracer(0)
window.setup(width=1400, height=800)


paddle = Paddle((0, -350))
ball = Ball()
ball.goto((0, -330))
bricks = Bricks()
scoreboard = Scoreboard(0, 3, bricks.bricks_left())


def pause_game():
    global is_paused
    is_paused = not is_paused

    if is_paused:
        scoreboard.goto(0, 0)
        scoreboard.write("PAUSED", align="center", font=("Arial", 30, "normal"))
    else:
        scoreboard.clear()
        scoreboard.update_scoreboard()


def reset_game():
    global game_is_on, bricks_broken_counter
    if not game_is_on:
        scoreboard.clear()
        scoreboard.score = 0
        scoreboard.lives = 3
        bricks_broken_counter = 0
        scoreboard.goto(0, 360)
        scoreboard.update_scoreboard()


        for brick in bricks.bricks:
            brick.hideturtle()
        bricks.bricks.clear()
        bricks.create_wall()

        scoreboard.update_bricks(bricks.bricks_left())
        ball.reset_position()

        game_is_on = True



window.listen()
window.onkeypress(paddle.move_left, "Left")
window.onkeypress(paddle.move_right, "Right")
window.onkeypress(reset_game, "r")
window.onkeypress(pause_game, "p")

while True:
    while game_is_on:
        window.update()

        if is_paused:
            time.sleep(0.1)
            continue

        ball.move()


        if ball.ycor() > 380 and ball.y_move > 0:
            ball.bounce_y()
        if ball.xcor() > 680 and ball.x_move > 0:
            ball.bounce_x()
        if ball.xcor() < -680 and ball.x_move < 0:
            ball.bounce_x()

        #
        if ball.y_move < 0 and -350 < ball.ycor() < -325 and abs(ball.xcor() - paddle.xcor()) < 90:
            offset = ball.xcor() - paddle.xcor()
            ball.bounce_paddle(offset)



        points = bricks.check_collision(ball)
        if points:
            scoreboard.increase_score(points)
            scoreboard.update_bricks(bricks.bricks_left())

            bricks_broken_counter += 1

            if bricks_broken_counter % 5 == 0:
                ball.increase_speed()


        if ball.ycor() < -380:
            scoreboard.lose_life()
            ball.reset_position()


        if scoreboard.lives == 0:
            game_is_on = False
            scoreboard.goto(0, 0)
            scoreboard.write("Game Over. Press 'r' to Restart", align="center", font=("Arial", 22, "normal"))


        if len(bricks.bricks) == 0:
            game_is_on = False
            scoreboard.goto(0, 0)
            scoreboard.write("You Won! Press 'r' to Restart", align="center", font=("Arial", 22, "normal"))

        time.sleep(ball.move_speed)

    window.update()