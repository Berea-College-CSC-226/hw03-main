#################################################################################
# Author: Cody Bandy
# Username: bandyc
#
# Assignment: HW03
# Purpose: Draw something and use functions
# Google Doc Link: https://docs.google.com/document/d/1NKZj9D6Pb3AakT7FzAY3_hwjKZ2PUx8db1sWfIzOIiU/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################


import turtle


def draw_house(length, color):
    jimbo.fillcolor(color)
    jimbo.begin_fill()
    for h in range(4):
        jimbo.forward(length)
        jimbo.right(90)
    jimbo.end_fill()

def draw_roof(length, color):
    jimbo.fillcolor(color)
    jimbo.begin_fill()
    for r in range(3):
        jimbo.forward(length)
        jimbo.left(120)
    jimbo.end_fill()

def draw_door(width, height, color):
    jimbo.fillcolor(color)
    jimbo.begin_fill()
    for d in range(2):
        jimbo.forward(width)
        jimbo.right(90)
        jimbo.forward(height)
        jimbo.right(90)
    jimbo.end_fill()

def draw_window(length, color):
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
    screen = turtle.Screen()
    screen.colormode(255)
    screen.bgcolor((41, 187, 216))

    jimbo = turtle.Turtle()
    jimbo.pensize(10)
    draw_house(100, "green")
    screen.exitonclick()

main()
