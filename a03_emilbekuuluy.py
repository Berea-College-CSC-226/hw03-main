######################################################################
# Author: Yryskeldi Emilbek uulu
# Username: emilbekuuluy
#
# Assignment: A03: Fully Functional Gitty Psychedelic Robotc Turtles
# Purpose: To continue practicing creating and using functions, more practice on using the turtle library,
# learn about how computers represent colors,
# learn about source control and git.
######################################################################
# Acknowledgements:
# # I heavily relied on the code modified by Dr. Jan Pearce. Original code:
# http://openbookproject.net/thinkcs/python/english3e/hello_little_turtles.html
# I also modified a code to create the fire flame. Original code:
# https://learn.wecode24.com/animation-with-turtle-graphics/
#
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
#################################################################################

import turtle               # allows us to use the turtles library


def make_a_tree(pos1, pos2):
    """
    Draws a beautiful tree with green leaves
    :param pos1: x coordinate
    :param pos2: y coordinate
    :return: None
    """
    # Draws the first tree "triangle":

    shape = turtle.Turtle()
    wn = turtle.Screen()
    shape.speed(9)
    shape.penup()
    shape.setpos(pos1, pos2)
    shape.pendown()
    shape.color("#32CD32")
    shape.begin_fill()
    for i in range(3):
        shape.forward(150)
        shape.left(120)
    shape.end_fill()

    # Draws the second tree "triangle":

    shape.penup()
    shape.left(90)
    shape.forward(120)
    shape.right(90)
    shape.forward(20)
    shape.pendown
    shape.color("#7CFC00")
    shape.begin_fill()
    for i in range(3):
        shape.forward(110)
        shape.left(120)
    shape.end_fill()

    # Draws the tree branch:

    shape.penup()
    shape.right(90)
    shape.forward(120)
    shape.left(90)
    shape.forward(45)
    shape.color("#8B4513")
    shape.begin_fill()
    for i in range(2):
        shape.forward(20)
        shape.right(90)
        shape.forward(40)
        shape.right(90)
    shape.end_fill()
    shape.hideturtle()


def some_text(text, pos1, pos2):
    """
    Writes a slogan in the middle
    :param text: Text that shows up on screen
    :param pos1: x coordinate of the text
    :param pos2: y coordinate of the text
    :return: None
    """
    shape = turtle.Turtle()
    shape.color("#FF0000")
    shape.size = 30
    shape.penup()
    shape.setpos(pos1, pos2)
    shape.pendown()
    shape.hideturtle()
    shape.write(text, move=False, align='center', font=("Georgia",20, ("bold", "normal")))


def background_for_text(pos1, pos2):
    """
    Gives the text a readable background
    :param pos1: x coordinate
    :param pos2: y coordinate
    :return: None
    """
    shape = turtle.Turtle()
    shape.color("#F5F5F5")
    shape.penup()
    shape.setposition(pos1, pos2)
    shape.pendown()
    shape.begin_fill()
    for i in range(2):
        shape.forward(226)
        shape.left(90)
        shape.forward(70)
        shape.left(90)
    shape.end_fill()
    shape.hideturtle()


def fires_and_flames(pos1, pos2):
    """
    Creates a moving fire flame, representing the destruction of the Amazon forest
    :param pos1: x coordinate of the fire flame
    :param pos2: y coordinate
    :return: None
    """
    screen = turtle.Screen()
    shape = turtle.Turtle()
    screen.tracer(0)
    screen.addshape("fireball.gif")
    shape.speed(0.01)
    shape.shape("fireball.gif")  # now set the turtle's shape to it
    shape.penup()
    shape.goto(pos1, pos2)
    while True:
        screen.update()
        shape.forward(0.1)
        if shape.position() == (-100, -50):
            break


def main():
    """
    The "boss" function - consolidates all functions together, and determines and alters background pictures.
    :return: None
    """
    wn = turtle.Screen()
    wn.bgpic("cool_background.gif")
    make_a_tree(-250, -127)
    make_a_tree(-170,-135)
    make_a_tree(-200, -140)
    background_for_text(-30, 50)
    wn.bgpic("forest_fire.gif")
    some_text("STOP AMAZON \n DESTRUCTION!", 80, 50)
    fires_and_flames(-170, -50)
    wn.exitonclick()


main()
