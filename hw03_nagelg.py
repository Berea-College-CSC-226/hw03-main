#################################################################################
# Author: Gerard Nagel
# Username: nagelg
# Google Doc: https://docs.google.com/document/d/1CtGVE73xZCMP0tAIBb7fdBZGuHK2BC2an2vo10VEUag/edit?usp=sharing
# Assignment: HW03
# Purpose:
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle


def drawBlade(t, sz):
    """
    Draws blade of sword
    """
    t.penup()
    t.goto(0, 100)
    t.pendown()
    t.begin_fill()
    t.right(45)
    t.forward(sz)
    t.backward(sz)
    t.right(90)
    t.forward(sz)
    t.left(45)
    t.forward(125)
    t.left(90)
    t.forward(36)
    t.left(90)
    t.forward(125)
    t.end_fill()


def setBackground(t, wn):
    """

    """
    wn.register_shape("table-nagelg.gif")   # sets file as a usable shape
    t.penup()
    t.setpos(0, 0)
    t.pendown()
    t.shape("table-nagelg.gif")   # sets turtles shape as the file
    t.stamp()

def drawHilt(t, b, sz):
    """
    draws hilt using two turtles and two loops
    """
    t.penup()
    t.goto(-50, -45)
    t.pendown()
    t.begin_fill()
    for i in range(2):  # draws cross guard
        t.right(90)
        t.forward(100)
        t.right(90)
        t.forward(20)
    t.end_fill()
    b.penup()
    b.goto(-15, -70)
    b.pendown()
    b.begin_fill()
    for l in range(2):  # draws hilt
        b.forward(sz)
        b.right(90)
        b.forward(sz + 20)
        b.right(90)
    b.end_fill()
def stoneFloor(t, wn):
    wn.register_shape("Stone_floor_nagelg.gif")  # sets file as a usable shape
    t.penup()
    t.setpos(0, 0)
    t.pendown()
    t.shape("Stone_floor_nagelg.gif")  # sets turtles shape as the file
    t.stamp()

def main():
    """

    """
    wn = turtle.Screen()
    ego = turtle.Turtle()  # first turtle, used for blade and cross guard
    wn.colormode(255)
    ego.pensize(5)
    ego.color(150, 14, 0)
    ego.shape("turtle")
    id = turtle.Turtle()  # second turtle used for table
    id.shape("turtle")
    superego = turtle.Turtle()   # third turtle used for hilt
    superego.pensize(5)
    superego.shape("turtle")
    superego.color(0, 0, 0)
    freud = turtle.Turtle()   # fourth turtle for stone floor
    freud.shape("turtle")
    stoneFloor(freud, wn)
    setBackground(id, wn)
    drawBlade(ego, 25)            # These call my three functions
    drawHilt(ego, superego, 30)
    wn.exitonclick()



main()
