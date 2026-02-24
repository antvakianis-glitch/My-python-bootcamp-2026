from turtle import  Turtle
import random

class Bar(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def move_up(self):
        new_y = self.ycor() + 30
        if new_y < 250:
            self.sety(new_y)

    def move_down(self):
        new_y = self.ycor() - 30
        if new_y > - 250:
            self.sety(new_y)