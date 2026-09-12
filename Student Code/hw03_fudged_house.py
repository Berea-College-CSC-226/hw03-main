#################################################################################
# Author: Demetri Fudge
# Username: fudged
#
# Assignment: HW03 - Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Drawing a house
# Google Doc Link: https://docs.google.com/document/d/1AbNSF82yNFrVIakRkAtp-AM72y4IbijL1r1pgXPx-b0/edit?tab=t.0
#
#################################################################################

import turtle                       # Imports turtle from the Turtle library.

def main():
    """
    Spawns in the screen which is baby blue and spawns the turtle which is invisible.
    Also defines the pieces of the drawing and exits the screen on click.
    """
    turtle.Turtle()                 # Spawns the turtle from the Turtle library.
    bert = turtle.Turtle()          # Turtle is named bert.
    wn = turtle.Screen()            # Spawns the screen to draw on.
    wn.bgcolor("#89cff0")           # Screen color is baby blue.
    bert.hideturtle()               # Makes the turtle invisible.
    bert.pensize(10)
    house_frame(bert)               # Makes all the functions work when called.
    house_roof(bert)
    house_door(bert)
    house_window(bert)
    wn.exitonclick()                # Closes the screen by clicking it.

def house_frame(bert):
    """
    Draws the frame of the house.
    """
    bert.penup()
    bert.goto(-200, -200)
    bert.color("#FFF44F")           # Makes the color of the frame lemon yellow.
    bert.pendown()
    bert.begin_fill()
    for i in range(4):              # Makes a square for the frame.
        bert.forward(300)
        bert.left(90)
    bert.end_fill()

def house_roof(bert):
    """
    Draws the roof of the house.
    """
    bert.penup()
    bert.goto(-250, 100)
    bert.color("#ff000d")           # Makes the color of the roof pure red.
    bert.pendown()
    bert.begin_fill()
    bert.forward(400)
    for i in range(2):              # Makes a triangle for the roof.
        bert.left(120)
        bert.forward(400)
    bert.end_fill()

def house_door(bert):
    """
    Draws the door to the house.
    """
    bert.setheading(0)              # Makes the turtle go back to its original orientation.
    bert.penup()
    bert.goto(-175, -200)
    bert.color("#6495ED")           # Makes the color of the door cornflower blue.
    bert.pendown()
    bert.begin_fill()
    bert.forward(100)               # Makes a rectangle for the door.
    bert.left(90)
    bert.forward(200)
    bert.left(90)
    bert.forward(100)
    bert.left(90)
    bert.forward(200)
    bert.end_fill()

def house_window(bert):
    """
    Draws the window to the house.
    """
    bert.setheading(0)
    bert.penup()
    bert.goto(-25, -50)
    bert.color("#568203")           # Makes the color of the window avocado green.
    bert.pendown()
    for i in range(4):              # Makes a square for the window frame.
        bert.forward(75)
        bert.left(90)
    bert.penup()
    bert.goto(13, -45)
    bert.pendown()
    bert.left(90)                   # Makes the lines for the window.
    bert.forward(70)
    bert.setheading(0)
    bert.penup()
    bert.goto(-20, -10)
    bert.pendown()
    bert.forward(70)

main()                              # Calls all the functions back so it can now work.
