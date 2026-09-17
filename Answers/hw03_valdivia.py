#################################################################################
# Author:Adrian Valdivia
# Username: Valdivia
#
# Assignment: HW03
# Purpose: Turtle drawing
# Google Doc Link:https://docs.google.com/document/d/1avDIaI_vXNeZpUOLWRCDWST3CjX3gdANEbaxNMM-iUo/edit?tab=t.0
#
#################################################################################

import turtle
def draw_tree():
    """""
    draws a simple tree
    """""

    turtle.color("brown")
    turtle.begin_fill()

    for i in range(2):
         turtle.forward(40)
         turtle.left(90)
         turtle.forward(100)
         turtle.left(90)

    turtle.end_fill()

    turtle.penup()
    turtle.goto(20,100)
    turtle.pendown()

    turtle.color(115,134,120)
    turtle.begin_fill()
    turtle.circle(60)
    turtle.end_fill()

def draw_house():
    """""
    draws simple house
    """""

    turtle.penup()
    turtle.goto(-200,0)
    turtle.pendown()

#draws the house body
    turtle.color("tan")
    turtle.begin_fill()

    for i in range (4):
        turtle.forward(150)
        turtle.left(90)

    turtle.end_fill()

    turtle.penup()
    turtle.goto(-200, 150)
    turtle.pendown()

    turtle.color("red")
    turtle.begin_fill()

    turtle.goto(-125, 225)
    turtle.goto(-50, 150)
    turtle.goto(-200, 150)
    turtle.end_fill()

def main():
    """""
    draws the full scene
    """""
    screen = turtle.Screen()
    screen.colormode(255)
    screen.bgcolor("lightblue")

    draw_tree()
    draw_house()
    turtle.done()


main()

