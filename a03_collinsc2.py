#################################################################################
# Author: Cole Collins
# Username: collinsc2
#
# Assignment: HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose:
# Google Doc Link: https://docs.google.com/document/d/1itSw0tFeor3TvMc2jZ3oWxOdPR9XmoUvIeU5qbnJzSo/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle


def barn(zeus, hera):
    """
    This function creates the barn
    One turtle(zeus) makes the body
    The other(hera) makes the roof
    """
    hera.penup()
    hera.setpos(-300, 20)
    hera.pendown()
    hera.begin_fill()
    hera.color("white")
    for i in range(3):
        hera.left(45)
        hera.forward(83)
        hera.right(90)
    hera.end_fill()
# The above code makes the roof
    zeus.penup()
    zeus.setpos(-300, -100)
    zeus.pendown()
    zeus.color("#C71313")
    zeus.begin_fill()
    for i in range(2):
        zeus.forward(200)
        zeus.left(90)
        zeus.forward(120)
        zeus.left(90)
    zeus.end_fill()
# The above code makes the body
    pass
    # ....


def windows_doors(zeus, hera):
    """
    zeus is making the doors
    hera is making two windows
    """
    zeus.penup()
    zeus.setpos(-200, -100)
    zeus.pendown()
    zeus.color("white")
    zeus.pensize(4)
    for i in range(4):
        zeus.forward(25)
        zeus.left(90)
        zeus.forward(25)
    zeus.color("white")
    zeus.setpos(-225, -100)
    zeus.setpos(-175, -50)
    zeus.setpos(-225, -50)
    zeus.setpos(-175, -100)
    zeus.setpos(-200, -100)
    zeus.setpos(-200, -50)
# The above code is the door
    hera.penup()
    hera.color("orange")
    hera.setpos(-280, 0)
    hera.left(135)
    hera.pendown()
    hera.begin_fill()
    for i in range(4):
        hera.forward(30)
        hera.right(90)
    hera.end_fill()
    hera.penup()
    hera.color("white")
    hera.setpos(-265, 0)
    hera.pendown()
    hera.setpos(-265, -30)
    hera.penup()
    hera.setpos(-280, -15)
    hera.pendown()
    hera.setpos(-250, -15)
# The above code is the first window
    hera.penup()
    hera.setpos(-150, 0)
    hera.pendown()
    hera.color("orange")
    hera.begin_fill()
    for i in range(4):
        hera.forward(30)
        hera.right(90)
    hera.end_fill()
    hera.penup()
    hera.color("white")
    hera.setpos(-135, 0)
    hera.pendown()
    hera.setpos(-135, -30)
    hera.penup()
    hera.setpos(-120, -15)
    hera.pendown()
    hera.setpos(-150, -15)
# The above code is the second window
    pass
    # ...


def main():
    """
    Docstring for main
    """
    wn = turtle.Screen()
    turtle.Screen().setup(700, 700)
    wn.bgcolor("#A7EBE6")

    zeus = turtle.Turtle()
    hera = turtle.Turtle()

    # ...
    barn(zeus, hera)  # Function call to barn
    windows_doors(zeus, hera)  # Function call to windows
    wn.exitonclick()


main()
