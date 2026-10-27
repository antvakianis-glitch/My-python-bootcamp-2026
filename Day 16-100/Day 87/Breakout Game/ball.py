from turtle import Turtle
import random

MIN_SPEED = 0.006

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.02

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def bounce_paddle(self, offset):
        self.y_move = abs(self.y_move)
        self.x_move = offset / 9
        if abs(self.x_move) < 2:
            self.x_move = 2 if self.x_move >= 0 else -2

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.02
        self.x_move = random.choice([-10, 10])
        self.y_move = 10

    def increase_speed(self):
        self.move_speed = max(self.move_speed * 0.95, MIN_SPEED)
