#################################################################################
# Author: Jaren Vessels
# Username: vesselsj2
#
# Assignment: T03: Boustrophedon Turtles
# Purpose: To draw an illusion with a person floating on it
#################################################################################
# Acknowledgements:
#   Runestone Academy Chapter 5: Modules
#   Used AI to help debug random module that was not letting me randomize the color of my screen and turtles
#   Used AI to help me debug my illusion pattern that was not increasing in size on each repetition
#################################################################################

import turtle
import random


def ran_col():
    """
    Creates the random rgb generator for my code
    """
    r = int(random.random() * 255)
    g = int(random.random() * 255)
    b = int(random.random() * 255)
    return r, g, b


def draw_person(ben, wn):
    """
    Randomizes the color of the background screen when this function is called
    """
    wn.bgcolor(ran_col())
    ben.speed(0)
    ben.pensize(10)
    ben.penup()
    ben.goto(-100, 50)  # Setting up the position of ben to draw the person
    ben.right(90)
    ben.pendown()

    ben.color(ran_col())  # Randomizes the color of the person's head

    for i in range(4):  # This is drawing the person's head
        ben.forward(50)
        ben.left(90)

    ben.color(ran_col())  # Randomizes the color of the person's torso

    ben.penup()  # This is drawing the person's torso
    ben.goto(-50, 25)
    ben.left(90)
    ben.pendown()
    ben.forward(130)

    ben.color(ran_col())  # Randomizes the color of the person's legs

    ben.left(45)  # This is drawing the person's legs
    ben.forward(80)
    ben.penup()
    ben.goto(80, 25)
    ben.right(90)
    ben.pendown()
    ben.forward(80)
    ben.penup()

    ben.color(ran_col())  # Randomizes the color of the person's arms

    ben.goto(10, 25)  # This is drawing the person's arms
    ben.pendown()
    ben.right(90)
    ben.forward(80)
    ben.right(90)
    ben.forward(35)
    ben.penup()
    ben.goto(10, 25)
    ben.pendown()
    ben.forward(80)
    ben.left(90)
    ben.forward(35)


def draw_illusion(gilbert, wn):
    """
    Randomizes the color of the background screen when this function is called
    """
    wn.bgcolor(ran_col())
    gilbert.speed(0)
    gilbert.color(ran_col())  # Randomizes the color of the illusion
    gilbert.pensize(2)
    length = 2   # Defines the length of each line the turtle makes, so it can increase
    for i in range(400):  # Draws the entire illusion
        gilbert.forward(length)
        gilbert.left(270)
        length += 2  # Increases the line of the turtle by 2 each time

    gilbert.hideturtle()


def main():
    """
    Changing the color mode to allow for a large range of randomly generated rgb colors
    Assigning gilbert to turtle then colling draw_illusion to draw the illusion first, then assigning ben to turtle and
    drawing the person after for the person to be seen as under the water
    """
    wn = turtle.Screen()
    wn.colormode(255)
    gilbert = turtle.Turtle()
    draw_illusion(gilbert, wn)
    ben = turtle.Turtle()
    draw_person(ben, wn)
    wn.exitonclick()


main()
