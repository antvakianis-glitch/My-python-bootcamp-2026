import turtle as t


tim = t.Turtle()

########### Challenge 2 - Draw a Dashed Line ########
#or count in range(300):
#   tim.pencolor("black")
#   tim.forward(10)
#   tim.pencolor("white")
#   tim.forward(10)

for count in range(15):
    tim.forward(10)  # Draw a dash
    tim.penup()      # Lift pen (stop drawing)
    tim.forward(10)  # Move forward without drawing
    tim.pendown()