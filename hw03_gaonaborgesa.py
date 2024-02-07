#################################################################################
# Author: America Gaona Borges
# Username: gaonaborgesa
#
# Assignment: HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Continue practicing creating and using functions.
# More practice on using the turtle library.
# Learn about how computers represent colors.
# Learn about source control and Git.
#
# Google Doc Link: https://docs.google.com/document/d/1h14KMmSeHQAEvo7u2CwElS8fjyTEb8Z_fG7SychdmWs/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle


def draw_grass(t):
    """
    Makes grass and fills it in.

    :param t: turtle object
    :return: None
    """
    t.penup()              # positions turtle
    t.setpos(-310, -200)
    t.pendown()

    for i in range(2):          # makes grass
        t.forward(610)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(610)
        t.left(90)
        t.forward(25)
        t.left(90)


def draw_sun(t):
    """
    Makes sun and sun rays.

    :param t: turtle object
    :return: None
    """
    t.penup()              # positions turtle
    t.setpos(212, 265)
    t.pendown()
    t.right(105)

    for i in range(17):       # sun
        t.forward(10)
        t.left(10)

    t.penup()              # sun rays 1/4
    t.setpos(187, 250)
    t.pendown()
    t.left(100)
    t.forward(25)
    t.penup()

    t.setpos(195, 210)      # sun rays 2/4
    t.pendown()
    t.left(45)
    t.forward(25)
    t.penup()

    t.setpos(230, 178)      # sun rays 3/4
    t.pendown()
    t.left(35)
    t.forward(25)
    t.penup()

    t.setpos(280, 165)      # sun rays 4/4
    t.pendown()
    t.left(25)
    t.forward(25)


def draw_flower(t):
    """
    Makes flower.

    :param t: turtle object
    :return: None
    """

    stem = turtle.Turtle()        # flower stem
    stem.color("green")
    stem.pensize(15)
    stem.setpos(0, -200)
    stem.left(90)
    stem.forward(200)
    stem.speed(10)

    t.begin_fill()
    t.color("#dc99ec")    # DC99EC (light purple)

    for i in range(8):         # flower petals
        t.right(20)
        t.forward(70)
        t.left(30)
        t.forward(40)
        t.left(125)
        t.forward(40)
        t.left(50)
        t.forward(70)
        t.right(50)
    t.end_fill()


def main():

    """
    The main function of the program, where all functions are activated. Makes all turtle objects and the screen.

    :return: None
    """
    wn = turtle.Screen()

    wn.bgcolor("lightblue")

    peter = turtle.Turtle()         # turtle for grass
    peter.pensize(25)
    peter.color("green")
    peter.hideturtle()
    peter.speed(0)

    lois = turtle.Turtle()          # turtle for flower
    lois.pensize(10)
    lois.hideturtle()
    lois.speed(7)

    meg = turtle.Turtle()            # turtle for sun
    meg.pensize(10)
    meg.pencolor("yellow")
    meg.hideturtle()
    meg.speed(9)

    draw_grass(peter)
    draw_sun(meg)
    draw_flower(lois)

    wn.exitonclick()


main()
