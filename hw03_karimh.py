
# Author: Hira Karim
# Username: karimh
#
# Assignment: HW03-Fully Functional Gitty Psychedelic Robotic Turtle
# Purpose: To create a code using functions, and submit a pull request.
# Google Doc Link: https://docs.google.com/document/d/12MLXaEkr6jyzp5jVL2UXoEJTj2VyV12LwCJIk-eW6fs/edit?usp=sharing

import turtle

Heer = turtle.Turtle()

def tyre_1(rad, th):
    "rad = radius of the circle"
    "th = thickness of the tyre"
    Heer.pensize(th)
    Heer.circle(rad)

def tyre_2(rad, th):
    "rad = radius of the circle"
    "th = thickness of the tyre"

    Heer.pensize(th)
    Heer.circle(rad)
    Heer.fillcolor("grey")
    Heer.begin_fill()
def lower_body(l, w):
    "l = length of the lower rectangular body of car"
    "w = width of the lower rectangular body of car"

    Heer.fillcolor("black")
    Heer.begin_fill()

    Heer.left(180)
    Heer.forward(l)
    Heer.right(90)
    Heer.forward(w)
    Heer.right(90)
    Heer.forward(l)
    Heer.right(90)
    Heer.forward(w)
    Heer.end_fill()

def upper_body(ul,uw):
    "ul = length of the upper rectangular body"
    "uw = width of the upper rectangular body"

    Heer.left(180)
    Heer.forward(ul)
    Heer.right(90)
    Heer.forward(uw)
    Heer.right(90)
    Heer.forward(ul)
    Heer.right(90)
    Heer.forward(uw)
    Heer.fillcolor("orange")
    Heer.begin_fill()


def main ():
    wn = turtle.Screen()
    wn.colormode(255)
    wn.bgcolor("lightblue")
    Heer.speed(0)

    Heer.penup()
    Heer.goto(-150, -200)
    Heer.pendown()

    #call functions
    tyre_1(50, 5)   #call function 1

    Heer.penup()
    Heer.goto(150, -200)
    Heer.pendown()

    tyre_2(50,5)    # call function 2

    Heer.penup()
    Heer.goto(300, -100)
    Heer.pendown()

    lower_body(600,130)     #call function 3

    Heer.setheading(180)
    Heer.penup()
    Heer.goto(-200,130)
    Heer.pendown()

    upper_body(400,200)

    Heer.penup()
    Heer.goto(0,60 )
    Heer.pendown()

    Heer.write("Hira's self-driving car!", align="center", font=("Verdana", 18, "normal"))

    wn.exitonclick()

main()