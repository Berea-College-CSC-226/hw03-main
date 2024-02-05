import turtle

miska = turtle.Turtle()
wn = turtle.Screen()

miska.pencolor('purple')
miska.pensize(30)
wn.bgcolor('yellow')
miska.shape('square')
turtle.colormode(255)
miska.fillcolor((111, 132, 103))
miska.begin_fill()

for _ in range(4):
    miska.forward(130)
    miska.left(90)

miska.end_fill()

wn.exitonclick()
