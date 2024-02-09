
# TODO Do not edit this file directly! Instead, create a new file called
#        hw03_username.py and copy this code into it!

#################################################################################
# Author: DieuMerci Nshizirungu
# Username: nshizirungud
#
# Assignment: HW03
# Purpose: use of functions
# Google Doc Link:https://docs.google.com/document/d/1m23K6hlgA8TN49LO0zYzClcpq-a_XaZsNUA405dDUDU/edit?usp=sharing
#
#################################################################################
# Acknowledgements: Bishal Timalsina(TA)
#
#
#################################################################################

import turtle

def draw_building(merci):
    """This function is used to draw buildings"""
    merci.color("purple")

    merci.begin_fill()
    merci.forward(200)
    merci.left(90)
    merci.forward(150)
    merci.left(90)
    merci.forward(200)
    merci.left(90)
    merci.forward(150)
    merci.end_fill()


def draw_windows(merci):
    """This function draws windows """
    merci.color("yellow")

    for _ in range(1):
        merci.penup()
        merci.goto(60,100)
        merci.pendown()
        merci.begin_fill()
        for _ in range(4):
            merci.forward(40)
            merci.right(90)
        merci.end_fill()
        merci.penup()
        merci.goto(160,100)
        merci.pendown()
        merci.begin_fill()
        for _ in range(4):
            merci.forward(40)
            merci.right(90)
        merci.end_fill()
        merci.penup()


def draw_door(merci):
    """
    This function draws door
    """

    merci.color("pink")
    merci.goto(120,60)
    merci.pendown()
    merci.begin_fill()
    for _ in range(4):
        merci.forward(60)
        merci.right(90)
    merci.end_fill()

def draw_bushes(merci):
    """
    This function draws bushes
    """
    merci.color("green")
    merci.penup()
    merci.goto(-200,-150)
    merci.pendown()
    merci.begin_fill()
    merci.circle(30)
    merci.end_fill()
    merci.goto(-150,-150)
    merci.begin_fill()
    merci.circle(30)
    merci.end_fill()

def draw_roof(merci):
    """
    This function will draw a roof
    """
    merci.penup()
    merci.goto(0,148)

    merci.pendown()
    merci.begin_fill()
    merci.left(135)
    merci.forward(100)
    merci.right(45)
    merci.forward(75)
    merci.right(54.80)
    merci.forward(80)
    merci.end_fill()
def main():
    wn = turtle.Screen()
    wn.bgcolor("red")

    merci = turtle.Turtle()       # create turtle object

    merci.speed(0)

    draw_building(merci)                 # draws the building

    draw_windows(merci)                  # draws windows on the building



    draw_door(merci)


    draw_bushes(merci)                    # draw trees
    draw_roof(merci)

    merci.hideturtle()
    merci.penup()
    merci.goto(340,100)
    merci.pendown()
    merci.write("This is my house")

    wn.exitonclick()



main()  # Starts the program!