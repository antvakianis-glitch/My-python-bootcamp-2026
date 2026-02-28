from turtle import Turtle

class Countdown(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(250, 210)
        self.time_left = 600
        self.is_paused = False

    def update_timer(self):
        if self.is_paused:
            return

        if self.time_left < 60:
            self.color("red")

        if self.time_left > 0 and not self.is_paused:
           self.clear()
           minutes = self.time_left // 60
           seconds = self.time_left % 60
           self.write(f"Time: {minutes:02d}:{seconds:02d}", align="center", font=("Courier", 15, "bold"))
           self.time_left -= 1
           self.getscreen().ontimer(self.update_timer, 1000)
        else:
           self.clear()
           self.write("TIME'S UP!", align="center", font=("Courier", 15, "bold"))










