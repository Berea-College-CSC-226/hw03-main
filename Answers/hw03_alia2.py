#################################################################################
# Author: Amna Ali
# Username: alia2
#
# Assignment: HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Practicing functions
# Google Doc Link: https://docs.google.com/document/d/1tdSwyRPuaKRquYpfHS9FHvYgye5x6cK-lxjJt9qTgqs/edit?usp=sharing
#
#################################################################################

import turtle

#I am going try to make a shark
def draw_body(s):
     """"the sharks body is just an oval"""
     s.penup()
     s.goto(100,-50)
     s.pendown()
     s.fillcolor("#768692")
     s.begin_fill()
     for i in range(2):
         s.circle(100, 180)
         s.forward(160)
     s.end_fill()

def draw_tail(s):
    """the tail will be triangle"""
    s.penup()
    s.goto(180,10)
    s.pendown()
    s.fillcolor("#768692")
    s.begin_fill()
    for i in range(3):
            s.forward(130)
            s.left(120)
    s.end_fill()

def draw_fin(s):
        """triangle on the top"""
        s.penup()
        s.goto(-20,158)
        s.pendown()
        s.fillcolor("#768692")
        s.begin_fill()
        for i in range(3):
            s.forward(100)
            s.left(120)
        s.end_fill()

def draw_eye(s):
    """one eye that is literally just a dot"""
    s.penup()
    s.goto(-60,85)
    s.pendown()
    s.fillcolor("white")
    s.begin_fill()
    s.circle(20)
    s.end_fill()
    s.penup()
    s.goto(-60,90)
    s.fillcolor("black")
    s.begin_fill()
    s.circle(10)
    s.end_fill()

def draw_mouth(s):
    s.penup()
    s.goto(-150,40)
    s.pendown()
    s.pencolor("black")
    s.pensize(10)
    for i in range (12):
        s.forward(5)
        s.left(4)

def draw_teeth(s):
    s.penup()
    s.goto(-150,30)
    s.pendown()
    s.fillcolor("white")
    s.begin_fill()
    for i in range(1):
        s.right(100)
        s.forward(30)
        s.left(120)
        s.forward(40)
    s.end_fill()

def draw_gill(s):
    s.penup()
    s.goto(50,10)
    s.pendown()
    s.pensize(7)
    s.pencolor("black")
    s.begin_fill()
    for i in range(20):
            s.right(-3)
            s.forward(5)

    s.penup()
    s.goto(80,10)
    s.setheading(70)
    s.pendown()
    for i in range(20):
        s.right(-3)
        s.forward(5)



        #            main function
def main():
    wn = turtle.Screen()
    wn.colormode(255)
    wn.bgcolor((0,105,148)) #if i am right this is ocean blue

    s = turtle.Turtle()
    s.shape()
    s.pensize(10)
    s.speed(0)

    draw_body(s)
    draw_tail(s)
    draw_fin(s)
    draw_eye(s)
    draw_mouth(s)
    draw_teeth(s)
    draw_gill(s)



    wn.exitonclick()

main() # calling functions to draw the shark