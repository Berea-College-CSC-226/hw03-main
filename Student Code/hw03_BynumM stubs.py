#################################################################################
# Author: Mekiyan Bynum
# Username: BynumM
#
# Assignment:CSC 226 –  Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Draws a cozy house scene using turtle graphics.
# Google Doc Link: https://docs.google.com/document/d/12D_upVFQFNvAMoilJQtLgh-uOQF5U_I57C58WWYqn4M/edit?tab=t.0
#
#################################################################################
# Acknowledgements: N/A
#
#
#################################################################################


import turtle

def square(t, size):
    """Draw a square."""
    for _ in range(4):
        t.forward(size)
        t.left(90)


def rectangle(t, width, height):
    """Draw a rectangle."""
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)


def move_to(t, x, y):
    """Lift pen and move turtle safely."""
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_sun(t):
    """Draw the sun."""
    move_to(t, -280, 200)
    t.color("yellow")
    t.begin_fill()
    t.circle(40)
    t.end_fill()


def draw_house_base(t):
    """Draw the main house body."""
    move_to(t, -100, -120)
    t.color(210, 180, 140)  # tan
    t.begin_fill()
    rectangle(t, 200, 150)
    t.end_fill()


def draw_roof(t):
    """Draw triangular roof."""
    move_to(t, -120, 30)
    t.color(150, 75, 0)

    t.begin_fill()
    t.goto(0, 150)
    t.goto(120, 30)
    t.goto(-120, 30)
    t.end_fill()


def draw_door(t):
    """Draw the house door."""
    move_to(t, -20, -120)
    t.color("saddlebrown")
    t.begin_fill()
    rectangle(t, 40, 80)
    t.end_fill()


def draw_window(t, x, y):
    """Draw one window with cross lines."""
    move_to(t, x, y)

    t.color("lightblue")
    t.begin_fill()
    square(t, 40)
    t.end_fill()

    # window cross
    move_to(t, x + 20, y)
    t.left(90)
    t.forward(40)
    t.backward(20)
    t.right(90)
    t.forward(20)
    t.backward(40)
    t.setheading(0)


def draw_tree(t, x, y):
    """Draw a tree using custom Xanadu color leaves."""
    xanadu= (115, 134, 120)  # unnamed RGB color requirement

    # trunk
    move_to(t, x, y)
    t.color(101, 67, 33)
    t.begin_fill()
    rectangle(t, 20, 60)
    t.end_fill()

    # leaves
    move_to(t, x + 10, y + 80)
    t.color(xanadu)
    t.begin_fill()
    t.circle(40)
    t.end_fill()


def draw_smoke(t):
    """Draw small smoke puffs from chimney for detail."""
    move_to(t, 50, 150)
    t.color("lightgray")

    for _ in range(3):
        t.begin_fill()
        t.circle(10)
        t.end_fill()
        t.penup()
        t.forward(15)
        t.left(20)
        t.pendown()


# =====================================================
# Main program
# =====================================================

def main():
    """Create screen and draw the full scene."""

    screen = turtle.Screen()
    screen.colormode(255)
    screen.bgcolor(180, 220, 255)  # sky blue



    t = turtle.Turtle()
    t.speed(0)
    t.width(2)

    # Draw objects
    draw_sun(t)
    draw_house_base(t)
    draw_roof(t)
    draw_door(t)

    draw_window(t, -70, -30)
    draw_window(t, 30, -30)

    draw_tree(t, 150, -120)
    draw_tree(t, -180, -120)

    draw_smoke(t)

    screen.exitonclick()



main()
