#################################################################################
# Author: Harry Adkins
# Username: adkinsh2
#
# Assignment: HW03
# Purpose: Drawing stars
# Google Doc Link: https://docs.google.com/document/d/1DqjcrDnNRH_vvrzYEIaPAd95IWsKW53YRXWLzz5ADKw/edit
#
#################################################################################
# Acknowledgements: Python documentation
#
#
#################################################################################

import turtle

def drawStar():
    """
    Draws six 5-pointed stars
    """
    bigStar = turtle.Turtle()
    bigStar.pensize(4)
    bigStar.color("white")

    bigStar.penup()
    bigStar.left(60)
    bigStar.forward(200)
    bigStar.right(60)
    bigStar.pendown()

    for i in range(6):
        for j in range(5):
            bigStar.forward(30)
            bigStar.right(144)
        bigStar.penup()
        bigStar.right(60)
        bigStar.forward(100)
        bigStar.pendown()

def drawMoon():
    """
    Draws a crescent moon
    """
    moon = turtle.Turtle()
    moon.pensize(5)
    moon.color(172,176,42)
    moon.pensize(4)
    moon.fillcolor(172,176,42)

    moon.penup()
    moon.left(60)
    moon.forward(155)
    moon.right(60)

    moon.pendown()
    moon.circle(-25,-200)
    moon.right(35)
    moon.circle(-23,160)

def main():
    """
    Main function
    """
    wn = turtle.Screen()
    wn.colormode(255)
    wn.bgcolor(20, 7, 101)
    # Function calls to function_1 and function_2.
    drawStar()
    drawMoon()

    wn.exitonclick()

main()  # Starts the program!