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


from turtle import*

wn = Screen()
wn.bgcolor("#99CCFF")

def draw_house(turt1):
    """
    Draws a house.
    """
    x1_pos = -150
    y1_pos = -150
    turt1.penup()
    turt1.goto(x1_pos, y1_pos)
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

def door_windows (turt2):
    """
    Draws a door and two windows.
    """
    x1=-35
    y1=-150
    turt2.penup()
    turt2.goto(x1, y1)
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
    turt2.goto(x1-75, y1+125)
    turt2.pendown()
    turt2.begin_fill()

    for x in range(2):

        for i in range(4):
            turt2.forward(50)
            turt2.left(90)

        turt2.penup()
        turt2.goto(x1+100, y1+125)
        turt2.pendown()

    turt2.end_fill()
    turt2.hideturtle()

def draw_roof(turt3):
    """
    Draws the roof of the house.
    """
    turt3.penup()
    turt3.goto(-150, 50)
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

def draw_sun(turt4):
    """
    Draws the sun.
    """
    turt4.penup()
    turt4.goto(-200, 150)
    turt4.pendown()
    turt4.color("yellow")
    turt4.begin_fill()
    turt4.circle(50)
    turt4.end_fill()
    turt4.hideturtle()

def draw_flowers(turt5):
    """
    Draws flowers around the house.
    """
    x2=-200
    y2=-150
    turt5.penup()
    turt5.goto(x2, y2)
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
        turt5.goto(x2+400, y2)
        turt5.pendown()
        turt5.left(150)

    turt5.hideturtle()


def main():
    """
    Calls all previously defined functions and writes a message at the bottom of the page.
    """
    jana = Turtle()
    draw_house(jana)

    debi = Turtle()
    door_windows(debi)

    teni = Turtle()
    draw_roof(teni)

    mimi = Turtle()
    draw_sun(mimi)

    jeni = Turtle()
    draw_flowers(jeni)

    jada = Turtle()
    jada.penup()
    jada.goto(0, -200)
    jada.pendown()
    jada.color("white")
    jada.write("Welcome Home :)", move=False, align="center", font=("Courier", 30, "italic"))
    jada.hideturtle()


main()  # Starts the program!

wn.exitonclick()