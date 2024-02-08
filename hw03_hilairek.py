# Author: Kervens Hilaire
# Username: hilairek
#
# Assignment: HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Learning more about functions, git, and RGB.
# Google Doc Link: https://docs.google.com/document/d/1qX_R1QL3Qg3_BBGEiCuX8spbrTxbjD2ipZlsZpv2VWk/edit
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle


def drawroof():
    """
    This function draws the roof
    """

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.goto(-200, 50)
    t.pendown()
    t.color('red')
    t.begin_fill()
    for i in range(1):
        t.forward(450)
        t.left(110)
        t.forward(199)
        t.left(70)
        t.forward(300)
        t.left(66)
        t.forward(205)
    t.end_fill()


def drawroofwindow():
    """
    This function draws the roof window

    """
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.color("white")
    t.penup()
    t.goto(-60, 100)
    t.pendown()
    t.pensize(5)
    t.forward(130)
    for i in range(2):
        t.left(90)
        t.forward(80)
        t.left(90)
        t.forward(130)
    t.backward(65)
    t.left(90)
    t.forward(80)
    t.backward(40)
    t.right(90)
    t.forward(60)
    t.backward(120)


def bodyofhouse():
    """
    This function draws the body of a house
    """
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-190, 50)
    t.pendown()
    t.hideturtle()
    t.color("#d2b48c")
    t.begin_fill()
    for i in range(1):
        t.forward(426)
        t.right(90)
        t.forward(256)
        t.right(90)
        t.forward(426)
        t.right(90)
        t.forward(256)
        t.end_fill()


def door():
    """
    This function draws the door of the house
    """
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-160, -207)
    t.pendown()
    t.hideturtle()
    t.color("#556b2f")
    t.begin_fill()
    t.left(90)
    t.forward(150)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(150)
    t.right(90)
    t.forward(100)
    t.end_fill()
    t.penup()
    t.backward(200)
    t.right(90)
    t.forward(110)
    t.pendown()
    t.pencolor("white")
    t.pensize(3)
    for i in range(2):
        t.forward(70)
        t.right(90)
        t.forward(50)
        t.right(90)
    t.forward(35)
    t.right(90)
    t.forward(50)
    t.penup()
    t.backward(149)
    t.pensize(9)
    t.pencolor("brown")
    t.pendown()
    for i in range(2):
        t.right(90)
        t.forward(142)
        t.right(90)
        t.fd(100)
    t.penup()
    t.right(90)
    t.fd(70)
    t.right(90)
    t.forward(20)
    t.pendown()
    t.circle(1)


def grass():
    """
    This function draws the grass below the house
    """
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.penup()
    t.goto(-190, -207)
    for i in range(2):
        t.right(90)
    t.pendown()
    t.color('green')
    t.begin_fill()
    t.circle(100, 180,)
    t.forward(425)
    t.circle(100, 180)
    t.end_fill()


def sun():
    """
    This function draws the sun above the house
    """
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.penup()
    t.goto(-400, 100)
    t.pendown()
    t.color('yellow')
    t.begin_fill()
    t.circle(100)
    t.end_fill()


def main():
    """
    This function draws my beautiful house
    """
    wn = turtle.Screen()
    wn.bgcolor("#87ceeb")
    drawroof()
    drawroofwindow()
    bodyofhouse()
    door()
    grass()
    sun()

    wn.exitonclick()


main()  # Starts the program!
