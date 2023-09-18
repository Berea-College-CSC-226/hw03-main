
#################################################################################
# Author: Nancy Alvarado Ruiz
# Username:alvaradoruiz
#
# Assignment:HW03
# Purpose: Create a complex drawing
# Google Doc Link:https://docs.google.com/document/d/1MJcOBvwG28zuDBP83rLQiCzc2plLyxOdp0uERAAff4o/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################
import turtle
def setupWindow(square):
    """
    Set up screen to draw square part of house
    """
    square.penup()
    square.setpos(-150,-150)
    square.pendown()
    square.pensize(17)
    square.color("pink")

def setup_window(triangle):
    triangle.penup()
    triangle.setpos(-150,-15)
    triangle.pendown()
    triangle.pensize(17)
    triangle.color("light blue")
def setupwindow(door):
    door.penup()
    door.setpos(-70,-140)
    door.pendown()
    door.pensize(10)
    door.color("yellow")

def makeDoor(t):
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(50)
def makeTriangle(t,sz):
    for i in range(3):
        t.forward(sz)
        t.left(sz)
def makesqaure(t,sz):
    """
    creates square
    """
    for i in range(4):
        t.forward(sz)
        t.left(90)
    # ...


def main():
    """
    Docstring for main
    """
    wn = turtle.Screen()
    wn.bgcolor("dark blue")
    square = turtle.Turtle()
    triangle = turtle.Turtle()
    door = turtle.Turtle()
    setupWindow(square)
    setup_window(triangle)# Function call to function_1
    setupwindow(door)
    makesqaure(square,120)
    makeTriangle(triangle,120)
    makeDoor(door)
    wn.exitonclick() # Function call to function_2


main()