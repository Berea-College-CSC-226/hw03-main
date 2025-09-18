import turtle
# main
def main():
    wn = turtle.Screen()
    wn.setup(width=600, height=600)
    wn.bgcolor("black")
    t1 = turtle.Turtle()
    t1.color("red")
    t1.speed(100)
    t1.penup()
    t1.setposition(-250,-250)
    t1.pendown()

    # Wall loop
    for i in range (4):
        t1.forward(250)
        t1.left(90)
    # Roof loop
    t1.penup()
    t1.setposition(-250, 0)
    t1.pendown()
    t1.left(45)
    t1.forward(190)
    t1.right(95)
    t1.forward(180)



    wn.exitonclick()

main()