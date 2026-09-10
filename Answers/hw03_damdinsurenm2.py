#################################################################################
# Author: Michael Damdinsuren
# Username: damdinsurenm2
#
# Assignment: Turtle Project
# Purpose: Make design using turtles
# Google Doc Link: https://docs.google.com/document/d/1gIlcfwIxLvQ4U5u7RQEEqbjnZf8J-Sm4ciO3QzV_nLE/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################


import turtle

def draw_house_frame(shape):
    """
    Example docstring for function_1. function_1 is not a good function name and should be changed.
    """
    shape.color("white")
    shape.teleport(-180,-200)
    shape.fillcolor("white")

    shape.begin_fill()

    shape.left(90)
    shape.forward(250)
    shape.right(45)
    shape.forward(250)
    shape.right(90)
    shape.forward(250)
    shape.right(45)
    shape.forward(250)
    shape.right(90)
    shape.forward(354)

    shape.end_fill()

def main():
    """
    Docstring for main. Should describe the main functionality of this file.
    """
    wn = turtle.Screen()
    wn.colormode(255)
    wn.bgcolor(144,213,255)
    shape = turtle.Turtle()
    shape.hideturtle()

    draw_house_frame(shape)

    wn.exitonclick()

main()