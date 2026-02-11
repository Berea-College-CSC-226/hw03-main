#####################################################################################################################
# Author: Artem Kurasov
# Username: kurasova
#
# Assignment: HW03
# Purpose: get used to GitHub and practice working with the turtle module
# Google Doc Link: https://docs.google.com/document/d/1hLxgBxV4L7K39ix4ZtJPwIToweDyPeu30wUBAxvmEsg/edit?usp=sharing
#
#####################################################################################################################
# Acknowledgements:
#
# kfc.png: taken from https://en.wikipedia.org/wiki/KFC
# flowers.png: taken from https://freepngimg.com/png/15354-flowers-png-3
#
# I consulted the Python Documentation for this assignment: https://docs.python.org/3/library/turtle.html#turtle.shape
#
#####################################################################################################################


from turtle import *
from math import pi

def move(t, x, y):
    """
    moves the turtle to the specified coordinates without leaving any trace.
    """
    t.up()
    t.goto(x, y)
    t.down()

def bottlecap(t, n, radius):
    """
    draws a star-like shape, reminiscent of a bottle cap.
    """

    circumference = 2 * pi * radius
    # C = 2πr, which is a math formula for circumference

    part = circumference / n
    # this variable would be the length of one side for a polygon

    step = part / (2**(1/2))
    # this is an actual length of each side of the bottle-cap shape
    # this is a math formula for the leg of an isosceles right triangle

    move(t, t.xcor() - part/2, t.ycor() + radius)
    # when being drawn, the bottle-cap shape goes a little off of the center
    # that's why I decided to move it a bit to the left and to the up
    # (using the turtle's current coordinates: turtle.xcor() and turtle.ycor())

    t.begin_fill()
    for _ in range(n):
        t.left(45)
        t.forward(step)
        t.right(90)
        t.forward(step)
        t.left(45)
        t.right(360 // n)
    t.end_fill()
    # two 45-degree turns to the left and one 90-degree turn to the right is
    # what allows us to draw the bottle-cap shape, not just a polygon

def arched_text(t, radius, phrase, degree = 180):
    """
    writes text like an arch.
    """

    circumference = pi * radius * (degree/180)
    # this is a math formula for a sector of a circle

    step = circumference / len(phrase)
    # distributes the symbols equally across the arch.

    for i in phrase:
        t.up()
        t.forward(step/2)
        t.down()
        t.write(i, font = ("Arial", 12, "bold"), align = "center")
        t.up()
        t.forward(step/2)
        t.right(degree // len(phrase))
        t.down()
    # making two half steps forward ensures the text is center-aligned.


def main():
    s = Screen()
    tess = Turtle()

    tess.shape("circle")
    tess.pensize(5)
    tess.speed(0)

    s.colormode(255)
    s.bgcolor(100, 0, 0)
    s.screensize(500, 500)
    s.addshape("kfc.png")
    s.addshape("flowers.png")

    tess.color("white")
    move(tess, 0, 0)
    bottlecap(tess, 20, 100)
    move(tess, 0, 0)
    tess.shape("kfc.png")
    tess.stamp()
    tess.shape("circle")

    tess.left(84)
    move(tess, -140, -10)
    arched_text(tess, 135, "THE BEST FRIED CHICKEN")

    tess.shape("flowers.png")
    move(tess, 0, -200)
    tess.stamp()
    tess.shape("circle")

    tess.color(100, 0, 0)
    move(tess, 0, 200)

    s.exitonclick()

if __name__ == "__main__":
    main()
