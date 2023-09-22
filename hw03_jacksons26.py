################################################################################
# Author: Spencer Jackson
# Username: jacksons26
#
# Assignment: HW03
# Purpose: Draw a complex object with turtles
# Google Doc Link:https://docs.google.com/document/d/1QC2UiH_zJBEsrs8GDyEZ5EjlqP9cXw5uBxGqsJAqnJo/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#################################################################################

import turtle


def draw_square(sq):
    """
    Draws a square for the house
    """
    sq.penup()
    sq.goto(20,20)
    sq.pendown()
    sq.color("red")
    sq.fillcolor("red")
    sq.begin_fill()
    sq.forward(200)
    sq.left(90)
    sq.forward(200)
    sq.left(90)
    sq.forward(200)
    sq.left(90)
    sq.forward(200)
    sq.end_fill()


def draw_roof(rf):
    """
    Draws the roof for the house
    """
    rf.penup()
    rf.goto(20,220)
    rf.pendown()
    rf.color("blue")
    rf.fillcolor("blue")
    rf.begin_fill()
    rf.forward(200)
    rf.left(135)
    rf.forward(150)
    rf.left(92)
    rf.forward(150)
    rf.end_fill()


def draw_door(dr):
    """
    Draws a door for the house
    """
    dr.penup()
    dr.goto(80,20)
    dr.pendown()
    dr.color("yellow")
    dr.fillcolor("yellow")
    dr.begin_fill()
    dr.forward(50)
    dr.left(90)
    dr.forward(100)
    dr.left(90)
    dr.forward(50)
    dr.left(90)
    dr.forward(100)
    dr.end_fill()

def draw_windows(wd):
    """
    Draws two windows for the house
    """
    wd.penup()
    wd.goto(50,150)
    wd.pendown()
    wd.color("blue")
    wd.fillcolor("blue")
    wd.begin_fill()
    wd.forward(50)
    wd.left(90)
    wd.forward(50)
    wd.left(90)
    wd.forward(50)
    wd.end_fill()
    wd.penup()
    wd.goto(200, 150)
    wd.pendown()
    wd.color("blue")
    wd.fillcolor("blue")
    wd.begin_fill()
    wd.forward(50)
    wd.left(90)
    wd.forward(50)
    wd.left(90)
    wd.forward(50)
    wd.end_fill()



def main():
    """
    Setups background and turtles and runs functions
    """
    wn = turtle.Screen()
    wn.bgcolor("green")
    sq = turtle.Turtle()
    rf = turtle.Turtle()
    dr = turtle.Turtle()
    wd= turtle.Turtle()





    draw_square(sq)            # Function call to function_1
    draw_roof(rf)            # Function call to function_2
    draw_door(dr)
    draw_windows(wd)
    wn.exitonclick()


main()


