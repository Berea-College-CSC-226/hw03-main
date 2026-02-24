#################################################################################
# Author: Pride Akana Techa
# Username: techap
#
# Assignment: HW03 - Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: To show effective use of functions and turtle methods in Python.
# Google Doc Link: https://docs.google.com/document/d/1RcjcQ88EDyKiG31gs6bNng1g_oic5dEuExgSP8kU784/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################


from turtle import *

def draw_house(x1, y1):
    """
    Draws a house.
    """
    turt1 = Turtle()
    turt1.penup()
    turt1.goto(x1, y1)
    turt1.pendown()
    turt1.color("white")
    turt1.begin_fill()

    for i in range(2):
        turt1.forward(300)
        turt1.left(90)
        turt1.forward(200)
        turt1.left(90)

    turt1.end_fill()
    turt1.hideturtle()

def door_windows (x2, y2):
    """
    Draws a door and two windows.
    """
    turt2 = Turtle()
    turt2.penup()
    turt2.goto(x2, y2)
    turt2.pendown()
    turt2.color("#CC9999")
    turt2.begin_fill()


    for i in range(2):
        turt2.forward(75)
        turt2.left(90)
        turt2.forward(100)
        turt2.left(90)

    turt2.end_fill()
    turt2.penup()
    turt2.goto(x2-75, y2+125)
    turt2.pendown()
    turt2.begin_fill()

    for x in range(2):

        for i in range(4):
            turt2.forward(50)
            turt2.left(90)

        turt2.penup()
        turt2.goto(x2+100, y2+125)
        turt2.pendown()

    turt2.end_fill()
    turt2.hideturtle()

def draw_roof(x3, y3):
    """
    Draws the roof of the house.
    """
    turt3 = Turtle()
    turt3.penup()
    turt3.goto(x3, y3)
    turt3.pendown()
    turt3.color("#669999")
    turt3.begin_fill()
    turt3.backward(50)
    turt3.left(60)
    turt3.forward(100)
    turt3.right(60)
    turt3.forward(300)
    turt3.right(60)
    turt3.forward(100)
    turt3.left(60)
    turt3.backward(50)
    turt3.end_fill()
    turt3.hideturtle()

def draw_sun(x4, y4):
    """
    Draws the sun.
    """
    turt4 = Turtle()
    turt4.penup()
    turt4.goto(x4, y4)
    turt4.pendown()
    turt4.color("yellow")
    turt4.begin_fill()
    turt4.circle(50)
    turt4.end_fill()
    turt4.hideturtle()

def draw_flowers(x5, y5):
    """
    Draws flowers around the house.
    """
    turt5= Turtle()
    turt5.penup()
    turt5.goto(x5, y5)
    turt5.pendown()
    turt5.pensize(3)

    for x in range(2):
        turt5.color("lightgreen")
        turt5.left(90)
        turt5.forward(100)

        turt5.begin_fill()
        for i in range(6):
            turt5.color("pink")
            turt5.circle(50, 80)
            turt5.left(100)
            turt5.circle(50, 80)


        turt5.end_fill()
        turt5.penup()
        turt5.goto(x5+400, y5)
        turt5.pendown()
        turt5.left(150)

    turt5.hideturtle()

def write_message(x6, y6):
    """
    Writes a welcome message.
    """
    turt6 = Turtle()
    turt6.penup()
    turt6.goto(x6, y6)
    turt6.pendown()
    turt6.color("white")
    turt6.write("Welcome Home :)", move=False, align="center", font=("Courier", 30, "italic"))
    turt6.hideturtle()


def main():
    """
    Draws a house scene with the sun and flowers, and writes a welcome message at the bottom of the screen.
    """
    wn = Screen()
    wn.bgcolor("#99CCFF")

    draw_house(-150, -150)

    door_windows(-35, -150)

    draw_roof(-150, 50)

    draw_sun(-200, 150)

    draw_flowers(-200, -150)

    write_message(0, -200)


    wn.exitonclick()

main()

