
#################################################################################
# Author: Kirsten
# Username:fusonk
#
# Assignment:hw03
# Purpose: To create a house
# Google Doc Link: https://docs.google.com/document/d/1v6GNZ_V6VjfPpHWQ78XGHKlYIS5PJB8pmnq4gvcog70/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle


def draw_house():
    """
       creates turtle called house, colors the turle red, draws a box, fills box
        """
    house = turtle.Turtle()
    house.color('red')  #Set house color
    house.penup()
    house.goto(-150,-100)
    house.pendown()
    house.begin_fill()
    for x in range(4): #Creating the box for the house
        house.forward(200)
        house.left(90)
    house.end_fill()

def draw_roof():
    """
        creates a turtle called extra, colors it green, creates a roof the is slanted on two sides with a flat top, fills roof color
        """
    extra = turtle.Turtle()
    extra.color('green') #Setting color
    extra.penup()
    #Roof Creation
    extra.goto(-150,100)
    extra.begin_fill()
    extra.pendown()
    extra.forward(200)
    extra.left(120)
    extra.forward(50)
    extra.left(60)
    extra.forward(150)
    extra.left(60)
    extra.goto(-150,100)
    extra.end_fill()

def draw_door():
    """
           creates a turtle called door, changes color to brown, creates square, fills color
           """
    #Door Creation
    door = turtle.Turtle()
    door.penup()
    door.goto(-120,-100)
    door.pendown()
    door.color("brown")
    door.begin_fill()
    for b in range(4):
        door.forward(40)
        door.left(90)
    door.end_fill()

def draw_windows():
    """
        creates a turtle called window. colors window blue, creates 3 windows, and fills the color in with blue
        """
    window = turtle.Turtle()
    window.penup()
    window.color('blue')
    window.goto(-70,-80)
    window.pendown()
    window.begin_fill()
    for y in range(4): #first floor windows
        window.forward(15)
        window.left(90)
    window.penup()
    window.forward(40)
    window.pendown()
    for y in range(4): #first floor windows moved over 40
        window.forward(15)
        window.left(90)
    window.penup()
    window.forward(40)
    window.pendown()
    for y in range(4): #first floor windows moved over by 40 again
        window.forward(15)
        window.left(90)
    window.end_fill()

def draw_outside(): #creating the grass outside the house
    """
        creates a turtle called out. turtle is turned green, creates a box for grass, fills in the green color
        """
    out = turtle.Turtle()
    out.color('green')
    out.penup()
    out.goto(-400,-100)
    out.pendown()
    out.begin_fill()
    for n in range(4): #making a box for the grass to fill in
        out.forward(800)
        out.right(90)
    out.end_fill()

def draw_sunshine(): #Creating the sun
    """
        creates turtle called sun, sets color to yellow, makes circle, fills the circles color in.
        """
    sun = turtle.Turtle()
    sun.color('yellow')
    sun.penup()
    sun.begin_fill()
    sun.goto(300,100)
    sun.pendown()
    sun.circle(180) #The circle that gets filled
    sun.end_fill()


def main():
    """
            creates screen and the color of the background using rgb. calls all other functions
            """
    wn = turtle.Screen() #Brings up turtle screen
    turtle.colormode(255) #Uses RGB to choose color
    wn.bgcolor(144,222,225) #Creates a blue/tealish color
    draw_house()
    draw_roof()
    draw_door()
    draw_windows()
    draw_outside()
    draw_sunshine()
    wn.exitonclick()

main()  # Starts the program!