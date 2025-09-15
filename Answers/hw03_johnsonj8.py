#################################################################################
# Author: Aiden Johnson
# Username: johnsonj8
#
# Assignment: HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Learn how to use turtle and functions while also learning to avoid merge conflicts.
# Google Doc Link:https://docs.google.com/document/d/1W_otoa0aZvFVuU_kdvjaK53dI2mnBg9d3pxpl0F2sr0/edit?tab=t.0#heading=h.isd6vwob791e
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################


import turtle

def draw_house(turt):
    """
    Draws the basic house shape with bottom left corner at turtle's location.
    """
    turt.color(127, 0, 255)
    turt.begin_fill()
    turt.setheading(0)
    for n in range(4):
        turt.forward(100)
        turt.left(90)
    turt.end_fill()
    turt.penup()
    turt.left(180)
    turt.forward(10)
    turt.right(90)
    turt.forward(100)
    turt.pendown()
    turt.color("red")
    turt.right(90)
    turt.begin_fill()
    for n in range(3):
        turt.forward(120)
        turt.left(120)
    turt.end_fill()

def draw_door(turt):
    """
    Makes the door of the house with bottom left corner at turtle's current position.
    """
    turt.color("blue")
    turt.setheading(90)
    turt.begin_fill()
    for n in range(2):
        turt.forward(40)
        turt.right(90)
        turt.forward(20)
        turt.right(90)
    turt.end_fill()
    turt.color("black")
    turt.penup()
    turt.forward(25)
    turt.right(90)
    turt.forward(19)
    turt.setheading(90)
    turt.pendown()
    turt.begin_fill()
    turt.circle(2)
    turt.end_fill()

def draw_window(turt):
    """
    Draws a window at the turtle's current location.
    """
    turt.pencolor("white")
    turt.fillcolor(135, 206, 250)
    turt.setheading(0)
    turt.begin_fill()
    for n in range(4):
        turt.forward(30)
        turt.left(90)
    turt.end_fill()
    turt.penup()
    turt.forward(15)
    turt.left(90)
    turt.pendown()
    turt.pensize(3)
    turt.forward(30)
    turt.penup()
    for n in range(2):
        turt.left(90)
        turt.forward(15)
    turt.left(90)
    turt.pendown()
    turt.forward(30)
    turt.pensize(1)
    turt.color("black")

def draw_clover(turt):
    """
    Draws a little clover for decoration.
    """
    turt.color("dark green")
    turt.setheading(90)
    turt.forward(30)
    turt.setheading(-45)
    turt.begin_fill()
    turt.speed(0)
    for n in range(4):
        turt.forward(5)
        for i in range(60):
            turt.left(3)
            turt.forward(0.5)
        turt.forward(5)
        turt.right(90)
    turt.end_fill()
    turt.speed(3)


def main():
    """
    Draws a house with a four leaf clover in the lawn.
    """
    wn = turtle.Screen()
    wn.bgcolor("light green")
    wn.colormode(255)
    finn = turtle.Turtle()
    finn.teleport(-50, -50)
    draw_house(finn)
    finn.teleport(-30, -50)
    draw_door(finn)
    finn.teleport(0, 0)
    draw_window(finn)
    finn.teleport(150, -200)
    draw_clover(finn)
    finn.hideturtle()

    wn.exitonclick()

main()