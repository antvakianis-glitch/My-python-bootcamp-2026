from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self,score,lives, count):
        super().__init__()
        self.score = score
        self.lives = lives
        self.bricks_left = count
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 360)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  Lives: {self.lives}  Bricks Left: {self.bricks_left}", align="center",font=("Arial", 18, "normal"))

    def increase_score(self,points):
        self.score += points
        self.update_scoreboard()

    def lose_life(self):
        self.lives -= 1
        self.update_scoreboard()

    def update_bricks(self,number):
        self.bricks_left = number
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align="center",font=("Arial",18,"normal"))

    def you_win(self):
        self.goto(0,0)
        self.write("You Won",align="center",font=("Arial",18,"normal"))

    def clear_message(self):
        self.clear()
        self.update_scoreboard()
