import turtle as t
import random

tim = t.Turtle()

########### Challenge 3 - Draw Shapes ########
colours = ["red", "blue", "green", "yellow", "orange", "pink"]

for numb_sides in range(3, 11):
    tim.color(random.choice(colours))
    angle = 360 / numb_sides
    for i in range(numb_sides):
        tim.right(angle)
        tim.forward(100)
