#################################################################################
# Author: Skylar McDaniel
# Username: mcdaniels
#
# Assignment: HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: To practice the usage of functions and format of scripts
# Google Doc Link: https://docs.google.com/document/d/1wlcpS-7suqoB14_YtH9vi02ABiim4AlqRQeTEtMyr7A/edit?usp=sharing
#
#################################################################################


import turtle


def maketurtle(turtlename, r, g, b, size):
    """
    Creates a turtle.
    """
    turtlename = turtle.Turtle()
    turtlename.color(r, g, b)
    turtlename.hideturtle()
    turtlename.pensize(size)
    turtlename.speed(0)
    return turtlename

def moveto(turtlename, x, y, direction):
    """
    Moves the turtle to desired location.
    """
    turtlename.penup()
    turtlename.goto(x, y)
    turtlename.setheading(direction)
    turtlename.pendown()

def buildingsflat(turtlename, x, y, direction, width, height):
    """
    Creates the base of the buildings in flat colors.
    """
    moveto(turtlename, x, y, direction)
    turtlename.begin_fill()
    for i in range(2):
        turtlename.forward(height)
        turtlename.right(90)
        turtlename.forward(width)
        turtlename.right(90)
    turtlename.end_fill()

def bricks(turtlename, width, height):
    """
    Creates the windows of the buildings.
    """
    turtlename.color(244, 240, 0)
    for i in range(2):
        turtlename.forward(height)
        turtlename.right(90)
        turtlename.forward(width)
        turtlename.right(90)

def main():
    """
    Creates two city buildings at nighttime with windows.
    """
    # screen setup
    wn = turtle.Screen()
    wn.screensize(500, 500)
    wn.colormode(255)
    wn.bgcolor(61, 66, 124)

    # create a turtle
    waluigi = maketurtle("waluigi", 41, 39, 73, 20)

    # building one
    buildingsflat(waluigi, -200, -250, 90, 200, 400)
    # building two
    buildingsflat(waluigi, 0, -250, 90, 200, 500)

    # creates windows
    yIn = -230
    for i in range(5):
        yIn = yIn + 70
        xIn = -180
        for i in range(5):
            moveto(waluigi, xIn, yIn, 90)
            bricks(waluigi, 35, 15)
            xIn = xIn + 70

    yIn = 190
    xIn = 30
    moveto(waluigi, xIn, yIn, 90)
    for i in range(2):
        bricks(waluigi, 35, 15)
        xIn = xIn + 70
        moveto(waluigi, xIn, yIn, 90)

    wn.exitonclick()
main()