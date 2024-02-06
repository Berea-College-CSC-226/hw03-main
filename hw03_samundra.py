#################################################################################
# Author: Samundra Adhikari
# Username: hw03_samundra
#
# Assignment: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: To familiarize functions, turtle graphics, computer color representation, and Git basics.
# Google Doc Link: https://docs.google.com/document/d/1Mj5nshMpoanpbSKld58QdK__H9CcjM_WI2m9WeCyrzo/edit?usp=sharing
#
#################################################################################
# Acknowledgements: Used ChatGPT to ask questions, and used textbook.
#
#
#################################################################################

import turtle


def draw_head(cat):
    """ This function draws the head of a cat"""
    cat.penup()
    cat.goto(0, -100)
    cat.pendown()
    cat.begin_fill()
    cat.color("#110101")
    cat.circle(100)
    cat.end_fill()


def draw_eyes(cat):
    """This function draws the eyes of cat"""
    cat.begin_fill()
    cat.color("white")
    cat.penup()
    cat.forward(-50)
    cat.pendown()
    cat.circle(-25)
    cat.penup()
    cat.forward(100)
    cat.pendown()
    cat.circle(-25)
    cat.end_fill()


def draw_ear(cat):
    """This function draws the ear of cat."""
    cat.begin_fill()
    cat.color("white")
    cat.penup()
    cat.goto(-70, 70)  # Position the turtle
    cat.pendown()
    for i in range(3):
        cat.forward(50)
        cat.left(120)
    cat.end_fill()


def right_ear(cat):
    """This function draws the right side ear of a cat."""
    cat.begin_fill()
    cat.color("white")
    cat.penup()
    cat.goto(20, 70)
    cat.pendown()
    for i in range(3):
        cat.forward(50)
        cat.left(120)
    cat.end_fill()


def draw_mouth(cat):
    """This function is supposed to draws mustache """
    cat.penup()
    cat.goto(-55, -55)  # Position the turtle
    cat.pendown()
    cat.circle(radius=60, extent=80)
    cat.right(20)
    cat.left(-20)
    cat.pendown()
    cat.right(120)
    cat.circle(radius=60, extent=80)


def draw_body(cat):
    """ This function draws the body of a cat"""
    cat.penup()
    cat.goto(-8, -315)
    cat.pendown()
    cat.begin_fill()
    cat.color("#110101")
    cat.circle(120)
    cat.end_fill()


def draw_tail(cat):
    """ draw's triangle shape white tail"""
    cat.penup()
    cat.begin_fill()
    cat.forward(5)
    cat.color("white")
    cat.circle(radius=25, extent=180)
    cat.pendown()
    cat.forward(-200)
    cat.end_fill()


def main():
    """Draw the cat's head"""

    cat = turtle.Turtle()
    wn = turtle.Screen()
    cat.speed(7)
    draw_head(cat)
    wn.bgcolor("orange")
    cat.speed(10)
    cat.goto(0, 50)
    draw_eyes(cat)
    draw_ear(cat)
    draw_mouth(cat)
    right_ear(cat)
    draw_body(cat)
    draw_tail(cat)
    cat.hideturtle()
    wn.exitonclick()


main()
