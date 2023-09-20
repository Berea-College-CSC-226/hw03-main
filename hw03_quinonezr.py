#################################################################################
# Author:Ruben Quinonez
# Username:quinonezr
#
# Assignment:HW03 Fully Functional Gitty Turtles
# Purpose:
# Google Doc Link:https://docs.google.com/document/d/1FCB9KRG7pKzSgf5R-j-xW5jRYbEhy0kJC9hHV7eF9No/edit?usp=sharing
#
#################################################################################
# Acknowledgements: code edited from HW02
#
#
#################################################################################

import turtle


def cathead(t):
    """Creates the head portion of the cat"""
    t.pensize(5)
    t.penup()
    t.forward(-100)
    t.left(90)
    t.forward(200)
    t.right(90)
    t.pendown()
    t.begin_fill()
    for i in range(2):
        t.forward(200)
        t.right(45)
        t.forward(100)
        t.right(45)
        t.forward(100)
        t.right(45)
        t.forward(100)
        t.right(45)
    t.end_fill()


def catears(t):
    """gives the cat ears"""
    t.penup()
    t.pensize(5)
    t.backward(172)
    t.left(90)
    t.forward(40)
    t.pendown()
    t.begin_fill()
    t.forward(200)
    t.right(120)
    t.forward(83)
    t.left(30)
    t.end_fill()
    t.penup()
    t.forward(272)
    t.right(90)
    t.forward(160)
    t.left(180)
    t.pendown()
    t.begin_fill()
    t.forward(200)
    t.left(120)
    t.forward(83)
    t.right(30)
    t.end_fill()


def cateyes(t):
    """Draws the cat's eyes"""
    t.right(90)
    t.penup()
    t.forward(120)
    t.left(90)
    t.forward(-40)
    t.color('yellow')
    t.begin_fill()
    t.pendown()
    t.left(60)
    for i in range(2):
        t.forward(60)
        t.right(120)
        t.forward(60)
        t.right(60)

    t.end_fill()
    t.penup()
    t.right(60)
    t.forward(220)
    t.pendown()
    t.begin_fill()
    t.left(60)
    for i in range(2):
        t.forward(60)
        t.right(120)
        t.forward(60)
        t.right(60)
    t.end_fill()
    t.penup()
    t.forward(60)
    t.right(150)
    t.color("black")  # draws the iris part of the eye from here on
    t.forward(10)
    t.pendown()
    t.forward(85)
    t.penup()
    t.right(90)
    t.forward(220)
    t.right(90)
    t.pendown()
    t.forward(85)
    t.penup()


def catmouth(t):
    """puts a little mouth on the cat"""
    t.color("white")
    t.forward(-75)
    t.right(90)
    t.forward(70)
    t.pendown()
    for i in range(2):
        t.right(60)
        t.forward(30)
        t.left(90)
        t.forward(30)


def catbody(t):
    """Draws the cat's body"""
    t.setposition(0,0)
    t.color('purple')
    t.penup()
    t.forward(50)
    t.left(90)
    t.forward(45)
    t.color('black')
    t.pendown()
    t.begin_fill()
    t.right(20)
    t.forward(200)
    t.left(110)
    t.forward(225)
    t.left(110)
    t.forward(200)
    t.left(70)
    t.forward(90)
    t.end_fill()


def main():
    gato = turtle.Turtle()
    gatosecond = turtle.Turtle()
    gato.speed(0)
    gatosecond.speed(0)
    wn = turtle.Screen()
    wn.colormode(255)
    wn.bgcolor(235, 97, 35)
    cathead(gato)
    catears(gatosecond)
    cateyes(gato)
    catmouth(gato)
    catbody(gatosecond)
    wn.exitonclick()


main()
