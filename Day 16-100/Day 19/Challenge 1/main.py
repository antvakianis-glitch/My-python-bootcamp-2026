from turtle import Turtle , Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(100)
def move_backward():
    tim.backward(100)
def move_left():
    tim.left(10)
def move_right():
    tim.right(10)
def clear():
    tim.clear()
def move_home():
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()

screen.onkey(key = "w", fun = move_forward)
screen.onkey(key = "s", fun = move_backward)
screen.onkey(key = "a", fun = move_left)
screen.onkey(key = "d", fun = move_right)
screen.onkey(key = "c", fun = clear)
screen.onkey(key = "h", fun = move_home)
screen.exitonclick()