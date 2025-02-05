# TODO Do not edit this file directly!
# TODO Instead, create a new file called hw03_username.py and copy this code into it!

#################################################################################
# Author: Aije Ebosele
# Username: eboselea
#
# Assignment: HW03  - Fully Functioning Gitty Pychedelic Robotic Turtles
# Purpose: Gain more pratice with turtles and fuctions,
# Google Doc Link: https://docs.google.com/document/d/16Y0xEFJ3f_ICamBh3k_8JRpmHmy1obomjudzBOIt6rE/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################


import turtle

# def make_roof(wn, shape):
"""
    Creates the roof with a navy blue color

    :param wn: a turtle Screen object
    :param shape: a Turtle object
    :return: None
    """
    # wn.register_shape()  # Registers a shape so it can be used by the turtle library
    # shape.penup()
    # shape.setpos(20, 20)
    # shape.pendown()
    # shape.shape("navy blue")  # Sets the shape to the image registered above
    # shape.stamp()

def make_main_house(shape):
    """
    Creates the base of the house in the shape of a square

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


    # ....


def make_door(shape):
    """
    Add a door for the house

    :param shape: a turtle object
    :return: None
    """
    shape.penup()
    shape.setpos(-8, -30)
    shape.pendown()
    shape.color('#1C1C25')
    shape.begin_fill()
    for side in range(2):
        shape.forward(40)
        shape.left(90)
        shape.forward(65)
        shape.left(90)
    shape.end_fill()


def main():
    """
    Docstring for main. Should describe the main functionality of this file.
    """
    wn = turtle.Screen()
    wn.colormode(255)
    wn.bgcolor("light blue")
    shape = turtle.Turtle()
    shape.hideturtle()

    # make_roof(wn, shape)
    make_main_house(shape)
    make_door(shape)
    wn.exitonclick()
    
    
    # Function calls to function_1 and function_2.
    # function_1()
    # function_2()


main()  # Starts the program!