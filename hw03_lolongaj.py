
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
#
#################################################################################


import turtle

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
    """Create and return a turtle pen for fast drawing."""
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


def draw_filled_rect(pen, x, y, w, h, outline, fill, thickness=2):
    """Draw a filled rectangle starting at bottom-left (x, y)."""
    pen.pensize(thickness)
    pen.color(outline, fill)
    go_to(pen, x, y)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(w)
        pen.left(90)
        pen.forward(h)
        pen.left(90)
    pen.end_fill()


def draw_filled_triangle(pen, x, y, size, outline, fill, thickness=2):
    """Draw an equilateral triangle with its left corner at (x, y)."""
    pen.pensize(thickness)
    pen.color(outline, fill)
    go_to(pen, x, y)
    pen.begin_fill()
    for _ in range(3):
        pen.forward(size)
        pen.left(120)
    pen.end_fill()


def draw_circle(pen, x, y, radius, outline, fill=None, thickness=2):
    """Draw a circle centered at (x, y). If fill is None, draws outline only."""
    pen.pensize(thickness)
    if fill is None:
        pen.color(outline)
    else:
        pen.color(outline, fill)

    pen.penup()
    pen.goto(x, y - radius)
    pen.setheading(0)
    pen.pendown()

    if fill is not None:
        pen.begin_fill()
    pen.circle(radius)
    if fill is not None:
        pen.end_fill()


def draw_line(pen, x1, y1, x2, y2, color, thickness=2):
    """Draw a straight line from (x1, y1) to (x2, y2)."""
    pen.pensize(thickness)
    pen.color(color)
    pen.penup()
    pen.goto(x1, y1)
    pen.pendown()
    pen.goto(x2, y2)


def draw_house(pen, base_x, base_y):
    """Draw a house with roof, windows, door."""
    #  House base
    draw_filled_rect(
        pen,
        base_x, base_y,
        w=360, h=220,
        outline="black",
        fill=(210, 170, 120)  # warm tan
    )

    #  Roof
    draw_filled_triangle(
        pen,
        base_x - 20, base_y + 220,
        size=400,
        outline="black",
        fill=(140, 60, 60)  # RGB Color Wheel tool
    )

    # Door
    draw_filled_rect(
        pen,
        base_x + 150, base_y,
        w=70, h=120,
        outline="black",
        fill=(80, 55, 40)
    )

    #  Windows (2)
    for wx in (base_x + 50, base_x + 240):
        draw_filled_rect(
            pen,
            wx, base_y + 95,
            w=70, h=60,
            outline="black",
            fill=(180, 235, 255)  # used RGB Color Wheel tool
        )
        # Window cross
        draw_line(pen, wx, base_y + 125, wx + 70, base_y + 125, color="black", thickness=2)
        draw_line(pen, wx + 35, base_y + 95, wx + 35, base_y + 155, color="black", thickness=2)


def draw_tree(pen, x, y, scale=1.0):
    """Draw a simple tree (trunk + leafy circles)."""
    trunk_w = 35 * scale
    trunk_h = 90 * scale

    # Trunk
    draw_filled_rect(
        pen,
        x, y,
        w=trunk_w, h=trunk_h,
        outline="black",
        fill=(80, 55, 40)
    )

    # Leaves in overlapping circles
    leaf_color = "green"
    centers = [
        (x + trunk_w / 2, y + trunk_h + 40 * scale),
        (x - 25 * scale, y + trunk_h + 20 * scale),
        (x + trunk_w + 25 * scale, y + trunk_h + 20 * scale),
        (x + trunk_w / 2, y + trunk_h + 10 * scale),
    ]
    for (cx, cy) in centers:
        draw_circle(pen, cx, cy, 40 * scale, outline="black", fill=leaf_color, thickness=2)


def draw_cloud(pen, x, y, scale=1.0):
    """Draw a fluffy cloud made of overlapping circles."""
    cloud_fill = "white"
    cloud_outline = "white"
    parts = [
        (x, y, 25 * scale),
        (x + 30 * scale, y + 10 * scale, 30 * scale),
        (x + 60 * scale, y, 25 * scale),
        (x + 30 * scale, y - 10 * scale, 28 * scale),
    ]
    for cx, cy, r in parts:
        draw_circle(pen, cx, cy, r, outline=cloud_outline, fill=cloud_fill, thickness=1)


def draw_sun(pen, x, y):
    """Draw a sun with rays."""
    draw_circle(pen, x, y, 35, outline="yellow", fill="yellow", thickness=2)

    # Rays
    for i in range(0, 360, 30):
        pen.color("yellow")
        pen.pensize(3)
        pen.penup()
        pen.goto(x, y)
        pen.setheading(i)
        pen.forward(45)
        pen.pendown()
        pen.forward(20)


def draw_ground(pen):
    """Draw the ground as a rectangle."""
    draw_filled_rect(
        pen,
        -520, -350,
        w=1040, h=220,
        outline=(0, 0, 0),
        fill="green",
        thickness=0
    )


def main():
    """Main function: sets up screen and draws the full scene using above functions."""
    screen = setup_screen()
    pen = make_pen(speed=0)

    draw_ground(pen)
    draw_sun(pen, x=-380, y=260)

    draw_cloud(pen, -120, 240, scale=1.2)
    draw_cloud(pen, 180, 270, scale=0.9)
    draw_cloud(pen, 320, 220, scale=1.0)

    draw_house(pen, base_x=-180, base_y=-190)

    draw_tree(pen, x=-430, y=-210, scale=1.1)
    draw_tree(pen, x=260, y=-220, scale=0.95)

    screen.exitonclick()


main()