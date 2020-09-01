####################################################################
# Author: Ndizeye Tschesquis
# Username: tschesquisn
#
# Assignment: A03:
# Purpose: Learn about branching and pull requests
# Google Doc Link: https://docs.google.com/document/d/1SRFFZfc9JMOGY7m7fqqXt14In3wUl-YUaVTJxr8e5q0/edit?usp=sharing
####################################################################
# Acknowledgements:
# t02_turtle_spiral.py
#
#################################################################################

import turtle


def roof(fish):
    """
    this function make the roof of the building
    :param fish: name of the turtle
    :return:
    """
    fish.penup()
    fish.setpos(-260, 45)
    fish.pendown()
    fish.fillcolor("red")
    fish.begin_fill()
    fish.fd(220)
    fish.left(120)
    fish.fd(50)
    fish.left(60)
    fish.fd(171)
    fish.left(60)
    fish.fd(60)
    fish.end_fill()


def rectangle(fish, w, l):
    """
    This function make a rectangle with the width and length of choice
    :param fish: Name of the Turtle
    :param w: Width of the rectangle
    :param l: length of the rectangle
    :return:
    """
    for x in range(2):
        fish.forward(w)
        fish.left(90)
        fish.forward(l)
        fish.left(90)


def make_windows(fish, amount, xcor, goup=-0):
    """
    this function uses the rectangle function to make windows for the building
    :param fish: Name of the turtle
    :param amount: amount of windows to make
    :param xcor: sets the X-Coordinate
    :param goup: sets the Y-coordinate with a starting value of -300
    :return:
    """

    for x in range(amount):
        fish.penup()
        fish.fillcolor("white")
        fish.begin_fill()
        goup = goup + 55  # got the idea from t02_turtle_spiral.py example
        fish.goto(xcor, goup)
        fish.pendown()
        rectangle(fish, 50, 50)
        fish.penup()
        fish.end_fill()


def main():
    wn = turtle.Screen()
    wn.bgcolor("grey")  # sets the window to a grey color
    fish = turtle.Turtle()
    fish.penup()
    fish.goto(-260, -260)
    fish.pendown()

    ##########################################
    # The following will make a black building shape
    fish.fillcolor("black")
    fish.begin_fill()
    rectangle(fish, 220, 305)
    fish.end_fill()

    fish.penup()
    fish.goto(-175, -260)
    fish.pendown()
    ##########################################
    # The following will make a door and paint it red
    fish.fillcolor("red")
    fish.begin_fill()
    rectangle(fish, 50, 75)
    fish.end_fill()
    ###########################################
    # the following will make windows
    make_windows(fish, 5, -245, goup=-290)  # Makes 5 windows on the left side of the building
    make_windows(fish, 4, -175, goup=-235)  # Makes 4 windows above the door
    make_windows(fish, 5, -105, goup=-290)  # Makes 5 windows on the right side of the building

    roof(fish)

    wn.exitonclick()


if __name__ == '__main__':
    main()
