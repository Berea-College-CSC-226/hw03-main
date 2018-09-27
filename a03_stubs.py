#################################################################################
# Author: Austin Dunn
# Username: Dunn
# google document link: https://docs.google.com/document/d/1iwhNuP1GCuYYg9CxR7RsfQPheS2nBi-41BDC-BQh054/edit?usp=sharing
# Assignment: A03
# Purpose: Making a house
#################################################################################
# Acknowledgements:
#
#
#################################################################################
import turtle
wn = turtle.Screen()
wn.bgcolor('Black')

#draws a house on the screen
square = turtle.Turtle()

def function1():#Makes the base of the house
   square = turtle.Turtle()

square.color('blue')
square.begin_fill()
for side in range(2):
    square.forward(140)
    square.right(90)
    square.forward(160)
    square.right(90)
square.end_fill()

def function2():#makes the roof
    square.color('#ff0000')
square.begin_fill()
for side in range(3):
    square.forward(140)
    square.left(120)
square.end_fill()

def drawdoor(door): #makes a door
    door.penup()
    door.setpos(130,-100)
    door.pendown()
    door.color('#ff0000')
    door.begin_fill()
    for shape in range(2):
        door.forward(-50)
        door.left(90)
        door.forward(-60)
        door.left(90)
    door.end_fill()

def main():

    door = turtle.Turtle()

    function1()
    function2()
    drawdoor(door)
    wn.exitonclick()

main()
