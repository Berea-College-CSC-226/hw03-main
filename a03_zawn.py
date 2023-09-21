#################################################################################
# Author: Nyan Lin Zaw
# Username:zawn
#
# Assignment:Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose:To be skillfull in color, function and git
# Google Doc Link:https://docs.google.com/document/d/1r17pww-mxfp3ElXqVg5Uid0_WJ2i8Hf8J6ZJ-g2rC9o/edit?usp=sharing
#
#################################################################################
# Acknowledgements: to Dr Heggen for being a wonderful professor
#
#
#################################################################################


import turtle


def rel1(tr, fr1, fr2):
    """
  to relocate turtle to the bottom right of the screen
    """
    tr.penup()
    tr.right(90)
    tr.forward(fr1)
    tr.right(90)
    tr.forward(fr2)
    tr.right(180)
    tr.pendown()
    #


def relo(tr, x, y, ang):
    """
    to relocated the turtle on x,y plane by using the coordinates.
    """
    tr.penup()
    tr.goto(x, y)
    tr.pendown()
    tr.left(ang)


def door(tr, fr5, fr6):
    """
    to draw the door which will be nested in the house function
    """
    for i in range(2):
        tr.forward(fr5)
        tr.left(90)
        tr.forward(fr6)
        tr.left(90)


def roof(tr, ang1, fr):
    """
    to draw a roof of the church
    """
    tr.left(ang1)
    tr.forward(fr)
    tr.right(90)
    tr.forward(fr)
    tr.left(ang1)
def house(tr, fr3, fr4):
    """
   to draw the rectangle of the church
    """
    for a in range(2):
        tr.forward(fr3)
        tr.left(90)
        tr.forward(fr4)
        tr.left(90)
    tr.forward(fr3 / 2 - 20)
    tr.color("#5C5C57")
    tr.begin_fill()
    door(tr, 40, 80)
    tr.end_fill()
    # ...


def cross(tr, fr7, fr8, clo):
    """
    to draw a cross with variation size
    """
    tr.color(clo)
    tr.begin_fill()
    tr.forward(fr7)
    tr.left(90)
    tr.forward(fr8)
    tr.right(90)
    for b in range(3):
        tr.forward(fr7)
        tr.left(90)
        tr.forward(fr7)
        tr.left(90)
        tr.forward(fr7)
        tr.right(90)
    tr.forward(fr8)
    tr.end_fill()


def ghost(tr, fr9, fr10):
    """
    to draw a ghost to hover on the cemetery
    """
    tr.left(90)
    tr.forward(fr9)
    tr.circle(15, 180, 50)
    tr.forward(fr9)
    for c in range(3):
        tr.left(135)
        tr.forward(fr10)
        tr.right(120)
        tr.forward(fr10)


def main():
    """
    this is main
    """
    # ...
    wn = turtle.Screen()
    tess = turtle.Turtle()
    wn.bgcolor("#1F355C")
    tess.color("#FFFFC6")
    tess.shape("arrow")
    tess.pensize(5)
    tess.speed(0)
    rel1(tess, 250, 250)
    house(tess, 175, 350)
    tess.penup()
    tess.goto(-182.5, -120)
    tess.pendown()
    cross(tess, 40, 100, "#CDF2FF")
    relo(tess, -250, 100, 90)
    roof(tess, 45, 124)
    relo(tess, 0, -250, 360)
    cross(tess, 10, 30, "#CDF2FF")
    relo(tess, 0, -150, 90)
    cross(tess, 10, 30, "#CDF2FF")
    relo(tess, 0, -50, 180)
    tess.right(90)
    cross(tess, 10, 30, "#CDF2FF")
    relo(tess, 100, -150, 90)
    cross(tess, 10, 30, "#CDF2FF")
    relo(tess, 200, -150, 90)
    cross(tess, 10, 30, "#CDF2FF")
    relo(tess, 50, 150, 90)
    ghost(tess, 30, 10)
    relo(tess, 150, 50, 90)
    tess.setheading(0)
    ghost(tess,30,10)
    relo(tess, 300, 70, 90)
    tess.setheading(0)
    ghost(tess, 30, 10)
    wn.exitonclick()


main()

