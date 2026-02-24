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
#I watched a Youtube video on how to pass a turtle down into the next function while keeping it defined in main.
# I made some research on how to properly navigate the turtle to the exact screen coordinates
#################################################################################

import turtle


def main():
    """
    This function draws a house in daylight with the sun shining bright,
    standing just before a green lawn.
    """
    wn = turtle.Screen()
    wn.bgcolor("skyblue")

    t = turtle.Turtle()
    t.speed(7)

    coordinator(t)

    t.hideturtle()
    wn.exitonclick()

def draw_lawn(t):
    """Draws a green lawn."""
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

def draw_house_base(t):
    """Draws the base of the house."""
    t.penup()
    t.goto(-100, -80)
    t.pendown()
    t.color("black", "burlywood")
    t.begin_fill()

    for i in range(2):
        t.forward(200)
        t.left(90)
        t.forward(140)
        t.left(90)

    t.end_fill()

def draw_roof(t):
    """Draws the roof."""
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

def draw_window_left(t):
    """Draws the left window."""
    t.color("black", "lightyellow")
    t.penup()
    t.goto(-70, -20)
    t.pendown()
    t.begin_fill()

    for i in range(4):
        t.forward(40)
        t.left(90)

    t.end_fill()

def draw_window_right(t):
    """Draws the right window."""
    t.color("black", "lightyellow")
    t.penup()
    t.goto(30, -20)
    t.pendown()
    t.begin_fill()

    for i in range(4):
        t.forward(40)
        t.left(90)

    t.end_fill()

def draw_door(t):
    """Draws the door."""
    t.penup()
    t.goto(-15, -80)
    t.pendown()
    t.color("black", "saddlebrown")
    t.begin_fill()

    for i in range(2):
        t.forward(30)
        t.left(90)
        t.forward(70)
        t.left(90)

    t.end_fill()

def draw_sun_rays(t):
    """Draws the sun and its rays."""
    t.penup()
    t.goto(180, 140)
    t.pendown()
    t.color("orange", "yellow")
    t.begin_fill()
    t.circle(35)
    t.end_fill()

    for i in range(12):
        t.penup()
        t.goto(180, 175)
        t.setheading(i * 30)
        t.forward(35)
        t.pendown()
        t.forward(15)

def coordinator(t):
    """Calls the drawing functions in order."""
    draw_lawn(t)
    draw_house_base(t)
    draw_roof(t)
    draw_window_left(t)
    draw_window_right(t)
    draw_door(t)
    draw_sun_rays(t)

main()
