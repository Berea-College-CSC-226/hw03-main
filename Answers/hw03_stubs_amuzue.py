
#################################################################################
# Author: Elom Amuzu
# Username: amuzue
#
# Assignment: Hw03
# Purpose:
# Google Doc Link:
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################


import turtle


def house_1(tess):


    tess.speed(10)
    tess.color("black", "darkblue")

    tess.penup()
    tess.goto(0,100)
    tess.pendown()
    tess.begin_fill()
    tess.forward(300)
    tess.left(140)
    tess.forward(130)
    tess.left(40)
    tess.forward(45)
    tess.right(90)
    tess.forward(50)
    tess.left(90)
    tess.forward(35)
    tess.left(90)
    tess.forward(50)
    tess.right(90)
    tess.forward(460)
    tess.left(40)
    tess.forward(130)
    tess.left(140)
    tess.forward(690)
    tess.end_fill()

    tess.color("black", "lightgray")
    tess.right(90)
    tess.begin_fill()
    tess.forward(300)
    tess.right(90)
    tess.forward(640)
    tess.right(90)
    tess.forward(300)
    tess.end_fill()





def house_2(tess):

    tess.speed(10)
    tess.color("black", "beige")
    tess.penup()
    tess.goto(0,0)
    tess.pendown()
    tess.begin_fill()
    tess.left(180)
    tess.forward(200)
    tess.left(180)
    tess.forward(200)
    tess.left(90)
    tess.forward(100)
    tess.left(90)
    tess.forward(200)
    tess.end_fill()

    tess.penup()
    tess.goto(-200, 20)
    tess.pendown()
    for i in range(4):
        tess.forward(100)
        tess.right(90)

    tess.color("black", "white")
    tess.begin_fill()
    for i in range(2):
        tess.forward(50)
        tess.right(90)
        tess.forward(50)
        tess.right(90)
        tess.forward(50)
        tess.right(180)

    tess.forward(100)
    tess.left(90)
    tess.forward(50)
    tess.left(90)
    tess.forward(50)
    tess.end_fill()



def sun(tess):
    tess.speed(10)

    tess.penup()
    tess.goto(500,300)
    tess.pendown()
    tess.color("black", "yellow")
    tess.begin_fill()
    tess.circle(50)
    tess.end_fill()

    tess.color("orange")
    tess.pensize(3)
    for i in range(0, 360, 45):
        tess.penup()
        tess.goto(500, 490)
        tess.setheading(i)
        tess.pendown()
        tess.forward(25)
    tess.pensize(1)



def main():

    tess = turtle.Turtle()
    wn = turtle.Screen()
    wn.bgcolor("skyblue")

    # Function calls to function_1 and function_2.
    house_1(tess)
    house_2(tess)
    sun(tess)

    tess.speed(10)
    tess.color("black")
    tess.penup()
    tess.goto(630,-150)
    tess.pendown()
    tess.left(225)
    tess.forward(380)
    tess.penup()
    tess.goto(-388, -150)
    tess.pendown()
    tess.forward(255)

    wn.exitonclick()

main()  # Starts the program!