"""
Author: Karina Ismailova
Username: ismailovak
Google Doc Link: https://docs.google.com/document/d/1BO5SaybMPpMOE6mnmhUppz9oMr0X19wmRQ2bosPUnZc/edit?usp=sharing

This program uses the turtle module to draw a house with a tree, a sun, and grass on a colored background.
"""

import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("#87CEEB")  # Light blue sky


def draw_square(x, y, size, color):
    """
    Draws a filled square.
    :param x: x-coordinate
    :param y: y-coordinate
    :param size: length of a side
    :param color: fill color
    """
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()


def draw_triangle(x, y, size, color):
    """
    Draws a filled triangle (for the roof).
    """
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(size)
        turtle.left(120)
    turtle.end_fill()


def draw_rectangle(x, y, width, height, color):
    """
    Draws a filled rectangle.
    """
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()


def draw_circle(x, y, radius, color):
    """
    Draws a filled circle.
    """
    turtle.penup()
    turtle.goto(x, y - radius)  # Adjust for turtle’s circle drawing
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


def draw_house():
    """
    Draws a house with a door, windows, and a chimney.
    """
    draw_square(-100, 100, 200, "#8B4513")  # House base (brown)
    draw_triangle(-120, 100, 240, "#A52A2A")  # Roof (red)
    draw_rectangle(-30, 5, 60, 90, "#654321")  # Door (dark brown)
    draw_square(-80, 10, 40, "white")  # Left window
    draw_square(40, 10, 40, "white")  # Right window
    draw_rectangle(50, 130, 20, 40, "gray")  # Chimney
    draw_circle(55, 170, 10, "lightgray")  # Smoke


def draw_tree():
    """
    Draws a tree with a trunk and leaves.
    """
    draw_rectangle(150, -100, 20, 50, "#8B4513")  # Trunk
    draw_circle(160, -50, 40, "green")  # Leaves


def draw_sun():
    """
    Draws a sun in the sky.
    """
    draw_circle(-200, 150, 40, "yellow")  # Sun


def draw_grass():
    """
    Draws a grassy ground at the bottom of the screen.
    """
    draw_rectangle(-300, -150, 600, 50, "#228B22")  # Green grass


def main():
    """
    Main function that calls all drawing functions.
    """
    draw_grass()
    draw_house()
    draw_tree()
    draw_sun()
    turtle.hideturtle()
    turtle.done()


main()
