#################################################################################
# Author: Kevin Lopez Hernandez
# Username: lopezhernandezk
#
# Assignment: A03
# Purpose:
# Google Doc Link: https://docs.google.com/document/d/1NyI9iPmbHpFiEXiJNeVxi0ARpSbPC9MnIQRED8kl_TA/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle


def pet():              # Black cat near fire hydrant
    cat = turtle.Turtle()
    cat.speed(0)
    cat.hideturtle()
    cat.penup()
    cat.setpos(-100, 0)
    cat.pendown()
    for body in range(2):  # Body of cat
        cat.color("Black")
        cat.begin_fill()
        cat.forward(45)
        cat.right(90)
        cat.forward(20)
        cat.right(90)
        cat.end_fill()
    cat.circle(15, -90)
    cat.penup()
    cat.setpos(-96, -7)
    cat.pendown()
    cat.color("burlywood")
    cat.begin_fill()
    cat.circle(4)
    cat.penup()
    cat.setpos(-80, -12)
    cat.pendown()
    cat.circle(6)
    cat.end_fill()
    cat.color("black")
    cat.penup()
    cat.setpos(-55, 5)  # Head and Ears of the cat
    cat.pendown()
    cat.begin_fill()
    cat.circle(12)
    cat.end_fill()
    cat.penup()
    cat.setpos(-50, 15)
    cat.right(200)
    cat.pendown()
    for ears in range(2):
        cat.begin_fill()
        cat.forward(15)
        cat.right(145)
        cat.forward(15)
        cat.left(100)
        cat.end_fill()
    cat.penup()
    cat.setpos(-100, -20)
    cat.right(80)
    cat.pendown()
    cat.setheading(0)
    for legs in range(4):  # Cat Legs
        cat.begin_fill()
        cat.right(90)
        cat.forward(20)
        cat.left(90)
        cat.forward(5)
        cat.left(90)
        cat.forward(20)
        cat.right(90)
        cat.forward(6.5)
        cat.end_fill()
    pass


def hooman():               # Purple ghost human looking at his cat
    dude = turtle.Turtle()
    dude.hideturtle()
    dude.speed(0)
    dude.penup()
    dude.setpos(5, -20)
    dude.pendown()
    dude.color("purple")
    dude.begin_fill()
    dude.left(70)
    dude.forward(150)
    dude.right(70)
    dude.forward(140)
    dude.right(90)
    dude.forward(40)
    dude.right(90)
    dude.forward(90)
    dude.right(180)
    dude.forward(45)
    dude.right(70)
    dude.forward(110)
    dude.right(110)
    dude.forward(186)
    dude.end_fill()
    dude.color("black")
    dude.penup()
    dude.right(110)
    dude.forward(75)
    dude.right(70)
    dude.forward(30)
    dude.right(90)
    dude.pendown()
    dude.forward(50)
    dude.forward(-50)
    dude.left(90)
    dude.penup()
    dude.forward(101)
    dude.pendown()
    dude.forward(60)
    eyes = turtle.Turtle()
    eyes.speed(0)
    eyes.hideturtle()
    eyes.penup()
    eyes.setpos(100, 90)
    eyes.begin_fill()
    eyes.pendown()
    eyes.circle(10)
    eyes.penup()
    eyes.forward(50)
    eyes.pendown()
    eyes.circle(10)
    eyes.end_fill()

    pass


def hydrant():              # Fire Hydrant: Place of accident
    fire = turtle.Turtle()
    fire.color("red")
    fire.hideturtle()
    fire.speed(0)
    fire.penup()
    fire.setpos(-200, 0)
    fire.pendown()
    for i in range(2):
        fire.begin_fill()
        fire.forward(30)
        fire.right(90)
        fire.forward(50)
        fire.right(90)
        fire.end_fill()
    fire.forward(30)
    fire.left(90)
    fire.begin_fill()
    fire.circle(15, 180)
    fire.end_fill()
    fire.forward(12.5)
    for p in range(2):
        fire.begin_fill()
        fire.forward(25)
        fire.right(90)
        fire.forward(10)
        fire.right(90)
        fire.end_fill()
    fire.penup()
    fire.setpos(-170, -12.5)
    fire.pendown()
    for t in range(2):
        fire.begin_fill()
        fire.forward(25)
        fire.left(90)
        fire.forward(10)
        fire.left(90)
        fire.end_fill()
    fire.color("black")
    fire.begin_fill()
    fire.forward(12.5)
    fire.circle(-15)
    fire.end_fill()


def dookie():                   # Cat Feces
    lol = turtle.Turtle()
    lol.penup()
    lol.hideturtle()
    lol.speed(0)
    lol.color("brown")
    lol.setpos(-150, -50)
    lol.pendown()
    lol.begin_fill()
    for e in range(2):
        lol.forward(40)
        lol.right(90)
        lol.forward(5)
        lol.right(90)
    lol.end_fill()
    lol.forward(5)
    lol.begin_fill()
    for r in range(2):
        lol.forward(30)
        lol.right(-90)
        lol.forward(5)
        lol.right(-90)
    lol.end_fill()
    lol.left(90)
    lol.forward(5)
    lol.right(90)
    lol.forward(5)
    lol.begin_fill()
    for f in range(2):
        lol.forward(20)
        lol.right(-90)
        lol.forward(5)
        lol.right(-90)
    lol.end_fill()


def main():             # Purple ghost human telling cat to go home after incident!
    wn = turtle.Screen()
    wn.bgcolor("sky blue")
    hydrant()  # Function call to hydrant
    dookie()  # Function call to dookie
    pet()  # Function call to pet
    hooman()  # Function call to hooman

    wn.exitonclick()


main()
