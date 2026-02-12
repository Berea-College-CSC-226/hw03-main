######################################################################
# Author: A M Fahad
# Username: fahada
#
# Assignment: HW03
# Purpose: Draw a complex scene using functions and turtle graphics
#
# Google Doc Link: https://docs.google.com/document/d/1qUEvHRXhWzXMO05sNg7iUz_6izg6OduR6nlVHhSqtxI/edit?usp=sharing
######################################################################

import turtle


def setup_screen():
    """Set up the turtle screen and background."""
    screen = turtle.Screen()
    screen.setup(width=900, height=600)
    screen.bgcolor("#87CEEB")
    return screen


def setup_turtle():
    """Create and configure the turtle."""
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.pensize(2)
    return t


def draw_rectangle(t, width, height, color):
    """Draw a filled rectangle."""
    t.fillcolor(color)
    t.begin_fill()
    for i in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()


def draw_square(t, size, color):
    """Draw a filled square."""
    draw_rectangle(t, size, size, color)


def draw_triangle(t, size, color):
    """Draw a filled equilateral triangle."""
    t.fillcolor(color)
    t.begin_fill()
    for i in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()


def draw_house(t):
    """Draw a house with roof, windows, and door."""
    # House base
    t.penup()
    t.goto(-150, -100)
    t.setheading(0)
    t.pendown()
    draw_rectangle(t, 300, 200, "#F4A460")

    # Roof
    t.penup()
    t.goto(-150, 100)
    t.setheading(0)
    t.pendown()
    draw_triangle(t, 300, "#8B0000")

   # Door
    t.penup()
    t.goto(-25, -100)
    t.setheading(0)
    t.pendown()
    draw_rectangle(t, 50, 90, (0.4, 0.2, 0.1))

    # Windows
    for x in (-100, 60):
        t.penup()
        t.goto(x, 0)
        t.setheading(0)
        t.pendown()
        draw_square(t, 40, "#ADD8E6")


def draw_sun(t):
    """Draw a sun."""
    t.penup()
    t.goto(250, 180)
    t.pendown()
    t.fillcolor("#FFD700")
    t.begin_fill()
    t.circle(40)
    t.end_fill()


def draw_tree(t, x, y):
    """Draw a tree."""
    # Trunk
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    draw_rectangle(t, 30, 80, "#8B4513")

    # Leaves
    t.penup()
    t.goto(x - 35, y + 80)
    t.pendown()
    t.fillcolor("#228B22")
    t.begin_fill()
    t.circle(60)
    t.end_fill()


def draw_ground(t):
    """Draw the ground."""
    t.penup()
    t.goto(-450, -200)
    t.setheading(0)
    t.pendown()
    draw_rectangle(t, 900, 120, "#32CD32")

def draw_cloud(t):
    "Draw a cloud."
    start_x = -200
    y = 200
    for i in range(3):
        t.penup()
        t.goto(start_x - i*35,y)
        t.pendown()
        t.fillcolor("#FFFFFF")
        t.begin_fill()
        t.circle(40)
        t.end_fill()


def main():
    """Draw the background, the house, the sun, the island, and the trees"""
    wn = setup_screen()
    t = setup_turtle()

    # Scene
    draw_ground(t)
    draw_house(t)
    draw_sun(t)
    draw_cloud(t)
    draw_tree(t, -300, -100)
    draw_tree(t, 250, -100)

    wn.exitonclick()


main()
