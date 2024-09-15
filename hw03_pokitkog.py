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

#my functions

def window(w):
    """
       Draws two windows for the house (plus door).
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


#2nd window
    w.penup()
    w.forward(250)
    w.pendown()

    w.begin_fill()

    w.right(90)
    w.forward(37.5)
    w.left(90)

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


#draw door
    w.penup()
    w.left(180)
    w.fd(150)
    w.left(90)
    w.fd(82)
    w.pendown()

    w.fillcolor("#8E674D")
    w.begin_fill()
    w.left(180)
    w.forward(200)
    w.left(90)
    w.forward(100)
    w.left(90)
    w.forward(200)
    w.end_fill()



def house(h):
        """
        Draws a house using a square and triangle for the roof.
        """

        #square body
        h.begin_fill()
        for i in range(2):
            h.forward(500)
            h.left(90)
            h.forward(300)
            h.left(90)
        h.end_fill()

        # triangle roof
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

    wn = turtle.Screen()
    wn.bgpic("landscape.png")

    #turtle (house) object 1

    houseObject = turtle.Turtle()
    houseObject.pensize(10)
    houseObject.speed(5)
    houseObject.fillcolor("#AAAF89")


#position start of house shape
    houseObject.up()
    houseObject.goto(-250, -200)
    houseObject.down()

    house(houseObject)





#turtle (window) object 2
    windowObject = turtle.Turtle()
    windowObject.speed(10)

#change position of where window is drawn
    windowObject.up()
    windowObject.goto(-200,-150)
    windowObject.down()

    window(windowObject)

    wn.exitonclick()
main()