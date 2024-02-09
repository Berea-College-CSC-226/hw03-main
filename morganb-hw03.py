#################################################################################
# Author: Baella Morgan
# Username:morganb
#
# Assignment:Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose:Continue practicing functions and using the turtle library.
# Google Doc Link:https://docs.google.com/document/d/1NjbTxTAXg0Cuo1YH1nipYNSgiDWNQ2J3X0UAzkHL87w/edit?usp=sharing
#
#################################################################################
# Acknowledgements: turtle documentation page, geeksforgeeks.org, and Ruben Quinonez for help with the arch loop and troubleshooting.
#
#
#################################################################################

import turtle


def edoras(middlearth):
    """
        This is the basic outline of the building.
    """
    middlearth.left(30)
    middlearth.forward(30)
    middlearth.left(60)
    middlearth.forward(60)
    middlearth.right(90)
    middlearth.forward(70)
    middlearth.right(90)
    middlearth.forward(60)
    middlearth.right(90)
    middlearth.forward(70)
    middlearth.left(30)
    middlearth.forward(40)
    middlearth.right(120)
    middlearth.forward(80)
    middlearth.right(90)
    middlearth.forward(100)
    middlearth.left(30)
    middlearth.forward(150)
    middlearth.right(120)
    middlearth.forward(120)
    middlearth.right(40)
    middlearth.goto(95.98, -145)
    middlearth.right(140)
    middlearth.forward(60)
    middlearth.left(90)
    middlearth.forward(300)
    middlearth.left(70)
    middlearth.forward(70)
    middlearth.goto(0, -160)
    middlearth.right(160)
    middlearth.forward(230)
    middlearth.right(90)
    middlearth.forward(220)
    middlearth.right(90)
    middlearth.forward(90)
    middlearth.left(180)
    middlearth.forward(90)
    middlearth.left(90)
    middlearth.forward(425)
    middlearth.left(90)
    middlearth.forward(150)
    middlearth.right(180)
    middlearth.forward(150)
    middlearth.left(130)
    middlearth.forward(30)
    middlearth.right(180)
    middlearth.forward(180)
    middlearth.right(87)
    middlearth.forward(150)
    middlearth.left(180)
    middlearth.forward(150)
    middlearth.right(150)
    middlearth.forward(300)



def arches(t):
    """
           This is the function to create the arches for the front of the hall.
       """
    t.penup()
    t.goto(-40,-85)
    t.left(105)
    t.pendown()
    for i in range(3):
        t.forward(70)
        t.circle(20,180)
        t.forward(70)
        t.right(90)
        t.forward(20)
        t.right(90)

    """
    
    """
    pass
    # ...


def main():
    """

    """
    rohan = turtle.Screen()
    turtle.turtles()
    theoden = turtle.Turtle()
    theoden.shape("turtle")
    rohan.colormode(255)
    rohan.bgcolor("gray")
    theoden.color(39, 76, 31)
    theoden.speed(3)
    theoden.penup()
    theoden.setpos(0, -160)
    theoden.pendown()
    # Function calls to function_1 and function_2.
    edoras(theoden)
    arches(theoden)

    rohan.exitonclick()

main()

