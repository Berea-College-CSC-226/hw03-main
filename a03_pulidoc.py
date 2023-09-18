

#################################################################################
# Author:Claudia Pulido
# Username: pulidoc
#
# Assignment:Hw3
# Purpose:
# Google Doc Link:
# https://docs.google.com/document/d/1AogX32QRhDn63KLXeTTo4sUARmfhCANY6IuMRZVQCpo/edit
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle


def create_roof(circle):
    """
    Docstring for function_1
    """
    circle.penup()
    circle.setpos(-50, 100)
    circle.pendown()
    circle.begin_fill()
    for i in range(3):
        circle.forward(160)
        circle.left(120)
    circle.end_fill()
    circle.stamp()

    # ....


def create_house(bunny):
    """
    Docstring for function_2
    """
    bunny.penup()
    bunny.setpos(-50, 100)
    bunny.forward(5)
    bunny.pendown()
    bunny.begin_fill()
    for i in range(2):
        bunny.forward(150)
        bunny.right(-270)
        bunny.forward(150)
        bunny.right(-270)
    bunny.end_fill()
    bunny.stamp()
    # ...


def create_window(dolphin):
    """
    create window
    :return: none
    """
    dolphin.penup()
    dolphin.setpos(80, 40)


def main():
    """
    Draws a house and some trees.
    :return none:
    """
    turtle.colormode(255)
    wn = turtle.Screen()  # Makes a new turtle screen
    wn.bgcolor("black")  # Sets background to an image; must be a gif!
    circle = turtle.Turtle()
    circle.speed(1)
    circle.color("purple")

    bunny = turtle.Turtle()
    bunny.speed(1)
    bunny.color("blue")

    dolphin = turtle.Turtle()
    dolphin.speed(1)
    dolphin.color("#D04D70")

    create_roof(circle)      # Function call to function_1
    create_house(bunny)  # Function call to function_2
    create_window(dolphin)  # Function to call to function_3


main()
