######################################################################
# Author: Alina Cooper
#
# Username: coopera2
#
# Assignment: A03 Fully Functional Gitty Psychedelic Robotic Turtles
#
# Purpose: Drawing something more complex using turtles
#
######################################################################
#
# Acknowledgements: Python Library
####################################################################################

import turtle

wn = turtle.Screen()
wn.bgcolor(0.45, 0.53, 0.47)

yin = turtle.Turtle()    # the big yellow part
yin.color(1, 1, 0)
yin.setpos(-120, 0)

win = turtle.Turtle()    # the windows
win.color(0.78, 0.78, 1)
win.penup()
win.setpos(-100, 100)

whe = turtle.Turtle()    # wheels
whe.color(0, 0, 0)
whe.penup()
whe.setpos(-120, -20)

peep = turtle.Turtle()   # all of the passengers
peep.shape("turtle")
peep.color(0.47, 0, 0.47)
peep.left(90)
peep.penup()
peep.setpos(-90, 80)


def function_1():
    """
    Makes the big yellow rectangle and fills it in.
    :return:
    """
    yin.begin_fill()
    for rectangle in range(2):
        yin.forward(240)
        yin.left(90)
        yin.forward(120)
        yin.left(90)
    yin.end_fill()


def function_2():
    """
    Draws and fills in three blue squares for windows and one bigger rectangle for the windshield
    :return:
    """
    win.begin_fill()  # makes a blue square and fills it in
    for square in range(2):
        win.forward(30)
        win.right(90)
        win.forward(30)
        win.right(90)
    win.end_fill()
    win.penup()
    win.forward(60)
    win.pendown()

    win.begin_fill()
    for square in range(2):
        win.forward(30)
        win.right(90)
        win.forward(30)
        win.right(90)
    win.end_fill()
    win.penup()
    win.forward(60)
    win.pendown()

    win.begin_fill()
    for square in range(2):
        win.forward(30)
        win.right(90)
        win.forward(30)
        win.right(90)
    win.end_fill()
    win.penup()
    win.forward(60)
    win.left(90)
    win.forward(20)
    win.right(90)
    win.pendown()

    win.begin_fill()  # the last window is a rectangle and it's bigger than the others
    for square in range(2):
        win.forward(40)
        win.right(90)
        win.forward(50)
        win.right(90)
    win.end_fill()


def function_3():
    """
    Makes for black circles for the wheels on the bus.
    :return:
    """
    whe.begin_fill()
    whe.circle(20)
    whe.end_fill()
    whe.penup()

    whe.forward(60)
    whe.begin_fill()
    whe.circle(20)
    whe.end_fill()

    whe.forward(60)
    whe.begin_fill()
    whe.circle(20)
    whe.end_fill()

    whe.forward(60)
    whe.begin_fill()
    whe.circle(20)
    whe.end_fill()


def function_4():
    """
    Puts passengers in each of the windows and a driver up front using the stamp
    :return:
    """
    peep.stamp()
    peep.right(90)
    peep.forward(60)
    peep.left(90)
    peep.stamp()
    peep.right(90)
    peep.forward(60)
    peep.left(90)
    peep.stamp()
    peep.right(90)
    peep.forward(60)
    peep.left(90)
    peep.stamp()


def main():
    """

    :return:
    """
    function_1()
    function_2()
    function_3()
    function_4()


main()
wn.exitonclick()
