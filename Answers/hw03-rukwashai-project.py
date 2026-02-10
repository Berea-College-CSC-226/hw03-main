import turtle

alex=turtle.Turtle()
turtle.Screen()
turtle.bgcolor("green")

alex.penup()
alex.forward(-550)
alex.right(90)
alex.penup()
alex.forward(200)
alex.left(90)
alex.pendown()
def rectangle():
    for i in range(2):
        alex.forward(1000)
        alex.left(90)
        alex.forward(500)
        alex.left(90)
        # alex.speed(0)


def house():
    alex.penup()
    alex.forward(30)
    alex.left(90)
    alex.forward(400)
    alex.right(90)
    alex.pendown()
    for i in range(1):
        alex.forward(50)
        alex.left(90)
        for ka in range(4):
            alex.forward(25)
            alex.left(60)

def simba():
    alex.penup()
    alex.forward(200)
    alex.left(90)
    alex.right(40)
    alex.pendown()
    for lig in range(6):
        alex.forward(30)
        alex.left(60)
    alex.left(200)
    alex.forward(150)
    alex.left(140)
    alex.forward(30)
    alex.left(45)
    alex.forward(100)
    alex.right(45)
    alex.forward(20)
    alex.right(120)
    alex.forward(70)
    alex.left(90)
    alex.forward(20)
    alex.left(90)
    alex.forward(50)
    alex.right(60)
    alex.forward(200)
    alex.right(30)
    alex.right(45)
    alex.forward(50)
    alex.left(90)
    alex.forward(20)
    alex.left(80)
    alex.forward(110)
    alex.left(80)
    alex.forward(200)
    turtle.color("black", "red")
    turtle.begin_fill()
    turtle.circle(80)
    turtle.end_fill()




def main():
    rectangle()
    house()
    simba()

main()
alex.speed(0)
turtle.done()



