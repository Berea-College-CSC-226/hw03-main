

#################################################################################
# Author: Kichemy Dorcena
# Username: dorcenak
#
# Assignment: HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Continue practicing creating and using functions.
# More practice on using the turtle library.
# Learn about how computers represent colors.
# Learn about source control and Git.
# Google Doc Link: https://docs.google.com/document/d/1UZY5L1eSWr3LZ14KEjOlTP3esWBjTNbh02Yjg-hQox4/edit?usp=sharing
#
#################################################################################
# Acknowledgements: Dr Scott Heggen for the layout
#

import turtle               # allows us to use the turtles library


def make_roof(wn, shape):
    """
    A new roof! (Made from an image of bricks)

    :param wn: a turtle Screen object
    :param shape: a Turtle object
    :return: None
    """
    wn.register_shape("top.gif")         # Registers a shape so it can be used by the turtle library
    shape.penup()
    shape.setpos(120, 80)
    shape.pendown()
    shape.shape("top.gif")               # Sets the shape to the image registered above
    shape.stamp()

def make_main_house(shape):
    """
    Makes the main house rectangle.

    :param shape: a Turtle object
    :return: None
    """

    shape.setpos(1, 30)
    shape.color('#3333FF')
    shape.begin_fill()
    for side in range(2):
        shape.forward(230)
        shape.right(90)
        shape.forward(140)
        shape.right(90)
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
    shape.color('#00ff22')
    shape.begin_fill()
    for side in range(2):
        shape.forward(50)
        shape.right(90)
        shape.forward(20)
        shape.right(90)
    shape.end_fill()


def make_door(shape):
    """
    Adds a door to the house.

    :param shape: a Turtle object
    :return: None
    """
    shape.penup()
    shape.setpos(70, -60)
    shape.pendown()
    shape.color('#00ff22')
    shape.begin_fill()
    for side in range(2):
        shape.forward(60)
        shape.right(90)
        shape.forward(50)
        shape.right(90)
    shape.end_fill()


def make_flower(wn, shape):
    """
    Adds flower in the front of the house.

    :param wn: a turtle Screen object
    :param shape: a Turtle object
    :return: None
    """
    wn.register_shape("flower.gif")
    shape.penup()
    shape.setpos(110, -170)
    shape.shape("flower.gif")
    shape.stamp()
    shape.up()


def make_text(shape, txt):
    """
    Writes text to the screen.

    :param shape: a Turtle object
    :return: None
    """
    shape.color("#0F00F0")
    shape.setpos(70,140)
    shape.write(txt, move=False, align='center', font=("Arial", 30, ("bold", "normal")))


def main():
    """
    Draws a house at x, y on the screen.

    :return: None
    """

    turtle.colormode(255)           # change color modes

    wn = turtle.Screen()            # Makes a new turtle screen
    wn.bgpic("beach.gif")      # Sets background to an image; must be a gif!
    shape = turtle.Turtle()
    shape.hideturtle()

    # Function calls for each part of the house
    make_roof(wn, shape)
    make_main_house(shape)
    make_window(shape, 45, 0)
    make_window(shape, 88, 0)
    make_door(shape)
    make_flower(wn, shape)
    make_text(shape, "Kichemy's first/ugly house")

    wn.exitonclick()  # wait for a user click on the canvas


main() # call main()


