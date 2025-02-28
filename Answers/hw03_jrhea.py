#################################################################################
# Author: Jaron Rhea
# Username: jrhea
#
# Assignment:
# Purpose:
# Google Doc Link: https://docs.google.com/document/d/1XOrAD93BrASoKCDR1KJQMptN25PuiVSdCkeXo4dkEvY/edit?tab=t.0
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################

from turtle import *

def house(turtle):
    """
        this function will draw a house
    """
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(140)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(140)
    turtle.right(90)
    turtle.forward(100)

    turtle.backward(100)
    turtle.left(45)
    turtle.forward(142)
    turtle.right(90)
    turtle.forward(142)





def house_detail(turtle1):
    """
    this function will draw the details of the house
    """

    turtle1.penup()
    turtle1.goto(-70,-110 )
    turtle1.pendown()

    for i in range(2):
        turtle1.forward(20)
        turtle1.left(90)
        turtle1.forward(30)
        turtle1.left(90)

    turtle1.forward(10)
    turtle1.left(90)
    turtle1.forward(30)
    turtle1.left(90)
    turtle1.penup()
    turtle1.goto(-70,-110)
    turtle1.right(180)
    turtle1.pendown()
    turtle1.left(90)
    turtle1.forward(15)
    turtle1.right(90)
    turtle1.forward(20)

    turtle1.penup()
    turtle1.goto(50,-110)
    turtle1.pendown()


    for i in range(2):
        turtle1.forward(20)
        turtle1.left(90)
        turtle1.forward(30)
        turtle1.left(90)

    turtle1.forward(10)
    turtle1.left(90)
    turtle1.forward(30)
    turtle1.left(90)
    turtle1.penup()
    turtle1.goto(50, -110)
    turtle1.right(180)
    turtle1.pendown()
    turtle1.left(90)
    turtle1.forward(15)
    turtle1.right(90)
    turtle1.forward(20)
    turtle1.penup()
    turtle1.goto(-15,-140)
    turtle1.pendown()
    turtle1.left(90)
    turtle1.forward(50)
    turtle1.right(90)
    turtle1.forward(30)
    turtle1.right(90)
    turtle1.forward(50)
    turtle1.penup()
    turtle1.goto(7,-120)
    turtle1.pendown()
    turtle1.circle(2)



def main():
    """
    this function calls the functions that draw the house
    """

    # Function calls to function_1 and function_2.
    wn = Screen()
    wn.bgcolor("Teal")

    turtle = Turtle()
    turtle1 = Turtle()
    turtle.hideturtle()
    turtle1.hideturtle()


    house(turtle)
    house_detail(turtle1)
    wn.exitonclick()


main() # Starts the program!


