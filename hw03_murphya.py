# Author: Aaliyah Murphy
# Username: Murphya
#
# Assignment: Hw03
# Google Doc Link:https://docs.google.com/document/d/1QOq5mSUdxNJacGKRdWqrQEk5mgNh5cuqwZO52XxC4JY/edit?usp=sharing
#

import turtle

wn = turtle.Screen()
abby = turtle.Screen()
abby.bgpic('skyy.gif')

abby = turtle.Turtle()
aaliyah = turtle.Turtle()

#This code makes the horizon line and makes the water blue.
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
#This code makes the ship dock
abby.forward(250)
abby.left(90)
abby.color("#8E5B3A", "#8E5B3A")
def drawRectangle(t, w, h):
    for i in range(2):
        abby.begin_fill()
        abby.forward(w)
        abby.left(90)
        abby.forward(h)
        abby.left(90)
        abby.end_fill()

#worked on the boat
aaliyah.penup()
aaliyah.goto(-90,-150)
aaliyah.pendown()
aaliyah.color("#8E5B3A", "#8E5B3A")
aaliyah.begin_fill()
aaliyah.right(90)
aaliyah.circle(100,180)
aaliyah.left(90)
aaliyah.forward(200)
aaliyah.end_fill()
aaliyah.backward(100)
aaliyah.right(90)
aaliyah.forward(75)
aaliyah.backward(15)

def drawFlag(t, sz):
    t.begin_fill()
    for i in range(4):
        t.color("#A24C66", "#A24C66")
        t.forward(sz)
        t.left(90)
    t.end_fill()

#fishing pole
    aaliyah.backward(60)
    aaliyah.right(90)
    aaliyah.forward(50)
    aaliyah.left(55)
    aaliyah.forward(120)
    aaliyah.right(145)
    aaliyah.forward(140)
    aaliyah.stamp()
def main():
    drawRectangle(abby, 180, 75)
    drawFlag(aaliyah, 50)
    wn.exitonclick()
main()
