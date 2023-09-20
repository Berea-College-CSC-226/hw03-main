#################################################################################
# Author: Josh Wakin
# Username:thealphagurlux
#
# Assignment: HW03
# Purpose: To draw a circle, fill it, then draw a * over it.
# Google Doc Link:https://docs.google.com/document/d/1638XgwboqPy_1V2K1NU523jD-TeApx-yEHIs-DOrhQ8/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#################################################################################

import turtle


t1=turtle.Turtle() #turtle to draw with
t1=turtle.penup()  #pull the turtles pen up because we are going to offset it
t1=turtle.pensize(30)
wn=turtle.Screen()
wn.bgcolor("Blue")

########(functions)########
def draw_linesthick():
    ##move to the center of the circle.
    t1=turtle.left(90)
    t1=turtle.forward(100)
    t1=turtle.right(90)
    t1=turtle.pencolor(1,.2,.6)
    for i in range(8):
        ##Draw the lines with a loop.


        t1 = turtle.left(45)
        t1 = turtle.forward(100)
        t1 = turtle.forward(100 * -1)


def draw_linesthin():
    ##Drawoverlines but smaller lines.
    t1=turtle.pencolor(1,.8,.2)
    t1=turtle.pensize(12)
    for i in range(8):
        ##Draw the lines with a loop.


        t1 = turtle.left(45)
        t1 = turtle.forward(100)
        t1 = turtle.forward(100 * -1)


def draw_circle():
    ####move the turtle down and draw a circle around the center and fill it.
    t1=turtle.right(90)
    t1=turtle.forward(100)
    t1=turtle.pendown()
    t1 = turtle.fillcolor(.2,.3,.1)
    t1=turtle.begin_fill()
    t1 = turtle.right(-90)
    t1=turtle.pencolor(.2,.3,.1)
    t1=turtle.circle(100)
    t1=turtle.end_fill()




def main():
    ####Calls functions to draw a circle, fill it, then a * on top
    draw_circle()

    draw_linesthick()
    ###Draw over same lines but with a thinner pen width.
    draw_linesthin()



##Body##

main()


wn.exitonclick()




