#################################################################################
# Author: Tawanda Kumbula
# Username: kumbula369
#
# Assignment: A03_A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Creating useful functions
#################################################################################
# Acknowledgements:
# Google document URL: https://docs.google.com/document/d/1pYePMqtWoGBR1tD9cJOawBtUxx7mR0Frm8LI3ebTi98/edit?usp=sharing
#
#################################################################################

import turtle
from time import sleep

#

def move(t, x, y):
    t.up()
    t.setpos(x, y)
    t.down()

def Draw_Right(t,p, R, G, B):
        """"
         Draws the right side of the butterfly.
        :param p: Determines the perimeter of the turtle drawing the right wing.
        :param R: Determines the red value of the turtle drawing the right wing
        :param G: Determines the green value of the turtle drawing the right wing.
        :param B: Determines the blue value of the turtle drawing the right wing.
        :return: Returns None

        """
        t.color(R, G, B)
        t.pensize(3)
        t.pencolor(1, 0.6, 0)
        t.setpos(0, 0)
        t.right(75)
        t.begin_fill()
        t.fd(80)
        t.circle(40, 120)
        t.fd(50)
        t.circle(10, 100)
        t.circle(10, 5)
        t.circle(5, 90)
        t.right(90)
        t.fd(90)
        t.right(145)
        t.fd(70)
        t.circle(40, 50)
        t.circle(5, 90)
        t.right(60)
        t.fd(70)
        t.left(45)
        t.circle(40, 90)
        t.fd(110)
        t.end_fill()
        print(t.pos())

def Draw_left(t,R, G, B):
    t.color(R, G, B)
    t.pensize(3)
    t.pencolor(1, 0.6, 0)
    move(t,-15,-10)

    t.left(20)
    t.begin_fill()
    t.fd(80)
    t.circle(-40, 120)
    t.fd(50)
    t.circle(-10, 100)
    t.circle(-10, 5)
    t.circle(-5, 90)
    t.right(-90)
    t.fd(90)
    t.right(-145)
    t.fd(70)
    t.circle(-40, 50)
    t.circle(-5, 90)
    t.right(-60)
    t.fd(70)
    t.left(-45)
    t.circle(-40, 90)
    t.fd(110)
    t.end_fill()

def Draw_Body(t,R, G, B):
    """"
    """
    t.color(R, G, B)
    t.shape("turtle")
    t.pensize(1)
    move(t, -5, 5)
    t.right(90)
    t.stamp()
    t.fd(20)
    t.right(180)
    t.fd(30)
    print(t.pos())





def main():
    """"
    Draws the whole butterfly.
    :Return none
    """
    cast = turtle.Turtle()
    cast.color(0,0,1)      # Draws the right side wings.
    tusk = turtle.Turtle() # Draws the butterfly's body.
    wn = turtle.Screen()
    wn.bgpic("C.PNG")
    Draw_Right(cast, 0, 0, 0, 1)
    Draw_left(cast,0, 0, 1)
    Draw_Body(tusk, 0.6, 0.5, 0.5)

    wn.exitonclick()

main()

