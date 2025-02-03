#################################################################################
# Author: Dayton Conwell
# Username:conwelld
#
# Assignment:HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose:to draw a unique object
# Google Doc Link:https://docs.google.com/document/d/16yg3ch82DAR6bArUB5gwlDlm5b43f2yEVE2Y9IcKr5g/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
# Professor Scott Hegen
#
#################################################################################

import turtle

wn = turtle.Screen() #initialize screen window
wn.bgcolor('grey') #sets bg color to gray
turtle.colormode(255) #allows for rgb values to be input for color

def foundation(base):
    base.goto(0,-200)
    base.fillcolor('black')
    base.begin_fill()
    for i in range(4): #makes the base of the house and fills it black
        base.forward(100)
        base.left(90)
        base.forward(100)
    base.end_fill()

def roof(base):
    base.penup()
    base.goto((-100.00,0.00)) #draws the shape of the roof (triangle) and fills it black
    base.pendown()
    base.left(45)
    base.fillcolor('black')
    base.begin_fill()
    base.forward(142)
    base.right(90)
    base.forward(142)
    base.end_fill()
def window(base):
    base.pencolor('white') #makes the window shapes and fills them whwite
    base.penup()
    base.goto(-80,-40)
    base.pendown()
    base.right(45)
    base.fillcolor('white')
    square(base)
    base.penup()
    base.goto(20,-40)
    base.pendown()
    square(base)

def square(base):
    base.begin_fill()
    for i in range(4): # a function for making square shapes
        base.forward(40)
        base.left(90)
        base.forward(20)
    base.end_fill()
def door(base):
    base.penup()
    base.goto(-25, -130) #makes the door shape
    base.pendown()
    base.begin_fill()
    base.forward(72)
    base.left(180)
    base.forward(72)
    base.right(90)
    base.forward(50)
    base.right(90)
    base.forward(72)
    base.right(90)
    base.forward(50)
    base.end_fill()
    base.hideturtle()

def moon(base):
    base.penup()
    base.goto(-280, 100) #the function for making the moon and making it yellow
    base.right(150)
    base.pendown()
    base.pencolor('yellow')
    base.fillcolor('yellow')
    base.begin_fill()
    base.circle(100)
    base.end_fill()
def road(base):
    base.penup()
    base.goto(-100, -200) #makes the road shape and fills it an unnamed color
    base.pendown()
    base.color((155,147,94))
    base.right(180)
    base.begin_fill()
    base.forward(130)
    base.left(150)
    base.forward(380)
    base.left(135)
    base.forward(90)
    base.left(45)
    base.forward(200)
    base.end_fill()

def main():
    screen = turtle.Screen()
    base = turtle.Turtle()
    base.speed('fastest')
    foundation(base) #uses all oof the functions
    roof(base)
    window(base)
    door(base)
    moon(base)
    road(base)

main()

wn.exitonclick()



