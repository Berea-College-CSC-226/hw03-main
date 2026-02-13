#################################################################################
# Author:   Daniel Rukwasha
# Username:rukwashai
#
# Assignment:hm003
# Purpose:Fully Functional Gitty Psychedelic Robotic Turtles
# Google Doc Link:https://docs.google.com/document/d/1qerRtPi3EMTcMuRWiiZvx7bcrKqj_BnofJ4Sg2V1Zac/edit?usp=sharing
#
#################################################################################
# Acknowledgements:

import turtle

def rectangle(alex):
    """
    This function basically create a rectangle
    """
    for i in range(2):
        alex.forward(1000)
        alex.left(90)
        alex.forward(500)
        alex.left(90)


def house(alex):
    """
    THis function create a small house in the corner
    """
    alex.penup()
    alex.forward(30)
    alex.left(90)
    alex.forward(400)
    alex.right(90)
    alex.pendown()

    alex.forward(50)
    alex.left(90)
    for ka in range(4):
        alex.forward(25)
        alex.left(60)

def simba(alex):
    """This function help to draw a god figure"""
    alex.penup()
    alex.forward(200)
    alex.left(90)
    alex.right(40)
    alex.pendown()
    for lig in range(6):
        alex.forward(30)
        alex.left(60)
    alex.left(200)
    alex.forward(150)
    alex.left(140)
    alex.forward(30)
    alex.left(45)
    alex.forward(100)
    alex.right(45)
    alex.forward(20)
    alex.right(120)
    alex.forward(70)
    alex.left(90)
    alex.forward(20)
    alex.left(90)
    alex.forward(50)
    alex.right(60)
    alex.forward(200)
    alex.right(30)
    alex.right(45)
    alex.forward(50)
    alex.left(90)
    alex.forward(20)
    alex.left(80)
    alex.forward(110)
    alex.left(80)
    alex.forward(200)
    turtle.color("black", "red")
    turtle.begin_fill()
    turtle.circle(80)
    turtle.end_fill()


def main():
    alex = turtle.Turtle()
    wn=turtle.Screen()
    turtle.bgcolor("green")

    alex.penup()
    alex.forward(-550)
    alex.right(90)
    alex.penup()
    alex.forward(200)
    alex.left(90)
    alex.pendown()
    rectangle(alex)
    house(alex)
    simba(alex)
    alex.speed(0)
    wn.exitonclick()

main()



