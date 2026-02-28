from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.read_score()
        self.update_scoreboard()

    def read_score(self):
        with open("data.txt", "r") as file:
            content = file.read()
            if content:
                self.high_score = int(content)
        self.store_score()

    def store_score(self):
        with open("data.txt", "w") as file:
            file.write(f"{self.high_score}")

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", False, align="center", font=("Courier", 18, "bold"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.store_score()
        self.score = 0
        self.update_scoreboard()

