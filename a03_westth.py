#################################################################################
# Author:Tom West
# Username:Westth
#
# Assignment:A03
# Purpose:to creatively use turtles
#################################################################################
# Acknowledgements:
#
#
#################################################################################
import turtle
wn = turtle.Screen()
wn.bgcolor("#237A08")

f: int = int(input("please put in a number: "))

box_t = turtle.Turtle()

def box_boi():
    """draw the head"""
    box_t.begin_fill()
    box_t.color("#FFB341")
    for i in [0, 1, 2, 3]:
        box_t.forward(f)
        box_t.left(90)
    box_t.end_fill()


def neck_boi():
    """draw body"""
    box_t.color("#3B5323")
    box_t.fd(f/2)
    box_t.right(90)
    box_t.pensize(f/9)
    box_t.fd(f)


def lleg_boi():
    """draw left leg"""

    box_t.color("#458B74")

    box_t.right(45)
    box_t.fd(f/2)
    box_t.left(180)
    box_t.fd(f/2)

def rleg_boi():
    """draw right leg"""

    box_t.color("#458B74")

    box_t.right(90)
    box_t.fd(f/2)
    box_t.right(180)
    box_t.fd(f/2)


def rarm_boi():
    """draw right arm"""

    box_t.color("#3B5323")

    box_t.right(45)
    box_t.fd(f*(2/3))
    box_t.color("#FFB341")

    box_t.right(135)
    box_t.forward(f/2)
    box_t.right(180)
    box_t.forward(f/2)

def larm_boi():
    """draw left arm"""

    box_t.color("#FFB341")

    box_t.left(90)
    box_t.forward(f/2)
    box_t.right(180)
    box_t.forward(f/2)


def hat_boi():
    """draw a hat"""

    hatter = turtle.Turtle()
    hatter.penup()
    hatter.color("red")
    hatter.left(90)
    hatter.forward(f)
    hatter.left(90)
    hatter.pendown()
    hatter.begin_fill()
    hatter.forward(f)
    hatter.right(90)
    hatter.forward(f/10)
    hatter.right(90)
    hatter.fd(f)
    hatter.left(90)
    hatter.forward(f/2)
    hatter.right(90)
    hatter.forward(f)
    hatter.right(90)
    hatter.forward(f/2+f/10)
    hatter.right(90)
    hatter.forward(f)
    hatter.end_fill()


def eye_boi():
    """draw eyes"""

    eye = turtle.Turtle()
    eye.penup()
    eye.forward(f/4)
    eye.left(90)
    eye.forward(f*(2/3))
    eye.stamp()
    eye.right(90)
    eye.fd(f*(1/2))
    eye.left(90)
    eye.stamp()


def smile():
    """draw a smile"""
    smile = turtle.Turtle()
    smile.penup()
    smile.forward(f/4)
    smile.left(90)
    smile.forward(f/5)
    smile.right(90)
    smile.pendown()
    smile.fd(f/2)


def main():
    """bring them all together """
    box_boi()
    neck_boi()
    lleg_boi()
    rleg_boi()
    rarm_boi()
    larm_boi()
    hat_boi()
    eye_boi()
    smile()
    wn.exitonclick()


main()
