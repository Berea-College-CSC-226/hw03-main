
#################################################################################
# Author: Luis Olivas
# Username: rockero241
#
# Assignment: hw03 - Fully Functional Gitty Psychedelic Robot Turtles
# Purpose:
# Google Doc Link: https://docs.google.com/document/d/1mrc8WmON440HpzEmCvNJ3uzkPaZT3mTe7Op433ShEAs/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################


import turtle


def draw_building(building):
    """
    Draws the building using the building turtle.
    """
    building.color('gold')
    building.fillcolor(115, 134, 120)
    building.begin_fill()

    for i in range(2):
        building.fd(120)
        building.right(90)
        building.fd(240)
        building.right(90)
    building.end_fill()

def draw_windows(windows):
    """
    Draws the building's windows row by row.
    """
    # object attributes
    windows.color(0, 0, 0)
    windows.fillcolor('gold')
    windows.hideturtle()

    b = -25 # for row position
    for i in range(4):
        a = 35
        row_position = (a, b)
        # row position
        windows.penup()
        windows.goto(row_position)
        windows.begin_fill()
        make_window_row(windows)
        windows.end_fill()
        b -= 55

def makeRectangle(windows, a, b):
    """"
    Basic rectangle making function. Used in making the building's windows
    """
    for i in range(4):
        windows.fd(a)
        windows.right(90)
        windows.fd(b)

def make_window_row(windows):
    """
    Makes an entire row of windows.
    """
    windows.pendown()
    makeRectangle(windows, 15, 15)
    windows.penup()
    windows.fd(52.5)
    windows.pendown()
    makeRectangle(windows, 15, 15)

def main():
    """
    Defines turtles, sets window attributes, and calls other functions.
    """
    wn = turtle.Screen()
    wn.colormode(255)
    wn.bgcolor(0, 0, 0)

    building = turtle.Turtle() # creates turtle 1
    windows = turtle.Turtle() # creates turtle 2

    # Function calls to function_1 and function_2.
    draw_building(building)  # calls function 1 that draws the building
    draw_windows(windows)   # calls function 2 that draws windows

    wn.exitonclick()
main()  # Starts the program!