#################################################################################
# Author: Sam Edelman
# Username: edelmans
#
# Assignment: hw03 Fully Functional Gitty Psychedelic Robotic Turtles
#
# Purpose:
#   Continue practicing creating and using functions.
#   More practice on using the turtle library.
#   Learn about how computers represent colors.
#   Learn about source control and Git.
#
# Google Doc Link: https://docs.google.com/document/d/1d-mX4dTe4ysHzNasPZLG1phhV-ksM9_mMCXrIqtT3wU/edit#heading=h.ju96mtye4s7l
#################################################################################
# Acknowledgements: Scott Heggen (for template)
#
#################################################################################

import turtle


def head():
    """
    Head of turtle
    """
    skull = turtle.Turtle()
    skull.pensize(10)
    skull.pencolor("#64ae26")
    skull.speed(10)
    skull.penup()
    skull.goto(220, -45)
    skull.pendown()

    skull.left(25)
    skull.forward(100)
    skull.right(110)
    skull.forward(45)
    skull.right(90)
    skull.forward(40)
    skull.left(10)
    skull.forward(15)
    skull.left(90)
    skull.forward(15)
    skull.left(70)
    skull.forward(45)
    skull.right(140)
    skull.forward(45)
    skull.right(45)
    skull.forward(60)

    skull.shape("circle")
    skull.shapesize(.5, .5, .5)
    skull.penup()
    skull.goto(280, -35)
    skull.stamp()

    skull.penup()
    skull.goto(1000, 1000)
    # ....


def tail():
    """
    Tail of turtle
    """

    spine = turtle.Turtle()
    spine.pensize(10)
    spine.pencolor("#64ae26")
    spine.speed(10)
    spine.penup()
    spine.goto(-210, -40)
    spine.pendown()

    spine.left(195)
    spine.forward(90)
    spine.left(30)
    spine.forward(60)
    spine.left(30)
    spine.forward(50)
    spine.left(30)
    spine.forward(30)
    spine.left(45)
    spine.forward(90)
    spine.left(20)
    spine.forward(120)
    spine.left(170)
    spine.forward(100)
    spine.right(20)
    spine.forward(50)
    spine.right(20)
    spine.forward(40)
    spine.right(70)
    spine.forward(60)
    spine.right(40)
    spine.forward(60)

    spine.penup()
    spine.goto(1000, 1000)


def body():
    """
    Body of turtle
    """
    shell = turtle.Turtle()
    shell.pensize(10)
    shell.pencolor("#295412")
    shell.speed(10)
    shell.penup()
    shell.goto(-195, -100)
    shell.pendown()

    shell.right(5)
    shell.forward(200)
    shell.left(10)
    shell.forward(200)
    shell.left(75)
    shell.forward(80)
    shell.left(70)
    shell.forward(180)
    for i in range(3):
        shell.left(15)
        shell.forward(40)
    shell.left(15)
    shell.forward(180)
    shell.left(70)
    shell.forward(80)

    shell.penup()
    shell.goto(1000, 1000)
    # ...


def main():
    """
    Drawing a alligator snapping turtle
    """
    # ...
    window = turtle.Screen()
    window.bgcolor("#5f3414")
    head()            # Function call to function_1
    tail()
    body()            # Function call to function_2

    window.exitonclick()


main()
