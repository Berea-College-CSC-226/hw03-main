
#################################################################################
# Author: John Lolonga
# Username: lolongaj
#
# Assignment: HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose:
# Google Doc Link: https://docs.google.com/document/d/1x_WexBtZg-YCuaQghw5p5tWwszkFBhvNL_ejZXBIquE/edit?tab=t.0#heading=h.j4414z2ufr72
#
#################################################################################
# Acknowledgements:
#
# https://www.youtube.com/watch?v=WEUloPdIfRk
# chatgpt.com (Used to correct my coordinates positions to come up with correct shape and to draw overlapping circles)
# RGB Color Wheel tool
#################################################################################

import turtle

def setup_screen(width=1000, height=700):
    """Create and return a Turtle screen """
    screen = turtle.Screen()
    screen.setup(width, height)
    screen.title("Turtle House Scene")

    # Sky blue background
    screen.colormode(255)
    screen.bgcolor("light blue")
    return screen

def make_pen(speed=0):
    """Create and return a turtle pen for fast drawing and hiding it form the screen."""
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(speed)
    pen.penup()
    return pen

def go_to(pen, x, y):
    """Move pen to (x, y) without drawing."""
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

def draw_filled_rect(pen, x, y, w, h, fill):
    """Draw a filled rectangle starting at bottom-left using the coordinates (x, y)."""
    pen.color(fill)
    go_to(pen, x, y)
    pen.begin_fill()
    for i in range(2):
        pen.forward(w)
        pen.left(90)
        pen.forward(h)
        pen.left(90)
    pen.end_fill()


def draw_filled_triangle(pen, x, y, size,fill):
    """Draw an equilateral triangle with its left corner at (x, y)."""
    pen.color(fill)
    go_to(pen, x, y)
    pen.begin_fill()
    for i in range(3):
        pen.forward(size)
        pen.left(120)
    pen.end_fill()

def draw_circle(pen, x, y, radius, color):
    pen.color(color)
    pen.penup()
    pen.goto(x, y - radius)
    pen.setheading(0)
    pen.pendown()

    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

def draw_line(pen, x1, y1, x2, y2, color):
    """Draw a straight line from (x1, y1) to (x2, y2)."""
    pen.color(color)
    pen.penup()
    pen.goto(x1, y1)
    pen.pendown()
    pen.goto(x2, y2)


def draw_house(pen, base_x, base_y):
    """Draw a house with roof, windows, door."""
    #  House base
    draw_filled_rect(pen,base_x, base_y,w=360, h=220,
        fill=(210, 170, 120))

    #  Roof
    draw_filled_triangle(pen,base_x - 20, base_y + 220,size=400, fill=(140, 60, 60))

    # Door
    draw_filled_rect(pen,base_x + 150, base_y, w=70, h=120, fill=(80, 55, 40))

    #  Windows (2 of them)
    for wx in (base_x + 50, base_x + 240):
        draw_filled_rect(pen,wx, base_y + 95,w=70, h=60,fill=(180, 235, 255))
        # Window cross
        draw_line(pen, wx, base_y + 125, wx + 70, base_y + 125, color="black")
        draw_line(pen, wx + 35, base_y + 95, wx + 35, base_y + 155, color="black")

def draw_ground(pen):
    """Draw the ground as a rectangle."""
    draw_filled_rect(pen, -520, -350, w=1040, h=220,fill="green")


def main():
    """Main function: sets up screen and draws the full scene using above functions."""
    screen = setup_screen()
    pen = make_pen(speed=0)

    draw_ground(pen)
    draw_circle(pen, 100, 150, 30, "white")
    draw_circle(pen, 130, 160, 35, "white")
    draw_circle(pen, 160, 150, 30, "white")
    draw_circle(pen, -380, 260, 35, "yellow")
    draw_house(pen, base_x=-180, base_y=-190)

    screen.exitonclick()

main()