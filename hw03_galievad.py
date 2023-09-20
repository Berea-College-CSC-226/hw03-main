#################################################################################
# Author: Diliara Galieva
# Username: galievad
#
# Assignment: HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Understand how to work with branches.
# Google Doc Link: https://docs.google.com/document/d/1ziOkalEagxAs5wZARwje3YD6OTARGMf6KSKmtaUOseY/edit?usp=sharing
#
#################################################################################

import turtle


# the function draws a body of a frog
def drawbody(bd):
    bd.penup()
    bd.forward(112)
    bd.right(90)
    bd.forward(200)
    bd.left(90)
    bd.pendown()
    bd.color("#549465")
    bd.pencolor("#1F5B39")
    bd.begin_fill()
    bd.circle(100, 360)
    bd.end_fill()
    pass


# the function draws a head of the frog
def drawhead(hd):
    hd.penup()
    hd.forward(112)
    hd.right(90)
    hd.forward(50)
    hd.left(90)

    hd.pendown()
    hd.color("#549465")
    hd.pencolor("#1F5B39")
    hd.begin_fill()
    hd.circle(50, 360)
    hd.end_fill()
    pass


# the function draws two eyes of the frog
def draweyes(eye):
    for i in range(2):  # the loop allows the programmer to draw two identical eyeballs
        eye.penup()
        eye.forward(75)
        eye.pendown()

        eye.color("white")
        eye.pencolor("#1F5B39")
        eye.begin_fill()
        eye.circle(25, 360)
        eye.end_fill()
    eye.color("black")
    eye.penup()
    eye.left(90)
    eye.forward(25)
    eye.pendown()
    eye.stamp()

    eye.penup()
    eye.left(90)
    eye.forward(75)
    eye.stamp()   # the action draws two pupils of the eyes
    pass


# the function draws a smile of the frog
def drawsmile(sm):
    sm.penup()
    sm.forward(88)
    sm.right(90)
    sm.forward(12)
    sm.pendown()
    sm.circle(25, 180)
    pass


# the function draws two legs of the frog
def drawlegs(lg):
    lg.penup()
    lg.forward(160)
    lg.right(90)
    lg.forward(200)
    lg.left(90)
    lg.forward(40)

    lg.pendown()
    lg.color("#549465")
    lg.pencolor("#1F5B39")
    lg.begin_fill()
    lg.circle(30, 360)
    lg.end_fill()

    lg.penup()
    lg.right(201)
    lg.forward(170)

    lg.pendown()
    lg.color("#549465")
    lg.pencolor("#1F5B39")
    lg.begin_fill()
    lg.circle(30, 360)
    lg.end_fill()
    pass


# the function draws three fingers per leg (two legs)
def drawtoes(ts):
    ts.penup()
    ts.forward(160)
    ts.right(90)
    ts.forward(200)
    ts.left(90)
    ts.forward(40)
    for i in range(3):   # loop allows you to draw three fingers using fewer functions
        ts.penup()
        ts.forward(17)
        ts.pendown()
        ts.color("#549465")
        ts.pencolor("#1F5B39")
        ts.begin_fill()
        ts.circle(5, 360)
        ts.end_fill()
        ts.penup()
        ts.right(-20)
        ts.pendown()
    ts.penup()
    ts.left(120)
    ts.forward(175)
    for i in range(3):   # the loop repeats with the previous one
        ts.penup()
        ts.forward(17)
        ts.pendown()
        ts.color("#549465")
        ts.pencolor("#1F5B39")
        ts.begin_fill()
        ts.circle(5, 360)
        ts.end_fill()
        ts.penup()
        ts.right(-20)
        ts.pendown()
    pass


def main():
    eye = turtle.Turtle()
    eye.shape("circle")
    eye.pencolor("#1F5B39")
    eye.speed(10)
    eye.pensize(10)

    hd = turtle.Turtle()
    hd.shape("circle")
    hd.pencolor("#1F5B39")
    hd.speed(1)
    hd.pensize(10)

    sm = turtle.Turtle()
    sm.shape("circle")
    sm.color("red")
    sm.pensize(10)

    bd = turtle.Turtle()
    bd.shape("circle")
    bd.pencolor("#1F5B39")
    bd.pensize(10)

    lg = turtle.Turtle()
    lg.shape("circle")
    lg.pencolor("#1F5B39")
    lg.pensize(10)

    ts = turtle.Turtle()
    ts.shape("circle")
    ts.pencolor("#1F5B39")
    ts.pensize(10)

    wn = turtle.Screen()
    wn.bgcolor("#53A3BC")

    drawbody(bd)  # Function call to drawbody
    drawhead(hd)  # Function call to drawhead
    draweyes(eye)  # Function call to draweyes
    drawsmile(sm)  # Function call to drawsmile
    drawlegs(lg)  # Function call to drawlegs
    drawtoes(ts)  # Function call to drawtoes

    wn.exitonclick()


main()
