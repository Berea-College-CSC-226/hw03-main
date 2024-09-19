
#################################################################################
# Author: Gloire Muzeba
# Username:muzebag
#
# Assignment:hw03
# Purpose:Learn about source control and Git
# Google Doc Link:https://docs.google.com/document/d/1Cc8hE9zoNiUNEWM6DXcvrsf9pb6mtfM_NMNJyaw85Go/edit
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################


import turtle


def draw_square(muzebag):


    """" we will utilize the for loop function to draw it instead of writing so much code."""

    muzebag.pensize(10)
    muzebag.penup()
    muzebag.goto(-100,40)
    muzebag.pendown()

    for i in range(4):
        muzebag.forward(300)
        muzebag.right(90)


def draw_triangle(muzebagg):

    muzebagg.left(50)
    muzebagg.forward(200)
    muzebagg.right(90)
    muzebagg.forward(230)
    muzebagg.right(60)
    muzebagg.forward(20)



def draw_rectangle(muzebagg):
    muzebagg.pensize(10)
    muzebagg.penup()
    muzebagg.goto(20, -140)
    muzebagg.pendown()

    muzebagg.left(100)
    muzebagg.forward(80)
    for i in range(3):
        muzebagg.right(90)
        muzebagg.forward(120)
    muzebagg.right(90)
    muzebagg.forward(60)

    muzebagg.pensize(10)
    muzebagg.penup()
    muzebagg.goto(-70, 10)
    muzebagg.pendown()

    for i in range(4):
        muzebagg.forward(60)
        muzebagg.right(90)
    muzebagg.forward(30)
    muzebagg.right(90)
    muzebagg.forward(60)

def main():
    """
    Docstring for main. Should describe the main functionality of this file.
    """
    muzebag=turtle.Turtle()
    wn = turtle.Screen()
    wn.bgcolor('blue')


    draw_square(muzebag)
    draw_triangle(muzebag)
    draw_rectangle(muzebag)
    wn.exitonclick()

main()  # Starts the program!