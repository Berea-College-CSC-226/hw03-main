#################################################################################
# Author: Jenifer Fidelia
# Username: Fideliaj
#
# Assignment: Assignment A03: A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Practice with turtles
# Google Doc Link: https://docs.google.com/document/d/1AprOdlvU8YhPuuFHKBv7yRZcV577FbII6cN51yRFOkI/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#TA: Thank you, Audrey Craft, for your assistance and awesomeness :)
#
#################################################################################

import turtle


def make_square(t,size):
    """
    Make a square. Parameter (size) is how big you want it to be.
    """
    # This will be the house
    for i in range (4):
        t.forward (size)
        t.left (90)

    t.speed(0)

def make_triangle(t,base,side):
    """
    Making triangle.Parameter (size) is how big you want it to be.
    """
    # This will be the roof and the tree
    t.right(45)
    t.forward (side)
    t.right(90)
    t.forward(side)
    t.right(135)
    t.forward (base)

def make_rectangle(t,l,w):
    """
    This function will draw a triangle
    :param t: turtle name
    :param l: length
    :param w: width
    :return: none
    """
    for i in range (2):
        t.forward (w)
        t.left (90)
        t.forward(l)
        t.left(90)

def main():
    """
    Main functions: place to call other functions
    """

    # set up screens and background
    wn= turtle.Screen()
    wn.colormode(255)
    wn.bgcolor(176,224,230)

    #make my turtles
    squary=turtle.Turtle()
    tri=turtle.Turtle()
    rector=turtle.Turtle()
    winny=turtle.Turtle()
    sunny=turtle.Turtle()

    #set turtles colormode
    wn.colormode(255)

    #Drawing body of house
    squary.penup()
    squary.setpos(-150,-150)
    squary.pendown()
    squary.fillcolor("Pale Goldenrod")
    squary.begin_fill()
    make_square(squary,180)   # Function call to make the body of the house
    squary.end_fill()

    #Drawing roof
    tri.penup()
    tri.setpos(-150,-150)
    tri.pendown()
    tri.left(90)
    tri.forward(180)
    tri.fillcolor("Goldenrod")
    tri.begin_fill()
    make_triangle(tri,180,127.8)       # Function call to make the roof
    tri.end_fill()

    #Drawing door
    rector.penup()
    rector.setpos(-150,-150)
    rector.pendown()
    rector.forward(67.5)
    rector.fillcolor("Light Yellow")
    rector.begin_fill()
    make_rectangle(rector,60,35)
    rector.end_fill()

    #Drawing window
    winny.penup()
    winny.backward(25)
    winny.right(90)
    winny.forward(30)
    winny.left(90)
    winny.pendown()
    winny.fillcolor("Pale Turquoise")
    winny.begin_fill()
    make_square(winny,30)       #function call to make window
    winny.end_fill()

    #Drawing line
    squary.forward(-210)
    squary.forward(800)
    squary.backward(310)

    #Drawing tree
    squary.fillcolor("sienna")
    squary.begin_fill()
    make_rectangle(squary,60,40)
    squary.end_fill()
    squary.left(90)
    squary.forward(60)
    squary.left(90)
    squary.forward(20)
    squary.right(90)
    for i in range(3):
        squary.fillcolor("Olive Drab")
        squary.begin_fill()
        make_triangle(squary,80,56.56)
        squary.end_fill()
        squary.penup()
        squary.right(90)
        squary.forward(40)
        squary.pendown()

    #Drawing sun
    sunny.penup()
    sunny.setpos(200,110)
    sunny.pendown()
    sunny.fillcolor("gold")
    sunny.begin_fill()
    sunny.circle(60)
    sunny.end_fill()

    #hideturtles
    squary.hideturtle()
    tri.hideturtle()
    rector.hideturtle()
    winny.hideturtle()
    sunny.hideturtle()

    #exitonclick
    wn.exitonclick()

main()
