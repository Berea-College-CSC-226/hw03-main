#################################################################################
# Author: Eber Seco Lima
# Username: secolimae
#
# Assignment: HW03
# Purpose: draw something complex, like a house, animal, or person
# Google Doc Link: https://docs.google.com/document/d/1Yly3A38OkWE3aWIDQkU3zJiA4JyoJ8n5bg0Jnhc5tZ4/edit?usp=sharing
#
#################################################################################
# Acknowledgements: Firstly I defined the turtle in the global scope and I forgot how to define it within each scope of each function.
# So I asked ChatGPT "how I can define the turtle within each function?" and it showed me to treat turtle as a parameter for each function. That worked well!
# I also asked ChatGPT how to set the RBG color mode by saying "how I can use the RGB code style in the colors?"
# I wasn't sure about the signal for docstrings so I searched it in this website: https://peps.python.org/pep-0257/
#################################################################################

import turtle

def create_grass(t):
    """This functions creates the grass and adds it to t"""
    t.penup()
    t.color((0, 128, 0)) # RGB color mode for green
    t.speed("fastest")
    t.goto(-300, 0)
    t.pendown()
    t.begin_fill()
    t.forward(600)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(600)
    t.right(90)
    t.end_fill()
    t.penup()


def create_trunk(t):
    """This functions creates a trunk and adds it to t"""
    t.goto(-280, 0)
    t.pendown()
    t.color((139, 69, 19)) # RGB color mode for Brown
    t.speed("fastest")
    t.begin_fill()
    t.forward(100)
    t.right(90)
    t.forward(35)
    t.right(90)
    t.forward(100)
    t.end_fill()
    t.penup()


def create_leaves(t):
    """This functions creates leaves and adds it to t"""
    t.color((34, 139, 34)) # RGB color mode for green
    t.speed("fastest")
    t.left(180)
    t.forward(100)
    t.right(110)
    t.pendown()
    t.begin_fill()
    for i in range(7):
        t.circle(20, 130)
        t.right(90)
    t.circle(20, 150)
    t.end_fill()
    t.penup()


def create_walls(t):
    """This functions creates walls and adds it to t"""
    t.color((245, 245, 220)) # RGB color mode for beige
    t.speed("fastest")
    t.goto(-175, 0)
    t.left(40)
    t.pendown()
    t.begin_fill()
    t.forward(100)
    t.right(90)
    t.forward(175)
    t.right(90)
    t.forward(100)
    t.end_fill()
    t.penup()


def create_roof(t):
    """This functions creates a roof and adds it to t"""
    t.color((255, 0, 0)) # RGB color mode for red
    t.speed("fastest")
    t.goto(0, 100)
    t.right(180)
    t.pendown()
    t.begin_fill()
    t.left(45)
    t.forward(123)
    t.left(90)
    t.forward(121)
    t.end_fill()
    t.penup()


def create_door(t):
    """This functions creates a door and adds it to t"""
    t.color((255, 255, 0)) # RGB color mode for yellow
    t.speed("fastest")
    t.goto(-155, 0)
    t.right(135)
    t.pendown()
    t.begin_fill()
    t.forward(60)
    t.right(90)
    t.forward(35)
    t.right(90)
    t.forward(60)
    t.end_fill()
    t.penup()
    t.pencolor((0, 0, 0)) # RGB color mode for black
    t.goto(-125, 30)
    t.pendown()
    t.left(90)
    t.stamp() # Door handle
    t.penup()
    t.goto(100, 30)


def create_window(t):
    """This functions creates a window and adds it to t"""
    t.color((0, 0, 255)) # RGB color mode for blue
    t.speed("fastest")
    t.goto(-75, 50)
    t.pendown()
    t.begin_fill()
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(60)
    t.right(90)
    t.forward(20)
    t.penup()
    t.end_fill()
    t.goto(100, 100) # Put the turtle somewhere else


def main():
    """This function sets the turtle and create objects such as grass, trunk, leaves, walls, roofs, door, and window."""
    wn = turtle.Screen()  # Set the screen
    wn.screensize(600, 600)
    wn.colormode(255)  # Define color mode to RGB
    wn.bgcolor((135, 206, 235))  # RGB color mode for blue

    t = turtle.Turtle()
    create_grass(t)
    create_trunk(t)
    create_leaves(t)
    create_walls(t)
    create_roof(t)
    create_door(t)
    create_window(t)

    wn.exitonclick()
main()


