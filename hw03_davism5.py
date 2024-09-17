#################################################################################
# Author: Mauricha Davis
# Username: davism5
#
# Assignment: HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose:
# Google Doc Link: https://docs.google.com/document/d/1GffD-r3WjBjP_JdkNARFkIGOf5sZ6pIk-gUKqU8K7fQ/edit?usp=sharing
#
#################################################################################

import turtle

def house(t):
    for i in range(4):
        t.forward(200)
        t.left(90)
    return t

def roof(t):
    for i in range(3):
         t.forward(100)
         t.left(120)
    return t

def create_turtle(pensize, color):
    t_turtle=turtle.Turtle()
    t_turtle.pensize(pensize)
    t_turtle.color(color)
    return t_turtle


def main():
    wn=turtle.Screen()
    wn.screensize(canvwidth=600, canvheight=600)

    t_house= create_turtle(pensize=10, color="red")
    t_house.penup()
    t_house.setposition(-250, -250)
    t_house.pendown()

    wn.exitonclick()

main()









