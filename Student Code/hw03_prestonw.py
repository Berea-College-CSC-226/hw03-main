#################################################################################
# Author: Preston Worrix
# Username: PrestonW
#
# Assignment: Hw03
# Purpose:
# Google Doc Link: https://docs.google.com/document/d/1wp-QNkUn3xx7g0dSDVIFPG55qqMa7v1_PquHjwZZhhc/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle

def draw_pig_1(turt):

    """this function moves the turtle to the propper loctation to start
    drawing the pig on the screen along with setting the color and pen size"""

    turt.speed()
    turt.penup()
    turt.forward(1)
    turt.forward(40)
    turt.forward(1)
    turt.color("black")
    turt.forward(40)
    turt.left(90)
    turt.pensize(3)


def draw_pig_2(turt):

    """ this function draws the first large circle for the pig and fills
    it in"""

    turt.penup()
    turt.forward(120)
    turt.left(90)
    turt.forward(1)
    turt.forward(120)
    turt.forward(1)
    turt.left(90)
    turt.forward(60)
    turt.left(90)
    turt.forward(60)
    turt.pensize(3)
    turt.left(90)
    turt.forward(120)
    turt.left(90)

    turt.pendown()
    turt.color("black")
    turt.fillcolor(255,0,255)
    turt.begin_fill()
    for i in range(360):
        turt.forward(3)
        turt.left(1)
    turt.end_fill()

def draw_pig_3(turt):

    """ this function draws the semi circles for the ears
     and fills them in"""

    turt.penup()
    for i in range(30):
        turt.forward(3)
        turt.left(1)
    turt.right(90)

    turt.pendown()
    turt.fillcolor(255,0,255)
    turt.begin_fill()
    for i in range(215):
        turt.forward(1)
        turt.left(1)
    turt.end_fill()

    turt.penup()
    turt.left(90)
    for i in range(90):
        turt.forward(3)
        turt.right(1)
    turt.forward(3)

    turt.pendown()
    turt.left(90)
    turt.begin_fill()
    for i in range(220):
        turt.forward(1)
        turt.right(1)
    turt.end_fill()

def draw_pig_4(turt):

    """ this function teleports the turtle back to the 0,0 and draws the face
    of the pig nose and eyes"""

    turt.teleport(0,0)
    turt.left(155)
    turt.color("black")
    turt.pensize(20)
    turt.forward(1)

    turt.penup()
    turt.forward(40)

    turt.pendown()
    turt.forward(1)

    turt.penup()
    turt.forward(40)
    turt.left(90)

    turt.pendown()
    turt.pensize(3)
    for i in range(180):
        turt.left(2)
        turt.forward(2)

    turt.penup()
    turt.forward(120)
    turt.color("black")
    turt.left(90)

    turt.pendown()
    turt.pensize(20)
    turt.forward(1)

    turt.penup()
    turt.forward(120)

    turt.pendown()
    turt.forward(1)

def main():

    """ this function main creates the turtle and screen along with calling
    all other functions the program in total should use multiple functions
    to set the background color to green and draw a basic pig colored in
    using a combination of circles dots and semi circles."""

    tess = turtle.Turtle()
    tess.pensize(3)

    wn = turtle.Screen()
    wn.bgcolor("green")
    wn.colormode(255)

    # Function calls to function_1 and function_2.
    draw_pig_1(tess)
    draw_pig_2(tess)
    draw_pig_3(tess)
    draw_pig_4(tess)

    wn.exitonclick()

main()  # Starts the program!