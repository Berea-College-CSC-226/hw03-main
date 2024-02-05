#################################################################################
# Author: Samuel McFarland
# Username: mcfarlands
#
# Assignment: Homework 03
# Purpose: Use turtles to draw a complex picture, get acquainted with functions, and learn to use Git pull requests.
# Google Doc Link: https://docs.google.com/document/d/1Xg2nZ8jbQbaRZrFfuFfSr1sExkCC4W9jZvHoHLHrQH4/edit?usp=sharing
#
#################################################################################
# Acknowledgements: https://rgbcolorcode.com/ - Used for finding RGB values used in the code.
#
#
#################################################################################

import turtle   # Allows us to use the turtle module in the code.


def draw_grass(t):  # Function that draws grass in the window.
    """ Make turtle t draw grass on the window."""
    t.speed(0)
    t.penup()
    t.goto(-700, -370)
    t.fillcolor("green")
    t.begin_fill()
    t.forward(1500)
    t.left(90)
    t.forward(300)
    t.left(90)
    t.forward(1500)
    t.left(90)
    t.forward(300)
    t.end_fill()


def draw_house(t):  # Draws a house in the window.
    """ Make turtle t draw a house with a door. """
    t.penup()
    t.hideturtle()
    t.color(102, 68, 0)
    t.speed(0)
    t.goto(-100, 110)
    t.fillcolor(102, 68, 0)

    t.begin_fill()  # (Lines 44-52) Fills in a brown square for the body of the house.
    t.forward(200)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(200)
    t.end_fill()

    t.fillcolor("red")     # (Lines 54-63) Draws a red roof on the house.
    t.color("red")
    t.begin_fill()
    t.right(45)
    t.forward(141.421)
    t.right(90)
    t.forward(141.421)
    t.right(135)
    t.forward(200)
    t.end_fill()

    t.fillcolor("yellow")    # (Lines 65-79) Draws a yellow door so the house has an entrance.
    t.color("yellow")
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(80)
    t.begin_fill()
    t.forward(40)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(100)
    t.end_fill()

    t.goto(0, 0)   # (Lines 81-83) Goes to the center of the screen to print a message.
    t.color("red")
    t.write("Welcome to my crib!", align="center", font=("Arial", 30))


def draw_sky(t):    # Uses a turtle to draw the sun and a cloud in the sky.
    """ Make turtle t draw the sun and a cloud on the window. """
    t.hideturtle()  # hides the turtle shape
    t.speed(0)
    t.penup()
    t.color("yellow")
    t.goto(-200, 250)
    t.dot(80)       # Makes a dot on the turtles location with a size of 80.

    t.color("white")    # (Lines 95-107) Using t.dot, it creates a cloud in the sky.
    t.goto(200, 200)
    t.dot(60)
    t.forward(40)
    t.dot(50)
    t.left(45)
    t.forward(40)
    t.dot(60)
    t.left(135)
    t.forward(40)
    t.dot(60)
    t.forward(45)
    t.dot(50)


def main():  # Calls the previously defined functions to draw a whole picture.
    """ Use draw_grass, draw_sky, and draw_house functions to assemble a complete picture. """
    turtle.colormode(255)   # Allows us to use RGB values for colors.
    wn = turtle.Screen()
    wn.bgcolor(87, 216, 255)    # Sets the background color of the window to a light blue.

    roger = turtle.Turtle()     # (Lines 116-118) Creates the turtles to be used in our previously defined functions.
    jenny = turtle.Turtle()
    mike = turtle.Turtle()

    draw_grass(roger)
    draw_sky(mike)
    draw_house(jenny)

    wn.exitonclick()


main()
