#################################################################################
# Author: ARAYN SEHRAWAT
# Username: sehrawata
#
# Assignment: HW03
# Purpose: Continue practicing creating and using functions.
# Google Doc Link: https://docs.google.com/document/d/13lm9JXxWqP7ejt714ez6ZrrqFPwTSMihwu2emzKWuOc/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################


import turtle


def move_to(pen, x, y):
    pen.penup()
    pen.goto(x, y)
    pen.setheading(0)
    pen.pendown()


def draw_rectangle(pen, x, y, width, height, color):
    move_to(pen, x, y)
    pen.color(color)
    pen.begin_fill()

    for side in range(2):
        pen.forward(width)
        pen.left(90)
        pen.forward(height)
        pen.left(90)

    pen.end_fill()


def draw_circle(pen, x, y, radius, color):
    move_to(pen, x, y - radius)
    pen.color(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()


def draw_ground(pen):
    draw_rectangle(pen, -400, -300, 800, 180, "#345B40")
    draw_rectangle(pen, -30, -300, 60, 180, "#B8A58C")


def draw_chimney(pen):
    """to draw a brick chimney with three puffs of smoke."""
    draw_rectangle(pen, 65, 70, 35, 100, "#955B4B")

    # Smoke rises above the chimney.
    draw_circle(pen, 83, 192, 12, "#AAB4C2")
    draw_circle(pen, 96, 222, 17, "#AAB4C2")
    draw_circle(pen, 80, 258, 22, "#AAB4C2")


def draw_house(pen):

    # Main walls.
    draw_rectangle(pen, -140, -120, 280, 190, "#D9AB79")

    # Roof.
    move_to(pen, -165, 70)
    pen.color("#713F46")
    pen.begin_fill()
    pen.goto(0, 180)
    pen.goto(165, 70)
    pen.goto(-165, 70)
    pen.end_fill()


def draw_window(pen, x, y):
    draw_rectangle(pen, x, y, 60, 65, "#493E42")
    draw_rectangle(pen, x + 5, y + 5, 50, 55, "#FFD875")

    # Vertical and horizontal window crossbars.
    draw_rectangle(pen, x + 28, y + 5, 4, 55, "#493E42")
    draw_rectangle(pen, x + 5, y + 30, 50, 4, "#493E42")


def draw_door(pen):
    draw_rectangle(pen, -25, -120, 50, 95, "#61483E")
    draw_rectangle(pen, -17, -70, 34, 35, "#856250")
    draw_circle(pen, 13, -82, 3, "#FFD875")


def draw_tree(pen):
    draw_rectangle(pen, -285, -120, 25, 100, "#73513C")
    draw_circle(pen, -273, 25, 45, "#39684A")
    draw_circle(pen, -305, -5, 35, "#457D53")
    draw_circle(pen, -240, -5, 35, "#457D53")


def draw_flowers(pen):

    for x in [195, 240, 285]:
        draw_rectangle(pen, x - 2, -165, 4, 35, "#78A85B")

        # Four petals surround each flower's center.
        draw_circle(pen, x - 7, -130, 6, "#E89AB8")
        draw_circle(pen, x + 7, -130, 6, "#E89AB8")
        draw_circle(pen, x, -123, 6, "#E89AB8")
        draw_circle(pen, x, -137, 6, "#E89AB8")
        draw_circle(pen, x, -130, 4, "#FFD875")


def main():

    screen = turtle.Screen()
    screen.setup(800, 600)
    screen.title("A Quiet Night")
    screen.bgpic("nightsky.gif")

    pen = turtle.Turtle()
    pen.speed(0)
    pen.hideturtle()

    # Background scenery.
    draw_ground(pen)

    # House and its details.
    draw_chimney(pen)
    draw_house(pen)
    draw_window(pen, -110, -35)
    draw_window(pen, 50, -35)
    draw_door(pen)

    # Garden decorations.
    draw_tree(pen)
    draw_flowers(pen)

    screen.exitonclick()


main()