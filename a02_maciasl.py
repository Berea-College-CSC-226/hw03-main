###########################################################
# Author: Luis Macias
# Username: Maciasl
# Google Doc: https://docs.google.com/document/d/15IR5S7NKkSJEYyjrQzMTa7fgAXK4ZtF6nM_8iNNUrlQ/edit?usp=sharing
###########################################################

import turtle

wn = turtle.Screen()
luis = turtle.Turtle()
luis.pensize(20)
wn.colormode(255)
luis.pencolor(0, 0, 0)
wn.bgcolor(100, 100, 255)


def building():
    for i in range(2):
        luis.forward(300)
        luis.left(90)
        luis.forward(660)
        luis.left(90)


def color():
    luis.color('grey')
    luis.penup()
    luis.forward(20)
    luis.left(90)
    luis.forward(20)
    luis.right(90)
    luis.pendown()
    for i in range(15):
        luis.forward(260)
        luis.left(90)
        luis.forward(20)
        luis.left(90)
        luis.forward(260)
        luis.right(90)
        luis.forward(20)
        luis.right(90)
    luis.forward(260)
    luis.left(90)
    luis.forward(20)
    luis.left(90)
    luis.forward(260)
    luis.penup()
    luis.forward(20)
    luis.left(90)
    luis.forward(640)
    luis.left(90)


def windows():
    luis.pencolor(0, 0, 0)
    for i in range(2):
        luis.forward(54)
        luis.left(90)
        luis.forward(114)
        luis.left(90)
        luis.forward(54)
        luis.left(90)
        luis.forward(114)
        luis.left(90)
        luis.penup()
        luis.forward(108)
        luis.pendown()


def main():
    luis.penup()
    luis.forward(-300)
    luis.right(90)
    luis.forward(300)
    luis.left(90)
    luis.pendown()
    building()
    color()
    luis.penup()
    luis.forward(60)
    luis.left(90)
    luis.forward(120)
    luis.right(90)
    luis.pendown()
    windows()
    luis.penup()
    luis.forward(-216)
    luis.left(90)
    luis.forward(177)
    luis.right(90)
    luis.pendown()
    windows()
    luis.penup()
    luis.forward(-216)
    luis.left(90)
    luis.forward(177)
    luis.right(90)
    luis.pendown()
    windows()


main()

wn.exitonclick()
