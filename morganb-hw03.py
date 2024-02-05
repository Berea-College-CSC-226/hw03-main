#################################################################################
# Author: Baella Morgan
# Username:morganb
#
# Assignment:Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose:Continue practicing fucntions and using the turtle library.
# Google Doc Link:https://docs.google.com/document/d/1NjbTxTAXg0Cuo1YH1nipYNSgiDWNQ2J3X0UAzkHL87w/edit?usp=sharing
#
#################################################################################
# Acknowledgements: turtle documentation page, geeksforgeeks.org, and Ruben Quinonez for help with the arch loop and troubleshooting.
#
#
#################################################################################

import turtle










def edoras(turtle):
    """
    Example docstring for function_1. function_1 is not a good function name and should be changed.
    """
    turtle.left(30)
    turtle.forward(30)
    turtle.left(60)
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(70)
    turtle.right(90)
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(70)
    turtle.left(30)
    turtle.forward(40)
    turtle.right(120)
    turtle.forward(80)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(30)
    turtle.forward(150)
    turtle.right(120)
    turtle.forward(120)
    turtle.right(40)
    turtle.goto(95.98, -145)
    turtle.right(140)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(300)
    turtle.left(70)
    turtle.forward(70)
    turtle.goto(0, -160)
    turtle.right(160)
    turtle.forward(230)
    turtle.right(90)
    turtle.forward(220)
    turtle.right(90)
    turtle.forward(90)
    turtle.left(180)
    turtle.forward(90)
    turtle.left(90)
    turtle.forward(425)
    turtle.left(90)
    turtle.forward(150)
    turtle.right(180)
    turtle.forward(150)
    turtle.left(130)
    turtle.forward(30)
    turtle.right(180)
    turtle.forward(180)
    turtle.right(87)
    turtle.forward(150)
    turtle.left(180)
    turtle.forward(150)
    turtle.right(150)
    turtle.forward(300)
    # ....


def arches(t):
    t.penup()
    t.goto(-40,-85)
    t.left(105)
    t.pendown()
    for i in range(3):
        t.forward(70)
        t.circle(20,180)
        t.forward(70)
        t.right(90)
        t.forward(20)
        t.right(90)

    """
    Example docstring for function_2. function_2 is not a good function name and should be changed.
    """
    pass
    # ...


def main():
    """
    Docstring for main. Should describe the main functionality of this file.
    """
    rohan = turtle.Screen()
    turtle.turtles()
    theoden = turtle.Turtle()
    theoden.shape("turtle")
    rohan.colormode(255)
    rohan.bgcolor("gray")
    theoden.color(39, 76, 31)
    theoden.speed(3)
    theoden.penup()
    theoden.setpos(0, -160)
    theoden.pendown()
    # Function calls to function_1 and function_2.
    edoras(theoden)            # TODO  Remove when you replace it with your function
    arches(theoden)            # TODO  Remove when you replace it with your function

    rohan.exitonclick()

main()  # Starts the program!

