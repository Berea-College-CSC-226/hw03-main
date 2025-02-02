import turtle

screen =  turtle.Screen()
screen.colormode(255)
screen.bgcolor(0, 0, 0)

turtle.begin_fill()
turtle.color((87,112,92))
turtle.fillcolor((87,112,92))
for i in range(4):
    turtle.forward(100)
    turtle.right(90)
turtle.fillcolor(87,112,92)
turtle.end_fill()
screen.exitonclick()



