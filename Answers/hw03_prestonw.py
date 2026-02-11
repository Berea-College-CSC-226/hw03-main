#################################################################################
# Author: Preston Worrix
# Username: PrestonW
#
# Assignment: Hw03
# Purpose:
# Google Doc Link: https://docs.google.com/document/d/1wp-QNkUn3xx7g0dSDVIFPG55qqMa7v1_PquHjwZZhhc/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################


import turtle


def pig_start(turt):
    turt.speed()
    turt.penup()
    turt.forward(1)
    turt.forward(40)
    turt.forward(1)
    turt.color("black")
    turt.forward(40)
    turt.left(90)
    turt.pensize(3)


def pig_2(turt):
    turt.penup()
    turt.forward(120)
    turt.left(90)
    turt.forward(1)
    turt.forward(120)
    turt.forward(1)
    turt.left(90)
    turt.forward(60)
    turt.left(90)
    turt.forward(60)
    turt.pensize(3)
    turt.left(90)
    turt.forward(120)
    turt.left(90)
    turt.pendown()
    turt.color("black")
    turt.fillcolor(255,0,255)
    turt.begin_fill()
    for i in range(360):
        turt.forward(3)
        turt.left(1)
    turt.end_fill()

def pig_3(turt):
    turt.penup()
    for i in range(30):
        turt.forward(3)
        turt.left(1)
    turt.right(90)
    turt.pendown()
    turt.fillcolor(255,0,255)
    turt.begin_fill()
    for i in range(215):
        turt.forward(1)
        turt.left(1)
    turt.end_fill()
    turt.penup()
    turt.left(90)
    for i in range(90):
        turt.forward(3)
        turt.right(1)
    turt.forward(3)
    turt.pendown()
    turt.left(90)
    turt.begin_fill()
    for i in range(220):
        turt.forward(1)
        turt.right(1)
    turt.end_fill()
def pig_4(turt):
    turt.teleport(0,0)
    turt.left(65)
    turt.teleport(0,0)
    turt.speed()
    turt.penup()
    turt.forward(1)
    turt.forward(40)
    turt.forward(1)
    turt.color("black")
    turt.forward(40)
    turt.pendown()
    turt.left(90)
    turt.pensize(3)
    turt.fillcolor(255,0,255)
    turt.begin_fill()
    for i in range(180):
        turt.left(2)
        turt.forward(2)
    turt.end_fill()

def pig_5(turt):
    turt.teleport(0,0)
    turt.left(155)
    turt.color("black")
    turt.pensize(20)
    turt.forward(1)
    turt.penup()
    turt.forward(40)
    turt.pendown()
    turt.forward(1)
    turt.penup()
    turt.forward(40)
    turt.left(90)
    turt.pendown()
    turt.pensize(3)
    for i in range(180):
        turt.left(2)
        turt.forward(2)
    turt.penup()
    turt.forward(120)
    turt.color("black")
    turt.left(90)
    turt.pendown()
    turt.pensize(20)
    turt.forward(1)
    turt.penup()
    turt.forward(120)
    turt.pendown()
    turt.forward(1)


def main():

    tess = turtle.Turtle()
    tess.pensize(3)

    wn = turtle.Screen()
    wn.bgcolor("green")
    wn.colormode(255)





    # Function calls to function_1 and function_2.
    pig_start(tess)
    pig_2(tess)
    pig_3(tess)
    pig_5(tess)

    wn.exitonclick()
main()  # Starts the program!