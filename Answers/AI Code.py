import turtle

t = turtle.Turtle()

# Set fill color to xanadu
t.fillcolor("#738678")  # Hex code for xanadu

# Draw and fill a shape
t.begin_fill()
for _ in range(5):  # Draw a pentagon
    t.forward(100)
    t.left(72)
t.end_fill()

turtle.done()
