

#################################################################################
# Author: Aije Ebosele
# Username: eboselea
#
# Assignment: HW03  - Fully Functioning Gitty Pychedelic Robotic Turtles
# Purpose: Gain more pratice with turtles and fuctions, and make a complex creation in Github.
# Google Doc Link: https://docs.google.com/document/d/16Y0xEFJ3f_ICamBh3k_8JRpmHmy1obomjudzBOIt6rE/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################


import turtle



def make_main_house(shape):
    """
    Creates the base of the house in the shape of a rectangle

    :param shape: aTurtle object
    :return: None
    """
    shape.setpos(-40, -30)
    shape.color('#2C7A8A')
    shape.begin_fill()
    for side in range(2):
        shape.forward(100)
        shape.left(90)
        shape.forward(150)
        shape.left(90)
    shape.end_fill()

def make_door(shape):
    """
    Add a door for the house

    :param shape: a turtle object
    :return: None
    """
    shape.penup()
    shape.setpos(-10, -30)
    shape.pendown()
    shape.color('#1C1C25')
    shape.begin_fill()
    for side in range(2):
        shape.forward(40)
        shape.left(90)
        shape.forward(80)
        shape.left(90)
    shape.end_fill()

def make_window(shape, x, y):
    """
    Adds a window to the house.

    :param shape: a Turtle object
    :param x: the x coordinate of the window
    :param y: the y coordinate of the window
    :return: None
    """
    shape.penup()
    shape.setpos(x, y)
    shape.pendown()
    shape.color('#EFF0F0')
    shape.begin_fill()
    for side in range(2):
        shape.forward(30)
        shape.right(90)
        shape.forward(20)
        shape.right(90)
    shape.end_fill()

def make_roof(shape):
    """
    Creates a grey roof on screen

    :param wn: a turtle Screen object
    :param shape: a Turtle object
    :return: None
    """

    shape.penup()
    shape.setpos(-20, 120)
    shape.pendown()
    shape.color('#686161')
    shape.begin_fill()
    for side in range(3):
        shape.forward(60)
        shape.left(120)
    shape.end_fill()



def main():
    """
    Draw a house using the code given in the previous functions
    """
    wn = turtle.Screen()
    wn.colormode(255)
    wn.bgcolor("light blue")
    shape = turtle.Turtle()
    shape.hideturtle()


    make_main_house(shape)
    make_door(shape)
    make_roof(shape)
    make_window(shape, -30, 80)
    make_window(shape, 20, 80)
    wn.exitonclick()

main()