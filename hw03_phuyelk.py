#################################################################################
# Author: Kushal Phuyel
# Username:phuyelk
#
# Assignment: HW03
# Purpose: Drawing something complex
# Google Doc Link: https://docs.google.com/document/d/1_a3kuwXeeRDXZFCeHBbTFcxotTxqELsMHovHVWuTinw/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle

wn = turtle.Screen()
kush = turtle.Turtle()
wn.bgcolor("gray")
kush.color("blue")
kush.pensize(2)


def draw_square(t, size):
    #draws a square
    for _ in range(4):
        t.forward(size)
        t.left(90)


def draw_triangle(t, size):
    #draws a roof
    for _ in range(3):
        t.forward(size)
        t.left(120)


def draw_house():
    # Draw the house base
    kush.penup()
    kush.goto(-50, -50)
    kush.pendown()
    kush.fillcolor("lightblue")
    kush.begin_fill()
    draw_square(kush, 100)
    kush.end_fill()

    # Draw the roof
    kush.penup()
    kush.goto(-50, 50)  # Move to the top of the square
    kush.pendown()
    kush.fillcolor("light green")
    kush.begin_fill()
    draw_triangle(kush, 100)
    kush.end_fill()


def draw_door():
    #Draws a door at the bottom center of the house
    kush.penup()
    kush.goto(-15, -50)  # Position at the bottom center of the house
    kush.pendown()
    kush.color("brown")
    kush.fillcolor("brown")
    kush.begin_fill()
    for _ in range(2):
        kush.forward(30)
        kush.left(90)
        kush.forward(50)
        kush.left(90)
    kush.end_fill()
    kush.color("blue")  # Reset color

def draw_cloud(radius, color):
    kush.penup()
    kush.goto(50, 100)
    kush.pendown()
    kush.color(color, color)
    kush.begin_fill()
    for w in range(3):
        kush.circle(radius)
        kush.penup()
        kush.forward(radius)
        kush.pendown()
    kush.end_fill()

def main():
    draw_house()
    draw_door()
    draw_cloud(20, "white")
    wn.exitonclick()

main()
