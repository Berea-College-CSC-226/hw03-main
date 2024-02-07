#################################################################################
# Author: Juno Smith
# Username: smithj
#
# Assignment: Hw03
# Purpose: HW
# Google Doc Link:https://docs.google.com/document/d/12MjBFSdEOX1sSblb_gTghHuoPa7JGxCLgrh2dcQSNbs/edit
#
#################################################################################
# Acknowledgements:
# Happy meal
###############################

import turtle

def drawsquare(JK):     ##Draws House
    """
    Drawing the Square Turtle
    """
    JK.color('red')
    JK.pensize(20)
    JK.penup()
    JK.goto(-300,-300)
    JK.pendown()

    for i in range(4):
        JK.forward(250)
        JK.left(90)

def drawTriangle(JK): ## this is the roof
    """
        Drawing the roof Turtle
        """
    ##Draws roof
    JK.pencolor(255,199,44)
    JK.pensize(25)
    JK.penup()
    JK.goto(-335,-55)
    JK.pendown()

    for i in range(2):
        JK.right(-45)
        JK.forward(230)
        JK.right(135)

def drawsign(JK):       ##Draws "M" in MC donalads sign
    """
        Drawing the M in McDonalds sign
        """
    JK.penup()
    JK.pensize(10)
    JK.goto(-220,-220)

    JK.forward(20)
    JK.pendown()

    for i in range (2):
        JK.right(90)
        JK.forward(100)
        JK.right(90)
        JK.forward(40)
        JK.right(90)
        JK.forward(100)
        JK.right(90)

def drawletterC(JK):        ##Draws "c" in MC sign

    """ Drawing the c in McDonalds sign """
    JK.penup()
    JK.goto(-150,-220)
    JK.pendown()

    JK.forward(-60) ## path for c
    JK.forward(60)
    JK.right(90)
    JK.forward(75)
    JK.right(90)
    JK.forward(60)
def main(): #sets up main
    # import turtle
    turtle.colormode(255)
    wn = turtle.Screen()
    wn.bgcolor("light blue")
    JK= turtle.Turtle()
    JK.hideturtle()
    JK.speed(4)

    drawsquare(JK)  # call to function_1    House
    drawTriangle(JK)  # call to function_2
    drawsign(JK) #call Function 3 letter M
    drawletterC(JK)      #draw function 4 letter c
    wn.exitonclick()

main()      ##Invoke Main