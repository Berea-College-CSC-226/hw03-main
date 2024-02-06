#################################################################################
# Author: Ariana Meatchem
# Username: Meatchema
#
# Assignment:Hw03-main
# Purpose:To use functions to create an image
# Google Doc Link:https://docs.google.com/document/d/1WP_0oslYu8R1FTGSm0tFqRG0flc_PhVXGzIbjHYsBwQ/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
# https://redketchup.io/color-picker
# https://www.w3schools.com/colors/colors_picker.asp
#################################################################################
import turtle


def build_grass(apple):
    """ This function helps to create grass """
    apple.pensize(10)
    apple.color("green")
    apple.speed(0)

    apple.penup()  # This set of directions positions apple to get ready to create the ground
    apple.goto(x=-350, y=-200)
    apple.pendown()
    apple.forward(800)
    apple.begin_fill()

    for g in range(6):  # this for statement creates the grassy colored ground
        apple.right(90)
        apple.forward(100)
        apple.right(90)
        apple.forward(1000)
    apple.end_fill()


def build_windows(twinkle):
    """ This creates the window for the apartment building """
    twinkle.speed(0)
    twinkle.penup()
    twinkle.goto(x=170, y=110)
    twinkle.pendown()
    twinkle.pensize(2)
    twinkle.color("white")
    twinkle.fillcolor("#e5f5f5")

    twinkle.begin_fill()  # This is the start of the window creation
    for p in range(4):
        twinkle.left(90)
        twinkle.forward(125)
        twinkle.left(90)
        twinkle.forward(125)
        twinkle.left(90)
        twinkle.forward(200)
        twinkle.end_fill()


def build_apartment(cutie):
    """ This function helps make the grey apartment """
    cutie.speed(0)
    cutie.pensize(6)
    cutie.color("#B0B4B5")
    cutie.penup()
    cutie.goto(x=200, y=-200)
    cutie.pendown()

    cutie.begin_fill()
    for i in range(2):  # creates rectangular building
        cutie.left(90)
        cutie.forward(500)
        cutie.left(90)
        cutie.forward(250)
    cutie.end_fill()


def draw_sun(beam):
    """ This function helps to draw the sun """
    beam.speed(0)
    beam.pensize(3)
    beam.color("#ffcc00")
    beam.penup()

    beam.goto(-400, 350)  # puts beam into position to start the sun
    beam.forward(100)
    beam.pendown()

    beam.begin_fill()  # creates the sun
    for i in range(24):
        beam.right(15)
        beam.forward(30)
    beam.end_fill()


def draw_door(little):
    """ This function helps to create the door for the apartment building"""
    little.pensize(5)
    little.color("grey")
    little.penup()
    little.goto(55, -100)
    little.pendown()
    for i in range(4):  # create rectangle
        little.forward(50)
        little.right(90)
        little.forward(100)
        little.right(90)
    little.penup()

    little.goto(97, -150)  # create door nob
    little.pendown()
    for i in range(22):
        little.forward(1)
        little.left(15)
    little.penup()
    little.goto(500, 500)


def main():
    """ The goal of this file is to create an area that has an apartment building as its main focus"""
    wn = turtle.Screen()
    wn.bgcolor("light blue")
    apple = turtle.Turtle()
    cutie = turtle.Turtle()
    twinkle = turtle.Turtle()
    beam = turtle.Turtle()
    little = turtle.Turtle()

    build_grass(apple)
    build_apartment(cutie)
    build_windows(twinkle)
    draw_sun(beam)
    draw_door(little)
    wn.exitonclick()


main()
