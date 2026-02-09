#################################################################################
# Author: Bright Feitsop
# Username: feitsopb
#
# Assignment:  Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: draw a house with a sun and a lawn
# Google Doc Link: https://docs.google.com/document/d/1uAakEGkZq1KC7OyOWdHyhTWRtLaLklQSOeIZ5m73O_8/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################


import turtle
wn = turtle.Screen()
wn.bgcolor("skyblue")

t = turtle.Turtle()
t.speed(0)
def main():
    def lawn():
        t.penup()
        t.goto(-300, -200)
        t.pendown()
        t.color("green")
        t.begin_fill()

        for _ in range(2):
            t.forward(600)
            t.left(90)
            t.forward(120)
            t.left(90)

        t.end_fill()
    lawn()

    def house_base():
        t.penup()
        t.goto(-100, -80)   # just above the lawn
        t.pendown()
        t.color("black", "burlywood")
        t.begin_fill()

        for _ in range(2):
            t.forward(200)
            t.left(90)
            t.forward(140)
            t.left(90)

        t.end_fill()
    house_base()

    def roof():
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
    roof()

    t.color("black", "lightyellow")
    def window_left():

        t.penup()
        t.goto(-70, -20)
        t.pendown()
        t.begin_fill()
        for _ in range(4):
            t.forward(40)
            t.left(90)
        t.end_fill()
    window_left()

    def window_right():

        t.penup()
        t.goto(30, -20)
        t.pendown()
        t.begin_fill()
        for _ in range(4):
            t.forward(40)
            t.left(90)
        t.end_fill()
    window_right()

    def door():
        t.penup()
        t.goto(-15, -80)   # centered at bottom of house
        t.pendown()
        t.color("black", "saddlebrown")
        t.begin_fill()

        for _ in range(2):
            t.forward(30)
            t.left(90)
            t.forward(70)
            t.left(90)

        t.end_fill()
    door()

    def sun_rays():
        t.penup()
        t.goto(180, 140)
        t.pendown()
        t.color("orange", "yellow")
        t.begin_fill()
        t.circle(35)
        t.end_fill()

        # Sun rays
        for _ in range(12):
            t.penup()
            t.goto(180, 175)
            t.setheading(_ * 30)
            t.forward(35)
            t.pendown()
            t.forward(15)
        sun_rays()

    t.hideturtle()
    wn.exitonclick()
main()