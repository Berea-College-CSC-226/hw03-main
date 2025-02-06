#################################################################################
# Author: Kamau Clark
# Username: clarkk2
#
# Assignment: HW03 - Draw a House with cool scenery
# Purpose: Demonstrates drawing skills using Python's turtle module by creating a dynamic scene with a house and landscape.
# Google Doc Link: https://docs.google.com/document/d/1LZ3DV3lAJDGKOAQcKRvpJAOLilXaLWfjOhu-GKiDgs0/edit?usp=sharing
#################################################################################
# Acknowledgements:
# https://www.geeksforgeeks.org/print-a-spirograph-using-turtle-in-python/
# https://www.geeksforgeeks.org/python-turtle-pencolor-method/
# https://www.w3schools.com/python/module_random.asp
# https://docs.python.org/3/library/turtle.html
# https://www.geeksforgeeks.org/turtle-circle-method-in-python/
# https://cs111.wellesley.edu/labs/lab02/colors
# Based on initial template and discussions in class.
#################################################################################
import turtle
import random

def draw_square(t, size):
    """Draws a square of specified size using a specific turtle object."""
    for _ in range(4):
        t.forward(size)
        t.right(90)

def draw_triangle(t, size):
    """Draws an equilateral triangle of specified size using a specific turtle object."""
    for _ in range(3):
        t.forward(size)
        t.left(120)

def draw_rectangle(t, width, height):
    """Draws a rectangle with given width and height using a specific turtle object."""
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)

def draw_sky(t):
    """Fills the top canvas with sky blue to set the background using a specific turtle object."""
    t.penup()
    t.goto(-400, 300)
    t.pendown()
    t.fillcolor("skyblue")
    t.begin_fill()
    draw_rectangle(t, 800, 600)
    t.end_fill()

def draw_cloud(t, x, y):
    """Places a fluffy cloud at my specified coordinates using a specific turtle object."""
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
    """Draws a bright sun at the location using a specific turtle object."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(50)
    t.end_fill()

def draw_hill(t, x, y, size):
    """Creates a hill using a semicircle at the provided coordinates and size using this turtle object."""
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
    """Draws the base landscape with grass and hills using a specific turtle object."""
    t.penup()
    t.goto(-400, -200)
    t.pendown()
    t.fillcolor("green")
    t.begin_fill()
    draw_rectangle(t, 800, 200)
    t.end_fill()

    for pos in range(-300, 301, 100):
        draw_hill(t, pos, -200, random.choice([80, 100, 120, 150]))

def draw_house(t):
    """Draws the house, complete with roof, chimney, and windows, using the given turtle."""
    # Base of the house
    t.fillcolor("#FAEBD7")
    t.begin_fill()
    draw_square(t, 200)
    t.end_fill()

    # Roof
    t.fillcolor("#8B4513")
    t.begin_fill()
    t.setheading(90)
    t.forward(200)
    t.right(90)
    draw_triangle(t, 200)
    t.end_fill()

    # Chimney
    t.fillcolor("#A9A9A9")
    t.penup()
    t.goto(70, 70)
    t.pendown()
    t.begin_fill()
    draw_rectangle(t, 30, 70)
    t.end_fill()

    # Door
    t.penup()
    t.goto(-30, -200)
    t.setheading(90)
    t.pendown()
    t.fillcolor("#8B4513")
    t.begin_fill()
    draw_rectangle(t, 40, 60)  # Door
    t.end_fill()

    # Windows on either side of the door
    for x in [-80, 40]:
        t.penup()
        t.goto(x, -70)
        t.pendown()
        t.fillcolor("white")
        t.begin_fill()
        draw_square(t, 40)  # Windows
        t.end_fill()

    # Path
    t.penup()
    t.goto(30, -200)
    t.setheading(270)
    t.pendown()
    t.fillcolor("#A9A9A9")
    t.begin_fill()
    t.forward(200)
    t.right(90)
    t.forward(60)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(60)
    t.end_fill()

    # A simple tree
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
    """Sets up the scene and draws everything: the house, sun, clouds, and hills."""
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