######################################################################
# Author: Joey Martin
# Username: martinj2
#

# Assignment: A03
######################################################################


import turtle
wn = turtle.Screen()
ne = turtle.Turtle()
fe = turtle.Turtle()


def draw_star():
    ne.penup()
    ne.forward(85)
    ne.left(90)
    ne.forward(200)
    ne.pendown()
    for i in range(12):
        ne.left(90)
        ne.forward(180)
        ne.right(-60)
        """Function that creates a star on the canvas."""


def draw_star2():
    fe.penup()
    fe.forward(-85)
    fe.left(-90)
    fe.forward(200)
    fe.pendown()
    for i in range(12):
        fe.left(90)
        fe.forward(180)
        fe.right(-60)
        """Function that creates a second star reflected across from the second one."""


def main_func():
    draw_star()
    draw_star2()
    """Creates a main function that houses all other functions."""


main_func()
wn.exitonclick()