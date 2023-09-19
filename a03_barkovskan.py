# Author: Nadia Barkovska
# Username: barkovskan
#
# Assignment: a03
# Purpose:
# Google Doc Link: https://docs.google.com/document/d/1-ibxsP64Y9TbDlPXR_dkQkF39-UAC4n8e4f66QF4NnQ/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle


def drawsquare (bubbles, size):
    """" I defined function drawsquare to get turtle "bubbles" to draw a square """
    for i in range(4):
        bubbles.forward(size)
        bubbles.left(90)
    # ....


def main ():
    """I used the main function to define some attributes and invoke drawsquare function."""
    wn = turtle.Screen()
    wn.bgcolor("black")
    bubbles = turtle.Turtle()
    bubbles.speed(0)
    bubbles.penup()
    bubbles.setpos(-220, 100)
    bubbles.pendown()

    for i in range(8):
        if (i) % 2 == 0:
            bubbles.fillcolor("pink")
        else:
            bubbles.fillcolor(0.245,0.245,0.220)
        bubbles.begin_fill()
        drawsquare(bubbles, 60)
        bubbles.forward(60)
        bubbles.end_fill()


    bubbles.penup()
    bubbles.setpos(-220, 40)
    bubbles.pendown()
    for i in range(8):
        if (i) % 2 == 0:
            bubbles.fillcolor(0.165, 0.42, 0.42)
        else:
            bubbles.fillcolor("white")
        bubbles.begin_fill()
        drawsquare(bubbles, 60)
        bubbles.forward(60)
        bubbles.end_fill()

    bubbles.penup()
    bubbles.setpos(-220, -20)
    bubbles.pendown()
    for i in range(8):
        if (i) % 2 == 0:
            bubbles.fillcolor("orange")
        else:
            bubbles.fillcolor(0.237, 0.145, 0.33)
        bubbles.begin_fill()
        drawsquare(bubbles, 60)
        bubbles.forward(60)
        bubbles.end_fill()

    bubbles.penup()
    bubbles.setpos(-220, -80)
    bubbles.pendown()
    for i in range(8):
        if (i) % 2 == 0:
            bubbles.fillcolor(0.80, 0.203, 0.118)
        else:
            bubbles.fillcolor("blue")
        bubbles.begin_fill()
        drawsquare(bubbles, 60)
        bubbles.forward(60)
        bubbles.end_fill()

    bubbles.penup()
    bubbles.setpos(-220, -140)
    bubbles.pendown()
    for i in range(8):
        if (i) % 2 == 0:
            bubbles.fillcolor("yellow")
        else:
            bubbles.fillcolor(0.85, 0.107, 0.47)
        bubbles.begin_fill()
        drawsquare(bubbles, 60)
        bubbles.forward(60)
        bubbles.end_fill()

    bubbles.penup()
    bubbles.setpos(-220, -200)
    bubbles.pendown()
    for i in range(8):
        if (i) % 2 == 0:
            bubbles.fillcolor(0.143, 0.188, 0.143)
        else:
            bubbles.fillcolor("purple")
        bubbles.begin_fill()
        drawsquare(bubbles, 60)
        bubbles.forward(60)
        bubbles.end_fill()


    wn.exitonclick()

main()

