#################################################################################
# Author: Galina Pokitko
# Username: pokitkog
#
# Assignment: draw a complex house using turtle graphics
# Purpose: practice using functions and working on dealing with GitHub
# Google Doc Link: https://docs.google.com/document/d/1nGBaaGFuUaYQQ-xqeM0qtCf1zjFduuhstGlMuZziIF8/edit
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle


def draw_window(w):
    """
       Draws two windows for the house.
    """

    w.fillcolor("#BCE6E6")
    w.begin_fill()
    for i in range(2):
        w.forward(75)
        w.left(90)
        w.forward(75)
        w.left(90)
    w.end_fill()

    w.forward(37.5)
    w.left(90)
    w.forward(75)

    for i in range(2):
        w.left(90)
        w.forward(37.5)

    w.left(90)
    w.forward(75)

def draw_door(d):
    """
    Draws door for house.
    """
    d.penup()
    d.left(180)
    d.fd(150)
    d.left(90)
    d.fd(82)
    d.pendown()

    d.fillcolor("#8E674D")
    d.begin_fill()
    d.left(180)
    d.forward(200)
    d.left(90)
    d.forward(100)
    d.left(90)
    d.forward(200)
    d.end_fill()



def draw_house(h):
    """
    Draws a house using a square and triangle for the roof.
    """

    h.begin_fill()
    for i in range(2):
        h.forward(500)
        h.left(90)
        h.forward(300)
        h.left(90)
    h.end_fill()

    h.penup()
    h.left(90)
    h.forward(300)
    h.pendown()

    h.fillcolor("#B31F29")
    h.begin_fill()
    h.right(65)
    h.forward(290)
    h.right(52)
    h.forward(265)
    h.end_fill()


def main():
    """
    Sets up the screen and uses turtles to draw a house with windows and a door.
    """

    wn = turtle.Screen()
    wn.bgpic("landscape.png")

    houseObject = turtle.Turtle()
    houseObject.pensize(10)
    houseObject.speed(10)
    houseObject.fillcolor("#AAAF89")

    houseObject.up()
    houseObject.goto(-250, -200)
    houseObject.down()

    draw_house(houseObject)


    windowObject = turtle.Turtle()
    windowObject.speed(10)

    windowObject.up()
    windowObject.goto(-200,-150)
    windowObject.down()

    draw_window(windowObject)

    windowObject.up()
    windowObject.goto(120, -150)
    windowObject.down()

    draw_window(windowObject)


    doorObject = turtle.Turtle()
    doorObject.speed(10)

    doorObject.up()
    doorObject.goto(200, -113)
    doorObject.down()

    draw_door(doorObject)

    wn.exitonclick()
main()