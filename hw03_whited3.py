#################################################################################
# Author: Destiny White
# Username: whited3
#
# Assignment:HW03- Fully Functional GItty Psychedelic Turtles
# Purpose: To learn more about git, functions, and doc strings
# Google Doc Link: https://docs.google.com/document/d/1JwFWjoXfjxo1U_hnxmwLi8dFDfw2O1sIfiP6n8Y5bWw/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle

def main_body(spe):
    """
    Creating the main building part of my house
    """
    mb = turtle.Turtle()
    mb.pensize(2)
    mb.speed(spe)
    mb.ht()
    mb.up()
    mb.setpos(-100, -100)
    mb.down()
    mb.fillcolor('#bf4122')
    mb.pencolor('#bf4122')
    mb.begin_fill()
    for i in range(2):      # BRICK LAYER
        mb.fd(200)
        mb.left(90)
        mb.fd(50)
        mb.left(90)
    mb.end_fill()

    mb.left(90)
    mb.fd(50)

    mb.pencolor('#f6efe6')
    mb.fillcolor('#f6efe6')
    mb.begin_fill()
    for i in range(2):
        mb.fd(100)
        mb.right(90)
        mb.fd(200)
        mb.right(90)
    mb.end_fill()

    mb.pencolor('brown')
    mb.fillcolor('brown')
    mb.begin_fill()
    mb.fd(100)                         # ROOF
    mb.right(45)
    mb.fd(100)
    mb.right(45)
    mb.fd(60)
    mb.right(45)
    mb.fd(100)
    mb.right(135)
    mb.fd(200)
    mb.end_fill()

def chimney(spe):
    ch = turtle.Turtle()
    ch.pensize(2)
    ch.speed(spe)
    ch.pencolor('#e4590d')
    ch.ht()
    ch.up()
    ch.setpos(50, 100)
    ch.left(90)
    ch.down()

    ch.fillcolor('#e4590d')
    ch.begin_fill()
    ch.fd(20)
    ch.right(90)
    ch.fd(40)
    ch.right(90)
    ch.fd(80)
    ch.right(135)
    ch.fd(60)
    ch.end_fill()

def extension(spe):
    ex = turtle.Turtle()
    ex.pensize(2)
    ex.speed(spe)
    ex.ht()
    ex.up()
    ex.setpos(20, -100)
    ex.down()
    ex.fillcolor("#f6efe6")
    ex.begin_fill()
    for i in range(2):
        ex.fd(80)
        ex.left(90)
        ex.fd(150)
        ex.left(90)
    ex.end_fill()
    ex.left(90)
    ex.fd(150)
    ex.begin_fill()
    ex.right(50)
    ex.fd(58)
    ex.right(85)
    ex.fd(52)
    ex.right(135)
    ex.fd(60)
    ex.end_fill()

def window(spe):
    bay = turtle.Turtle()
    bay.pensize(2)
    bay.speed(spe)
    bay.ht()
    bay.up()
    bay.setpos(-80,20)
    bay.down()
    bay.fillcolor('#37b5b7')
    bay.begin_fill()
    for i in range(2):
        bay.fd(80)
        bay.right(90)
        bay.fd(50)
        bay.right(90)
    bay.end_fill()

    bay.pensize(5)
    bay.pencolor("black")
    for i in range(2):
        bay.fd(80)
        bay.right(90)
        bay.fd(50)
        bay.right(90)
    bay.fd(40)
    bay.right(90)
    bay.fd(50)
    bay.right(90)

def door(spe):
    door = turtle.Turtle()
    door.pensize(2)
    door.ht()
    door.speed(1)
    door.up()
    door.setpos(30, -100)
    door.down()
    door.fillcolor("brown")
    door.begin_fill()
    door.left(90)
    door.fd(100)
    door.circle(-30, 180)
    door.fd(100)
    door.right(90)
    door.fd(70)
    door.end_fill()

def background(spe):
    bg = turtle.Turtle()
    bg.speed(spe)
    bg.fillcolor("#265e82")    # blue
    bg.begin_fill()
    bg.up()
    bg.setpos(-200,-100)
    bg.up()
    for i in range(2):
        bg.fd(400)
        bg.left(90)
        bg.fd(400)
        bg.left(90)
    bg.end_fill()

def main():
    wn = turtle.Screen()
    wn.bgcolor("#84af47")   # green
    wn.setup(400, 400)

    spe = 0         #turtle speed
    background(spe)
    chimney(spe)
    main_body(spe)
    extension(spe)
    window(spe)
    door(spe)
    wn.exitonclick()

main()