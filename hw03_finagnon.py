#################################################################################
# Author:Finagnon Adjagbodjou
# Username: Fin
#
# Assignment: hw03
# Purpose: Learn the purpose of pulling, pushing, etc.
# Google Doc Link: https://docs.google.com/document/d/1BjZMQNg6d2PG-PlwE5gFo9XBrmMei0aY6B_CtXdtFLg/edit?usp=sharing
#
#################################################################################
# Acknowledgements: 
#
#
#################################################################################

import turtle
import random


def rightturn(shape):
    """
    turns the turtle to the right
    """
    shape.right(90)
    shape.forward(5)
    shape.right(90)


def leftturn(shape):
    """
    turns the turtle to the left
    """
    shape.left(90)
    shape.forward(5)
    shape.left(90)


def createrectangle(shape):
    """
    creates the starting rectangle in which the turtle will move
    """

    shape.penup()
    shape.pensize(20)
    shape.setpos(-200, 250)
    shape.pendown()
    shape.color('black')
    shape.forward(500)
    shape.right(90)
    shape.forward(505)
    shape.right(90)
    shape.forward(500)
    shape.right(90)
    shape.forward(500)


def finishup(shape):
    """
    stamps the turtle's shape on the screen for the width of the display window
    """
    for i in range(460):
        shape.stamp()
        shape.forward(1)
    rightturn(shape)
    for i in range(460):
        shape.stamp()
        shape.forward(1)


def makehouse(shape):
    """
    creates outline of house
    """
    shape.penup()
    shape.color('black')
    shape.pensize(10)
    shape.left(90)
    shape.forward(10)
    shape.right(270)
    shape.forward(225)
    shape.pensize(10)
    shape.left(90)
    shape.pendown()
    for i in range(2):
        shape.forward(160)
        shape.left(90)
        shape.forward(160)
        shape.left(90)
    shape.forward(160)
    shape.right(90)
    shape.forward(10)
    shape.left(120)
    shape.forward(180)
    shape.left(120)
    shape.forward(180)
    shape.left(120)
    shape.forward(40)
    shape.penup()


def makemoon(shape):
    """
    makes a swirly moon in the background
    """
    shape.setpos(-115, 150)
    shape.color("#D8E4EB")
    shape.pendown()
    for i in range(40):
        shape.forward(1 + i)
        shape.right(30)


def maketree(shape):
    """
    draws a simple Christmas tree
    """
    shape.penup()
    shape.setpos(200, -100)
    shape.color("#553B0E")
    shape.left(30)
    shape.pendown()
    shape.forward(150)
    shape.left(90)
    shape.penup()
    shape.forward(20)
    shape.left(90)
    shape.pendown()
    shape.forward(150)
    shape.penup()
    shape.setpos(280, -150)
    shape.left(30)
    shape.color("#19500B")
    shape.fillcolor("#19500B")
    shape.begin_fill()
    for i in range(3):
        shape.forward(150)
        shape.left(120)
    shape.end_fill()
    shape.setpos(265, -80)
    shape.begin_fill()
    for i in range(3):
        shape.forward(120)
        shape.left(120)
    shape.end_fill()


def doorsnwindows(shape):
    """
    draws doors and windows on the house
    """
    shape.penup()
    shape.color("black")
    shape.setpos(-50, -160)
    shape.pensize(10)
    shape.left(60)
    shape.pendown()
    for i in range(4):
        shape.forward(50)
        shape.right(90)
    shape.penup()
    shape.setpos(-10, -250)
    shape.right(90)
    shape.pendown()
    for i in range(2):
        shape.forward(70)
        shape.right(90)
        shape.forward(30)
        shape.right(90)
    shape.stamp()


def christmaslights(shape):
    """
    covers tree in colorful Christmas tree lights
    """
    shape.penup()
    shape.shape("circle")
    shape.pensize(10)

    shape.color("red")
    shape.setpos(180, -100)
    shape.stamp()

    shape.color("green")
    shape.setpos(215, -120)
    shape.stamp()

    shape.color("blue")
    shape.setpos(190, -55)
    shape.stamp()

    shape.color("yellow")
    shape.setpos(225, -40)
    shape.stamp()


def makesnow(shape):
    """
    makes snowflakes in the sky and covers ground in snow
    """
    shape.penup()
    shape.right(45)
    shape.color("#E1E4E3")
    shape.setpos(-200, 215)
    for i in range(8):
        shape.right(90)
        shape.forward(40)
        shape.stamp()
        shape.left(90)
        shape.forward(40)
        shape.stamp()
    shape.penup()
    shape.setpos(-200, 155)
    for i in range(8):
        shape.right(90)
        shape.forward(40)
        shape.stamp()
        shape.left(90)
        shape.forward(40)
        shape.stamp()
    shape.setpos(-200, 105)
    for i in range(8):
        shape.right(90)
        shape.forward(40)
        shape.stamp()
        shape.left(90)
        shape.forward(40)
        shape.stamp()
    shape.shape("square")
    shape.shapesize(1)
    shape.setpos(-180, -240)
    shape.right(45)
    finishup(shape)


def fillrectangle(shape):
    """
    fills rectangle with a color
    """
    shape.shape('square')
    shape.penup()
    shape.setpos(-186, 230)
    shape.color('#0A334B')
    shape.right(90)

    shape.forward(6)
    shape.pendown()
    shape.speed(20)
    for i in range(47):
        if i != 46:

            shape.stamp()
            shape.forward(460)
            shape.stamp()
            rightturn(shape)
            shape.stamp()
            shape.forward(460)
            leftturn(shape)
        else:
            finishup(shape)


def main():
    """
    This is the main function of the program. It creates a display window in which a snowy
    landscape with a house, a Christmas tree with lights, and the moon in the sky can be seen.
    """
    wn = turtle.Screen()

    shape = turtle.Turtle()
    createrectangle(shape)
    fillrectangle(shape)
    makehouse(shape)
    makemoon(shape)
    maketree(shape)
    doorsnwindows(shape)
    christmaslights(shape)
    makesnow(shape)
    wn.exitonclick()


main()
