######################################################################
# Authors: Arbjosa Halilaj
# Username: halilaja
# Google Doc: https://docs.google.com/document/d/14T5BiVZLmSIamvte978sTi6nW3gfJmRvPe6sXbFPgks/edit?usp=sharing
# Assignment: HW03: Fully Functional Gitty Psychedelic Robotic Turtles
#
# Purpose: A program that uses the Turtle library to create complex
# drawings with functions, custom colors, and embellishments, while
# reinforcing version control practices through Git for collaboration
# and code management.
######################################################################
# Acknowledgements:
######################################################################
import turtle

def draw_house():
    """
    Draws the main body of the house using a turtle.
    """
    house = turtle.Turtle()
    house.speed(3)

    # Draw the side of the house with a gray fill color
    house.color("#000000")
    house.fillcolor("#d8dcd6")
    house.begin_fill()
    house.left(10)
    for i in range(2):
        house.forward(150)
        house.left(80)
        house.forward(100)
        house.left(100)
    house.end_fill()

    # Draw the front square wall of the house
    house.setheading(0)
    house.setpos(0, 0)
    house.left(180)
    house.begin_fill()
    for i in range(4):
        house.forward(100)
        house.right(90)
    house.end_fill()

    house.hideturtle()

def draw_roof():
    """
    Draws the roof of the house with a red fill color.
    """
    roof = turtle.Turtle()
    roof.speed(3)

    # Draw the main triangular section of the roof
    roof.color("#000000")
    roof.fillcolor("#9C2B2B")
    roof.penup()
    roof.setpos(-100, 100)
    roof.pendown()
    roof.begin_fill()
    roof.left(45)
    roof.forward(70)
    roof.right(90)
    roof.forward(70)
    roof.end_fill()

    # Draw the second roof section to complete the shape
    roof.penup()
    roof.setpos(-50.5, 149.5)
    roof.pendown()
    roof.setheading(10)
    roof.begin_fill()
    roof.forward(145)
    roof.right(50)
    roof.forward(75)
    roof.right(130)
    roof.forward(153)
    roof.right(55)
    roof.forward(70)
    roof.end_fill()

    roof.hideturtle()

def draw_door():
    """
    Draws the door of the house using a brown fill color.
    The door is a small rectangular shape at the front base of the house.
    """
    door = turtle.Turtle()
    door.speed(3)

    # Draw the door with brown fill color
    door.color("#000000")
    door.fillcolor("#7a5901")
    door.setpos(-60, 0)
    door.begin_fill()
    for i in range(2):
        door.forward(30)
        door.left(90)
        door.forward(40)
        door.left(90)
    door.end_fill()

    door.hideturtle()

def draw_window1():
    """
    Draws the first window on the house with a light blue fill color.
    The window is a square with cross-sections.
    """
    window = turtle.Turtle()
    window.speed(3)

    # Draw the window frame
    window.color("#000000")
    window.fillcolor("#87CEEB")
    window.penup()
    window.setpos(20, 50)
    window.pendown()

    # Draw the square window
    window.begin_fill()
    window.left(10)
    for i in range(2):
        window.forward(40)
        window.left(80)
        window.forward(40)
        window.left(100)
    window.end_fill()

    # Draw the cross-section lines
    window.penup()
    window.setpos(20, 70)  # Horizontal line
    window.pendown()
    window.setheading(10)
    window.forward(40)

    window.penup()
    window.setpos(40, 55)  # Vertical line
    window.setheading(90)
    window.pendown()
    window.forward(40)

    window.hideturtle()

def draw_window2():
    """
    Draws the second window on the house with a light blue fill color.
    The window is similar to the first one with cross-sections.
    """
    window1 = turtle.Turtle()
    window1.speed(3)

    # Draw the window frame
    window1.color("#000000")
    window1.fillcolor("#87CEEB")
    window1.penup()
    window1.setpos(80, 60)
    window1.pendown()

    # Draw the square window
    window1.begin_fill()
    window1.left(10)
    for i in range(2):
        window1.forward(40)
        window1.left(80)
        window1.forward(40)
        window1.left(100)
    window1.end_fill()

    # Draw the cross-section lines
    window1.penup()
    window1.setpos(80, 80)  # Horizontal line
    window1.pendown()
    window1.setheading(10)
    window1.forward(40)

    window1.penup()
    window1.setpos(100, 65)  # Vertical line
    window1.setheading(90)
    window1.pendown()
    window1.forward(40)

    window1.hideturtle()

def draw_tree():
    """
    Draws a tree next to the house with a brown trunk and green leafy top.
    The tree consists of a rectangular trunk and a circular top.
    """
    t = turtle.Turtle()
    t.speed(3)

    # Draw the tree trunk
    t.penup()
    t.goto(-160, 0)
    t.pendown()
    t.pencolor("black")
    t.fillcolor("saddlebrown")
    t.begin_fill()
    for _ in range(2):
        t.forward(20)
        t.left(90)
        t.forward(60)
        t.left(90)
    t.end_fill()

    # Draw the leafy top
    t.penup()
    t.goto(-150, 60)
    t.pendown()
    t.pencolor("black")
    t.fillcolor("forestgreen")
    t.begin_fill()
    t.circle(40)
    t.end_fill()

    t.hideturtle()

def main():
    """
    Sets up the screen and calls the functions to draw the house, roof,
    door, windows, and tree.
    """
    wn = turtle.Screen()
    wn.bgcolor('#c1c6fc')  # Light blue background
    wn.title("House with a tree")
    draw_house()
    draw_roof()
    draw_door()
    draw_window1()
    draw_window2()
    draw_tree()
    turtle.exitonclick()

# Call the main function to execute the program
main()