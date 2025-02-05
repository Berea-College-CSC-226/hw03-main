# Author: Dumisani Chikomo
# Username: chikomod
# Google Doc link: https://docs.google.com/document/d/1AEgBFEs75gL-CptLqfFWgW7LBGcJHHfoziFUxTNb7G8/edit?usp=sharing
# Assignment: HW03: : Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: This program uses Python's Turtle library to draw a mobile phone with rounded edges, a screen, a home button,
# a speaker, and a charging battery icon.


import turtle


def setup_background(screen):
    """Sets up background using an RGB color."""
    screen.colormode(255)  # Enable RGB color mode
    screen.bgcolor((200, 220, 255))  # Light blue background


def draw_rectangle(x, y, width, height, color, t):
    """Draws a filled rectangle at (x, y) with given width, height, and color."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()

    for _ in range(2):
        t.forward(width)
        t.circle(10, 90)  # Rounded edges
        t.forward(height)
        t.circle(10, 90)

    t.end_fill()


def draw_circle(x, y, radius, color, t):
    """Draws a filled circle at (x, y) with given radius and color."""
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


def draw_battery_icon(t):
    """Draws a charging battery icon inside the phone screen."""
    # Battery frame
    draw_rectangle(-40, 50, 80, 40, (50, 50, 50), t)  # Dark gray frame

    # Battery charge level (green)
    draw_rectangle(-35, 55, 60, 30, (0, 255, 0), t)  # Green charge bar

    # Battery cap (small rectangle at the right end)
    draw_rectangle(42, 60, 10, 20, (50, 50, 50), t)  # Cap at the right end


def draw_mobile_phone(t):
    """Draws a mobile phone with a screen, button, speaker, and battery icon."""
    t.speed(3)

    # Draw phone body (RGB color)
    draw_rectangle(-100, -200, 200, 400, (20, 20, 20), t)  # Dark gray body

    # Draw screen (RGB color)
    draw_rectangle(-80, -160, 160, 320, (169, 169, 169), t)  # Light gray screen

    # Draw home button (RGB color)
    draw_circle(0, -180, 10, (250, 250, 250), t)  # Off-white

    # Draw top speaker (RGB color)
    draw_rectangle(-40, 170, 80, 10, (230, 230, 230), t)  # Light grayish white

    # Draw battery icon
    draw_battery_icon(t)

    t.hideturtle()


def main():
    """Main function to execute the drawing."""
    wn = turtle.Screen()
    setup_background(wn)  # Set a background

    t = turtle.Turtle()
    t.pensize(2)

    draw_mobile_phone(t)  # Draw mobile phone with battery icon

    wn.exitonclick()  # Closes window when clicked


if __name__ == "__main__":
    main()