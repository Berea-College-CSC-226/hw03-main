######################################################################
# Author: Will Pratt
# Username: prattw
# https://docs.google.com/document/d/1BYwAcLtaumWrIs0W1QkbSx6m2r7iBi08zLiBIwyRW3k/edit?usp=sharing
# Assignment: A03: A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Continue practicing creating and using functions.
######################################################################
# Acknowledgements:
# https://www.youtube.com/watch?v=OgOzNpUv3Gc - using background image
#################################################################################
import turtle


def house(builder):
    """
    This creates the main body of the house.
    :param builder
    :return none
    """

    builder.color(50, 100, 150)
    builder.penup()
    builder.setpos(-55, -80)
    builder.pendown()
    builder.setheading(90)
    builder.begin_fill()
    for side in range(4):
        builder.forward(100)
        builder.right(90)
    builder.end_fill()


def window(builder):
    """
    This creates the window for the house.
    :param builder:
    :return: none
    """

    builder.color(224, 224, 224)
    builder.penup()
    builder.setpos(-40, -15)
    builder.pendown()
    builder.setheading(90)
    builder.begin_fill()
    for side in range(2):
        builder.forward(20)
        builder.right(90)
        builder.forward(70)
        builder.right(90)
    builder.end_fill()


def roof(builder):
    """
    This creates roof for the house.
    :param builder:
    :return: none
    """
    builder.color(255, 128, 0)
    builder.penup()
    builder.setpos(45, 20)
    builder.pendown()
    builder.setheading(180)
    builder.begin_fill()
    for side in range(3):
        builder.forward(100)
        builder.right(120)
    builder.end_fill()


def door(builder):
    """
    This creates door for the house.
    :param builder:
    :return: none
    """

    builder.color(255, 51, 51)
    builder.penup()
    builder.setpos(-15, -80)
    builder.pendown()
    builder.setheading(90)
    builder.begin_fill()
    for side in range(2):
        builder.forward(50)
        builder.right(90)
        builder.forward(20)
        builder.right(90)
    builder.end_fill()


def question(builder):
    """
    Asks a question and is the end of the program.
    :param builder:
    :return: none
    """

    builder.penup()
    builder.setpos(-35, -80)
    builder.forward(50)
    builder.color(102, 255, 255)
    builder.write("Like my crib?")


def main():
    """
    Creates the whole house.
    :return: none
    """

    wn = turtle.Screen()
    wn.bgpic("a03_back1.gif")


    turtle.colormode(255)
    builder = turtle.Turtle()

    house(builder)
    window(builder)
    roof(builder)
    door(builder)
    question(builder)

    wn.exitonclick()


main()


