#################################################################################
# Author: Monica Amaya
# Username: amayahernandezm
#
# Assignment: HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: crate a small school-like shaped figure
# Google Doc Link:https://docs.google.com/document/d/1uGI_WWYKKKUxIKqABrURxDdOLg1ZnSJ_EcYJyw9GkG8/edit?usp=sharing
#
#################################################################################

import turtle


# draws a green square representing the grass
def grass(alex):
    alex.color("green")
    alex.fillcolor("green")
    alex.pensize(5)
    alex.penup()
    alex.goto(-357, -20)
    alex.pendown()
    alex.begin_fill()
    for i in range(2):
        alex.forward(705)
        alex.right(90)
        alex.forward(330)
        alex.right(90)
    alex.end_fill()


# draws the outside box representing the building
def outside_walls(alex):
    alex.color("bisque")
    alex.fillcolor("bisque")
    alex.penup()
    alex.goto(-175, 82)
    alex.pendown()
    alex.begin_fill()
    for i in range(2):
        alex.forward(350)
        alex.right(90)
        alex.forward(180)
        alex.right(90)
    alex.end_fill()


# draws a window with panels and repeats the process 3 times to form three windows
def windows(alex):
    alex.color("black")
    alex.fillcolor(127, 217, 239)
    alex.pensize(3)
    alex.penup()
    alex.goto(-140, 10)
    alex.pendown()
    alex.begin_fill()
    for i in range(3):      # here is where the process repeats 3 times
        for i in range(2):      # this one draws the square or outside part of the window
            alex.forward(60)
            alex.left(90)
            alex.forward(50)
            alex.left(90)
        for i in range(1):      # this one draws the inside panels
            alex.forward(30)
            alex.left(90)
            alex.forward(50)
            alex.left(90)
            alex.forward(30)
            alex.left(90)
            alex.forward(25)
            alex.left(90)
            alex.forward(60)
            alex.right(90)
            alex.forward(25)
            alex.right(90)
            alex.forward(60)
            alex.right(180)
        alex.penup()        # this allows for the turtle to go back to its original spot so it can start another one
        alex.forward(110)
        alex.pendown()
    alex.end_fill()


# draws the main door
def door(alex):
    alex.fillcolor(238, 186, 17)
    alex.penup()
    alex.goto(-20, -25)
    alex.pendown()
    alex.begin_fill()
    for i in range(2):
        alex.forward(45)
        alex.right(90)
        alex.forward(75)
        alex.right(90)
    alex.end_fill()
    alex.penup()
    alex.goto(20, -58)
    alex.pendown()
    alex.stamp()


# draws the top part of the building
def second_floor(jen):
    jen.color("bisque")
    jen.fillcolor("bisque")
    jen.penup()
    jen.goto(-60, 82)
    jen.pendown()
    jen.begin_fill()
    for i in range(2):
        jen.forward(120)
        jen.left(90)
        jen.forward(65)
        jen.left(90)
    jen.end_fill()


# draws a clock in the second floor
def clock(jen):
    jen.color("black")
    jen.fillcolor(50, 139, 65)
    jen.pensize(3)
    jen.penup()
    jen.goto(0, 85)
    jen.pendown()
    jen.begin_fill()
    jen.circle(25)
    jen.end_fill()
    jen.penup()
    jen.goto(0, 105)
    jen.pendown()
    jen.left(90)
    jen.forward(20)
    jen.goto(0, 105)
    jen.right(90)
    jen.forward(15)


# draws a flag at the top of the school
def flag(jen):
    jen.fillcolor(189, 57, 8)
    jen.left(90)
    jen.penup()
    jen.goto(0, 150)
    jen.pendown()
    jen.forward(50)
    jen.begin_fill()
    for i in range(2):
        jen.right(120)
        jen.forward(35)
    jen.end_fill()


# executes all functions previously defined by calling them in main
def main():
    wn = turtle.Screen()
    wn.colormode(255)
    wn.bgcolor(90, 180, 200)
    alex = turtle.Turtle()
    jen = turtle.Turtle()
    alex.speed(15)
    jen.speed(15)
    alex.hideturtle()
    jen.hideturtle()
    grass(alex)
    outside_walls(alex)
    windows(alex)
    door(alex)
    second_floor(jen)
    clock(jen)
    flag(jen)
    wn.exitonclick()


main()

