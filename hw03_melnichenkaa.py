#################################################################################
# Author: Aliaksandr Melnichenka
# Username: melnichenkaa
#
# Assignment:
# Purpose:
# Google Doc Link: https://docs.google.com/document/d/1SS2cktYFybPYRGyeDuiIRQVh62Jtxf-0xMK6qmmmdfg/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################


import turtle
import math

### Constants of the house
house_width = 300
house_height = 200
roof_angle = 30
roof_length = house_width / math.cos(math.radians(roof_angle)) / 2
door_width = house_width / 5
door_height = house_height / 2
windows_length = 2*math.pi * house_width / 10
windows_resolution = 50 #number of steps on window

def goto_invisible(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def drawBasement(t):
    """
    Drawing a rectangle of the house basement.
    """
    goto_invisible(t, -house_width/2, -house_height/2)
    t.forward(house_width)
    t.left(90)
    t.forward(house_height)
    t.left(90)
    t.forward(house_width)
    t.left(90)
    t.forward(house_height)
    t.left(90)

def drawRoof(t):
    """
    Drawing roof as a triangle
    """
    goto_invisible(t, -house_width/2, house_height/2)
    t.left(roof_angle)
    t.forward(roof_length)
    t.right(2*roof_angle)
    t.forward(roof_length)
    t.left(roof_angle)

def drawDoor(t):
    """
    Drawing a rectangle of the door.
    """
    t.left(90)
    goto_invisible(t, -house_width/2/1.5, -house_height/2)
    t.forward(door_height)
    t.right(90)
    t.forward(door_width)
    t.right(90)
    t.forward(door_height)
    t.left(90)

def drawWindow(t):
    """
    Drawing a circul of the window.
    """
    goto_invisible(t, house_width/4, house_height/4)
    for i in range(windows_resolution):
        t.forward(windows_length/windows_resolution)
        t.right(360/windows_resolution)




def main():

    screen = turtle.Screen()
    screen.bgpic('landscape.png')
    t1 = turtle.Turtle()
    t1.shape("turtle")
    t1.color("#0FF0FF")
    t1.speed(7)

    drawBasement(t1)
    drawRoof(t1)
    drawDoor(t1)
    drawWindow(t1)

    t1.hideturtle()
    screen.bgpic('landscape1.png')

    screen.exitonclick()

main()  # Starts the program!