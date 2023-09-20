######################################################################
# Author: Logan Anglin
# Username: anglinl
# Assignment: HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: To create an image of a pyramid using the Python turtle and use it to learn Git processes.
# Google Drive link: https://docs.google.com/document/d/14kBIsM65KMGQX2QgzxX9nVnjA9f2AQo2YVci1p7xbOY/edit?usp=sharing
######################################################################
# Acknowledgements:
#
#
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
######################################################################

import turtle


def draw_circles():
    """
    Draws two circles around the pyramids to create the illusion of a circular base.
    """
    t = turtle.Turtle()  # Creates a turtle to draw the circles.
    t.hideturtle()
    t.penup()

    t.right(90)  # Positioning for the first turtle.
    t.forward(170)
    t.left(90)

    t.pendown()  # Drawing the first circle.
    t.fillcolor("#BB6016")
    t.begin_fill()
    t.circle(170)
    t.end_fill()

    # Repositioning the turtle to draw a second circle this one a bit lighter to give the illusion of shadows.
    t.penup()
    t.left(90)
    t.forward(20)
    t.right(90)

    t.pendown()  # Drawing the second circle.
    t.fillcolor("#DD8238")
    t.begin_fill()
    t.circle(150)
    t.end_fill()


def draw_pyramid(length, t):
    """Draws a pyramid-looking shape."""
    for i in range(8):
        t.pendown()
        t.fillcolor("#FDA258") # A bit darker of a sandy color.
        t.begin_fill() # Creates the shape
        for i in range(4):
            t.forward(length)
            t.left(90)
        t.penup()
        t.left(45)
        t.forward(20)
        t.right(45)
        length = length - 28.28 # This makes the distance between each "step" approximately the same on all sides.
        t.end_fill()


def main():
    """
    This program will draw a pyramid shape as viewed from above.
    """
    drawing_pen = turtle.Turtle() # Creates the illustrative turtle. Passed to drawPyramid() as t.
    wn = turtle.Screen()
    wn.colormode(255) # Uses hex-code for colors.
    wn.bgcolor("#FFE7B3") # Makes the background "sandy".
    drawing_pen.hideturtle()
    drawing_pen.speed(0) # For convenience. Feel free to change.

    # These next five lines move the turtle so the pyramid is roughly centered in the window.
    drawing_pen.penup()
    drawing_pen.right(135)
    drawing_pen.forward(141.42)
    drawing_pen.left(135)
    drawing_pen.pendown()

    draw_circles()

    draw_pyramid(200, drawing_pen)

    wn.exitonclick()

main()