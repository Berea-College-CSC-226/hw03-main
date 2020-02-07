
# TODO Do not edit this file directly! Instead, create a new file called
# TODO a03_username.py and copy this code into it!

#################################################################################
# Author: Vyizigiro Reeves
# Username: reevesv2
#
# Assignment:
# Purpose:
# Google Doc Link: https://docs.google.com/document/d/1afOp47nAgQB0_ufltyQ6cCLIuz8R6Y31u8YZ1Vm3Jtk/edit?usp=sharing
#
#################################################################################
# Acknowledgements: Dr. Scott for creating the template for this assignment
#
#
#################################################################################

import turtle


def house(ab):
    """
    Docstring for function_1
    """
    pass
    ab.begin_fill()
    for i in range(2):
        ab.forward(500)
        ab.left(90)
        ab.forward(250)
        ab.left(90)
    ab.end_fill()
    # ....


def outlinehouse(ab):
    """
    Docstring for function_1
    """
    pass
    for i in range(2):
        ab.forward(500)
        ab.left(90)
        ab.forward(250)
        ab.left(90)


def roof(cd):
    """
    this function draws the wicked cool roof
    """
    pass
    cd.begin_fill()
    cd.forward(600)
    cd.left(150)
    cd.forward(500)
    cd.left(120)
    cd.forward(200)
    cd.right(90)
    cd.forward(167)
    cd.left(90)
    cd.forward(50)
    cd.end_fill()

    # ...

def outlineroof(cd):
    """
    this function draws the wicked cool roof
    """
    pass
    cd.forward(600)
    cd.left(150)
    cd.forward(500)
    cd.left(120)
    cd.forward(200)
    cd.right(90)
    cd.forward(167)
    cd.left(90)
    cd.forward(50)

    # ...

def pole(ef):
    """
    draw the pole for the flag
    """
    pass
    ef.begin_fill()
    ef.left(90)
    for i in range(2):
        ef.forward(10)
        ef.left(90)
        ef.forward(350)
        ef.left(90)
    ef.end_fill()

    #.....


def flag(gh):
    """
    this function draws the flag
    """
    pass
    gh.begin_fill()
    for i in range(2):
        gh.forward(90)
        gh.left(90)
        gh.forward(60)
        gh.left(90)
    gh.end_fill()

    #....


def cross(ij):
    """
    this function draws the white cross on the swiss flag
    """
    ij.begin_fill()
    for i in range(4):
        ij.left(90)
        ij.forward(25)
        ij.left(90)
        ij.forward(5)
        ij.left(90)
        ij.forward(25)
    ij.end_fill()

    #end of function

def door (kl):
    """
    this function draws the door the the door knob
    """
    kl.begin_fill()
    for i in range(2):
        kl.forward(60)
        kl.left(90)
        kl.forward(150)
        kl.left(90)
    kl.end_fill()

    #end of door function

def knob(mn):
    """
    this function draws the door knob
    """
    mn.begin_fill()
    for i in range(15):
        mn.forward(2)
        mn.left(24)

    mn.end_fill()

    #end of knob function


def window(op):
    """
    this function draws the door knob
    """
    op.begin_fill()
    for i in range(2):
            op.forward(89)
            op.left(90)
            op.forward(59)
            op.left(90)
    op.end_fill()

    #end of knob function


def bars(ij):
    """
    this function draws the bars across the window
    """
    ij.begin_fill()
    for i in range(2):
        ij.left(90)
        ij.forward(32)
        ij.left(90)
        ij.forward(5)
        ij.left(90)
        ij.forward(32)
        ij.left(90)
        ij.forward(47)
        ij.left(90)
        ij.forward(5)
        ij.left(90)
        ij.forward(47)
    ij.end_fill()
    ij.right(90)
    ij.forward(30)
    ij.left(90)
    ij.forward(44)
    ij.left(90)
    ij.forward(64)
    ij.left(90)
    ij.forward(94)
    ij.left(90)
    ij.forward(64)
    ij.left(90)
    ij.forward(49)

    #end of function


def rail(kl):
    """
    this function draws the bars across the window
    """
    for i in range(2):
        kl.begin_fill()
        kl.forward(3)
        kl.left(90)
        kl.forward(100)
        kl.left(90)


        kl.end_fill()

    #end of function


def toprail(mn):

    for i in range(2):
        mn.begin_fill()
        mn.forward(164)
        mn.left(90)
        mn.forward(6)
        mn.left(90)
        mn.end_fill()

    #end of function

def main():
    """
    Docstring for main
    """
    # ...
    wn = turtle.Screen()  # Set up the window and its attributes
    wn.bgcolor("green")
    wn.title("My Beautiful Dorm")

    reeves = turtle.Turtle()
    reeves.speed(0)
    reeves.pensize(3)

    reeves.penup()
    reeves.setpos(-250, -300)
    reeves.pendown()
    reeves.color("brown")
    reeves.pensize(3)
    house(reeves)
    reeves.color("black")

    reeves.penup()
    reeves.setpos(-300, -50)
    reeves.pendown()
    reeves.color("Blue")
    roof(reeves)
    reeves.color("black")

    reeves.penup()
    reeves.setpos(-210, 2)
    reeves.pendown()
    reeves.color("black")
    pole(reeves)

    reeves.penup()
    reeves.setpos(-200, 270)
    reeves.pendown()
    reeves.color("red")
    flag(reeves)

    reeves.penup()
    reeves.setpos(-150, 300)
    reeves.pendown()
    reeves.color("white")
    cross(reeves)

    reeves.penup()
    reeves.setpos(-80, -300)
    reeves.pendown()
    reeves.color("black")
    door(reeves)

    reeves.penup()
    reeves.setpos(-75, -240)
    reeves.pendown()
    reeves.color("blue")
    knob(reeves)

    # Below is the top left window
    reeves.penup()
    reeves.setpos(-199, -150)
    reeves.pendown()
    reeves.color("yellow")
    window(reeves)

    reeves.penup()
    reeves.setpos(-151, -123)
    reeves.pendown()
    reeves.color("black")
    bars(reeves)

    # Below is the bottom left window

    reeves.penup()
    reeves.setpos(-199, -245)
    reeves.pendown()
    reeves.color("yellow")
    window(reeves)

    reeves.penup()
    reeves.setpos(-151, -218)
    reeves.pendown()
    reeves.color("black")
    bars(reeves)

    # Below is the middle bottom window

    reeves.penup()
    reeves.setpos(0, -245)
    reeves.pendown()
    reeves.color("yellow")
    window(reeves)

    reeves.penup()
    reeves.setpos(48, -218)
    reeves.pendown()
    reeves.color("black")
    bars(reeves)

    # Below is the middle top window

    reeves.penup()
    reeves.setpos(0, -150)
    reeves.pendown()
    reeves.color("yellow")
    window(reeves)

    reeves.penup()
    reeves.setpos(48, -123)
    reeves.pendown()
    reeves.color("black")
    bars(reeves)

    # Below is the right top window

    reeves.penup()
    reeves.setpos(120, -150)
    reeves.pendown()
    reeves.color("yellow")
    window(reeves)

    reeves.penup()
    reeves.setpos(168, -123)
    reeves.pendown()
    reeves.color("black")
    bars(reeves)

    # Below is the right bottom window

    reeves.penup()
    reeves.setpos(120, -245)
    reeves.pendown()
    reeves.color("yellow")
    window(reeves)

    reeves.penup()
    reeves.setpos(168, -218)
    reeves.pendown()
    reeves.color("black")
    bars(reeves)

#Outline the house and the roof

    reeves.pensize(3)
    reeves.penup()
    reeves.setpos(-250, -300)
    reeves.pendown()
    reeves.color("black")
    outlinehouse(reeves)

    reeves.penup()
    reeves.setpos(-300, -50)
    reeves.pendown()
    reeves.color("black")
    outlineroof(reeves)
#Start drawing rail

    reeves.penup()
    reeves.setpos(-290, 2)
    reeves.pendown()
    reeves.color("white")
    reeves.left(90)
    rail(reeves)

    reeves.penup()
    reeves.setpos(-270, 2)
    reeves.pendown()
    reeves.color("white")
    rail(reeves)

    reeves.penup()
    reeves.setpos(-250, 2)
    reeves.pendown()
    reeves.color("white")
    rail(reeves)

    reeves.penup()
    reeves.setpos(-230, 2)
    reeves.pendown()
    reeves.color("white")
    rail(reeves)

    reeves.penup()
    reeves.setpos(-210, 2)
    reeves.pendown()
    reeves.color("white")
    rail(reeves)

    reeves.penup()
    reeves.setpos(-190, 2)
    reeves.pendown()
    reeves.color("white")
    rail(reeves)

    reeves.penup()
    reeves.setpos(-170, 2)
    reeves.pendown()
    reeves.color("white")
    rail(reeves)

    reeves.penup()
    reeves.setpos(-150, 2)
    reeves.pendown()
    reeves.color("white")
    rail(reeves)

    reeves.penup()
    reeves.setpos(-300, 80)
    reeves.pendown()
    toprail(reeves)

    reeves.penup()
    reeves.setpos(-1000, -1000)
    reeves.pendown()

    wn.exitonclick()








main()

