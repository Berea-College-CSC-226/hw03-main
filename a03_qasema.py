# Author Ala Qasem
#
# A03 Assignment.
#
# username:qasema
# goog Doc: https://docs.google.com/document/d/1KmxGDSYlMvPw7RvxMy8dhalMqZi-Sm9sydeMn83LnY0/edit?usp=sharing
################################################################################################
# in this cos e i will draw a shark. I hope you like. it does not look perfect but i spent a lot of time building it

"""first i will import the turtle library. """

import turtle

"""working on the window and importing an image as a background AND then name a turtle  """

wn = turtle.Screen()
wn.colormode(250)
wn.bgpic("ocean.gif")
wn.bgcolor("#006994")
shark = turtle.Turtle()
turtle.colormode(250)


def function_1():
    shark.speed(0)
    shark.pensize(120)
    shark.pencolor("#006994")
    shark.forward(83)
    shark.left(90)
    shark.forward(24)
    shark.left(90)
    shark.forward(148)
    shark.left(90)
    shark.forward(20)
    shark.left(90)
    shark.forward(100)
    shark.left(90)
    shark.pensize(45)
    shark.forward(125)
    shark.pensize(10)
    shark.right(90)
    shark.right(90)
    shark.forward(10)
    shark.left(90)
    shark.pensize(17)
    shark.forward(30)
    shark.right(90)
    shark.forward(30)
    shark.left(90)

    shark.penup()
    shark.goto(0.00, 0.00)
    shark.pendown()
    shark.pensize(4)
    shark.color("black")
    shark.left(90)
    shark.forward(170)
    print(shark.pos())
    shark.penup()
    shark.left(90)
    shark.forward(90)
    shark.pendown()
    shark.left(75)
    shark.forward(90)
    print(shark.pos())
    shark.left(105)
    shark.forward(170)
    print(shark.pos())


"""draw the shape of the eyes"""


def function_2():
    shark.begin_fill()
    shark.fillcolor("white")
    for i in range(36):
        shark.forward(3)
        shark.right(10)
    shark.penup()
    shark.forward(35)
    shark.pendown()
    for i in range(36):
        shark.forward(3)
        shark.right(10)
    shark.end_fill()
    shark.penup()
    shark.goto(56.71, 83.07)
    shark.fillcolor("#006994")
    shark.forward(45)
    shark.pendown()
    shark.forward(130)
    shark.right(115)
    shark.forward(40)


# draw the mouth
def function_3():
    shark.begin_fill()
    shark.fillcolor("#006994")
    for i in range(5):
        shark.right(14)
        shark.forward(25)

    for i in range(5):
        shark.forward(20)
        shark.right(5)

    shark.end_fill()


'''draw fins'''


def function_4():
    shark.begin_fill()
    shark.fillcolor("#006994")
    shark.penup()
    shark.goto(0.00, 0.00)
    shark.left(45)
    shark.forward(30)
    shark.pendown()
    for i in range(40):
        shark.left(3)
        shark.forward(3)
    shark.left(60)
    for i in range(40):
        shark.left(2.5)
        shark.forward(2.5)

    shark.end_fill()


'''draw the rest of the body'''


def function_5():
    shark.begin_fill()
    shark.penup()
    shark.goto(-113.29, 83.07)
    shark.left(130)
    shark.forward(33)
    shark.pendown()
    shark.end_fill()
    print(shark.pos())
    for i in range(9):
        shark.left(10)
        shark.forward(15)

    shark.penup()
    shark.left(15)
    shark.forward(62)
    shark.pendown()
    shark.right(5)

    for i in range(13):
        shark.left(5)
        shark.forward(16)
    shark.left(30)
    shark.forward(5)


'''draw the tale'''


def function_6():
    shark.penup()
    shark.goto(-127.24, 53.16)
    shark.pendown()
    shark.left(125)
    shark.forward(86)
    shark.left(-152)
    shark.forward(185)
    shark.penup()
    shark.goto(0.00, 170.00)
    shark.pendown()
    shark.right(60)
    for i in range(13):
        shark.forward(10.5)
        shark.right(8)


'''draw eyes'''


def function_7():
    shark.penup()
    shark.forward(15)
    shark.right(170)
    shark.pendown()
    shark.circle(5)

    shark.penup()
    shark.right(90)
    shark.forward(30)
    shark.pendown()
    shark.circle(5)


def shark_coloring():
    shark.penup()
    shark.goto(50, 30)
    shark.pendown()
    shark.pensize(29)
    shark.pencolor("#006994")
    shark.left(17)
    shark.forward(145)
    shark.left(55)
    shark.forward(27)
    shark.pensize(20)
    shark.left(117)
    shark.forward(85)
    shark.left(90)
    shark.forward(20)
    shark.left(90)
    shark.forward(60)
    shark.penup()
    shark.goto(50, 30)
    shark.left(130)
    shark.pendown()
    shark.forward(50)
    shark.pensize(28)
    shark.left(140)
    shark.forward(38)
    shark.penup()
    shark.goto(-127.24, 53.16)
    shark.pendown()
    shark.begin_fill()
    shark.pensize(3)
    shark.left(180)
    shark.forward(64)
    shark.right(35)
    shark.forward(48)
    shark.right(180)
    shark.forward(170)
    shark.left(160)
    shark.end_fill()
    shark.forward(90)
    shark.begin_fill()
    shark.left(40)
    shark.forward(80)
    shark.left(165)
    shark.forward(80)
    shark.end_fill()


def main():
    function_1()
    function_2()
    function_3()
    function_4()
    function_5()
    function_6()
    function_7()
    shark_coloring()
    shark.hideturtle()
    shark.color("red")
    shark.write("Hello Shark", move=False, align='right', font=("Arial", 30, ("bold","normal")))
main()
wn.exitonclick()
