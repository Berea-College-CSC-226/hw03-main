import turtle

turtle = turtle.Turtle()
turtle.colormode(255)
# Set the fill color
turtle.fillcolor(115, 134, 120)
turtle.color(115, 134, 120)

# Start filling the shape
turtle.begin_fill()

# Draw the ship (this is a simple approximation)
turtle.forward(100)   # Bottom of the ship
turtle.left(90)
turtle.forward(100)   # Left side
turtle.left(90)
turtle.forward(100)   # Right side
turtle.left(90)
turtle.forward(100)
# End filling the shape
turtle.end_fill()

# Hide the turtle and finish
turtle.hideturtle()
turtle.done()

