#################################################################################
# Author: Kafui
# Username: glek
#
# Assignment: hw03
# Purpose: Implemented a code that draws a house
# Google Doc Link: https://docs.google.com/document/d/1yGLLdFBhjPw96O7yJiaUsUuLIPZWXuOvJ6QDpzMWM_c/edit#heading=h.j4414z2ufr72
#
#################################################################################
# Acknowledgements: Tojo Tsimalay
#
#
#################################################################################

import turtle     # this imports the turtle.


def drawkkg():
    """
    This function draws the door, windows and roof of the house.
    """
    kkg = turtle.Turtle()
    kkg.pensize(15)
    kkg.penup()
    kkg.goto(-250, -250)
    kkg.pendown()
    kkg.forward(200)
    kkg.left(90)
    kkg.forward(140)
    kkg.right(45)
    kkg.forward(60)
    kkg.right(90)
    kkg.forward(60)
    kkg.right(45)
    kkg.forward(140)

    kkg.right(90)
    kkg.penup()
    kkg.forward(280)
    kkg.right(90)
    kkg.forward(350)
    kkg.pendown()
    kkg.color(0, 255, 0)
    kkg.right(45)
    kkg.forward(250)
    kkg.right(90)
    kkg.forward(250)
    kkg.hideturtle()
    kkg.penup()
    kkg.goto(-5, -5)
    kkg.pendown()
    kkg.left(45)

    for k in range(4):    # this is the for loop that is meant to draw the inner windows of the house.
        kkg.forward(45)
        kkg.left(90)

    kkg.penup()
    kkg.goto(-150, -6)
    kkg.pendown()

    for l in range(4):
        kkg.forward(45)
        kkg.left(90)


def drawomo():
    """
    This function draws the outer square of the house.
    """
    omo = turtle.Turtle()
    omo.pensize(15)
    omo.penup()
    omo.goto(-250, -250)
    omo.pendown()
    omo.hideturtle()

    # This for loop draws the outer square of the house.
    for i in range(4):
        omo.forward(350)
        omo.left(90)


def main():
    """
    This function creates the screen and the background color of the turtle screen.
    """
    wn = turtle.Screen()
    wn.colormode(255)
    wn.bgcolor(145, 180, 167)   # this sets the background color of the screen using rgb values.
    # Function calls to function_1 and function_2.
    drawomo()
    drawkkg()
    wn.exitonclick()


main()        # Starts the program!


