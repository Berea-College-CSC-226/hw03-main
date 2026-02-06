"""
CSC 226 - Turtle Drawing Assignment
Name: John Lolonga
Username: YOUR_USERNAME_HERE
Google Doc Link: PASTE_YOUR_GOOGLE_DOC_URL_HERE

Description:
Draws a detailed house scene (house + roof + door + windows + chimney smoke + trees + clouds + sun + fence + text)
on a non-white background using Turtle graphics.
"""

import turtle
import random


def setup_screen(width=1000, height=700):
    """Create and return a Turtle screen with a non-white background color."""
    screen = turtle.Screen()
    screen.setup(width, height)
    screen.title("Turtle House Scene")

    # Non-white background (unnamed RGB color)
    screen.colormode(255)
    screen.bgcolor((25, 35, 60))  # deep night-blue
    return screen


def make_pen(speed=0):
    """Create and return a turtle pen configured for fast drawing."""
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(speed)  # 0 = fastest
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
    """Draw a house with roof, windows, door, chimney, and smoke."""
    # --- House base ---
    draw_filled_rect(
        pen,
        base_x, base_y,
        w=360, h=220,
        outline=(10, 10, 10),
        fill=(210, 170, 120)  # warm tan
    )

    # --- Roof ---
    draw_filled_triangle(
        pen,
        base_x - 20, base_y + 220,
        size=400,
        outline=(10, 10, 10),
        fill=(140, 60, 60)  # muted red
    )

    # --- Door ---
    draw_filled_rect(
        pen,
        base_x + 150, base_y,
        w=70, h=120,
        outline=(10, 10, 10),
        fill=(80, 55, 40)
    )
    # Doorknob
    draw_circle(pen, base_x + 205, base_y + 60, 6, outline=(10, 10, 10), fill=(220, 210, 120))

    # --- Windows (2) ---
    for wx in (base_x + 50, base_x + 240):
        draw_filled_rect(
            pen,
            wx, base_y + 95,
            w=70, h=60,
            outline=(10, 10, 10),
            fill=(180, 235, 255)  # light glass
        )
        # Window cross
        draw_line(pen, wx, base_y + 125, wx + 70, base_y + 125, color=(10, 10, 10), thickness=2)
        draw_line(pen, wx + 35, base_y + 95, wx + 35, base_y + 155, color=(10, 10, 10), thickness=2)

    # --- Chimney ---
    draw_filled_rect(
        pen,
        base_x + 265, base_y + 260,
        w=45, h=90,
        outline=(10, 10, 10),
        fill=(90, 90, 95)
    )

    # --- Smoke (little bubbles) ---
    smoke_centers = [(base_x + 295, base_y + 360), (base_x + 320, base_y + 395), (base_x + 300, base_y + 430)]
    for (sx, sy) in smoke_centers:
        draw_circle(pen, sx, sy, 18, outline=(220, 220, 220), fill=(220, 220, 220), thickness=1)


def draw_tree(pen, x, y, scale=1.0):
    """Draw a simple tree (trunk + leafy circles)."""
    trunk_w = 35 * scale
    trunk_h = 90 * scale

    # Trunk
    draw_filled_rect(
        pen,
        x, y,
        w=trunk_w, h=trunk_h,
        outline=(10, 10, 10),
        fill=(90, 60, 40)
    )

    # Leaves (circles) - uses an unnamed RGB color
    leaf_color = (40, 160, 90)  # not a named color, pure RGB
    centers = [
        (x + trunk_w / 2, y + trunk_h + 40 * scale),
        (x - 25 * scale, y + trunk_h + 20 * scale),
        (x + trunk_w + 25 * scale, y + trunk_h + 20 * scale),
        (x + trunk_w / 2, y + trunk_h + 10 * scale),
    ]
    for (cx, cy) in centers:
        draw_circle(pen, cx, cy, 40 * scale, outline=(10, 10, 10), fill=leaf_color, thickness=2)


def draw_cloud(pen, x, y, scale=1.0):
    """Draw a fluffy cloud made of overlapping circles."""
    cloud_fill = (230, 235, 245)
    cloud_outline = (230, 235, 245)
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
    draw_circle(pen, x, y, 35, outline=(255, 220, 120), fill=(255, 220, 120), thickness=2)

    # Rays
    for angle in range(0, 360, 30):
        pen.color((255, 220, 120))
        pen.pensize(3)
        pen.penup()
        pen.goto(x, y)
        pen.setheading(angle)
        pen.forward(45)
        pen.pendown()
        pen.forward(20)


def draw_ground(pen):
    """Draw the ground as a big rectangle strip."""
    draw_filled_rect(
        pen,
        -520, -350,
        w=1040, h=220,
        outline=(0, 0, 0),
        fill=(30, 120, 70),  # grass
        thickness=0
    )


def draw_fence(pen, y=-170):
    """Draw a simple fence in front of the house."""
    # Fence rail
    draw_filled_rect(pen, -500, y + 40, 1000, 12, outline=(0, 0, 0), fill=(220, 220, 210), thickness=1)

    # Posts
    x = -480
    while x <= 480:
        draw_filled_rect(pen, x, y, 20, 60, outline=(0, 0, 0), fill=(235, 235, 225), thickness=1)
        # Pointy top
        draw_filled_triangle(pen, x - 2, y + 60, 24, outline=(0, 0, 0), fill=(235, 235, 225), thickness=1)
        x += 55


def write_text(pen, x, y, message, size=18):
    """Write text on the screen."""
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color((240, 240, 240))
    pen.write(message, align="center", font=("Arial", size, "bold"))


def draw_stars(pen, count=60):
    """Draw tiny stars in the sky for extra detail."""
    pen.pensize(2)
    for _ in range(count):
        x = random.randint(-500, 500)
        y = random.randint(0, 330)
        pen.color((245, 245, 245))
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        pen.dot(random.randint(2, 4))


def main():
    """Main function: sets up screen and draws the full scene using helper functions."""
    setup_screen()
    pen = make_pen(speed=0)

    # --- Background details ---
    draw_ground(pen)
    draw_stars(pen, count=70)
    draw_sun(pen, x=-380, y=260)

    # --- Clouds ---
    draw_cloud(pen, -120, 240, scale=1.2)
    draw_cloud(pen, 180, 270, scale=0.9)
    draw_cloud(pen, 320, 220, scale=1.0)

    # --- Main object: House ---
    draw_house(pen, base_x=-180, base_y=-190)

    # --- Trees / scenery ---
    draw_tree(pen, x=-430, y=-210, scale=1.1)
    draw_tree(pen, x=260, y=-220, scale=0.95)

    # --- Fence in front ---
    draw_fence(pen, y=-260)

    # --- Text embellishment ---
    write_text(pen, 0, -330, "Home Sweet Home", size=22)

    turtle.done()


main()
setup_screen.exitonclick()