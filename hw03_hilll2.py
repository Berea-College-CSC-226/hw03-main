#################################################################################
# Author: Langston Hill
# Username: hilll2
#
# Assignment: Homework 3: Sea of Stars
# Purpose: To learn the ins and outs of git, along with implementing RGB values into code
# Google Doc Link: https://docs.google.com/document/d/11EDVFiCCLZRo3eQhymX9W1aXn25xKEMBGwPpwzYjYQI/edit?usp=sharing
#
#################################################################################
# Acknowledgements: https://colorspire.com/rgb-color-wheel/
# https://docs.python.org/3/library/turtle.html
#
#
#################################################################################


import turtle
import random


def draw_star(john):
    """
       Draws a star of red, blue, purple, a randomly generated color, or white.
       They are also of random different sizes
     """

    john.pensize(random.randrange(1, 4))
    john.pendown()

    colorgen = random.randrange(1, 10)

    if colorgen == 1:  # switch statement that decides the color of the star
        color = 255, 0, 31
    elif colorgen == 2:
        color = 78, 238, 255
    elif colorgen == 3:
        color = 193, 84, 255
    elif colorgen == 4:
        color = random.randrange(1, 255), random.randrange(1, 255), random.randrange(1, 255)
    else:
        color = 255, 255, 255

    john.pencolor(color)
    x = random.randrange(2, 7)
    for i in range(4):
        john.forward(x)
        john.backward(x)
        john.left(90)


def draw_sun(john):
    """
       Draws the sun and its rays of random lengths and widths
    """
    john.pensize(10)
    john.pencolor("orange")
    john.fillcolor("yellow")
    john.goto(0, 100)
    john.pendown()
    john.begin_fill()
    john.circle(100)
    john.end_fill()
    john.left(90)
    john.penup()
    john.forward(100)
    john.right(50)

    for i in range(72):
        x = random.randrange(75, 250)
        john.pensize(random.randrange(1, 10))
        john.penup()
        john.forward(100)
        john.pendown()
        john.forward(x)
        john.backward(x)
        john.penup()
        john.backward(100)
        john.left(5)


def starfield(john):
    """
       Draws a star at random locations on the screen, and then shifts orientation. This is repeated 100 times
    """
    for i in range(100):
        x = random.randrange(-400, 400)
        y = random.randrange(-300, 300)
        john.left(45)
        draw_star(john)
        john.penup()
        john.goto(x, y)


def main():
    """
       Draws a sea of randomly generated stars along with a sun at the end.
    """
    wn = turtle.Screen()
    wn.colormode(255)
    wn.bgcolor("black")
    wn.title("Stars")

    john = turtle.Turtle()  # Creates john and set some attributes
    john.pensize(20)

    john.speed(0)

    starfield(john)
    draw_sun(john)
    wn.exitonclick()


main()
