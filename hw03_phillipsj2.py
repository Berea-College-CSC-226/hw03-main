######################################################################
# Authors: Chase Phillips
# Username: phillipsj2
#
# Assignment: HW03
#
# Purpose: A program that uses turtles to draw a complex object. This is also an intro to Git's more complex nature
#
# https://docs.google.com/document/d/1ScrNyDoxQ187_iHzXMwE0PJ0ZUmyG6eX1xUxiFIGk-Y/edit?usp=sharing
#####################################################################

import turtle


def draw_trailer(rect, door, w1, w2):
    """This is meant to draw the trailer, a mobile home. Compeleted with doors and windows"""
    # This is going to draw a blue trailer shape + the grey roof
    rect.fillcolor('blue')
    rect.begin_fill()
    for i in range(2):
        rect.forward(300)
        rect.left(90)
        rect.forward(125)
        rect.left(90)
    rect.end_fill()

    # This is drawing the "roof" of the trailer to add some depth
    rect.fillcolor('lightgrey')
    rect.begin_fill()
    rect.goto(0,125)
    rect.left(90)
    for i in range(2):
        rect.forward(30)
        rect.right(90)
        rect.forward(300)
        rect.right(90)
    rect.end_fill()
    rect.hideturtle()

    # This will put a door on the trailer
    door.penup()
    door.forward(135)
    door.pendown()
    door.left(90)

    door.fillcolor(102, 69, 11)
    door.begin_fill()
    for r in range(2):
        door.forward(50)
        door.right(90)
        door.forward(30)
        door.right(90)
    door.end_fill()
    door.hideturtle()

    # w1 and w2 will put 2 windows on the trailer
    w1.penup()
    w1.forward(70)
    w1.left(90)
    w1.forward(50)
    w1.pendown()

    w1.fillcolor(55, 136, 255)
    w1.begin_fill()
    for p in range(4):
        w1.forward(30)
        w1.right(90)
    w1.end_fill()

    w1.forward(15)
    w1.right(90)
    w1.forward(30)
    w1.right(90)
    w1.forward(15)
    w1.right(90)
    w1.forward(15)
    w1.right(90)
    w1.forward(30)
    w1.hideturtle()

    w2.penup()
    w2.forward(200)
    w2.left(90)
    w2.forward(50)
    w2.pendown()

    w2.fillcolor(55, 136, 255)
    w2.begin_fill()
    for p in range(4):
        w2.forward(30)
        w2.right(90)
    w2.end_fill()

    w2.forward(15)
    w2.right(90)
    w2.forward(30)
    w2.right(90)
    w2.forward(15)
    w2.right(90)
    w2.forward(15)
    w2.right(90)
    w2.forward(30)
    w2.hideturtle()


def draw_garage(sh, li):
    """This is meant to draw the garage. It will have a door and a different shape than the trailer"""
    # This block is for the garage's shape/outline
    sh.penup()
    sh.goto(-50, 0)
    sh.pendown()
    sh.left(180)
    sh.fillcolor('white')
    sh.begin_fill()
    for i in range(2):
        sh.forward(200)
        sh.right(90)
        sh.forward(125)
        sh.right(90)
    sh.end_fill()
    sh.begin_fill()
    sh.right(90)
    sh.forward(125)
    sh.left(67)
    sh.forward(110)
    sh.left(46)
    sh.forward(107)
    sh.end_fill()
    sh.right(203)
    sh.forward(200)
    sh.hideturtle()

    # The block is meant to draw the garage door
    li.penup()
    li.goto(-100, 0)
    li.pendown()
    li.left(90)
    li.fillcolor('blue')
    li.begin_fill()
    for l in range(2):
        li.forward(70)
        li.left(90)
        li.forward(100)
        li.left(90)
    li.end_fill()
    li.pensize(2)

    # This part creates the "open" part of the garage door
    li.fillcolor('black')
    li.begin_fill()
    for u in range(2):
        li.forward(20)
        li.left(90)
        li.forward(100)
        li.left(90)
    li.end_fill()

    # This mess makes the lines on the door to add texture
    li.forward(30)
    li.left(90)
    li.forward(100)
    li.right(90)
    li.forward(10)
    li.right(90)
    li.forward(100)
    li.left(90)
    li.forward(10)
    li.left(90)
    li.forward(100)
    li.right(90)
    li.forward(10)
    li.right(90)
    li.forward(100)
    li.hideturtle()


def main():
    """This is the main function. It calls on other functions and sets the scene for turtles."""

    wn = turtle.Screen()
    wn.colormode(255)
    wn.bgcolor(189, 229, 255)
    wn.screensize(700, 700)

    # This block is making the turtles for the trailer and calling it
    t = turtle.Turtle()
    t.pensize(5)
    t.speed(3)

    m = turtle.Turtle()
    m.pensize(5)
    m.speed(3)

    w1 = turtle.Turtle()
    w1.pensize(5)
    w1.speed(3)

    w2 = turtle.Turtle()
    w2.pensize(5)
    w2.speed(3)
    draw_trailer(t, m, w1, w2)

    # This block is for creating the turtles for the garage and calling the function
    s = turtle.Turtle()
    s.pensize(5)
    s.speed(3)

    l = turtle.Turtle()
    l.pensize(5)

    draw_garage(s, l)
    wn.exitonclick()


main()
