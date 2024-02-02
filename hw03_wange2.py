# Name: Eun Sung Wang
# Username: wange2
# Google Doc: https://docs.google.com/document/d/1jl7uXjys2F0Tu1IFPvjZcEspKPECxvctfCDyoPJD6h8/edit?usp=sharing

import turtle

def drawBase(eunsung):            #Function to draw the base of the house
    eunsung.pencolor("#FFF55A")
    eunsung.pensize(5)
    eunsung.penup()
    eunsung.goto(-20,-240)
    eunsung.pendown()
    for i in range(4):            #Making square foundation for the house
        eunsung.forward(130)
        eunsung.left(90)
        eunsung.forward(100)

def drawRoof(eunsung):         #Making a roof
    eunsung.pencolor("#405AC6")
    eunsung.pensize(5)
    eunsung.penup()
    eunsung.goto(-156,-3)
    eunsung.pendown()
    for i in range(3):       #Loop for a triangular roof
        eunsung.forward(300)
        eunsung.left(120)

def drawDoor(eunsung,w,h):   #Making a door
    eunsung.pencolor('orange')
    eunsung.penup()
    eunsung.goto(-44,-235)
    eunsung.pendown()
    for i in range(2):      #Making a rectangular door
        eunsung.forward(w)
        eunsung.left(90)
        eunsung.forward(h)
        eunsung.left(90)
    eunsung.penup()         #Making a door handle using drawDoor function
    eunsung.goto(-22,-180)
    eunsung.pendown()
    eunsung.circle(10)

def drawRoofWin(eunsung):      #Making a roof window
    eunsung.pencolor("#A169B9")
    eunsung.penup()
    eunsung.goto(-5,40)
    eunsung.pendown()
    eunsung.circle(50)         #Creating a circle window
    eunsung.penup()
    eunsung.goto(0,90)
    eunsung.pendown()
    eunsung.forward(40)        #Making a frame for the circular window
    eunsung.forward(-90)
    eunsung.forward(45)
    eunsung.right(90)
    eunsung.forward(50)
    eunsung.forward(-100)

def main():
    wn = turtle.Screen()
    wn.bgcolor("#26C350")
    eunsung = turtle.Turtle()
    eunsung.hideturtle()

    # Function calls to drawBase and drawRoof
    drawBase(eunsung)
    drawRoof(eunsung)
    drawDoor(eunsung,90,140)
    drawRoofWin(eunsung)
    wn.exitonclick()


main()  # Starts the program!