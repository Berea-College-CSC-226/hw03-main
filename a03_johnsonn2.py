#################################################################################
# Author: Yonnie
# Username: johnsonn2/yongningning(github)
#
# Assignment:a03
# Purpose: learning how to use branches and prevent merge conflicts
# Google Doc Link: https://docs.google.com/document/d/13b8f1wTfMEl2fzoRqzrwd5IkqCpHZVAUvNOBtM-U-E8/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle

def drawhouse(rua):
    """
    this drawhouse function will be used to draw squarish shapes
    """

    #setting rua up
    rua.penup()
    rua.goto(-150,100)
    rua.pendown()
    rua.begin_fill()
    rua.fillcolor("yellow")

    #this is the part where the square shape is drawn
    for i in range(4):
        rua.forward(300)
        rua.right(90)
    rua.end_fill()
    pass


def drawroof(rua):
    """
    this drawroof function will be used to draw triangular, roof-like shapes
    """

    # putting rua in the correct place that my drawings don't overlap
    rua.begin_fill()
    rua.fillcolor("red")
    rua.left(45)
    rua.forward(212)
    rua.right(90)
    rua.forward(212)
    rua.left(45)
    rua.end_fill()
    pass

def drawdoor(rua):
    """
    this drawdoor function will be used to draw rectangular, door-like shapes
    """

    #again just putting rua in the correct place and deciding her colors
    rua.penup()
    rua.goto(-100,-200)
    rua.left(90)
    rua.pendown()
    rua.begin_fill()
    rua.fillcolor((166/255, 154/255, 103/255))  #shoutout to ChatGPT for showing me this shortcut for using rgb values

    #drawing the door shape
    rua.forward(200)
    rua.right(90)
    rua.forward(90)
    rua.right(90)
    rua.forward(200)

    rua.end_fill()
def drawknob(rua):
    """
    this drawknob function will be used to draw circular, doorknob-like shapes
    """
    rua.penup()
    rua.goto(-40,-120)
    rua.pendown()
    rua.begin_fill()
    rua.fillcolor("orange")
    rua.circle(10)
    rua.end_fill()

    pass


def main():
    """
    this function contains all neccessary attributes for the turtle Rúa and the screen she exists in.
    this also contains all the unrelated functions to be 'called' on
    """
    #creating Rúa and her environment
    screen = turtle.Screen()
    rua = turtle.Turtle()
    rua.pensize(4)
    rua.pencolor("black")
    rua.speed(8)
    screen.bgcolor("#B2E8E2")   #shoutout to ChatGPT again for showing me yet another shortcut for using hex codes

    #the functions i'm using
    drawhouse(rua)
    drawroof(rua)
    drawdoor(rua)
    drawknob(rua)

    screen.exitonclick()

main()


