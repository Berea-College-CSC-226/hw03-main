#####################################################################################################################
# Author: Artem Kurasov
# Username: kurasova
#
# Assignment: HW03
# Purpose: get used to GitHub and practice working with the turtle module
# Google Doc Link: https://docs.google.com/document/d/1hLxgBxV4L7K39ix4ZtJPwIToweDyPeu30wUBAxvmEsg/edit?usp=sharing
#
#####################################################################################################################
# Acknowledgements:
#
# kfc.png: taken from https://en.wikipedia.org/wiki/KFC
# flowers.png: taken from https://freepngimg.com/png/15354-flowers-png-3
#
# I consulted the Python Documentation for this assignment: https://docs.python.org/3/library/turtle.html#turtle.shape
#
#####################################################################################################################


from turtle import *
from math import pi

def move(turtle: Turtle, x, y):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()

def back(turtle: Turtle, n, radius):
    circumference = 2 * pi * radius
    part = circumference / n
    step = part / (2**(1/2))
    move(turtle, turtle.xcor() - part/2, turtle.ycor() + radius)

    turtle.begin_fill()
    for _ in range(n):
        turtle.left(45)
        turtle.forward(step)
        turtle.right(90)
        turtle.forward(step)
        turtle.left(45)
        turtle.right(360 // n)
    t.end_fill()

def name(turtle: Turtle, radius, phrase, degree = 180):
    circumference = pi * radius * (degree/180)
    step = circumference / len(phrase)
    for i in phrase:
        turtle.up()
        turtle.forward(step/2)
        turtle.down()
        turtle.write(i, font = ("Arial", 12, "bold"))
        turtle.up()
        turtle.forward(step/2)
        turtle.right(degree // len(phrase))
        turtle.down()


def main():
    global t
    s = Screen()
    t = Turtle()

    t.shape("circle")
    t.pensize(5)
    t.speed(0)

    s.colormode(255)
    s.bgcolor(100, 0, 0)
    s.screensize(500, 500)
    s.addshape("kfc.png")
    s.addshape("flowers.png")

    t.color("white")
    move(t, 0, 0)
    back(t, 20, 100)
    move(t, 0, 0)
    t.shape("kfc.png")
    t.stamp()
    t.shape("circle")

    t.left(84)
    move(t, -140, -10)
    name(t, 135, "THE BEST FRIED CHICKEN")

    t.shape("flowers.png")
    move(t, 0, -200)
    t.stamp()
    t.shape("circle")

    t.color(100, 0, 0)
    move(t, 0, 200)

    s.exitonclick()

if __name__ == "__main__":
    main()
