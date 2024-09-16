#################################################################################
# Author: Utsa Seth
# Username: sethutsa
#
# Assignment: HW 03
# Purpose: Make a turtle artwork based on guidelines
# Google Doc Link: https://docs.google.com/document/d/1eaKOWOABEuIIrmJ1DmS89uaWYTad68SuiMbo4g9Pe5M/edit?usp=sharing
#
#################################################################################
# Acknowledgements: Learned how to add images and text from t03_functions_house.py
# provided with t03 assignment. Took the idea of changing Dory's "just keep swimming"
# to "just keep coding" from Nicholas Hamilton. Modified by adding more inputs to functions
# and reduced the number of functions

#################################################################################
import turtle


def draw_fish(t):
    """
       draws blue and yellow fish using ocean
    """
    t.pensize(4)
    t.color('yellow')
    t.lt(90)
    t.begin_fill()
    for i in range(3):
        t.forward(60)
        t.right(120)
    t.end_fill()
    t.lt(75)
    t.color('blue')
    t.begin_fill()
    for i in range(2):
        t.fd(120)
        t.rt(150)
    t.end_fill()
    t.color('yellow')
    t.begin_fill()
    t.right(30)
    t.fd(150)
    for i in range(2):
        t.rt(120)
        t.fd(30)
    t.end_fill()


def draw_bubbles(t, x, y):
    """
        draws bubbles using ocean
    """
    position = (x,y)
    t.penup()
    t.goto(position)
    t.pendown()
    for i in range(5):
        t.dot(15, 'navy')
        t.penup()
        x = x - 20
        y = y + 15
        t.goto(x,y)


def drawstarfish(t):
    """
        draws a row of starfish using turtles
    """
    t.pensize(5)
    t.color('IndianRed1')
    x = -250
    for i in range (6):
        position = (x, -145)
        t.goto(position)
        t.pendown()
        t.begin_fill()
        for i in range(6):
            t.lt(70)
            t.fd(10)
            t.rt(130)
            t.fd(15)
        t.end_fill()
        t.penup()
        x = x + 100


def drawseaweed(t, x, length, color):
    """
    draws seaweed using ocean
    """
    t.color(color)
    t.pensize(5)
    for i in range (3):
        position = (x, -178)
        t.goto(position)
        t.pendown()
        t.seth(60)
        for i in range(length):
            t.fd(15)
            t.lt(100)
            t.fd(15)
            t.rt(100)
        x = x + 15
        length = length - 1
        t.penup()


def make_text(t, txt):
    """
        Writes text to the screen.
    """
    t.color('navy')
    t.setpos(-100,180)
    t.write(txt, move=False, align='center', font=("Times New Roman", 20,))



def main():
    """
    creates screen and turtle objects. holds all the function calls
    """
    wn = turtle.Screen()
    wn.bgpic('ocean.gif')

    ocean = turtle.Turtle()
    ocean.speed(0)

    draw_fish(ocean)
    ocean.penup()
    ocean.goto(-70, -70)
    ocean.lt(45)
    ocean.pendown()
    draw_fish(ocean)
    draw_bubbles(ocean, 50, 70)
    draw_bubbles(ocean, 0, -20)
    drawstarfish(ocean)
    drawseaweed(ocean, 80, 5, 'DarkGreen')
    drawseaweed(ocean, 180, 5, 'green4')
    drawseaweed(ocean, -220, 7, 'green4')
    make_text (ocean, '"Just keep coding, just keep coding!"')

    wn.exitonclick()

main()