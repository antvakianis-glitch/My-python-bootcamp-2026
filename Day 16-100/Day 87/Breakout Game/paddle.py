from turtle import Turtle
X_LIMIT = 620

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=8)
        self.color("white")
        self.penup()
        self.goto(position)

    def move_left(self):
        new_x = self.xcor() - 50
        if new_x > -X_LIMIT:
            self.setx(new_x)

    def move_right(self):
        new_x = self.xcor() + 50
        if new_x < X_LIMIT:
            self.setx(new_x)

