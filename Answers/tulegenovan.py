"""
CSC 226
Name: Naz Tulegenova
Google Doc Link: https://docs.google.com/document/d/1b-g8DrpL_k0uf6yBpqkftCK4IqIwC72G-Nw-RtOOWH0/edit?tab=t.0

This program uses the turtle library to draw a house and a blue sky background.
"""

import turtle

# Function to set up the background
def setup_background():
    turtle.bgcolor("skyblue")  # Sets the background color

# Function to draw a rectangle
def draw_rectangle(x, y, width, height, color):
    """Draws a filled rectangle at (x, y) with given width, height, and color."""
    turtle.penup()
    turtle.goto(x - width // 2, y - height // 2)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

# Function to draw the house
def draw_house():
    draw_rectangle(0, -50, 200, 150, (150, 75, 0))  # House body (brown)

# Function to draw the roof
def draw_roof():
    """Draws a triangular roof closer to the house."""
    turtle.penup()
    turtle.goto(-100, 25)
    turtle.pendown()
    turtle.color("darkred")
    turtle.begin_fill()
    turtle.goto(0, 100)
    turtle.goto(100, 25)
    turtle.goto(-100, 25)
    turtle.end_fill()

# Function to draw the door
def draw_door():
    draw_rectangle(0, -100, 40, 50, "brown")

# Function to draw a window
def draw_window(x, y):
    draw_rectangle(x, y, 40, 40, "white")


# Main function
def main():
    turtle.speed(3)
    turtle.colormode(255)  # Enable RGB mode for unnamed colors
    setup_background()
    draw_house()
    draw_roof()
    draw_door()
    draw_window(-50, -30)
    draw_window(50, -30)
    turtle.hideturtle()
    turtle.exitonclick()

main()
