# Author: Emely Alfaro
# Username: alfarozavalae@berea.edu
#
# Assignment: A03: A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: To understand and create functions to draw more complex objects and use turtles.

# Link to my google docs file: https://docs.google.com/document/d/15YvyZJA45FgmATPoFIBMzD3koKYm8N8krjdFMuS-xI0/edit#

#################################################################################
# Acknowledgements:
# Giorgi Lomia - Taught me how to do xpos, ypos and how to work with the size of the objects.
#
#################################################################################

import turtle

def make_triangle(esa, sz, xpos, ypos, filling, pen):
    """
    :param esa: a turtle object
    :param sz: size of the triangle
    :param xpos: set x position
    :param ypos: set y position
    :param filling: fill the object
    :param pen: color of pen
    :return: none. void
    """
    esa.color(filling, pen) #setting the color for the object and the filling
    esa.penup()
    esa.setpos(xpos, ypos)  #setting the position for the turtle to start drawing
    esa.pendown()
    esa.begin_fill() #filling in the triangle(volcano)
    esa.left(45) #rotating 45 degrees for making the first side of the triangle
    esa.forward(sz) #going up the size of the volcano
    esa.right(90) #rotating 90 degrees for starting the second side
    esa.forward(sz) #going forward for the second side of triangle
    esa.right(135) #last rotation to finish the triangle
    esa.forward(1.405*sz) #going forward so the triangle can be finished
    esa.end_fill() #finishing the fill
    esa.right(180) #positioning turtle to draw again

def make_human(esa,sz, xpos, ypos, filling, pen):
    """

    :param esa: turtle object
    :param sz: size of turtle
    :param xpos: to set x position for the object
    :param ypos:  set y position for the object
    :param filling: to fill the object with color
    :param pen: to define the color for the pen
    :return: none. void
    """
    esa.penup()
    esa.setpos(xpos, ypos) #set x and y position for the object
    esa.color(filling,pen) #filling the object with color and defining pen color
    esa.pendown() #putting pen down to start drawing
    esa.begin_fill() #beginning the fill of the object
    esa.circle(sz/2.5) #drawing a circle of 2.5 of the size
    esa.end_fill() #finishing the fill for the circle
    esa.begin_fill()
    make_triangle(esa, sz, xpos-sz/1.4 , ypos-sz/1.5 , filling, pen) #calling the triangle function to draw the body
    esa.end_fill()
    esa.forward(sz/3) #going forward a third of the size so that the legs can be drawn
    esa.right(90)#turning 90 degrees to the right
    esa.forward(sz/4) #going forward a fourth of the size in order to draw first leg
    esa.penup() #pen up to move a little
    esa.left(90) #turning so that second leg can be drawn
    esa.forward(sz/1.4) #moving forward a fourth of the size to get to the right position
    esa.right(90)
    esa.pendown() #putting pen down to draw second leg
    esa.backward(sz/4) #drawing second leg
    esa.penup() #pen up for drawing the 1st hand
    esa.backward(sz/2.2) #moving so that we are at the right place
    esa.right(30) #turning a little for the right angle
    esa.pendown() #pen down to start drawing
    esa.backward(sz/2) #drawing the 1st hand
    esa.forward(sz/2) #moving to the other side for second hand
    esa.right(60) #turning right
    esa.penup() #putting pen up to move
    esa.forward(sz/1.8) #moving so that we are at the right place
    esa.right(30) #turning for the right angle for second hand
    esa.pendown() #putting pen down to draw again
    esa.forward(sz/2) #drawing second hand

def make_text(esa, wn, txt):
    """
    Writes text to the screen.
    :param esa: Turtle object
    :return: None
    """
    esa.color("blue")
    esa.penup()
    esa.setpos(-20,-100)
    esa.pendown()
    esa.write(txt, move=False, align='center', font=("Arial", 20, ("bold", "normal")))

def main():
    """
    """
esa = turtle.Turtle()
wn = turtle.Screen()   # Makes a new turtle screen
wn.colormode(255) #to enable rgb colors
turtle.bgcolor((173,216,230))           # change color of background
wn.title("Emely's homeland of Volcanoes") #to put a title for the window
esa.speed(7) #to set the speed for drawing
esa.pensize(4) #to set the pensize
esa.hideturtle()
esa.penup() #pen up so we can set the turtle first
esa.setpos(-250,-250) #setting position before starting
make_triangle(esa, 400, 0,0, (0,100,0), (60,179,113)) # Function call to make_triangle
make_triangle(esa, 400, -400,0, (0,100,0), (60,179,113)) # Function call to make_triangle
make_human(esa,50, 30, 90, "black", (222,184,135)) # function cal lto make_human
make_text(esa, "El Salvador, Land of volcanoes")



wn.exitonclick()
