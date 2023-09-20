


#################################################################################
# Author: Lizzie Joy Manabat
# Username: manabatl
#
# Assignment: H03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Understand the use of Git and using functions
# Google Doc Link: https://docs.google.com/document/d/1i5jlTs91At5VJJf4def4pzbbWYG79T8Ruj1psQwQm28/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle


def drawing_cat(cat, pen):
    cat.pensize(pen)
    cat.speed(10)
    cat.penup()
    cat.goto(0,-180)
    cat.pendown()

    cat.fillcolor("#C1CDCD")
    cat.begin_fill()
    cat.circle(172, 360)
    cat.end_fill()
def cat_ears(cat):
    cat.penup()                      # Cat's ears
    cat.goto(40, 165)
    cat.pendown()
    cat.fillcolor("#C1CDCD")
    cat.begin_fill()

    cat.left(40)                     # Left Ear
    cat.forward(135)
    cat.right(130)
    cat.forward(165)
    cat.end_fill()

    cat.begin_fill()
    cat.penup()                      # Cat's Ear
    cat.goto(-40,165)
    cat.pendown()

    cat.right(130)                   # Right Ear
    cat.forward(135)
    cat.left(130)
    cat.forward(165)
    cat.end_fill()
    cat.penup()
def cat_eyes(cat):
    cat.penup()
    cat.goto(40,40)
    cat.pendown()

    for i in range (60):
        cat.right(3)
        cat.backward(1)

    cat. penup()
    cat.goto(-40,40)
    cat.pendown()

    for i in range(60):
        cat.right(-3)
        cat.forward(1)
def cat_nose(cat):
    cat.penup()
    cat.goto(0,-60)
    cat.pendown()
    cat.left(150)
    cat.forward(40)
    cat.right(60)
    cat.backward(40)
    cat.right(55)
    cat.forward(40)
def cat_lips(cat):
    cat.penup()
    cat.goto(0, -60)
    cat.pendown()
    cat.setheading(60)
    for i in range(60):
        cat.right(1)
        cat.backward(2)

    cat.penup()
    cat.goto(0,-60)
    cat.pendown()
    cat.setheading(-60)
    for i in range(60):
        cat.right(-1)
        cat.forward(2)
def cat_outline(cat):
    cat.penup()
    cat.goto(0,-180)
    cat.pendown()
    cat.circle(172, 360)
def main():
    wn = turtle.Screen()
    wn.bgcolor("#D8BEE9")
    cat = turtle.Turtle()

    cat.shape("circle")
    cat.color("#50A191")

    head = 0
    pen = 10
    cat.speed(0)

    drawing_cat(cat, pen)
    cat_ears(cat)
    cat_eyes(cat)
    cat_nose(cat)
    cat_lips(cat)
    cat_outline(cat)
    wn.exitonclick()

main()
