################################################################################
# Author: Frederick Oguine
# Username:oguinef
#
# Assignment:Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose:
# Google Doc Link: https://docs.google.com/document/d/1MTjKbG3eNyli4OZdGSySFGS0vXhpDWP905gwgFDvtI0/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle

def draw_rectangle(x, y, width, height, color):
    """
    Draw a rectangle at (x, y) with a given width, height, and color.
    """
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

def draw_triangle(x, y, length, color):
    """
    Draw an equilateral triangle at (x, y) with a given length and color.
    """
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(length)
        turtle.right(120)
    turtle.end_fill()

def main():
    """
    Main function to draw a tree.
    """
    # Screen setup
    wn = turtle.Screen()
    wn.bgcolor("lightblue")  # Light blue sky as background
    turtle.speed(1)

    # Draw the trunk
    draw_rectangle(-15, -50, 30, 50, "brown")

    # Draw the leaves
    draw_triangle(-45, -50, 90, "green")
    draw_triangle(-30, -20, 60, "green")
    draw_triangle(-15, 10, 30, "green")

    turtle.done()

# Call the main function
main()
