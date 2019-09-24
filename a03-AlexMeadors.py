# Assignment: A03:  A Pair of Fully Functional Gitty Psychedelic  Robotic Turtles
# Purpose: Draws a Tree
######################################################################
# Acknowledgements:

# Original code by: Alex Meadors
######################################################################

import turtle


def setup(turt,scr):
    """
    Gets the Screen and Turtle ready for use

    :param turt:
    The turtle used

    :param scr:
    The screen used

    :return:
    None
    """
    scr.colormode(255)
    scr.bgcolor(75, 191, 172)
    turt.shape("turtle")
    turt.penup()
    turt.speed(0)


def draw_leaves(turt,radius,x,y):
    """
    Draws a green circle at the location given of a given size.

    :param turt:
    Turtle used

    :param radius:
    Size of leaves

    :param x:
    X Location of center

    :param y:
    Y location of center

    :return:
    None

    """
    turt.penup()
    turt.goto(x, y)
    turt.pendown()
    turt.color(48, 161, 31)
    turt.begin_fill()
    turt.circle(radius)
    turt.end_fill()
    turt.penup()


def draw_wood(turt, x1, y1, x2, y2):
    """
    Draws a brown rectangle with corners at the given coordinates.
    :param turt:
    Turtle used.
    :param x1:
    One corner x coord
    :param y1:
    One corner y coord
    :param x2:
    Other corner x coord
    :param y2:
    Other corner y coord
    :return:
    None
    """
    turt.color(107, 80, 36)
    turt.goto(x1, y1)
    turt.pendown()
    turt.begin_fill()
    turt.goto(x2, y1)
    turt.goto(x2,y2)
    turt.goto(x1,y2)
    turt.goto(x1,y1)
    turt.end_fill()
    turt.penup()


def draw_hole(turt, radius, x, y):
    """
    Makes a black circle of a given size at a given location
    :param turt:
    Turtle used
    :param radius:
    Size of circle
    :param x:
    X coord of center
    :param y:
    Y coord of center
    :return:
    None
    """
    turt.penup()
    turt.goto(x, y)
    turt.color(0, 0, 0)
    turt.pendown()
    turt.begin_fill()
    turt.circle(radius)
    turt.end_fill()
    turt.penup()


def main():
    minion = turtle.Turtle()
    win = turtle.Screen()
    setup(minion, win)
    draw_wood(minion, -50, -250, 50, 0)
    draw_wood(minion, 25, 0, 75, 50)
    draw_wood(minion, -25, 0, -75, 50)
    #Branch far left location for the loop
    branch_loc = -100
    #Leaf locations for the loops in a second
    leafx = -100
    leafy = 0
    for limb in range(3):
        draw_wood(minion, branch_loc , 50, (branch_loc + 50 ), 100)
        branch_loc += 75
    for leafcol in range(5):
        for leafrow in range(3):
            draw_leaves(minion,50, leafx, leafy)
            leafy += 50
        leafx += 50
        leafy = 0
    draw_hole(minion, 20, 0, -50)
    minion.goto(200,200)
    win.exitonclick()

main()