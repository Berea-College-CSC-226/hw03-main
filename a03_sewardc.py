#################################################################################
# Authors: Caleb Seward
# Username:Sewardc
#
# Assignment: Homework assignment 3
# Purpose: Draws a house using multiple functions and has colors using RGB
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle


wn = turtle.Screen()
wn.colormode()                                             # Allows us to use the colormode of the turtle screen
hou = turtle.Turtle()
wn.bgcolor("Purple")
hou.shape("circle")
size = 15


def draw_housefoundation():
    """
    Draws the base of the house
    """
    wn.colormode(255)
    hou.pencolor(120, 20, 5)
    hou.fillcolor(0, 128, 255)
    hou.begin_fill()
    hou.pensize(size)
    hou.penup()
    hou.goto(-260, -260)                                      # reposition turtle instance to the lower left corner of the turtle window about (-260, -260)
    hou.pendown()
    for i in range(4):
        hou.fd(300)
        hou.left(90)
    hou.end_fill()

def draw_roof():
    """
    Draws the roof on top of the house
    """

    hou.pensize(size)
    hou.penup()
    hou.goto(-260, 58)                     # reposition turtle instance to the left upper corner of square
    hou.pendown()
    wn.colormode(255)
    hou.color(25, 0, 47)
    hou.fillcolor(35, 100, 55)
    hou.begin_fill()
    for i in range(3):                     # draws the triangle on top of the house
        hou.forward(300)
        hou.left(120)
    hou.end_fill()





def add_text():
    """
    Adds text to the turtle screen
    """
    hou.goto(-120, -25)                             # Takes turtle instance to coordinates
    hou.hideturtle()
    hou.color('black')
    hou.up()
    hou.write("Assignment Finished!", move=False, align='center', font=('Comic Sans', 20, ('bold', 'normal')))       # setting up the write method that allows the instance to write on the screen


def main():
    """
    Calls the square and fills  it with the color for main
    """
    draw_housefoundation()           # Function call to draw_housefoundation()
    draw_roof()                      # Function call to draw_roof()
    add_text()


main()                               # Function call to main function()
wn.exitonclick()


