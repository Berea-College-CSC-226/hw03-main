#################################################################################
# Author: Bright Feitsop
# Username: feitsopb
#
# Assignment:  Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: draw a house with a sun and a lawn
# Google Doc Link: https://docs.google.com/document/d/1uAakEGkZq1KC7OyOWdHyhTWRtLaLklQSOeIZ5m73O_8/edit?usp=sharing
#
#################################################################################
# Acknowledgements
#
#
#################################################################################


import turtle
t = turtle.Turtle()

def main():
    """
    this function draws a house in daylight, with the sun shining Bright, standing on green lawn
    """
    wn = turtle.Screen()
    wn.bgcolor("skyblue")
    t.speed(7)
    coordinator()
    t.hideturtle()
    wn.exitonclick()


def lawn():
    """
    draws a lawn colored green
    """
    t.penup()
    t.goto(-300, -200)
    t.pendown()
    t.color("green")
    t.begin_fill()

    for i in range(2):
        t.forward(600)
        t.left(90)
        t.forward(120)
        t.left(90)

    t.end_fill()

def house_base():
    """
    draws the structure of the house with a mixture of 2 colors
    """
    t.penup()
    t.goto(-100, -80)  # just above the lawn
    t.pendown()
    t.color("black", "burlywood")
    t.begin_fill()

    for i in range(2):
        t.forward(200)
        t.left(90)
        t.forward(140)
        t.left(90)

    t.end_fill()

def roof():
    """
    draws the structure of the roof
    """
    t.penup()
    t.goto(-100, 60)
    t.pendown()
    t.color("black", "brown")
    t.begin_fill()

    t.forward(200)
    t.left(135)
    t.forward(140)
    t.left(90)
    t.forward(140)
    t.left(135)

    t.end_fill()


def window_left():
    """
    draws the window left
    """
    t.color("black", "lightyellow")
    t.penup()
    t.goto(-70, -20)
    t.pendown()
    t.begin_fill()
    for i in range(4):
        t.forward(40)
        t.left(90)
    t.end_fill()

def window_right():
    """
    draws the window right
    """

    t.penup()
    t.goto(30, -20)
    t.pendown()
    t.begin_fill()
    for i in range(4):
        t.forward(40)
        t.left(90)
    t.end_fill()

def door():
    """
    draws the door
    """
    t.penup()
    t.goto(-15, -80)  # centered at bottom of house
    t.pendown()
    t.color("black", "saddlebrown")
    t.begin_fill()

    for i in range(2):
        t.forward(30)
        t.left(90)
        t.forward(70)
        t.left(90)

    t.end_fill()




def sun_rays():
    """
    draws the sun with sun rays around it.
    """
    t.penup()
    t.goto(180, 140)
    t.pendown()
    t.color("orange", "yellow")
    t.begin_fill()
    t.circle(35)
    t.end_fill()

    # Sun rays
    for i in range(12):
        t.penup()
        t.goto(180, 175)
        t.setheading(i * 30)
        t.forward(35)
        t.pendown()
        t.forward(15)

def coordinator ():
    """
    call the functions in order as they line up.
    """
    lawn()
    house_base()
    roof()
    window_left()
    window_right()
    door()
    sun_rays()



main()