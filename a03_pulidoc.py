

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
    circle.setpos(-50,100)
    circle.pendown()
    circle.begin_fill()
    for i in range(3):
        circle.forward(160)
        circle.left(120)
    circle.end_fill()
    circle.stamp()

    # ....


def function_2():
    """
    Docstring for function_2
    """
    pass
    # ...


def main():
    """
    Docstring for main
    """
    # ...

    wn = turtle.Screen()  # Makes a new turtle screen
    wn.bgcolor("black")  # Sets background to an image; must be a gif!
    circle = turtle.Turtle()
    circle.speed(1)
    circle.color("purple")

    create_roof(circle)  # Function call to function_1
    function_2()  # Function call to function_2


main()
