#####################################################
# This program draws a familiar-looking house.
# It's supposed to be the Chacaltaya Ski Resort: deserted due to global warming, it has become a key
# data-collection center for atmospheric scientists in La Paz, including my father.
# Pictures of it can be easily found on Google, but here is the one I used for reference
# https://share.google/SN9hNYtHo4CX7sOZA
# Author: Mateo Andrade (andradem)

# Also note: the branch name was lake because I thought of making a lake before setting on the Ski Resort

import turtle
import random

#####################################################
# SETUP VARIABLES
# Yeah I know you told us to group all of our code inside of main() but I think it's ok to declare variables
# and the like here

ws = turtle.Screen()
ws.bgcolor("lightskyblue1")

koopa = turtle.Turtle()
koopa.pensize(10)
koopa.speed(0)

colorsStoneBase = ["maroon", "saddlebrown", "tan3", "tan4", "red4"]
colorsResort = ["firebrick4", "maroon"]
colorsRoof = ["azure", "azure1", "lavender"]
colorsRoof2 = ["lightsalmon", "lightsalmon", "lightsalmon3"]
colorsBackground = ["lightsteelblue1", "lightsteelblue2", "lightsteelblue", "lightsteelblue3"]

######################################################

def bostro (x, y, palette, triangle):
    """
    Draws a boustrophedon rectangle. Randomly switches colors using input palette.
    Triangle decreases the tip of the rectangle to turn it into an isosceles trapezoid, or triangle if it ends up
    surpassing x.
    x and y are not pensize dependant, but Triangle unfortunately is

    Args:
        x: x distance of rectangle
        y: y distance of rectangle
        palette: randomly switches pencolors using this array of colors
        triangle: decrease the x of the rectangle for what amount for each line, effectively turning the rectangle into
            an isosceles trapezoid or triangle
    :returns: none
    """
    random.seed(226)
    direction = 1
    for i in range(y//koopa.pensize()):
        lengthTaken = 0
        x -= triangle # decrease size (only triangle)
        while lengthTaken < x:
            step = 10*random.randint(3, 7)
            if lengthTaken + step >= x:
                step = x-lengthTaken
            koopa.pencolor(palette[random.randint(0,  len(palette)-1)])
            koopa.fd(step)
            lengthTaken += step
        koopa.up()
        koopa.left(90*direction)
        koopa.forward(koopa.pensize())
        koopa.left(90*direction)

        x -= triangle # decrease size (triangle only)
        koopa.forward(triangle) # same here

        koopa.down()
        direction *= -1

def background (thickness, palette):
    """
    The procedure to draw the background. It's rather meh.


    Args:
        thickness: thickness of the lines that make the background
        palette: randomly switches pencolors using this array of colors
    :returns: None
    """
    koopa.goto(-500, 100)
    koopa.down()
    for i in range(0,4):
        koopa.pencolor(colorsBackground[i])
        koopa.pensize(thickness)
        koopa.fd(1000)
        koopa.fd(-1000)
        koopa.right(90)
        koopa.fd(thickness)
        koopa.left(90)
    koopa.up()

def colordemo(palette):
    """
    A simple function used to test out palettes in the order they were added.
    Turtle moves as many times as there are colors in palette, and switches pencolors via palette.
    Args:
        palette: the colors to be tested
    :returns: none
    """
    for i in palette:
        koopa.pencolor(i)
        koopa.fd(20)

def rectangle (x, y, pen, fill):
    """
    A simple function that creates a rectangle.
    Args:
        x: x size of rectangle
        y: y size of rectangle
        pen: pencolor
        fill: fill color
    :returns: none
    """
    koopa.pencolor(pen)
    koopa.fillcolor(fill)
    koopa.begin_fill()
    for i in range(0,4):
        koopa.fd(y * (i%2) + x * ((i+1)%2))
        koopa.right(90)
    koopa.end_fill()

def windows():
    """
    This is just a way to build windows. It could be better made, but I am outta time. I'm sorry.
    :returns: none
    """
    for i in range(0,2):
        koopa.up()
        koopa.right(90)
        koopa.fd(130)
        koopa.left(90)
        koopa.fd(20)
        koopa.down()
        rectangle(30, 50, "lavender", "skyblue4")
        koopa.up()
        koopa.fd(-70)
        koopa.down()
        rectangle(30, 50, "lavender", "skyblue4")
        koopa.up()
        koopa.fd(55)

def main():
    # First draw the background
    background (150, colorsBackground)
    # Set-up for stone base
    koopa.pensize(10)
    koopa.goto(-50,-400)
    # Draw the stone base
    bostro(550, 300, colorsStoneBase, False)
    # Draw the hanging shed/patio
    koopa.right(180)
    rectangle(20, 90, "burlywood", "burlywood")
    koopa.right(180)
    # Draw the main room
    bostro(300, 100, colorsResort, False)
    # Overhang
    koopa.fd(-10)
    # Build the room out of two bostros
    bostro(320, 140, colorsRoof, 7)
    bostro(123, 100, colorsRoof2, 7)
    # Lastly, draw the windows
    windows()

    ws.exitonclick()

main()

