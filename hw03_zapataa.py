#################################################################################
# Author: Adolfo Zapata
# Username: zapataa
#
# Assignment: HW03
# Purpose: To practice creating and using functions, as well as learning more about Git.
# Google Doc Link:https://docs.google.com/document/d/15uYuTgh3gVOGoLn4trDeNj0eJUxllHVtLXcHX9tawog/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
# https://docs.python.org/3/library/turtle.html
#
#################################################################################

import turtle


def drawHouse(t):
    """
    Draw house with turtle including roof
    """
    t.fillcolor("black")
    t.begin_fill()          # begins to draw House (square)
    for i in range(4):
        t.forward(85)
        t.right(90)
    t.end_fill()
    t.fillcolor("red")      # begins to draw roof
    t.begin_fill()
    t.left(180)
    t.forward(10)
    t.right(145)
    t.forward(70)
    t.right(75)
    t.forward(65)
    t.end_fill()


def drawDoor(t):
    """
    draw Door to house
    """
    t.penup()
    t.goto(30, -33)
    t.pendown()
    t.fillcolor("brown")
    t.begin_fill()
    t.setheading(0)
    t.right(90)
    t.forward(50)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(30)
    t.end_fill()


def drawDoorKnob(t):
    """
    Draw a doorknob on the door to house
    """
    t.penup()
    t.goto(55, -55)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    t.circle(3)
    t.end_fill()


def addText(t):
    """
    Draw "Adolfo's House" above the house
    """
    t.penup()
    t.goto(-40, 35)
    t.pendown()
    t.write("Adolfo's House", font=("Times New Roman", 20, "bold"))


def drawStickPerson(t):
    """
        Draw a stick person figure beside the House
    """
    t.pensize(3)
    t.penup()
    t.goto(150, -30)
    t.pendown()
    t.pencolor(100/255, 167/255, 255/255)
    t.circle(10)                # draws head to body of stick figure
    t.penup()
    t.goto(150, -50)
    t.pendown()
    t.left(90)                  # draws body of stick figure
    t.forward(40)
    t.penup()
    t.goto(150, -60)
    t.pendown()
    t.left(45)             # draws right arm
    t.forward(15)
    t.penup()
    t.goto(150, -60)
    t.pendown()
    t.right(90)             # draws left arm
    t.forward(15)
    t.penup()
    t.goto(150, -90)
    t.pendown()
    t.left(90)              # draws right leg
    t.forward(15)
    t.penup()
    t.goto(150, -90)
    t.pendown()
    t.right(90)             # draws left leg
    t.forward(15)
    t.penup()
    t.goto(200, 100)        # moves turtle away from stick figure


def main():
    """
    Run all functions created to draw a house with a roof and door, as well as a stick figure beside the house.
    """
    wn = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    wn.bgcolor("lightblue")
    # Function calls.
    drawHouse(t)
    drawDoor(t)
    drawDoorKnob(t)
    addText(t)
    drawStickPerson(t)
    wn.exitonclick()


main()  # Starts the program!
