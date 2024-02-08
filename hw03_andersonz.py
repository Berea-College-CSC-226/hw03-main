#################################################################################
# Author:Zach Anderson
# Username:andersonz
#
# Assignment:hw03 psychedelic turtles
# Purpose:Draws a prism
# Google Doc Link:https://docs.google.com/document/d/16mN4UUvcI00iAaC6fagV-eFSV3rITOZuQpNa9O2vbgg/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle


def draw_triangle(bob):
    """
    Draws a triangle
    """
    bob.pencolor("black")
    bob.pensize(15)
    bob.forward(200)
    bob.left(130)
    bob.forward(311.145)
    bob.left(100)
    bob.forward(311.145)
    bob.left(130)
    bob.forward(200)


def white_line(bob):
    """
    Connects white line to triangle
    """
    bob.pencolor("white")
    bob.penup()
    bob.forward(-200)
    bob.left(90)
    bob.forward(130)
    bob.right(90)
    bob.forward(-200)
    bob.pensize(10)
    bob.pendown()
    bob.forward(313)


def red_line(bob):
    """
    Connects red line to triangle
    """
    bob.pencolor("red")
    bob.penup()
    bob.goto(-87.00, 135.00)
    bob.pendown()
    for i in range(10):
        bob.pensize(i + 5)
        bob.forward(20)
        bob.left(.7)
    for i in range(10, 20):
        bob.pensize(i + 5)
        bob.forward(10)
    bob.forward(150)


def yellow_line(bob):
    """
    Connects yellow line to triangle
    """
    bob.pencolor("yellow")
    bob.penup()
    bob.goto(-87.00, 132.500)
    bob.setheading(0)
    bob.pendown()
    for i in range(10):
        bob.pensize(i + 5)
        bob.forward(20)
        bob.left(.4)
    for i in range(10, 20):
        bob.pensize(i + 5)
        bob.forward(10)
    bob.forward(150)


def green_line(bob):
    """
    Connects green line to triangle
    """
    bob.pencolor("green")
    bob.penup()
    bob.goto(-87.00, 130.00)
    bob.setheading(0)
    bob.pendown()
    for i in range(10):
        bob.pensize(i + 5)
        bob.forward(20)
    for i in range(10, 20):
        bob.pensize(i + 5)
        bob.forward(10)
    bob.forward(150)


def blue_line(bob):
    """
    Connects blue line to triangle
    """
    bob.pencolor("blue")
    bob.penup()
    bob.goto(-87.00, 127.500)
    bob.setheading(0)
    bob.pendown()
    for i in range(10):
        bob.pensize(i + 5)
        bob.forward(20)
        bob.left(-.4)
    for i in range(10, 20):
        bob.pensize(i + 5)
        bob.forward(10)
    bob.forward(150)


def purple_line(bob):
    """
    Connects purple line to triangle
    """
    bob.pencolor("purple")
    bob.penup()
    bob.goto(-87.00, 125.00)
    bob.setheading(0)
    bob.pendown()
    for i in range(10):
        bob.pensize(i + 5)
        bob.forward(20)
        bob.left(-.8)
    for i in range(10, 20):
        bob.pensize(i + 5)
        bob.forward(10)
    bob.forward(150)


def main():
    """
    Fist sets up the canvas and sets the color to gray, then defines turlte to be named bob, then draws a triangle,
    then connects a white line to that triangle, and finaly runs through five functions all drawing different colored
    lines to make it look like a prism.
    """

    wn = turtle.Screen()
    wn.bgcolor("gray")

    bob = turtle.Turtle()
    draw_triangle(bob)  # draws triangle
    white_line(bob)  # connects line to triangle
    red_line(bob)  # connects red prism to triangle
    yellow_line(bob)  # connects yellow prism to triangle
    green_line(bob)  # connects green prism to triangle
    blue_line(bob)  # connects blue prism to triangle
    purple_line(bob)  # connects purple prism to triangle
    wn.exitonclick()
    # starting point for prism lights (-87.00,130.00)


main()
