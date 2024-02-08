#################################################################################
# Author:Aaliyah Murphy
# Username:Murphya
#
# Assignment:Hw03
# Purpose:Turtle practice and GIT branching.
# Google Doc Link:https://docs.google.com/document/d/1QOq5mSUdxNJacGKRdWqrQEk5mgNh5cuqwZO52XxC4JY/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle

def drawRectangle(t, w, h):
    """Makes rectangle with sides 180 and 75"""
    for i in range(2):
        t.begin_fill()
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
        t.end_fill()

def drawFlag(t, sz):
    """Makes square with sides 50"""
    t.begin_fill()
    for i in range(4):
        t.color("#A24C66", "#A24C66")
        t.forward(sz)
        t.left(90)
    t.end_fill()

def drawBoat(t):
    """Draws a boat with the given turtle t"""
    t.penup()
    t.goto(-90,-150)
    t.pendown()
    t.color("#8E5B3A", "#8E5B3A")
    t.begin_fill()
    t.right(90)
    t.circle(100,180)
    t.left(90)
    t.forward(200)
    t.end_fill()
    t.backward(100)
    t.right(90)
    t.forward(75)
    t.backward(15)

def main():
    wn = turtle.Screen()
    wn.bgpic('skyy.gif')

    abby = turtle.Turtle()
    abby.color("#5980C3", "#5980C3")
    abby.begin_fill()
    abby.penup()
    abby.right(90)
    abby.forward(65)
    abby.pendown()
    abby.left(90)
    abby.forward(375)
    abby.left(180)
    abby.forward(700)
    abby.left(90)
    abby.forward(200)
    abby.left(90)
    abby.forward(700)
    abby.left(90)
    abby.forward(200)
    abby.left(90)
    abby.end_fill()
    abby.penup()
    abby.goto(-40, -65)
    abby.pendown()
    abby.forward(250)
    abby.left(90)
    abby.color("#8E5B3A", "#8E5B3A")
    drawRectangle(abby, 180, 75)

    aaliyah = turtle.Turtle()
    drawBoat(aaliyah)

    drawFlag(aaliyah, 50)
    aaliyah.backward(60)
    aaliyah.right(90)
    aaliyah.forward(50)
    aaliyah.left(55)
    aaliyah.forward(120)
    aaliyah.right(145)
    aaliyah.forward(140)
    aaliyah.stamp()

    wn.exitonclick()

if __name__ == "__main__":
    main()
