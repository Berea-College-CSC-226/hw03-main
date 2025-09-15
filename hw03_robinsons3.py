#################################################################################
# Author: Stephen Aaron Robinson
# Username: robinsons3
#
# Assignment: HW03
# Purpose: Draws Dog
# Google Doc Link:
#
#################################################################################

import turtle
t = turtle.Turtle()
t.speed(0)
wn = t.getscreen()


def semicircle(dir):
    #Makes a semi-circle for use in other functions like leg()
    for i in range(36):
        t.forward(1)
        if dir == 'left':
            t.left(5)
        elif dir == 'right':
            t.right(5)
    pass
    # ....


def leg(length, dir):
    #Draws leg of dog
    t.forward(length)
    semicircle(dir)
    t.forward(length)


def main():
    """
    Docstring for main. Should describe the main functionality of this file.
    """
    #First pair of legs
    t.right(90)
    leg(20, "right")
    t.right(180)
    leg(20, "right")
    t.forward(1)
    t.left(90)
    t.forward(-23)

    #Second pair of legs
    t.forward(45)
    t.left(90)
    leg(20, "right")
    t.right(180)
    leg(20, "right")
    t.forward(1)
    t.left(90)
    t.forward(-23)
    t.forward(23)


    wn.exitonclick()


main()  # Starts the program!