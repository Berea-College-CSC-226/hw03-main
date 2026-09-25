#################################################################################
# Author: Gabriella Sloboh
# Username: slobohg
#
# Assignment: Hw03
# Purpose: to create a super duper special drawing
# Google Doc Link: https://docs.google.com/document/d/1bh_7HIPla6nbC4aN7mdhIksBKHLJJTHKEVZhdJLSu3Y/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#Help from textbook, google for the font size, and Scott Heggans coding from
#previous assignments
#
#
#################################################################################


import turtle

import time


wn = turtle.Screen()

def make_ken(ken):
    """
    creation of my turtle, ken, window edits, and positioning.
    """
    wn.colormode(255)
    wn.bgcolor(107, 255, 102)
    ken.shape("turtle")
    ken.color("light pink")
    ken.penup()
    ken.goto(-325, -100)

def make_table(ken):
    """
    This is the code for ken to make a dining room table!
    """

    ken.color(165, 104, 42)
    ken.pendown()
    ken.pensize(17)
    ken.begin_fill()
    for side in range(4):
        ken.forward(645)
        ken.right(90)
        ken.forward(15)
    ken.end_fill()

def operation_make_cake(ken):
    """
    This is where I begin the layers for the birthday cake!
     """
    ken.penup()
    ken.color("AntiqueWhite")
    ken.goto(-280, -80)

    ken.pen("AntiqueWhite")
    ken.begin_fill()
    ####first layer

    ken.forward(500)
    ken.right(90)
    ken.forward(100)
    ken.right(90)
    ken.forward(500)
    ken.right(90)
    ken.forward(95)
    ken.end_fill()



def second_layer(ken):

    #second layer of bday cake
    ken.penup()
    ken.goto(-280, -80)
    ken.color("AntiqueWhite")
    ken.pendown()
    ken.begin_fill()
    ken.right(90)
    ken.forward(80)
    ken.pendown()
    ken.left(90)
    ken.forward(75)
    ken.right(90)
    ken.forward(340)
    ken.right(90)
    ken.forward(75)
    ken.right(90)
    ken.forward(340)
    ken.end_fill()
    ken.speed(5)
    ken.goto(-280, -80)
    ken.color("hotpink")
    ken.pendown()
    ken.right(90)



def icing(ken):
#first round of icing for first layer
    ken.right(180)
    ken.forward(55)
    ken.right(180)
    ken.forward(56)
    for i in range(4):
        ken.right(90)
        ken.forward(50)
        ken.right(90)
        ken.forward(55)
        ken.left(180)
        ken.forward(54)
        ken.right(90)
        ken.forward(75)
        ken.right(90)
        ken.forward(75)
        ken.left(180)
        ken.forward(75)


def third_layer(ken):
#this is the third layer of the cake
    ken.penup()
    ken.color("AntiqueWhite")
    ken.goto(-200, 1)
    ken.begin_fill()
    ken.right(90)
    ken.forward(45)
    ken.pendown()
    ken.left(90)
    ken.forward(75)
    ken.right(90)
    ken.forward(250)
    ken.right(90)
    ken.forward(75)
    ken.right(90)
    ken.forward(250)
    ken.end_fill()
    ken.speed(5)
    ken.end_fill()

#this is the icing for the second layer
    ken.penup()
    ken.color("hotpink")
    ken.goto(-200, -5)
    ken.pendown()
    ken.left(90)
    ken.forward(45)
    ken.right(180)
    ken.forward(45)
    ken.right(90)

    ken.forward(50)

    ken.right(90)
    ken.forward(50)
    ken.left(180)
    ken.forward(45)
    for i in range(3):
        ken.right(90)
        ken.forward(75)
        ken.right(90)
        ken.forward(45)
        ken.left(180)
        ken.forward(43)
        ken.right(180)
        ken.forward(43)
        ken.right(180)
        ken.forward(45)

    ken.right(90)
    ken.forward(75)
    ken.right(90)
    ken.forward(45)

def last_icing(ken):
#icing for the third layer!
    ken.penup()
    ken.color("hotpink")
    ken.goto(-160, 1)
    ken.right(180)
    ken.forward(25)
    ken.pendown()
    ken.forward(50)

    for i in range(3):
        ken.right(90)
        ken.forward(75)
        ken.right(90)
        ken.forward(45)
        ken.left(180)
        ken.forward(43)
        ken.right(180)
        ken.forward(43)
        ken.right(180)
        ken.forward(45)

    ken.right(90)
    ken.forward(35)
    ken.right(90)
    ken.forward(55)

def candles(ken):
    ken.color("blue")
#creating of 4 candles with stamps as the fire!
    ken.penup()
    ken.goto(-160, 90)
    ken.right(180)
    ken.pendown()
    ken.color(255, 165, 0)
    ken.forward(35)
    ken.color(255, 128, 0)
    ken.stamp()

    ken.penup()
    ken.goto(-77, 90)
    ken.pendown()
    ken.color(255, 165, 0)
    ken.forward(35)
    ken.color(255, 128, 0)
    ken.stamp()

    ken.penup()
    ken.goto(6, 90)
    ken.pendown()
    ken.color(255, 165, 0)
    ken.forward(35)
    ken.color(255, 128, 0)
    ken.stamp()

    ken.penup()
    ken.goto(89, 90)
    ken.pendown()
    ken.color(255, 165, 0)
    ken.forward(35)
    ken.color(255, 128, 0)
    ken.stamp()

def happy(ken):
#andddd the happy birthday sign!
    ken.penup()
    ken.goto(-80, 150)
    ken.color(0, 0, 128)
    ken.write("HAPPY BIRTHDAY <3!!", move=False, align='center', font=("Arial", 24, "normal"))

def main():
    """
    to call all of my functions unanimously that create an awesome birthday cake!
    """

    ken = turtle.Turtle()

    ken.speed(10)
    make_ken(ken)
    ken.speed(10)
    make_table(ken)
    ken.speed(10)
    operation_make_cake(ken)
    ken.speed(10)
    second_layer(ken)
    ken.speed(10)
    icing(ken)
    ken.speed(10)
    third_layer(ken)
    ken.speed(10)
    last_icing(ken)
    ken.speed(10)
    candles(ken)
    ken.speed(10)
    happy(ken)



main()

wn.exitonclick()