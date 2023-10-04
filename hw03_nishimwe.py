#################################################################################
# Author: chretien
# Username: nishimwec
#
# Assignment: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: practice using functions and Git
# Google Doc Link: https://docs.google.com/document/d/1kRFAv5HfN869qaUhygp1dkj5ZqkFEl1q9QhuehhB9uk/edit
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle
wn = turtle.Screen()
wn.bgcolor("yellow")
C = turtle.Turtle()
C.hideturtle()
C.color("brown")

def draw_window():
    """
    Drawing the window
    """
    C.penup()
    C.goto(30,-60)
    C.pendown()
    C.begin_fill()
    for _ in range(4):
        C.forward(60)
        C.left(90)
    C.end_fill()

def draw_door():
    """
    Drawing the door
    """
    C.penup()
    C.goto(-80,-200)
    C.pendown()
    C.begin_fill()
    for _ in range(2):
        C.left(90)
        C.forward(200)
        C.left(90)
        C.forward(100)
    C.end_fill()

def draw_roof():
    """
    drawing the roof
    """
    C.penup()
    C.goto(-250, 100)
    C.pendown()
    C.pensize(10)
    C.begin_fill()
    C.left(45)
    C.forward(283)
    C.right(90)
    C.forward(283)
    C.right(135)
    C.forward(300)
    C.end_fill()


def main():
    """
    drawing the house
    """
    C.penup()
    C.goto(-250,-200)
    C.pendown()
    C.pensize(10)
    for _ in range(2):
        C.forward(400)
        C.left(90)
        C.forward(300)
        C.left(90)
    C.pensize(5)
    draw_door()
    draw_window()            # Function call to draw_window
    draw_roof()

    wn.exitonclick()

main()
