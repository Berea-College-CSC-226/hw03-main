#################################################################################
# Author: Sonam Tsering
# Username: Sonam
#
# Assignment: HW03
# Purpose: Draw a colorful house using functions.
# Google Doc Link: https://docs.google.com/document/d/17rrspYRGOVC_dS5D5XEZPSUfPYHl2pfgNTMXdx2hg_A/edit?usp=sharing
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle


def draw_house(jimbo, length, color):
    """
    Draws the base structure of the house.
    """
    jimbo.fillcolor(color)
    jimbo.begin_fill()
    for h in range(4):
        jimbo.forward(length)
        jimbo.right(90)
    jimbo.end_fill()

def draw_roof(jimbo, length, color):
    """
    Draws the roof of the house.
    """
    jimbo.fillcolor(color)
    jimbo.begin_fill()
    for r in range(3):
        jimbo.forward(length)
        jimbo.left(120)
    jimbo.end_fill()

def draw_door(jimbo, width, height, color):
    """
    Draws the front door of the house.
    """
    jimbo.fillcolor(color)
    jimbo.begin_fill()
    for d in range(2):
        jimbo.forward(width)
        jimbo.right(90)
        jimbo.forward(height)
        jimbo.right(90)
    jimbo.end_fill()

def draw_window(jimbo, length, color):
    """
    Draws a window for the house.
    """
    jimbo.fillcolor(color)
    jimbo.begin_fill()
    for w in range(4):
        jimbo.forward(length)
        jimbo.right(90)
    jimbo.end_fill()
    jimbo.forward(length/2)
    jimbo.right(90)
    jimbo.forward(length)
    for b in range(2):
        jimbo.right(90)
        jimbo.forward(length/2)
    jimbo.right(90)
    jimbo.forward(length)

def main():
    """
    Sets attributes for the turtle and screen, then performs the steps needed to draw the entire house using the other functions.
    """
    wn = turtle.Screen()
    wn.colormode(255)     # enables the use of RGB values to set a color attribute
    wn.bgcolor((41, 187, 216))     # baby blue background, or close enough

    jimbo = turtle.Turtle()     # named him jimbo because why not?
    jimbo.pensize(10)

    jimbo.penup()
    jimbo.goto(-100,50)     # get into position to draw the base of the house
    jimbo.pendown()
    draw_house(jimbo, 400, (216, 41, 99))     # draw a red house base
    draw_roof(jimbo, 400, (226, 194, 34))     # no repositioning needed for the yellow roof, draw it immediately
    jimbo.penup()
    jimbo.goto(50, -200)     # getting into position for the door
    jimbo.pendown()
    draw_door(jimbo, 100, 150, (18, 131, 26))     # draws a door that is green
    jimbo.penup()
    jimbo.goto(-50, -50)     # gets into position for the first window
    jimbo.pendown()
    draw_window(jimbo, 100, (255, 255, 255))     # draw a white window, split into panes
    jimbo.penup()
    jimbo.goto(150, -50)     # getting ready for the second one
    jimbo.pendown()
    draw_window(jimbo, 100, (255, 255, 255))     # a matching twin for the first window
    jimbo.hideturtle()     # hidden for your viewing pleasure


    wn.exitonclick()

main()     # without this function call, nothing would happen
