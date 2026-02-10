#################################################################################
# Author: Briana Nshimirimana
# Username: Nshimirimanao
#
# Assignment: HW03_Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose:
# Google Doc Link: https://docs.google.com/document/d/1ZtcYU7PHItUzZ4hzqbLtUHBl__7jwoWPN-NipuDiB8Q/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
# hw03_stubs_do_not_edit.py
#
#################################################################################


import turtle
import random

def draw_sun(t):
    """
    Uses turtle to draw sun on top and below the horizon.
    """
    t.hideturtle()
    t.penup()
    t.goto(0,-40)
    t.pendown()

    t.begin_fill()
    t.circle(40)
    t.end_fill()


def Horizon(Hz):
    """
     Uses turtle to draw a horizontal line across the screen to signify the horizon.
    """
    Hz.hideturtle()
    Hz.penup()
    Hz.goto(-700,0)
    Hz.pendown()
    Hz.fd(1400)


def draw_birds(bd,dist):
    """
         Uses turtle to draw birds off in the horizon.
    """


    bd.hideturtle()
    bd.penup()
    bd.goto(dist)
    bd.pendown()
    for i in range(2):
        bd.penup()
        bd.goto(dist)
        bd.pendown()


        bd.left(45)
        bd.fd(30)
        bd.right(45)
        bd.fd(10)
        bd.left(45)
        bd.fd(10)
        bd.right(45)
        bd.fd(30)
        dist = (120,120) #changing the distance for the second loop.






def main():
    """
    Docstring for main. Should describe the main functionality of this file.
    """
    wn = turtle.Screen()
    wn.bgcolor("blue")
    t = turtle.Turtle()
    t.color("orange""red")
    t.speed(0)

    Hz = turtle.Turtle()
    Hz.speed(0)
    Hz.color("darkblue")

    bd = turtle.Turtle()
    bd.speed(0)
    bd.color("black")
    dist = (-100,100)



    # calling functions to run
    draw_sun(t)
    Horizon(Hz)
    draw_birds(bd,dist)
    draw_stars(s)

    print("Enjoy the sunset!")

    wn.exitonclick()


main()  # Starts the program!