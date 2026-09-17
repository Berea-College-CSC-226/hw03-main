# ================================================================================================================
# Program: HW03_Victor.py
# Author: Emmanuel Victor Mucyo
# Username: victor
# Date: 9/16/2026
# Course: cc26
# Description: Complex Drawing
# Google Doc: [link here]
# =======================================================================================================

# CSC 226 - Homework: Complex Drawing
# Name: [Your Name]
# Username: [Your Berea Username]
# Google Doc: [link here]

import turtle


def setup_screen():
    """Create and configure the drawing window with a non-white background."""
    turtle.colormode(255)
    wn = turtle.Screen()
    wn.bgcolor("#87CEEB")  # unnamed color via hexadecimal (sky blue)
    return wn


def draw_house(t):
    """Draw a simple house: a square base and a triangular roof."""
    t.penup()
    t.goto(-100, -50)
    t.pendown()
    t.color("saddlebrown")
    t.begin_fill()
    for i in range(4):
        t.forward(100)
        t.left(90)
    t.end_fill()

    # Roof (equilateral triangle, all sides equal length)
    t.penup()
    t.goto(-100, 50)
    t.pendown()
    t.color((150, 30, 30))  # unnamed color via RGB tuple
    t.begin_fill()
    t.setheading(0)
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.end_fill()


def draw_window(t, x, y):
    """Draw a single square window at the given coordinates."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("lightyellow")
    t.begin_fill()
    for i in range(4):
        t.forward(20)
        t.left(90)
    t.end_fill()


def draw_chimney(t, x, y):
    """Draw a small rectangular chimney sticking out of the roof."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("dimgray")
    t.setheading(90)
    t.begin_fill()
    for i in range(2):
        t.forward(30)
        t.right(90)
        t.forward(10)
        t.right(90)
    t.end_fill()


def draw_chimney_smoke(t, x, y):
    """Draw a few small circles rising from the chimney to look like smoke."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("gray")
    for i in range(3):
        t.circle(8)
        t.penup()
        t.goto(x + i * 5, y + 20 * (i + 1))
        t.pendown()


def draw_tree(t, x, y):
    """Draw a simple tree: a brown trunk and a green circular top."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("brown")
    t.begin_fill()
    for i in range(4):
        t.forward(15)
        t.left(90)
    t.end_fill()

    t.penup()
    t.goto(x - 15, y + 15)
    t.pendown()
    t.color("darkgreen")
    t.begin_fill()
    t.circle(30)
    t.end_fill()


def draw_sun(t, x, y):
    """Draw a simple sun using an unnamed color (RGB)."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color((255, 215, 0))  # unnamed RGB color (gold)
    t.begin_fill()
    t.circle(30)
    t.end_fill()


def main():
    wn = setup_screen()
    my_house = turtle.Turtle()
    my_house.speed(5)

    # Draw the house body and roof
    draw_house(my_house)

    # Draw windows on the house
    draw_window(my_house, -80, -20)
    draw_window(my_house, -30, -20)

    # Draw the chimney on the roof
    draw_chimney(my_house, -30, 80)

    # Draw smoke rising from the chimney
    draw_chimney_smoke(my_house, -25, 115)

    # Draw a tree beside the house
    draw_tree(my_house, 120, -50)

    # Draw the sun in the sky
    draw_sun(my_house, -150, 120)

    wn.exitonclick()


main()