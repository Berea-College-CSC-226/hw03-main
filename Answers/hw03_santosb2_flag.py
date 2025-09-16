

#################################################################################
# Author:
# Username:
#
# Assignment:
# Purpose:
# Google Doc Link:
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################
import turtle
wn = turtle.Screen()
tess = turtle.Turtle()


def make_sqaure():
    tess.penup()
    tess.setposition(-200,-100)
    tess.pendown()
    tess.begin_fill()

    for i in range(2):
        tess.color(0, 156, 59)
        tess.forward(400)
        tess.left(90)
        tess.forward(270)
        tess.left(90)
    tess.end_fill()



def middle_shape():
    def make_circle():
        tess.left(135)
        tess.begin_fill()
        tess.penup()
        tess.setposition(5,-40)
        tess.pendown()
        tess.color(7, 7, 99)
        tess.circle(70)
        tess.end_fill()
    def make_weird_square():
        tess.begin_fill()
        tess.color("yellow")
        tess.penup()
        tess.setposition(-120,30)
        tess.pendown()
        tess.right(45)
        tess.forward(180)
        tess.left(90)
        tess.forward(180)
        tess.left(90)
        tess.forward(180)
        tess.left(90)
        tess.forward(180)
        tess.end_fill()
    make_weird_square()
    make_circle()



def main():
    wn.colormode(255)
    wn.bgcolor(152, 163, 175)
    tess.speed(5)

    # Function calls to function_1 and function_2.
    make_sqaure()            #
    middle_shape()
    wn.exitonclick()


main()  # Starts the program!