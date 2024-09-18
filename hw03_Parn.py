#################################################################################
# Author: Din din
# Username: Parn
#
# Assignment: HW03
# Purpose:
# Google Doc Link: https://docs.google.com/document/d/1sQnpXAVsiqnegxWI9VXq8K3qfozzuTXckaQppCD3Dh8/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle


def window(windows, x, y):
    """
    this takes the x and y coordinates and creates a window.
    """
    windows.penup()
    windows.goto(x, y)
    windows.pendown()

    # for the left window
    windows.fillcolor("black")
    windows.begin_fill()
    for i in range(4):
        windows.fd(40)
        windows.right(90)
    windows.end_fill()

def triangles(tree, x, y):
    """
    this is creating two triangles for the top part of the tree
    """
    tree.color("green")
    tree.penup()
    # tells python when to fill in the color once run down is done
    tree.goto(x, y)
    tree.begin_fill()
    tree.pendown()
    tree.forward(150)
    tree.left(150)
    tree.forward(90)
    tree.end_fill()
    tree.penup()


def main():
    """
    this makes the screen for the turtle that's created, and it'll make a tree and a house (both the tree and the house will be filled with colors).
    """
    wn = turtle.Screen()  # this initializes the screen
    wn.bgcolor('#8B969A')  # this sets the background color from the RGB website

    triangle = turtle.Turtle()
    rectangle = turtle.Turtle()
    bottom = turtle.Turtle()
    top = turtle.Turtle()
    door = turtle.Turtle()
    l_window = turtle.Turtle()
    r_window = turtle.Turtle()

    # this will make the bottom triangle (part of the tree)
    triangle.penup()
    triangles(triangle,  0,0)
    triangle.pendown()

    # this will make the trunk of the tree
    rectangle.color("#7C5806")
    rectangle.begin_fill()  # tells python when to fill in the color once run down is done
    rectangle.penup()
    rectangle.forward(35)
    rectangle.pendown()
    rectangle.right(90)
    rectangle.forward(70)

    # this is the loop to make the rectangle shape of the trunk
    for i in range(3):
        rectangle.left(90)
        rectangle.forward(70)
        # rectangle.left(90)
        # rectangle.forward(70)
    rectangle.end_fill()  # tells python when to fill in the color once run down is done

    # # I added this to make it look more like a tree
    triangle.right(150)
    triangles(triangle, 0 , 40)
    # setting the cordinates for the house
    bottom.penup()
    bottom.goto(-250, 30)
    bottom.pendown()

    # making the house (the square part)
    bottom.fillcolor("#E21515")
    bottom.begin_fill()
    for i in range(4):  # the house's location is suppose to look like it's more in front of the tree
        bottom.fd(180)
        bottom.right(90)
    bottom.end_fill()

    # coordinates for the roof
    top.penup()
    top.goto(-152, 140)
    top.pendown()

    top.fillcolor("black")
    top.begin_fill()
    top.right(43)
    top.fd(165)
    top.right(137)
    top.fd(259)
    top.right(137)
    top.fd(180)
    top.right(97)
    top.fd(15)
    top.end_fill()

    # making the door
    door.penup()
    door.goto(-190, -70)
    door.pendown()

    door.fillcolor("black")
    door.begin_fill()
    door.fd(50)
    door.right(90)
    door.fd(80)
    door.right(90)
    door.fd(50)
    door.right(90)
    door.fd(80)
    door.end_fill()
    window(l_window,-220, -0)
    window(r_window, -140, -0)

    wn.exitonclick()  #this exits the screen once you click on it

main() #this is needed to make everything else work