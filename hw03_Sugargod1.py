#################################################################################
# Author: Sugarragchaa Tumur-Ochir
# Username: Sugargod1
#
# Assignment: hw03_Sugargod1
# Purpose: Better understanding of git and Github
# Google Doc Link: https://docs.google.com/document/d/17NHKwPKQIHpA5JfAf-XqfP_sFllP3Gk8PNOkkDWPsdk/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
# Used Python Documentation(https://docs.python.org/3/library/turtle.html)
#################################################################################

import turtle


def housebody(turti):
    """
    Given a position of house's upper right corner then started drawing frame then fills it
    """
    turti.pencolor('orange')
    turti.penup()
    turti.goto(200, 50)
    turti.pendown()
    turti.left(180)
    turti.pensize(15)
    turti.begin_fill()
    turti.fillcolor('orange')
    turti.begin_fill()
    for i in range(4):  # Making a rectangular door
        turti.forward(400)
        turti.left(90)
    turti.end_fill()


def roofy(turti):
    """
    Draws house's roof by going to upper left corner and started drawing the fills
    """

    turti.fillcolor('pink')
    turti.penup()
    turti.goto(-210, 50)
    turti.pendown()
    turti.right(180)
    turti.pencolor('blue')
    turti.begin_fill()
    for i in range(3):  # Making a rectangular door
        turti.forward(420)
        turti.left(120)
    turti.end_fill()


def doory(turti):
    """
    Given a position near bottom right and draws a brown door
    """

    turti.penup()
    turti.goto(-60, -365)
    turti.pendown()
    turti.pencolor('brown')
    turti.begin_fill()
    turti.forward(140)
    turti.left(90)
    turti.forward(280)
    turti.left(90)
    turti.forward(140)
    turti.left(90)
    turti.forward(280)
    turti.end_fill()


def windowy(turti):
    """
    goes to the window space and draws the window
    """

    turti.penup()
    turti.goto(-200, 0)  # Position the turtle to draw the horizontal line
    turti.pendown()
    turti.pensize(5)
    turti.pencolor('white')
    for i in range(4):
        turti.forward(40)
        turti.left(90)
    turti.penup()
    turti.goto(-160, 0)  # Position the turtle to draw the horizontal line
    turti.pendown()
    for i in range(4):
        turti.forward(40)
        turti.left(90)
    turti.penup()
    turti.goto(-200, -40)  # Position the turtle to draw the horizontal line
    turti.pendown()
    for i in range(4):
        turti.forward(40)
        turti.left(90)
    turti.penup()
    turti.goto(-160, -40)  # Position the turtle to draw the horizontal line
    turti.pendown()
    for i in range(4):
        turti.forward(40)
        turti.left(90)
    turti.penup()
    turti.goto(110, 0)  # Position the turtle to draw the horizontal line
    turti.pendown()
    for i in range(4):
        turti.forward(40)
        turti.left(90)
    turti.penup()
    turti.goto(150, 0)  # Position the turtle to draw the horizontal line
    turti.pendown()
    for i in range(4):
        turti.forward(40)
        turti.left(90)
    turti.penup()
    turti.goto(110, -40)  # Position the turtle to draw the horizontal line
    turti.pendown()
    for i in range(4):
        turti.forward(40)
        turti.left(90)
    turti.penup()
    turti.goto(150, -40)  # Position the turtle to draw the horizontal line
    turti.pendown()
    for i in range(4):
        turti.forward(40)
        turti.left(90)


def main():
    """
    Creates a house with a roof, a body, a door, and two windows
    """

    alpha = turtle.Turtle()
    wn = turtle.Screen()
    wn.bgcolor("#7B68EE")
    housebody(alpha)
    roofy(alpha)
    doory(alpha)
    windowy(alpha)
    wn.exitonclick()


main()  # Starts the program!
