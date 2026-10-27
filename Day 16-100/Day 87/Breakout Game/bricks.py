from turtle import Turtle

BAR_COLOURS = ["red", "orange", "yellow", "green", "blue", "purple"]
START_X = -630
STEP_X = 70
START_Y = 330
STEP_Y = 30

class Brick(Turtle):
    def __init__(self,position,colour,points):
        super().__init__()
        self.points = points
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.color(colour)
        self.penup()
        self.goto(position)

class Bricks:
    def __init__(self):
        self.bricks = []
        self.create_wall()

    def check_collision(self,ball):
        for brick in self.bricks:
            if abs(ball.xcor() - brick.xcor()) < 40 and abs(ball.ycor() - brick.ycor()) < 20:
                points = brick.points
                brick.hideturtle()
                self.bricks.remove(brick)
                ball.bounce_y()
                return points
        return 0

    def bricks_left(self):
        return len(self.bricks)

    def create_wall(self):
        for row in range(6):
            y = START_Y - row * STEP_Y
            colour = BAR_COLOURS[row]
            for i in range(19):
                x = START_X + i * STEP_X
                self.bricks.append(Brick((x, y),colour,6-row))

