# --------------------------------------------------------------------------
# CSC 226 -
# Name: Mekiyan Bynum
# Username: hw03_bynumM
# Google Doc Link: https://docs.google.com/document/d/1RJxbwMkWsiSHi-ThbASyKpKRuPu4Y1Wc8sciRZzs9qc/edit?tab=t.0
#
# Description: This program draws a simple house
# --------------------------------------------------------------------------


import turtle

def draw_rectangle(t, x, y, width, height, fill_color, outline_color):
    """
    Draws a rectangle with the turtle.

    Args:
        t (turtle.Turtle): The turtle object used for drawing.
        x (int): The starting x-coordinate.
        y (int): The starting y-coordinate.
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        fill_color (str): The fill color of the rectangle.
        outline_color (str): The outline color of the rectangle.
    """
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(outline_color, fill_color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

def draw_triangle(t, x1, y1, x2, y2, x3, y3, fill_color, outline_color):
    """
    Draws a triangle with the turtle.

    Args:
        t (turtle.Turtle): The turtle object used for drawing.
        x1 (int): The x-coordinate of the first point.
        y1 (int): The y-coordinate of the first point.
        x2 (int): The x-coordinate of the second point.
        y2 (int): The y-coordinate of the second point.
        x3 (int): The x-coordinate of the third point.
        y3 (int): The y-coordinate of the third point.
        fill_color (str): The fill color of the triangle.
        outline_color (str): The outline color of the triangle.
    """
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.color(outline_color, fill_color)
    t.begin_fill()
    t.goto(x2, y2)
    t.goto(x3, y3)
    t.goto(x1, y1)
    t.end_fill()

def draw_circle(t, x, y, radius, fill_color, outline_color):
    """
    Draws a circle with the turtle.

    Args:
        t (turtle.Turtle): The turtle object used for drawing.
        x (int): The x-coordinate of the center.
        y (int): The y-coordinate of the center.
        radius (int): The radius of the circle.
        fill_color (str): The fill color of the circle.
        outline_color (str): The outline color of the circle.
    """
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.color(outline_color, fill_color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_house(t):
    """
    Draws the main body of the house, door, windows, and chimney.
    """
    # Main house body
    draw_rectangle(t, -100, 0, 200, 150, "brown", "black")

    # Roof
    draw_triangle(t, -150, 0, 150, 0, 0, 100, "red", "dark red")

    # Door
    draw_rectangle(t, -25, -50, 50, 100, "saddle brown", "black")
    draw_circle(t, 15, -75, 5, "black", "black")

    # Window 1
    draw_rectangle(t, -80, -20, 40, 40, "cyan", "black")

    # Window 2
    draw_rectangle(t, 40, -20, 40, 40, "cyan", "black")

    # Chimney
    draw_rectangle(t, 50, 100, 30, 50, "gray", "black")

def draw_sun(t):
    """
    Draws the sun in the sky.
    """
    draw_circle(t, 250, 200, 40, "yellow", "gold")

def draw_tree(t, x, y):
    """
    Draws a tree with a trunk and a green top.

    Args:
        t (turtle.Turtle): The turtle object used for drawing.
        x (int): The x-coordinate for the tree trunk.
        y (int): The y-coordinate for the tree trunk.
    """
    # Leaves
    draw_circle(t, x, y, 40, "green", "dark green")

    # Trunk
    draw_rectangle(t, x - 10, y - 40, 20, 60, "brown", "black")

def main():
    """
    The main function to set up the screen and draw the scene.
    """
    # Set up the screen
    screen = turtle.Screen()
    screen.title("My House")
    screen.setup(width=800, height=600)

    # A dark blue background color using an unnamed RGB value
    screen.bgcolor(0.27, 0.51, 0.71)

    # Create the turtle object
    t = turtle.Turtle()
    t.speed(0) # Set the drawing speed to fastest
    t.hideturtle() # Hide the turtle to make the final drawing clean

    # Draw the ground
    draw_rectangle(t, -400, -150, 800, 150, "forest green", "forest green")

    # Draw the sun
    draw_sun(t)

    # Draw the house and its embellishments
    draw_house(t)

    # Draw a tree on the left
    draw_tree(t, -250, -100)

    # Draw another tree on the right
    draw_tree(t, 250, -100)

    # Keep the window open until the user clicks
    turtle.done()

# Call the main function to run the program
main()

