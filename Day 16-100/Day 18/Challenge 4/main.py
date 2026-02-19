import turtle as t
import random

tim = t.Turtle()
tim.speed("fastest")
tim.pensize(10)
t.colormode(255)

########### Challenge 4 - Random Walk ########
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


direction = [0, 90, 180, 270]

for num in range(200):
    tim.setheading(random.choice(direction))
    tim.forward(30)
    tim.color(random_color())


