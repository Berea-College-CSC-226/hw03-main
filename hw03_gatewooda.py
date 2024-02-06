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
#https://www.geeksforgeeks.org/draw-circle-in-python-using-turtle/
# https://github.com/Berea-College-CSC-226/hw03-main/assets/147771488/f83d1a85-f43c-4b43-a752-2acc79d48d96)
#################################################################################
import turtle
import math


def face(radius):  # super slow creation
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
    for _ in range(360):  # In the range of 360 degrees radius is doubled than multiplied by pi
        happy.forward(radius * 2 * math.pi / 360)  # then divided by 360 degrees... If too small of radius circle
        # will not complete
        happy.left(1)  # If anything other than 1 it will be disproportionately small/big


def glasses_draw():
    """"
    Will create 3d glasses to go on their face
    """

    found = turtle.Turtle()
    found.penup()
    found.hideturtle()  # Creates the turtle than hides it for style
    found.goto(-10, 10)  # good position for glasses on "face"
    found.pendown()

    for side in range(4):  # creates first "lens"
        found.forward(50)
        found.right(90)

    for i in range(2):  # creates the ear part of the glasses
        found.right(225)
        found.forward(50)

    found.penup()
    found.goto(40, 10)  # moves to create the glasses bridge
    found.pendown()
    found.setheading(0)  # resets the positioning
    found.forward(30)   # creates the bridge

    for side in range(4):  # second lens
        found.forward(50)
        found.right(90)

    found.forward(50)   # moves forward so the second earpiece is on the outside of glasses

    for i in range(2):  # second earpiece
        found.right(225)
        found.forward(50)


def comment():
    """
    creates the nerds comment on the screen
    """

    text = turtle.Turtle()
    text.penup()
    text.goto(-60, 0)  # I found that moving the turtle works better than the align function below
    text.write("erm actually", align="right", font=("calibre", 24, "normal"))
    text.hideturtle()


def main():
    """
    Calls all functions defined in the code above, draws the Nerds face and glasses with his nerd Comment!
    """

    # Function calls to glasses_draw , face, and comment
    wn = turtle.Screen()
    face(75)
    glasses_draw()
    comment()
    wn.exitonclick()


main()  # Starts the program!
