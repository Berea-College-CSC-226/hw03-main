#################################################################################
# Author: Jose Zapata
# Username: zapatamezaj
# Google Doc Link: https://docs.google.com/document/d/1Zq2as7MCc36fKQ-mG_TrKfXLLRpVSfLs4w7kI8JvUmM/edit?usp=sharing
#
# Assignment: A03
# Purpose: More practice on using the turtle library. Learn about how computers represent colors.
#################################################################################
# Acknowledgements:

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
#################################################################################

import turtle

wn = turtle.Screen()
wn.colormode(255)
wn.bgcolor(120, 150, 130)
# sets the background color to xanadu


jose = turtle.Turtle()
# creates the turtle Jose


def roof():
    """
    Creates a red roof using the turtle Jose.
    """
    jose.color("red")
    jose.begin_fill()
    for i in range(3):
        jose.forward(250)
        jose.left(120)
        # Uses a loop to make a triangle.


def house():
    """
    Creates the body of the blue house using the turtle Jose.
    """

    jose.color(50, 50, 200)
    for i in range(4):
        jose.forward(250)
        jose.right(90)
        # Uses a loop to make a rectangle.


def window():
    """
    Creates blue windows of the house using the turtle Jose.
    """
    jose.penup()
    jose.setpos(25, -50)
    jose.pendown()
    for i in range(4):
        jose.forward(75)
        jose.right(90)
    jose.penup()
    jose.setpos(150, -50)
    jose.pendown()
    for i in range(4):
        jose.forward(75)
        jose.right(90)
    # Uses loops to make two windows.


def door():
    """
    Creates a door using the turtle Jose.
    :return: 
    """
    jose.penup()
    jose.setpos(100, -150)
    jose.pendown()
    jose.color("black")
    for i in range(2):
        jose.forward(50)
        jose.right(90)
        jose.forward(100)
        jose.right(90)
        # Uses a loop to make a door.


def fence():
    """
    Creates a white picket fence using the turtle Jose.
    """
    jose.penup()
    jose.setpos(-350, -200)
    jose.pendown()
    jose.color("white")
    for i in range(18):
        jose.forward(20)
        jose.right(90)
        jose.forward(75)
        jose.right(90)
        jose.forward(20)
        jose.right(90)
        jose.forward(75)
        jose.right(90)
        jose.penup()
        jose.forward(39)
        jose.pendown()
        # Uses a loop to make a lot of fences.


def sun():
    """
    Creates a yellow sun with the turtle Jose.
    """
    jose.penup()
    jose.setpos(-250, 175)
    jose.pendown()
    jose.color("yellow")
    jose.begin_fill()
    jose.circle(50)
    jose.end_fill()
    jose.hideturtle()
    # Uses the fill function to draw a bright yellow sun.


def main():
    """
    Creates the entire house using all of the functions.
    """
    roof()
    house()
    window()
    door()
    fence()
    sun()
    wn.exitonclick()


main()

