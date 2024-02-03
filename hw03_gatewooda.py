#################################################################################
# Author: Austin Gatewood
# Username:gatewooda
#
# Assignment:hw03 psychedelic turtles
# Purpose:learn pull requests/ git in general
# Google Doc Link:https://docs.google.com/document/d/1KOOO9_UM-Ka7Hg6IGKj9Xm-SKa6xDAZhze_jKE_fc78/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################
import turtle
import math

def face(radius):    # super slow creation
    """
    Will create the face for the 3d glasses.
    """
    happy = turtle.Turtle()  # will create the face for the glasses
    happy.hideturtle()
    happy.speed(0)
    happy.color("#087209")

    # Move forward to the position where the face should start
    happy.penup()
    happy.goto(20, -radius)
    happy.pendown()

    # Draw a circle
    for _ in range(360):
        happy.forward(radius * 2 * math.pi / 360)     # this might be why
        happy.left(1)




def glasses_draw():
    """"
    Will create 3d glasses to go on their face
    """

    found = turtle.Turtle()
    found.penup()
    found.hideturtle()
    found.goto(-10, 10)
    found.pendown()

    for side in range(4):
        found.forward(50)
        found.right(90)

    for i in range(2):
        found.right(225)
        found.forward(50)

    found.penup()
    found.goto(40, 10)
    found.pendown()
    found.setheading(0)
    found.forward(30)

    for side in range(4):
        found.forward(50)
        found.right(90)

    found.forward(50)

    for i in range(2):
        found.right(225)
        found.forward(50)


def comment():
    text = turtle.Turtle()
    text.penup()
    text.goto(-60,0)
    text.write("erm actually", align="right", font=("calibri", 24, "normal"))
    text.hideturtle() # id like to add more details like a mouth to add to the complex requirement

def main():
    """
    Docstring for main. Should describe the main functionality of this file.
    """
    text = turtle.Turtle()
    # Function calls to glasses_draw , face, and comment
    wn = turtle.Screen()
    face(75)
    glasses_draw()
    comment()
    wn.exitonclick()

main()  # Starts the program!

