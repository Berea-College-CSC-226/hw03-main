import turtle


def draw_rectangle(x, y, width, height, color):
    """Draws a filled rectangle at (x, y) with given width, height, and color."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()

    for _ in range(2):
        turtle.forward(width)
        turtle.circle(20, 90)  # Rounded edges
        turtle.forward(height)
        turtle.circle(20, 90)

    turtle.end_fill()


def draw_circle(x, y, radius, color):
    """Draws a filled circle at (x, y) with given radius and color."""
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


def draw_mobile_phone():
    """Draws a mobile phone with a screen, button, and speaker."""
    turtle.speed(3)
    turtle.bgcolor("white")

    # Draw phone body
    draw_rectangle(-100, -200, 200, 400, "black")

    # Draw screen
    draw_rectangle(-80, -160, 160, 320, "gray")

    # Draw home button
    draw_circle(0, -180, 10, "white")

    # Draw top speaker
    draw_rectangle(-40, 170, 80, 10, "white")

    turtle.hideturtle()
    turtle.done()


# Call function to draw the mobile phone
draw_mobile_phone()
