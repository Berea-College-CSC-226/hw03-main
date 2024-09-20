#################################################################################
# Author:Zak Shendera
# Username:Shenderaz
#
# Assignment:hw03
# Purpose: Draw a colorful house using functions
# Google Doc Link:https://docs.google.com/document/d/1daeBSg4mNVlEzkm8hCn4zdcdq5UD_bpJlcivOuc_3lM/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle

# Create screen and set background color
wn = turtle.Screen()
wn.bgcolor("yellow")

# Create turtle object
zak = turtle.Turtle()
zak.hideturtle()
zak.color("black")

def draw_window():
    """
    Drawing the window
    """
    zak.penup()
    zak.goto(20, -60)  # Position for the window
    zak.pendown()
    zak.begin_fill()
    for _ in range(4):  # Drawing a square window
        zak.forward(60)
        zak.left(90)
    zak.end_fill()

def draw_door():
    """
    Drawing the door
    """
    zak.penup()
    zak.goto(-80, -200)  # Position for the door
    zak.pendown()
    zak.begin_fill()
    for _ in range(2):  # Drawing a rectangle for the door
        zak.forward(100)  # Width of the door
        zak.left(90)
        zak.forward(201)  # Height of the door
        zak.left(90)
    zak.end_fill()

def draw_roof():
    """
    Drawing the roof
    """
    zak.penup()
    zak.goto(-250, 100)  # Position for the roof
    zak.pendown()
    zak.pensize(10)
    zak.begin_fill()
    zak.left(45)
    zak.forward(283)  # First side of the roof (triangle)
    zak.right(90)
    zak.forward(283)  # Second side of the roof (triangle)
    zak.right(135)
    zak.forward(400)  # Base of the roof
    zak.end_fill()

def main():
    """
    Drawing the house structure
    """
    zak.penup()
    zak.goto(-250, -200)  # Position for the base of the house
    zak.pendown()
    zak.pensize(10)
    for _ in range(2):  # Drawing a rectangle for the house base
        zak.forward(400)  # Width of the house
        zak.left(90)
        zak.forward(300)  # Height of the house
        zak.left(90)
    zak.pensize(7)

    # Call drawing functions
    draw_door()
    draw_window()
    draw_roof()

    # Close the window on click
    wn.exitonclick()

main()  # Start the program
