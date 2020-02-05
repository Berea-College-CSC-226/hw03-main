#################################################################################
# Author: Brandon Atu
# Username: Atu175
#
# Assignment: A03
# Purpose: Making branches
# Google Doc Link: https://docs.google.com/document/d/1c5eu4vL2XOw1urT8wXGVSEBSlOtsq3Ih0KEi_JZgfmU/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle

turt = turtle.Turtle()


def main():
    """
    Docstring for main
    """
    # ...
    wn = turtle.Screen()
    wn.bgcolor('grey')
    head = 0
    turt.pensize(5)
    build_body(turt)
    draw_door(turt)
    draw_window(turt)
    draw_roof(turt)
    wn.exitonclick()





def draw_roof(turt):
    turt.penup()
    turt.goto(-150, 100)
    turt.pendown()
    turt.left(60)
    turt.forward(150)
    turt.left(-60)
    turt.forward(150)
    turt.left(-60)
    turt.forward(150)


def draw_window(turt):
    turt.penup()
    turt.goto(55, 40)
    turt.pendown()
    turt.left(90)
    for i in range(4):
        turt.forward(50)
        turt.left(90)


def draw_door(turt):
    turt.penup()
    turt.forward(120)
    turt.pendown()
    turt.left(90)
    turt.forward(90)
    turt.right(90)
    turt.forward(60)
    turt.right(90)
    turt.forward(90)


def build_body(turt):
    turt.penup()
    turt.goto(-150, -100)
    turt.pendown()
    for i in range(2):
        turt.forward(300)
        turt.left(90)
        turt.forward(200)
        turt.left(90)


main()



