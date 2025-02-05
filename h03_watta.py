#################################################################################
# Author: Ahna Watt
# Username: watta
#
# Assignment: hw03
# Purpose: Make a house using the turtles, and make a tree in the background.
# Google Doc Link: https://docs.google.com/document/d/10mM268FLbMkQ00aMCzRf5z27e-7DZyTQ6ressDTDV5w/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle


def draw_house():
    """
    Draws a house with triangle roof, door, and window
    """
    t = turtle.Turtle()
    t.speed(3)

    #draws the square house
    for i in range(4):
        t.forward(100)
        t.left(90)

    #draws the roof
    t.goto(0,100)
    t.goto(50,150)
    t.goto(100,100)
    t.goto(0,100)

    #draws the door
    t.penup()
    t.goto(35,0)
    t.pendown()
    t.goto(35,50)
    t.goto(60,50)
    t.goto(60,0)

    #draw doorknob
    t.penup()
    t.goto(38,25)
    t.pendown()
    t.forward(3)
    t.penup()
    t.pendown()

    #draws tbe window
    t.penup()
    t.goto(10,60)
    t.pendown()
    for i in range(4):
        t.forward(20)
        t.right(90)

    t.hideturtle()


def draw_tree():
    """
    Draws the tree
    """
    t2 = turtle.Turtle()

    #draws the trunk of the tree
    t2.penup()
    t2.goto(150,0)
    t2.pendown()
    t2.color("brown")
    t2.begin_fill()
    for i in range(2):
        t2.forward(20)
        t2.left(90)
        t2.forward(60)
        t2.left(90)
    t2.end_fill()

    # draws some leaves
    t2.penup()
    t2.goto(160, 50)
    t2.pendown()
    t2.color("green")
    t2.begin_fill()
    t2.circle(40)
    t2.end_fill()
    t2.hideturtle()

def main():
    """
    Main function to draw the house and the tree
    """

    # Function calls to draw_house and draw_tree
    wn = turtle.Screen()
    wn.bgcolor("lightblue")
    draw_house()
    draw_tree()
    wn.exitonclick()

main()  # Starts the program!