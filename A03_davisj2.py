######################################################################
# Author: Jesse Davis              TODO: Change this to your name, if modifying
# Username: davisj2                     TODO: Change this to your username, if modifying
#
# Assignment: A03
# Purpose: To make a complex shape
######################################################################
# Acknowledgements: Assisted by Scott Heggen, Cody Auen, Will Romano, and Bria Williams and google search for hexidecimal colors
######################################################################

import turtle

def move(t, x, y):
    t.up()
    t.setpos(x, y)
    t.down()

def borders(t):
    t.penup()
    t.setpos(-250,-250)
    t.pendown()
    t.pensize(20)
    for i in range(4):
        t.forward(500)
        t.left(90)


def ground(t):
    t.penup()
    t.setpos(-250,-200)
    t.pendown()
    t.color('#00ff00')
    t.begin_fill()
    t.forward(500)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(500)
    t.right(90)
    t.forward(50)
    t.end_fill() 


def house(t):
    t.penup()
    t.setpos(-190,-200)
    t.pendown()
    t.color('#964b00')
    t.begin_fill()
    for i in range(4):
        t.forward(260)
        t.left(90)
    t.end_fill()

def roof(t):
    t.penup()
    t.setpos(-190,60)
    t.pendown()
    t.color('#B5651D')
    t.begin_fill()
    for i in range(3):
        t.forward(260)
        t.left(120)
    t.end_fill()

def sun(t):
    t.penup()
    t.setpos(160,60)
    t.pendown()
    t.color('#ffff00')
    t.begin_fill()
    t.circle(70)
    t.end_fill()



def main():
    J = turtle.Turtle()
    X = turtle.Turtle()
    C = turtle.Turtle()
    T = turtle.Turtle()
    S = turtle.Turtle()
    wn = turtle.Screen()
    wn.bgcolor('#add8e6')
    wn.screensize(500,500)

    borders(J)
    ground(X)
    house(C)
    roof(T)
    sun(S)

    wn.exitonclick()


main()