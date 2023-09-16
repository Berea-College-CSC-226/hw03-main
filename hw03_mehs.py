#################################################################################
# Author: Su Meh
# Username: mehs
#
# Assignment: HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: To get a better grasp of how Git works.
# Google Doc Link: https://docs.google.com/document/d/11qWG8MLGUfP-ofBRrbgEXcZg3TRbhSOh5YrcnjNUAkg/edit?usp=sharing
#
#################################################################################
# Acknowledgements: Dr Scotts Heggens for the layout.
#
#
#################################################################################

import turtle


def draw_roof(rf):
    """
    Docstring for function_1
    """
    pass
    # ....
    rf.penup()
    rf.fd(200)
    rf.left(145)

    for i in range(1):
        rf.speed(2)
        rf.pendown()
        rf.pensize(5)
        rf.pencolor("white")
        rf.fd(200)
        rf.left(35)
        rf.forward(200)
        rf.left(35)
        rf.fd(200)
        rf.left(145)
        rf.fd(530)



def fill_roof(filr):
    """
    Docstring for function_1
    """
    pass
    # ....
    filr.penup()
    filr.fd(189)
    filr.left(145)
    filr.fd(10)
    filr.color("red")

    for i in range(1):
        filr.pendown()
        filr.pensize(8)
        filr.fd(184)
        filr.left(35)
        filr.fd(190)
        filr.left(35)
        filr.fd(184)
        filr.left(145)
        filr.fd(496)

def fill_roof1(filr1):
    """
    Docstring for function_1
    """
    pass
    # ....
    filr1.penup()
    filr1.fd(176)
    filr1.left(145)
    filr1.fd(10)
    filr1.color("orange")

    for i in range(1):
        filr1.pendown()
        filr1.pensize(8)
        filr1.fd(174)
        filr1.left(35)
        filr1.fd(180)
        filr1.left(35)
        filr1.fd(174)
        filr1.left(145)
        filr1.fd(486)

def draw_house(hse):
    """
    Docstring for function_2
    """
    pass
    # ...'
    hse.penup()
    hse.fd(200)
    hse.right(90)

    for i in range(2):
        hse.pendown()
        hse.pensize(5)
        hse.pencolor("white")
        hse.fd(200)
        hse.right(90)
        hse.fd(528)
        hse.right(90)

def fill_house(filhse):
    """
    Docstring for function_1
    """
    pass
    # ....

def main():
    """
    Docstring for main
    """
    # ...

    wn = turtle.Screen()
    rf = turtle.Turtle()
    hse = turtle.Turtle()
    filr = turtle.Turtle()
    filhse = turtle.Turtle()
    filr1 = turtle.Turtle()

    wn.bgcolor("purple")

    draw_roof(rf)  # Function call to roof
    draw_house(hse)  # Function call to house
    fill_roof(filr)  # Function call to fill roof
    fill_house(filhse)  # Function call to fill roof
    fill_roof1(filr1)
    wn.exitonclick()

main()


