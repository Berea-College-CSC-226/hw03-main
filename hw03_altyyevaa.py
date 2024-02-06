#################################################################################
# Author: Aziza Altyyeva
# Username: altyyevaa
#
# Assignment: to create a creative project using functions, turtles, loops and etc.
# Purpose: to practice what I have learned until today
# Google Doc Link: https://docs.google.com/document/d/1qbbG98mVSgm59Zz0Qic8VSSfr2YC18v-gFslQo-V63c/edit
#
# ################################################################################
# Acknowledgements:
# https://colorspire.com/rgb-color-wheel/ (I used this website to get RGBs of the colors I used in my code
#
#
#################################################################################

import turtle


def draw_house(lomi):
    """
    Draws the house
    """
    lomi.pensize(10)
    turtle.colormode(255)
    lomi.pencolor((63, 37, 8))
    lomi.penup()
    lomi.goto(-300, -300)
    lomi.pendown()
    lomi.fillcolor("#3F2508")
    lomi.begin_fill()
    for i in range(4):  # draws the square of the house
        lomi.forward(200)
        lomi.left(90)
    lomi.end_fill()
    lomi.penup()
    lomi.left(45)
    lomi.forward(290)
    lomi.down()
    lomi.fillcolor("#D5AB7B")
    lomi.begin_fill()
    for a in range(2):
        lomi.left(90)
        lomi.forward(150)
    lomi.end_fill()
    lomi.penup()
    lomi.backward(150)
    lomi.right(135)
    lomi.pendown()
    lomi.pencolor('black')  # draws the flag
    lomi.forward(70)
    lomi.color("#19AC3B")
    lomi.fillcolor("#19AC3B")
    lomi.begin_fill()
    for b in range(3):  # draws the square shape of the flag
        lomi.right(90)
        lomi.forward(40)
    lomi.end_fill()


def draw_road(lomi):
    """
    Draws a gray straight road
    """
    lomi.pensize(10)
    turtle.colormode(255)
    lomi.pencolor("#B6B6B2")
    lomi.penup()
    lomi.right(240)
    lomi.forward(400)
    lomi.pendown()
    lomi.fillcolor("#B6B6B2")
    lomi.begin_fill()
    lomi.left(135)
    lomi.forward(645)
    lomi.right(75)
    lomi.forward(90)
    lomi.right(70)
    lomi.forward(665)
    lomi.left(-110)
    lomi.forward(487)
    lomi.end_fill()
    lomi.penup()
    lomi.pencolor("black")
    lomi.pensize(20)
    lomi.right(160)
    lomi.forward(245)
    lomi.pendown()


def draw_lines(lomi):
    """
    draws the black middle lines
    """
    lomi.setheading(0)
    lomi.left(90)
    lomi.pensize(40)
    lomi.forward(120)
    lomi.penup()
    lomi.forward(90)
    lomi.pendown()

    lomi.setheading(0)
    lomi.pensize(30)
    lomi.left(90)
    lomi.forward(120)
    lomi.penup()
    lomi.forward(90)
    lomi.pendown()

    lomi.setheading(0)
    lomi.pensize(25)
    lomi.left(90)
    lomi.forward(105)


def draw_windows(lomi):  # draws the windows and the door of the house
    """
    draws the windows and the door of the house
    """
    lomi.penup()
    lomi.goto(-300, -300)
    lomi.setheading(0)
    lomi.left(90)
    lomi.forward(130)
    lomi.right(90)
    lomi.forward(10)
    lomi.pendown()
    lomi.pensize(7)
    lomi.fillcolor('#F7D10E')
    lomi.begin_fill()
    for d in range(4):  # window no1
        lomi.forward(35)
        lomi.left(90)
    lomi.end_fill()
    lomi.penup()
    lomi.forward(145)
    lomi.pendown()
    lomi.fillcolor('#F7D10E')
    lomi.begin_fill()
    for d in range(4):  # window n02
        lomi.forward(35)
        lomi.left(90)
    lomi.end_fill()
    lomi.penup()
    lomi.goto(-300, -300)
    lomi.setheading(0)
    lomi.forward(75)
    lomi.pencolor("#903001")
    lomi.fillcolor('#903001')
    lomi.begin_fill()
    lomi.pendown()
    lomi.forward(60)  # draws the red rectangle door
    lomi.left(90)
    lomi.forward(90)
    lomi.left(90)
    lomi.forward(60)
    lomi.left(90)
    lomi.forward(90)
    lomi.end_fill()


def draw_stars(lomi):
    """
    draws the stars
    """
    lomi.penup()  # star no1
    lomi.goto(-300, -300)
    lomi.setheading(0)
    lomi.left(115)
    lomi.forward(550)
    lomi.pendown()
    lomi.pencolor('yellow')
    lomi.fillcolor('yellow')
    lomi.begin_fill()
    for f in range(5):
        lomi.forward(70)
        lomi.right(144)
    lomi.end_fill()

    lomi.setheading(0)  # star no2
    lomi.penup()
    lomi.left(30)
    lomi.forward(150)
    lomi.pendown()
    lomi.pencolor('yellow')
    lomi.fillcolor('yellow')
    lomi.begin_fill()
    for f in range(5):
        lomi.forward(70)
        lomi.right(144)
    lomi.end_fill()

    lomi.setheading(0)  # star no3
    lomi.penup()
    lomi.right(90)
    lomi.forward(150)
    lomi.pendown()
    lomi.pencolor('yellow')
    lomi.fillcolor('yellow')
    lomi.begin_fill()
    for f in range(5):
        lomi.forward(70)
        lomi.right(144)
    lomi.end_fill()

    lomi.setheading(0)  # star no4
    lomi.penup()
    lomi.left(45)
    lomi.forward(150)
    lomi.pendown()
    lomi.pencolor('yellow')
    lomi.fillcolor('yellow')
    lomi.begin_fill()
    for f in range(5):
        lomi.forward(70)
        lomi.right(144)
    lomi.end_fill()

    lomi.setheading(0)  # star no5
    lomi.penup()
    lomi.right(45)
    lomi.forward(100)
    lomi.pendown()
    lomi.pencolor('yellow')
    lomi.fillcolor('yellow')
    lomi.begin_fill()
    for f in range(5):
        lomi.forward(70)
        lomi.right(144)
    lomi.end_fill()


def main():
    """
    defines the main function
    """

    lomi = turtle.Turtle()
    wn = turtle.Screen()
    turtle.colormode(255)
    wn.bgcolor("#3A4997")
    draw_house(lomi)

    draw_road(lomi)

    draw_lines(lomi)

    draw_windows(lomi)

    draw_stars(lomi)

    wn.exitonclick()


main()  # calls the main function
