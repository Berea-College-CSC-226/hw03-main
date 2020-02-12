#################################################################################
# Author: Michael Hohl
# Username: hohlm
#
# Assignment: A03: A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Draws the Danforth building
# Google Doc Link: https://docs.google.com/document/d/1au_vIgBq9R9oMruHW2GL8MeyCLP_8GY-Wk_AulrXdsE/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle


def rectangle(t, x, y, colorpen, colorfill, height, width):
    """
    Draws a rectangle
    :param t: Turtle name
    :param x: Bottom left X position
    :param y: Bottom left Y position
    :param colorpen: Color of the sides
    :param colorfill: Color of the fill
    :param height: Length of the rectangles's x sides
    :param width: Length of the rectangles's y sides
    :return: None
    """
    t.setposition(x, y)
    t.pencolor(colorpen)
    t.fillcolor(colorfill)
    t.pendown()
    t.begin_fill()
    for n in range(2):
        t.forward(height)
        t.right(90)
        t.forward(width)
        t.right(90)
    t.end_fill()
    t.penup()
    # Draws a square


def scalene(t, x, y, pencolor, bgcolor, base):
    """
    Draws a 30-90-60 scalene triangle
    :param t: Turtle name
    :param x: Bottom left X position
    :param y: Bottom left Y position
    :param pencolor: Color of the sides
    :param bgcolor: Color of the fill
    :param base: Length of the base
    :return: None
    """
    t.setposition(x, y)
    t.pencolor(pencolor)
    t.fillcolor(bgcolor)
    t.pendown()
    t.begin_fill()
    t.right(60)
    t.forward(base*0.86602)
    t.right(90)
    t.forward(base*.5)
    t.right(120)
    t.forward(base)
    t.end_fill()
    t.penup()
    t.setheading(90)
    # Draws a 30-90-60 triangle


def entrance(t):
    """
    Draws the entrance of the building
    :param t: Turtle name
    :return: None
    """
    rectangle(t, -150, 0, "white", "black", 32, 16)     # Left Window
    rectangle(t, -134, 0, "white", "black", 32, 24)     # Left Door
    rectangle(t, -110, 0, "white", "black", 32, 24)     # Right Door
    rectangle(t, -86, 0, "white", "black", 32, 16)
    x = -150
    for i in range(5):
        rectangle(t, x, 32, "white", "black", 16, 16)
        rectangle(t, x, 48, "gray", "white", 2, 16)
        x = x + 16


def window(t):
    """
    Draws the window section of the building
    :param t: Turtle name
    :return: None
    """
    x = -70
    for i in range(19):
        rectangle(t, x, 0, "gray", "white", 24, 16)
        rectangle(t, x, 24, "light gray", "white", 24, 16)
        rectangle(t, x, 48, "gray", "white", 2, 16)
        x = x + 16


def roof(t):
    """
    Draws the sawtooth roof
    :param t: Turtle name
    :return: None
    """
    x = -150
    for i in range(6):
        scalene(t, x, 50, "gray", "white", 50)
        x = x + 50


def main():
    """
    Draws the Danforth Technology Building
    :return:
    """
    # Setup
    wn = turtle.Screen()
    wn.bgcolor("#87CEEB")
    tim = turtle.Turtle()
    tim.penup()
    tim.setheading(90)
    tim.speed(0)

    rectangle(tim, -400, 0, "#7CFC00", "#7CFC00", -300, 750)  # Makes the grass grow
    rectangle(tim, -200, 0, "#CB4154", "#CB4154", 50, 50)         # Draws the left section of the building
    entrance(tim)                                         # Draws the entrance
    window(tim)                                           # Draws the right section of the building
    roof(tim)                                             # Draws the roof saw thingies

    wn.exitonclick()
    # Main function


main()
