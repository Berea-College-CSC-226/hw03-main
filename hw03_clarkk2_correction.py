#################################################################################
# Author: Kamau Clark
# Username: clarkk2
#
# Assignment: HW03 - Draw a House with cool Scenery
# Purpose: Demonstrates drawing skills using Python's turtle module by creating a dynamic scene with a house and landscape.
# Google Doc Link: [Insert your Google Doc link here]
#################################################################################
# Acknowledgements:
# Based on initial template and discussions in class.
#################################################################################

import turtle
import random

def draw_square(t, size):
    """Draws a square using a turtle object."""
    for _ in range(4):
        t.forward(size)
        t.right(90)

def draw_triangle(t, size):
    """Draws an equilateral triangle using a turtle object."""
    for _ in range(3):
        t.forward(size)
        t.left(120)

def draw_rectangle(t, width, height):
    """Draws a rectangle using a turtle object."""
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)

def draw_sky(t):
    """Fills the top canvas with sky blue to set the background."""
    t.penup()
    t.goto(-400, 300)
    t.pendown()
    t.fillcolor("skyblue")
    t.begin_fill()
    draw_rectangle(t, 800, 600)
    t.end_fill()

def draw_cloud(t, x, y):
    """Places fluffy clouds at specified coordinates using a turtle object."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    for _ in range(6):
        t.circle(20)
        t.right(60)
    t.end_fill()

def draw_sun(t, x, y):
    """Draws a bright sun at the given location using a turtle object."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(50)
    t.end_fill()

def draw_hill(t, x, y, size):
    """Creates a hill using a semicircle at the provided coordinates and size."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("forestgreen")
    t.begin_fill()
    t.setheading(90)
    t.circle(size, 180)
    t.setheading(270)
    t.forward(size * 2)
    t.end_fill()

def draw_landscape(t):
    """Generates the base landscape with grass and hills using a turtle object."""
    t.penup()
    t.goto(-400, -200)
    t.pendown()
    t.fillcolor("green")
    t.begin_fill()
    draw_rectangle(t, 800, 200)
    t.end_fill()

    # Creating hills with varying positions and sizes
    for pos in range(-300, 301, 100):
        draw_hill(t, pos, -200, random.choice([80, 100, 120, 150]))

def draw_house(t):
    """Constructs a detailed house with multiple features using a turtle object."""
    # Base of the house
    t.fillcolor("#FAEBD7")
    t.begin_fill()
    draw_square(t, 200)
    t.end_fill()

    # Roof of the house
    t.fillcolor("#8B4513")
    t.begin_fill()
    t.setheading(90)
    t.forward(200)
    t.right(90)
    draw_triangle(t, 200)
    t.end_fill()

    # Chimney on top of the house
    t.fillcolor("#A9A9A9")
    t.penup()
    t.goto(70, 70)
    t.pendown()
    t.begin_fill()
    draw_rectangle(t, 30, 70)
    t.end_fill()

    # Door and windows
    t.penup()
    t.goto(-30, -200)
    t.setheading(90)
    t.pendown()
    t.fillcolor("#8B4513")
    t.begin_fill()
    draw_rectangle(t, 40, 60)
    t.end_fill()

    for x in [-80, 40]:
        t.penup()
        t.goto(x, -70)
        t.pendown()
        t.fillcolor("white")
        t.begin_fill()
        draw_square(t, 40)
        t.end_fill()

    # Path leading to the house
    t.penup()
    t.goto(30, -200)
    t.setheading(270)
    t.pendown()
    t.fillcolor("#A9A9A9")
    t.begin_fill()
    t.forward(100)
    t.right(90)
    t.forward(60)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(60)
    t.end_fill()

    # A simple tree next to the house
    t.penup()
    t.goto(-230, -110)
    t.pendown()
    t.color("saddlebrown")
    t.begin_fill()
    draw_rectangle(t, 30, 130)
    t.end_fill()
    t.penup()
    t.goto(-215, -110)
    t.pendown()
    t.color("green")
    t.begin_fill()
    t.circle(50)
    t.end_fill()

def main():
    """Main function orchestrates the drawing operations."""
    wn = turtle.Screen()
    t = turtle.Turtle()
    wn.title("KamKam House")
    t.speed(0)

    draw_sky(t)
    draw_cloud(t, -300, 200)
    draw_cloud(t, -100, 250)
    draw_cloud(t, 200, 220)
    draw_sun(t, 300, 250)
    draw_landscape(t)

    t.penup()
    t.goto(-100, -200)
    t.setheading(90)
    t.pendown()

    draw_house(t)

    t.hideturtle()
    wn.exitonclick()

main()
