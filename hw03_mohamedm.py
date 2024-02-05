#################################################################################
# Author: Malak Mohamed
# Username: mohamedm
#
# Assignment: HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: exploring turtles
# Google Doc Link: https://docs.google.com/document/d/1y-CIy7MdTK91WeMf1-7qtPrdj9Rpr0n_j_vf17A3Qe8/edit?usp=sharing
#
# Acknowledgements:
#
#################################################################################

import turtle

def drawRectangle(turtle,x,y):
    """
        this function draws the buildings
        """
    turtle.penup()
    turtle.setpos(x, y)
    turtle.pendown()
    turtle.color('hotpink')
    turtle.begin_fill()
    for side in range(2):
        turtle.forward(420)
        turtle.right(90)
        turtle.forward(600)
        turtle.right(90)
    turtle.end_fill()

def drawWindow(turtle, x, y):
    """
        this function draws the windows
        """
    turtle.penup()
    turtle.setpos(x, y)
    turtle.pendown()
    for i in range(7):
        turtle.penup()
        turtle.forward(50)
        turtle.pendown()
        turtle.color('purple')
        turtle.begin_fill()

        for side in range(2):
                turtle.forward(30)
                turtle.right(90)
                turtle.forward(20)
                turtle.right(90)
        turtle.end_fill()


def drawDoor(turtle,x,y):
    """
        this function draws the huge door
        """
    turtle.penup()
    turtle.setpos(x, y)
    turtle.pendown()
    turtle.color('purple')
    turtle.begin_fill()
    for side in range(2):
        turtle.forward(320)
        turtle.right(90)
        turtle.forward(400)
        turtle.right(90)
    turtle.end_fill()
def drawText(turtle, txt,x,y):
    """
        this function draws the text
        """
    turtle.penup()
    turtle.color("#A11551")
    turtle.setpos(x,y)
    turtle.forward(130)
    turtle.pendown()
    turtle.write(txt, move=False, align='center', font=("Times New Roman", 70, ("bold", "normal")))


def main():
    turtle.colormode(255)

    wn = turtle.Screen()
    wn.bgcolor("#FFE5FD")
    wn.bgpic("R.gif")
    malak = turtle.Turtle()
    tess = turtle.Turtle()
    malak.speed(0)
    tess.speed(0)
    tess.shape("turtle")
    malak.shape("turtle")
    drawRectangle(malak,250,300)
    drawRectangle(tess,-650,300)
    drawWindow(malak, 250, 270)
    drawWindow(tess,-650,270)
    drawDoor(malak,280, 100)
    drawDoor(tess, -600, 100)
    drawText(malak,"company",290,150)
    drawText(malak, "Malak's", -600, 150)
    drawText(tess, "Gimme the money!!!", -80, -280)
    wn.exitonclick()


main()