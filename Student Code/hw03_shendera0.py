#################################################################################
# Author: Beni Shendera
# Username: oshendera
#
# Assignment:HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose:Creating a complex shape
# Google Doc Link:https://docs.google.com/document/d/1K0_eEC7B2a8JhkXA6MIDyG--ymo9hbkhb52r23a1eRk/edit?tab=t.0#heading=h.j4414z2ufr72
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle


def draw_background():
    """Sets up the turtle screen background."""
    screen = turtle.Screen()
    screen.bgcolor("#87CEEB")  # RGB sky blue
    return screen


def draw_house(x,y,):
    """Draws a house at a specific location(x,y)."""
    t = turtle.Turtle()
    t.speed(10)
    t.penup()
    t.goto(x,y)
    t.pendown()

    # House base
    t.fillcolor("#B22222")  # firebrick red
    t.begin_fill()
    for _ in range(4):
        t.forward(200)
        t.left(90)
    t.end_fill()

    # Roof
    t.fillcolor("#8B4513")  # brown
    t.begin_fill()
    t.left(45)
    for _ in range(2):
        t.forward(200 / (2 ** 0.5))
        t.left(90)
    t.end_fill()


def draw_door(a, b):
    """Draws a door at the given (a, b) position."""
    t = turtle.Turtle()
    t.speed(10)
    t.penup()
    t.goto(a,b)
    t.pendown()

    t.fillcolor("#654321")  # dark brown
    t.begin_fill()
    for _ in range(2):
        t.forward(50)
        t.left(90)
        t.forward(100)
        t.left(90)
    t.end_fill()


def draw_window(x, y):
    """Draws a window with panes at the given (x, y) position."""
    t = turtle.Turtle()
    t.speed(10)
    t.penup()
    t.goto (x, y)
    t.pendown()

    t.fillcolor("#FFFF99")  # light yellow
    t.begin_fill()
    for _ in range(4):
        t.forward(50)
        t.left(90)
    t.end_fill()

    # Window panes
    t.forward(25)
    t.left(90)
    t.forward(50)
    t.backward(25)
    t.left(90)
    t.forward(25)
    t.backward(50)


def draw_tree(x, y):
    """Draws a tree at the given (x, y) position."""

    t = turtle.Turtle()
    t.speed(10)
    t.penup()
    t.goto(x, y)
    t.pendown()

    # Trunk
    t.fillcolor("#8B4513")
    t.begin_fill()
    for _ in range(2):
        t.forward(40)
        t.left(90)
        t.forward(100)
        t.left(90)
    t.end_fill()

    # Leaves
    t.penup()
    t.goto(x - 60, y + 100)
    t.pendown()
    t.fillcolor("green")
    t.begin_fill()
    t.circle(80)
    t.end_fill()


def draw_sun(x, y):
    """Draws a sun at the given (x, y) position."""
    t = turtle.Turtle()
    t.speed(10)
    t.penup()
    t.goto(x, y)
    t.pendown()

    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(50)
    t.end_fill()


def main():
    """Runs the program and draws the full scene."""
    screen = draw_background()

    draw_house(-100, -100)
    draw_door(-25, -100)
    draw_window(-80, -30)
    draw_window(20, -30)
    draw_tree(200, -100)
    draw_sun(-250, 200)

    screen.exitonclick()  # keeps window open


main()
