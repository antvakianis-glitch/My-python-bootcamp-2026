import random
from turtle import Turtle, Screen
screen = Screen()


screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")

message_turtle = Turtle()
message_turtle.hideturtle()
message_turtle.penup()
message_turtle.goto(0, 0)

turtles = []
positions = [0,20,40,-20,-40]
colours = ["red","green","blue","yellow","orange"]
random.shuffle(colours)
for index in range(5):
  new_turtle = Turtle(shape="turtle")
  new_turtle.color(colours[index])
  new_turtle.penup()
  new_turtle.goto(-240, positions[index])
  turtles.append(new_turtle)

is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
  for turtle in turtles:
      if turtle.xcor() > 230:
        is_race_on = False
        winning_color = turtle.pencolor()
        if winning_color == user_bet:
          message_turtle.write(f"You won! The {winning_color} turtle is first!", align="center", font=("Courier", 16, "bold"))
        else:
          message_turtle.write(f"You lose! The {winning_color} turtle won!", align="center", font=("Courier", 16, "bold"))
        break
      distance_traveled = random.randint(1, 20)
      turtle.forward(distance_traveled)

screen.exitonclick()