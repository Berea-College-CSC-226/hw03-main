#################################################################################
# Author: Eric Sparks
# Username: sparkse
#
# Assignment: HW03 Gitty
# Purpose:
# Google Doc Link: https://docs.google.com/document/d/13Jex3ZkqC03fEM9GkJspY7uE_Sa9_u_LsR-daa-SSo8/edit?usp=sharing
# 1
#################################################################################
# Acknowledgements:
#  https://stackoverflow.com/questions/20320921/python-turtle-pen-colour
#  Changed color to 255 type
#################################################################################


import turtle
import random


def move(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def rectangle(t, w, h):
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
    t.forward(15)
    t.left(90)
    t.forward(70)
    t.right(90)
    t.forward(15)
    t.right(90)
    t.forward(35)
    t.right(90)
    t.forward(30)
    t.right(180)


def house(t, j, w, h):
    t.penup()
    t.goto(-300, -250)
    t.pendown()
    t.color("lightyellow")
    t.begin_fill()
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
    t.end_fill()
    j.penup()
    j.goto(-300, -50)
    j.pendown()
    for i in range(1):
        j.color("brown")
        j.begin_fill()
        j.forward(-50)
        j.forward(w + 100)
        j.left(165)
        j.forward(364.15)
        print(j.xcor(), j.ycor())
        j.left(30)
        j.forward(365.15)
        j.end_fill()


# use distance formula?
def balloon(t,k):
    for i in range(100):
        t.penup()
        x = random.randint(0, 600)
        y = random.randint(100, 300)
        x = x - 300
        print(x, y)
        t.goto(x, y)
        t.pendown()
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        t.color((r, g, b))
        t.begin_fill()
        t.circle(random.randrange(10, 15))
        t.end_fill()
        k.penup()
        k.goto(x,y)
        k.pendown()
        k.goto(-1.74188, 44.24)


def main():
    tess = turtle.Turtle()
    jason = turtle.Turtle()
    kevin = turtle.Turtle()
    wn = turtle.Screen()
    wn.bgcolor("lightblue")

    jason.speed(0)
    kevin.speed(0)
    tess.speed(0)

    tess.pensize(3)
    jason.pensize(3)
    kevin.pensize(1)
    house(tess, jason, 600, 200)

    move(tess, -200, -150)
    tess.color("brown")
    rectangle(tess, 30, 70)

    move(tess, 170, -150)
    rectangle(tess, 30,70)
    turtle.colormode(255)
    balloon(tess, kevin)
    wn.exitonclick()


main()
