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
# provided with t03 assignment
#
#
#################################################################################
import turtle


def draw_fish(t):
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
    """
    draws orange and pink fish using ocean
    """

def draw_fish_2(t):
    t.penup()
    t.goto(-70,-70)
    t.lt(45)
    t.pendown()
    draw_fish(t)
    """
    draws second fish using ocean
    """

def draw_bubbles(t):
    x = 50
    y = 70
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
    ''' draws bubbles using ocean
    '''

def draw_bubbles2(t):
    x = 0
    y = -20
    position = (x, y)
    t.penup()
    t.goto(position)
    t.pendown()
    for i in range(5):
        t.dot(15, 'navy')
        t.penup()
        x = x - 20
        y = y + 15
        t.goto(x, y)
    ''' draws bubbles using ocean
    '''

def drawstarfish(t):
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
    ''' draws a row of starfish using turtles
    '''

def drawseaweed(t):
    t.color('DarkGreen')
    t.pensize(5)
    x = 80
    length = 5
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

def drawseaweed2(t):
    t.color('green4')
    t.pensize(5)
    x = 180
    length = 5
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

def drawseaweed3(t):
    t.color('green4')
    t.pensize(5)
    x = - 220
    length = 7
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
    t.color('navy')
    t.setpos(-100,180)
    t.write(txt, move=False, align='center', font=("Times New Roman", 20,))
    """
    Writes text to the screen.
    """


def main():
    wn = turtle.Screen()
    wn.bgpic('ocean.gif')

    ocean = turtle.Turtle()
    ocean.speed(0)

    """
    creates a screen object and a turtle object to make ocean artwork
    """

    draw_fish(ocean)
    draw_fish_2(ocean)
    draw_bubbles(ocean)
    draw_bubbles2(ocean)
    drawstarfish(ocean)
    drawseaweed(ocean)
    drawseaweed2(ocean)
    drawseaweed3(ocean)
    make_text (ocean, '"Just keep coding, just keep coding!"')

    wn.exitonclick()

main()  # Starts the program!