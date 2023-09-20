#################################################################################
# Author: John Cox
# Username: coxj2
#
# Assignment: HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Learn more about Git
# Google Doc Link: https://docs.google.com/document/d/1T62Guh1IfBQMbXtI0dodMTa7tjEZ7ntFdILqF9CpXVw/edit?usp=sharing
#
#################################################################################

import turtle
import random


def drawRectangle(t, l, w):
    """
    Draw a Rectangle at current position with 't' turtle
    l = length, w = width
    """
    for i in range(2):
        t.fd(l)
        t.right(90)
        t.fd(w)
        t.right(90)


def drawSquare(t, l):
    """
    Draws a square at current position using 't' turtle with 'l' side length
    """
    drawRectangle(t, l, l)


def drawTriangle(t, x1, y1, x2, y2, x3, y3):
    """
    Draws a triangle starting from x1 and y1
    size and length depends on how far apart coordinates are
    (accepts a turtle name and three x, y coordinates)
    """
    t.goto(x1, y1)
    t.goto(x2, y2)
    t.goto(x3, y3)
    t.goto(x1, y1)


def move(t, x, y):
    """
    Lifts pen and moves 't' turtle to specified x and y coordinates, then lowers the pen
    """
    t.penup()
    t.goto(x, y)
    t.pendown()


def drawProceduralTriangles(t):
    """
    draw random sized triangles procedurally in a sort of grid pattern with 't' turtle
    """
    x = -250
    y = -250
    move(t, x, y)
    i = 0
    while (i < 5):
        i += 1
        move(t, x, y)
        drawTriangle(t, x, y, random.randrange(x - 40, x + 40), random.randrange(y - 20, y + 20),
                     random.randrange(x - 40, x + 40), random.randrange(y - 20, y + 20))

        x += 80
        y = -250
        j = 0

        while (j < 5):
            j += 1
            move(t, x, y)
            drawTriangle(t, x, y, random.randrange(x - 40, x + 40), random.randrange(y - 20, y + 20),
                         random.randrange(x - 40, x + 40), random.randrange(y - 20, y + 20))

            y += 80


def main():
    pencil = turtle.Turtle()
    wn = turtle.Screen()

    move(pencil, 250, 200)
    drawRectangle(pencil, 50, 25)
    move(pencil, 200, 200)
    drawTriangle(pencil, pencil.xcor(), pencil.ycor(), 200, 175, 160, 110)
    move(pencil, 250, 250)
    drawSquare(pencil, 40)
    drawProceduralTriangles(pencil)
    wn.exitonclick()


main()
