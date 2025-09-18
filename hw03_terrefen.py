#################################################################################
# Author: Nahom Terrefe
# Username: terrefen
#
# Assignment: Be Creative
# Purpose: Draw a road with the sun on it
# Google Doc Link: https://docs.google.com/document/d/1iabSMZODh1u7U5lVtsQ9GN9U9FSqr3p_KqHxKGzxQfg/edit?usp=sharing
#
#################################################################################
# Acknowledgements: https://docs.python.org/3/library/turtle.html#turtle.circle
#################################################################################


import turtle


def create_road():
    """
    This Function creates the road first draws a rectangle and then fills it with gray color
    """
    road = turtle.Turtle()
    road.hideturtle() # hides the pointer when we draw
    road.penup()

    road.goto(-400, -150) # goes to the bottom to start drawing
    road.pendown()

    road.color("gray")

    road.begin_fill() # begins the fill process for the road

    for _ in range(2): # creats a rectange
        road.forward(800)
        road.right(90)
        road.forward(200)
        road.right(90)

    road.end_fill() # ends the fill process for the road


def create_sun():
    """
    Create_sun function draws a circle and then fills it with orange color
    """

    sun = turtle.Turtle()
    sun.hideturtle() # hides the pointer when we draw
    sun.penup()
    sun.goto(200, 150)
    sun.pendown()

    sun.color("orange")

    sun.begin_fill()
    sun.circle(60) # draws a circle with a radius as it's parameter
    sun.end_fill()


def create_line():
    """
        create_line function creats a yellow line with a gap on the bottom of the screen
    """

    lines = turtle.Turtle()
    lines.hideturtle() # hides the pointer when we draw
    lines.color("yellow")
    lines.width(5)


    lines.penup()
    lines.goto(-380, -220) # sets the line to be in the middle of the road

    for x in range(12): # draws a line with a separation of 20 units and a line length of 40
        lines.pendown()
        lines.forward(40)
        lines.penup()
        lines.forward(20)


def main():
    """
    This is the main function where all the functions are in. It decides if the program runs or not when
    it is called
    """

    screen = turtle.Screen()
    screen.bgcolor("#2A6F70")

    create_road() # Draws the road
    create_line() # creates the line on the road
    create_sun() # draws the sun

    screen.exitonclick()

main()  # Starts the program!


