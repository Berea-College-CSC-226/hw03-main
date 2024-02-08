#################################################################################
# Author: Malak Mohamed
# Username: mohamedm
#
# Assignment: HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: exploring turtles
# Google Doc Link: https://docs.google.com/document/d/1y-CIy7MdTK91WeMf1-7qtPrdj9Rpr0n_j_vf17A3Qe8/edit?usp=sharing
#
# Acknowledgements: https://stackoverflow.com/questions/29441237/how-to-draw-a-semicircle-in-python-turtle-only  used for doing the pattern function
#
#################################################################################

import turtle


def drawRectangle(shape,x,y):
    """
    this function draws the buildings
    """
    shape.penup()
    shape.setpos(x, y)
    shape.pendown()
    shape.color('#EC3434')
    shape.begin_fill()
    for side in range(2):
        shape.forward(420)
        shape.right(90)
        shape.forward(600)
        shape.right(90)
    shape.end_fill()


def drawWindow(shape, x, y):
    """
    this function draws the windows
    """
    shape.penup()
    shape.setpos(x, y)
    shape.pendown()
    for i in range(7):
        shape.penup()
        shape.forward(50)
        shape.pendown()
        shape.color('#2911A2')
        shape.begin_fill()

        for side in range(2):
                shape.forward(30)
                shape.right(90)
                shape.forward(20)
                shape.right(90)
        shape.end_fill()


def drawDoor(shape, x, y):
    """
    this function draws the huge door
    """
    shape.penup()
    shape.setpos(x, y)
    shape.pendown()
    shape.color('#2911A2')
    shape.begin_fill()
    for side in range(2):
        shape.forward(320)
        shape.right(90)
        shape.forward(400)
        shape.right(90)
    shape.end_fill()


def drawText(shape, txt, x, y):
    """
    this function draws the text
    """
    shape.penup()
    shape.color("#070418")
    shape.setpos(x, y)
    shape.forward(130)
    shape.pendown()
    shape.write(txt, move=False, align='center', font=("Times New Roman", 70, ("bold", "normal")))


def pattern(shape):
    """
    this function the pattern at the end
    """
    shape.penup()
    shape.forward(700)
    shape.left(90)
    shape.forward(200)
    shape.pendown()
    for i in range(30):
        shape.circle(100, 180)
        shape.circle(100 // 2, 180)
        shape.forward(1)


def main():
    """
    this function calls other functions to run the code
    """
    turtle.colormode(255)

    wn = turtle.Screen()
    wn.bgcolor("#87E5E8")
    wn.bgpic("R (1).gif")
    malak = turtle.Turtle()
    tess = turtle.Turtle()
    malak.speed(0)
    tess.speed(0)
    tess.shape("turtle")
    malak.shape("turtle")
    drawRectangle(malak, 250, 300)
    drawRectangle(tess, -650, 300)
    drawWindow(malak, 250, 270)
    drawWindow(tess,-650,270)
    drawDoor(malak,280, 100)
    drawDoor(tess, -600, 100)
    drawText(malak,"company",290,150)
    drawText(malak, "Malak's", -600, 150)
    drawText(tess, "Gimme the money!!!", -80, -280)
    pattern(tess)
    wn.exitonclick()


main()