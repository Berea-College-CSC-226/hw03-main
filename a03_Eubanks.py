##########################################################################
# eubanksn - Noah Eubanks
# a03-psychedelic turtles
#######################################################################

import turtle


def square():
    """This function draws the outside of the house. """
    box = turtle.Turtle()
    box.color("green")
    box.pensize(5)

    for i in range(2):
        box.forward(250)
        box.right(90)
        box.forward(250)
        box.right(90)


def door():
    """this creates the door"""
    dave = turtle.Turtle()
    dave.penup()
    dave.forward(250)  # this is setting the position at the bottom of square
    dave.right(90)
    dave.forward(250)
    dave.right(90)
    dave.forward(80)

    dave.pendown()
    dave.pencolor("purple")
    dave.right(90)
    dave.forward(100)  # this is actually creating the door
    dave.left(90)
    dave.forward(100)
    dave.left(90)
    dave.forward(100)


def roof():
    """makes roof of house"""
    jeb = turtle.Turtle()
    jeb.pensize(10)
    jeb.left(60)
    jeb.forward(200)
    jeb.right(110)
    jeb.forward(220)


def windows():
    deb = turtle.Turtle()
    deb.penup()
    deb.pensize(5)
    deb.right(90)
    deb.forward(20)
    deb.pencolor(165, 100, 20)  # makes first window
    deb.left(90)
    deb.forward(10)
    deb.pendown()

    for g in range(2):
        deb.forward(40)
        deb.right(90)
        deb.forward(40)
        deb.right(90)

    deb.penup()
    deb.forward(160)
    deb.pendown()

    for h in range(2):
        deb.forward(40)
        deb.right(90)
        deb.forward(40)
        deb.right(90)


def main():
    wn = turtle.Screen()

    wn.bgcolor("red")
    wn.colormode(255)

    square()

    door()

    roof()

    windows()

    wn.exitonclick()


main()
