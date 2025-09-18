import turtle


wn = turtle.Screen()
wn.setup(width=800, height=600)
turtle.colormode(255)
berea_blue = turtle.Turtle()
berea_blue.pensize(7)

berea_blue.speed(5)
berea_blue.color(120, 0, 0)
berea_blue.teleport(0, -110)
berea_blue.circle(160)

berea_blue.color(106, 13, 173)
berea_blue.left(90)
berea_blue.forward(85)

berea_blue.right(60)

for i in range(5):
    berea_blue.forward(75)
    berea_blue.color(0, 0, 0,)
    berea_blue.right(60)
    berea_blue.forward(80)
    berea_blue.left(180)
    berea_blue.forward(75)
    berea_blue.color(106, 13, 173)
    berea_blue.right(60)
#End of first sloop

#last turtle line
berea_blue.forward(75)

#turtle middle design

berea_blue.color(47, 91, 76)
berea_blue.penup()

berea_blue.left(120)

berea_blue.forward(40)
berea_blue.pendown()
berea_blue.right(60)

for j in range(6):
   berea_blue.forward(30)
   berea_blue.left(60)


berea_blue.hideturtle()
wn.exitonclick()
