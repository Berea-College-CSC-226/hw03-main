#################################################################################
# Author: Bryanna Erickson
# Username: ericksonb
#
# Assignment:HW03
# Purpose:
# Google Doc Link:https://docs.google.com/document/d/1xtqnVfdKkxr4C0jd47oIFCfKWOiEHnvoOJpZYP8M4Hs/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle

def draw_rect(turtle, color, length, height):
    """
    Draws a rectangle
    """
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()
    turtle.penup()

def draw_tri(turtle, color, length):
    """
    Draws a triangle
    """
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(length)
        turtle.left(120)
    turtle.end_fill()
    turtle.penup()

def draw_tree(turtle):
    """
    Draws a tree
    """
    for i in range(3):
        draw_tri(turtle,"#14651A",100)
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(-50)

def main():
    """
    Sets up the screen, sets up turtle, and draws a house and trees.
    """
    #Sets up the screen and changes the color.
    wn = turtle.Screen()
    wn.bgcolor("#2FA8E5")

    #Creates the turtle "tess" and sets speed to 10.
    tess = turtle.Turtle()
    tess.speed(10)

    #Sets position and draws the house.
    tess.penup()
    tess.setpos(-150,-288)
    draw_rect(tess,"#BAC475", 300, 400)

    #Sets the position and draws the door.
    tess.setpos(-50,-288)
    draw_rect(tess,"#493434",100,200)

    #Sets the positions and draws windows.
    tess.setpos(-130,-30)
    draw_rect(tess,"#4FC5F0",75,100)
    tess.setpos(50,-30)
    draw_rect(tess, "#4FC5F0", 75, 100)

    #Sets position and draws roof.
    tess.setpos(-150,112)
    draw_tri(tess,"#BF0707",300)

    #Sets positions and draws two trees.
    tess.setpos(225,-288)
    draw_rect(tess,"#542222",20,80)
    tess.setpos(185,-208)
    draw_tree(tess)
    tess.setpos(-225,-288)
    draw_rect(tess,"#542222",20,80)
    tess.setpos(-265,-208)
    draw_tree(tess)

    wn.exitonclick()

main()
