#################################################################################
# Author: Phun Mualcin
# Username:mualcinp
#
# Assignment:Drawing a house
# Purpose:
# Google Doc Link: https://docs.google.com/document/d/18hX6TBTxMAM3jqEVwUzHyhHAaNCBpwCo1KeekIJJCHw/edit#
#
#################################################################################
#
#
#
#################################################################################


import turtle


def create_box():
    """
    this function draws the bottom half of a house
    """
    square = turtle.Turtle()
    square.color("black")
    square.pensize(6)

    for i in range(2):
        square.forward(200)
        square.right(90)
        square.forward(200)
        square.right(90)
        square.forward(90)


def create_roof():
    """
    creates roof of house
    """
    tri = turtle.Turtle()
    tri.forward(200)
    tri.left(120)
    tri.forward(290)
    tri.left(120)
    tri.forward(300)


def create_window():
    """creates windows"""
    fry = turtle.Turtle()
    fry.pencolor(100, 40, 69)
    fry.penup()
    fry.right(90)
    fry.forward(30)
    fry.pendown()
    fry.right(90)
    fry.forward(50)
    fry.left(90)
    fry.forward(50)
    fry.left(90)
    fry.forward(50)
    fry.left(90)
    fry.forward(50)
    fry.penup()

    fry.right(90)
    fry.forward(110)

    for i in range(2):
        fry.pendown()
        fry.forward(50)
        fry.right(90)
        fry.forward(50)
        fry.right(90)
    fry.penup()


def create_door():
    dor = turtle.Turtle()
    dor.penup()
    dor.forward(30)
    dor.right(90)
    dor.forward(200)
    dor.pendown()
    dor.left(180)
    dor.forward(90)
    dor.right(90)
    dor.forward(60)
    dor.right(90)
    dor.forward(90)


def main():
    wn = turtle.Screen()

    wn.colormode(255)
    wn.bgcolor("pink")

    create_box()

    create_roof()

    create_window()

    create_door()

    wn.exitonclick()


main()
