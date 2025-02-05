import turtle
import random

def draw_square(size):
    """Draws a square of specified size."""
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)

def draw_triangle(size):
    """Draws an equilateral triangle of specified size."""
    for _ in range(3):
        turtle.forward(size)
        turtle.left(120)

def draw_rectangle(width, height):
    """Draws a rectangle with given width and height."""
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)

def draw_sky():
    """Fills the top canvas with sky blue to set the background."""
    turtle.penup()
    turtle.goto(-400, 300)
    turtle.pendown()
    turtle.fillcolor("skyblue")
    turtle.begin_fill()
    draw_rectangle(800, 600)
    turtle.end_fill()

def draw_cloud(x, y):
    """Places a fluffy cloud at specified coordinates."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor("white")
    turtle.begin_fill()
    for _ in range(6):
        turtle.circle(20)
        turtle.right(60)
    turtle.end_fill()

def draw_sun(x, y):
    """Draws a bright sun at the given location."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()

def draw_hill(x, y, size):
    """Creates a hill using a semicircle at the provided coordinates and size."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor("forestgreen")
    turtle.begin_fill()
    turtle.setheading(90)
    turtle.circle(size, 180)
    turtle.setheading(270)
    turtle.forward(size * 2)
    turtle.end_fill()

def draw_landscape():
    """Generates the base landscape with grass and hills."""
    turtle.penup()
    turtle.goto(-400, -200)
    turtle.pendown()
    turtle.fillcolor("green")
    turtle.begin_fill()
    draw_rectangle(800, 200)
    turtle.end_fill()

    # Creating hills with varying positions and sizes
    for pos in range(-300, 301, 100):
        draw_hill(pos, -200, random.choice([80, 100, 120, 150]))

def draw_house():
    """Constructs a detailed house with multiple features."""
    # Base of the house
    turtle.fillcolor("#FAEBD7")
    turtle.begin_fill()
    draw_square(200)
    turtle.end_fill()

    # Roof of the house
    turtle.fillcolor("#8B4513")
    turtle.begin_fill()
    turtle.setheading(90)
    turtle.forward(200)
    turtle.right(90)
    draw_triangle(200)
    turtle.end_fill()

    # Chimney on top of the house
    turtle.fillcolor("#A9A9A9")
    turtle.penup()
    turtle.goto(70, 70)
    turtle.pendown()
    turtle.begin_fill()
    draw_rectangle(30, 70)
    turtle.end_fill()

    # Door at the front of the house
    turtle.penup()
    turtle.goto(-30, -200)
    turtle.setheading(90)
    turtle.pendown()
    turtle.fillcolor("#8B4513")
    turtle.begin_fill()
    draw_rectangle(40, 60)
    turtle.end_fill()

    # Windows on either side of the door
    for x in [-80, 40]:
        turtle.penup()
        turtle.goto(x, -70)
        turtle.pendown()
        turtle.fillcolor("white")
        turtle.begin_fill()
        draw_square(40)
        turtle.end_fill()

    # Path leading to the house
    turtle.penup()
    turtle.goto(30, -200)
    turtle.setheading(270)
    turtle.pendown()
    turtle.fillcolor("#A9A9A9")
    turtle.begin_fill()
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(60)
    turtle.end_fill()

    # A simple tree next to the house
    turtle.penup()
    turtle.goto(-230, -110)
    turtle.pendown()
    turtle.color("saddlebrown")
    turtle.begin_fill()
    draw_rectangle(30, 130)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(-215, -110)
    turtle.pendown()
    turtle.color("green")
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()

def main():
    """Main function to orchestrate drawing operations."""
    turtle.speed(0)
    turtle.title("KamKam House")

    draw_sky()
    draw_cloud(-300, 200)
    draw_cloud(-100, 250)
    draw_cloud(200, 220)
    draw_sun(300, 250)
    draw_landscape()

    turtle.penup()
    turtle.goto(-100, -200)
    turtle.setheading(90)
    turtle.pendown()

    draw_house()

    turtle.hideturtle()
    turtle.done()

main()
#pulled my hair out trying to figure out the right (X,Y) coordinates