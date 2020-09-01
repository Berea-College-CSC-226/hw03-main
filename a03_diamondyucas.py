######################################################################
# Author: Diamond Yucas
# Username: diamondyucas
#
# Assignment: A03: Fully Functional Gitty Psychedelic Robotic Turtles
#
# Purpose: Practice with making functions and using Git
#
# This program creates my interpretation of a mountain with a full bright moon
# and the big dipper to help light up the night sky

# Google Doc Link: https://docs.google.com/document/d/1k9NEPLqzxsZzhp_NomwIHNL4_Qat2GAY-kY07_dW3ko/edit?usp=sharing

# I received help from Mr. Darian Sanders with organization!
######################################################################

import turtle


def move_turtle(me):    # moving turtle into corner
    me.speed(0)
    me.left(90)
    me.forward(285)
    me.left(90)
    me.forward(330)


def make_triangle(me):      # creating triangle
    me.fillcolor(20, 60, 80)
    me.begin_fill()
    me.pendown()
    me.left(120)
    me.forward(650)
    me.left(120)
    me.forward(650)
    me.left(120)
    me.forward(650)
    me.end_fill()


def trees(me):      # making three trees
    me.left(120)
    me.forward(200)
    me.left(150)
    me.pencolor("green")
    me.forward(50)
    me.stamp()
    me.back(50)
    me.right(150)
    me.forward(50)
    me.left(150)
    me.forward(80)
    me.stamp()
    me.back(80)
    me.right(150)
    me.forward(50)
    me.left(150)
    me.forward(50)
    me.stamp()


def mountains(me):      # making mountains
    me.hideturtle()
    me.back(50)  # mountains
    me.right(150)
    me.pencolor("black")
    me.forward(150)
    me.pencolor(160, 82, 45)
    me.left(100)
    me.forward(170)
    me.right(90)
    me.forward(123)
    me.left(110)
    me.pencolor("black")
    me.forward(40)
    me.pencolor(160, 82, 45)
    me.left(80)
    me.forward(50)
    me.left(80)
    me.forward(130)
    me.right(80)
    me.forward(140)
    me.left(100)
    me.forward(35)


def moon(shape):        # creating moon
    shape.penup()
    shape.speed(0)
    shape.pensize(2)
    shape.hideturtle()
    shape.pencolor("white")
    shape.left(90)
    shape.forward(100)
    shape.left(90)
    shape.forward(130)
    for i in range(10):
        shape.pendown()
        shape.left(90)
        shape.forward(30)
        shape.left(70)
        shape.forward(80)


def big_dipper(star):       # creating the big dipper
    star.penup()
    star.hideturtle()
    star.forward(40)
    star.left(90)
    star.forward(250)
    star.pendown()
    star.pencolor("pink")
    star.pensize(2)
    star.hideturtle()
    star.right(80)
    star.forward(50)
    star.right(40)
    star.forward(40)
    star.right(20)
    star.forward(30)
    star.right(30)
    star.forward(30)
    star.left(80)
    star.forward(50)
    star.left(80)
    star.forward(35)


def main():     # defining main functions
    wn = turtle.Screen()
    me = turtle.Turtle()
    star = turtle.Turtle()
    shape = turtle.Turtle()
    wn.title("mountain sky")
    me.penup()
    me.pensize(3)
    wn.colormode(255)
    wn.bgcolor(200, 150, 70)
    move_turtle(me)
    make_triangle(me)
    trees(me)
    mountains(me)
    moon(shape)
    big_dipper(star)
    wn.exitonclick()


main()  # call to the main function