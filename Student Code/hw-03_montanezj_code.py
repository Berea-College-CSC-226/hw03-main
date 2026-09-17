#################################################################################
# Author: Joey Montanez
# Username: montanezj
#
# Assignment: HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Create a House using the turtle library.
# Google Doc Link: https://docs.google.com/document/d/1ckaoLI5r4mMMfiLZjUKxUG7hHJQu1HLTDqvGKFMMaO0/edit?tab=t.0
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################
import turtle


def draw_rectangle(t, width, height, color):
    """Draws a filled rectangle with the given dimensions and color."""
    t.fillcolor(color)
    t.begin_fill()

    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

    t.end_fill()


def draw_circle(t, radius, color):
    """Draws a filled circle with the specified radius and color."""
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


def draw_house(t):
    """Draws the main house, including the walls and roof."""

    # House walls
    t.penup()
    t.goto(-220, -150)
    t.setheading(0)
    t.pendown()
    draw_rectangle(t, 440, 250, "#D98C5F")

    # Roof
    t.penup()
    t.goto(-250, 100)
    t.setheading(0)
    t.pendown()

    t.fillcolor("#4B2E2E")
    t.begin_fill()
    t.goto(0, 270)
    t.goto(250, 100)
    t.goto(-250, 100)
    t.end_fill()


def draw_door(t):
    """Draws the front door and its doorknob."""

    # Door
    t.penup()
    t.goto(-45, -150)
    t.setheading(0)
    t.pendown()
    draw_rectangle(t, 90, 160, "#5C4033")

    # Door knob
    t.penup()
    t.goto(25, -70)
    t.setheading(0)
    t.pendown()
    draw_circle(t, 7, "#FFD700")


def draw_window(t, x, y):
    """Draws one detailed window with four panes."""

    # Window frame
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    draw_rectangle(t, 80, 80, "#E8F1F2")

    # Vertical divider
    t.penup()
    t.goto(x + 40, y)
    t.setheading(90)
    t.pendown()
    t.pencolor("#5C4033")
    t.pensize(5)
    t.forward(80)

    # Horizontal divider
    t.penup()
    t.goto(x, y + 40)
    t.setheading(0)
    t.pendown()
    t.forward(80)

    t.pensize(1)


def draw_chimney(t):
    """Draws the chimney and smoke coming from the roof."""

    # Chimney
    t.penup()
    t.goto(120, 170)
    t.setheading(0)
    t.pendown()
    draw_rectangle(t, 55, 120, "#7A4E3A")

    # Smoke
    t.penup()
    t.goto(145, 290)
    t.setheading(0)
    t.pendown()
    draw_circle(t, 20, "#B8B8B8")

    t.penup()
    t.goto(165, 325)
    t.pendown()
    draw_circle(t, 25, "#A8A8A8")

    t.penup()
    t.goto(145, 365)
    t.pendown()
    draw_circle(t, 30, "#989898")


def draw_tree(t, x, y):
    """Draws a tree with a trunk and a leafy green canopy."""

    # Tree trunk
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    draw_rectangle(t, 45, 130, "#6B4226")

    # Leaves
    t.penup()
    t.goto(x - 45, y + 100)
    t.pendown()
    draw_circle(t, 55, "#2E7D32")

    t.penup()
    t.goto(x + 5, y + 125)
    t.pendown()
    draw_circle(t, 60, "#388E3C")

    t.penup()
    t.goto(x + 45, y + 100)
    t.pendown()
    draw_circle(t, 50, "#43A047")


def draw_flower(t, x, y, petal_color):
    """Draws a small flower with petals, a center, and a stem."""

    # Stem
    t.penup()
    t.goto(x, y)
    t.setheading(90)
    t.pendown()
    t.pencolor("#2E7D32")
    t.pensize(3)
    t.forward(35)

    # Petals
    t.pensize(1)
    t.penup()
    t.goto(x, y + 35)
    t.pendown()

    for _ in range(6):
        draw_circle(t, 7, petal_color)
        t.right(60)

    # Center
    draw_circle(t, 5, "#FFD700")


def draw_sun(t):
    """Draws a bright sun in the upper corner of the sky."""

    t.penup()
    t.goto(250, 210)
    t.pendown()
    draw_circle(t, 45, "#FFD54F")


def draw_path(t):
    """Draws the walkway leading from the house to the bottom of the scene."""

    t.penup()
    t.goto(-35, -150)
    t.setheading(-70)
    t.pendown()

    t.fillcolor("#C2A477")
    t.begin_fill()
    t.goto(-140, -300)
    t.goto(140, -300)
    t.goto(35, -150)
    t.goto(-35, -150)
    t.end_fill()


def main():
    """Creates the drawing window and draws the complete scene."""

    screen = turtle.Screen()
    screen.setup(800, 600)

    # Non-white background using an unnamed hexadecimal color
    screen.bgcolor("#6A5ACD")

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    # Draw the sunset sky
    draw_sun(t)

    # Draw the path behind the house
    draw_path(t)

    # Draw the house
    draw_house(t)

    # Draw windows
    draw_window(t, -180, -20)
    draw_window(t, 100, -20)

    # Draw the front door
    draw_door(t)

    # Draw chimney and smoke
    draw_chimney(t)

    # Draw trees
    draw_tree(t, -330, -150)
    draw_tree(t, 285, -150)

    # Draw flowers in front of the house
    draw_flower(t, -170, -230, "#FF69B4")
    draw_flower(t, -120, -245, "#FF6347")
    draw_flower(t, 130, -235, "#FF69B4")
    draw_flower(t, 180, -245, "#FFFF00")

    turtle.done()


main()