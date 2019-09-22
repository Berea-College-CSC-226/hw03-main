#################################################################################
# Author: Zyshavia Garrett
# Username: garrettz
#
# Assignment: A03: A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Practicing functions and coding to get a better understanding of what we are learning
# Google Doc Link: https://docs.google.com/document/d/14YjyvWSsdMgKiIYLNBry9LNaX2Z0cwDbTgxr8Tma30o/edit?usp=sharing
#
#################################################################################
# Acknowledgements: Shawn Villahermosa helped me upload my image into my code
#
#
#################################################################################

import turtle                       # Brings in a turtle from the library


def draw_roof(shape):
    """


    :param shape: a Turtle object, this function draws the roof
    :return: None
    """
    shape.penup()                               # Pen is up
    shape.setpos(30, 47)                        # The set position of the roof
    shape.pendown()                             # Pen is up
    shape.color("#1faf0a")                      # Color of the roof (green)
    shape.begin_fill()                          # Shape is filled in with the color green
    for num in range(3):                        # A loop to draw the triangle roof shape
        shape.forward(100)
        shape.left(120)
    shape.end_fill()                            # End the fill for the color of the roof

def draw_house(shape):

    '''

    :param shape: a turtle object, the function draws the house shape
    :return: None
    '''

    shape.setpos(30, 47)                        # The set position of the house
    shape.color('#ffc300')                      # The desired color of the house which is yellow
    shape.begin_fill()                          # Shape is filled in with the color yellow
    for side in range(2):                       # A loop to draw the rectangle shape of the house
        shape.forward(100)
        shape.right(90)
        shape.forward(140)
        shape.right(90)
    shape.end_fill()                            # End the fill for the shape of the house


def draw_window(shape, x, y):

    '''

    :param shape: a turtle function, that draws 2 windows on the house
    :param x: controls the left window
    :param y: controls the right window
    :return: None
    '''

    shape.penup()                               # Pen is up for the shape of the windows
    shape.setpos(x, y)                          # Set position for the windows
    shape.pendown()                             # Pen is down
    shape.color('#8a876b')                      # The color of the windows which is grey
    shape.begin_fill()                          # Begin to fill in the color of the windows
    for side in range(2):                       # A loop for the rectangle shape of the windows
        shape.forward(30)
        shape.right(90)
        shape.forward(20)
        shape.right(90)
    shape.end_fill()                            # End the fill for the color of the windows


def draw_door(shape):
    """

    :param shape: a turtle object, the shape of the door
    :return: None
    """

    shape.penup()                               # Pen is up
    shape.setpos(70, -42)                       # The set position for the door shape
    shape.pendown()                             # Pen is down
    shape.color('#8a876b')                      # The color of the door which is grey
    shape.begin_fill()                          # Begin to fill in the color for the door
    for side in range(2):                       # A loop for the shape of the door
        shape.forward(20)
        shape.right(90)
        shape.forward(50)
        shape.right(90)
    shape.end_fill()                            # End the fill for the color of the door


def window_screen(wn):
    """

    :param wn: a turtle object, the window screen
    :return: None
    """

    wn = turtle.Screen()                        # This sets up the window screen
    wn.title("garrettz")                        # This is the title on the window screen


def main():                                     # The function calls all the other functions
    """

    :return: None
    """

    wn = turtle.Screen()                        # Calls and pulls up the window screen
    wn.bgpic("island.gif")                      # The picture of the background on the window screen
    wn.title("garrettz")                        # The title name of the window
    shape = turtle.Turtle()                     # Shape is the name of the turtle that is being imported on the window
                                                # screen
    shape.hideturtle()                          # The turtle is invisible

    draw_roof(shape)
    draw_house(shape)
    draw_window(shape, 45, 0)                   # Position of the 'x' window
    draw_window(shape, 88, 0)                   # Position of the 'y' window
    draw_door(shape)

    wn.exitonclick()                            # Window will close when the users clicks on the screen


main()                                          # End of the call of the funcitons