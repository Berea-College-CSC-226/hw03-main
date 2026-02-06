#################################################################################
# Author: Boone Riley
# Username: rileyk
#
# Assignment: HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Creative drawing of a UFO
# Google Doc Link: https://docs.google.com/document/d/1Rr4vIPVRLXlNXfkz7AHrMYtzlTRI_a0lpDhTECapNCE/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
# Turtle documentation and class examples
# Color Codes: https://colorspire.com
#################################################################################

import turtle
import random

def move_to(tess, x, y):
    tess.penup()
    tess.goto(x, y)
    tess.pendown()


def draw_circle(tess, radius, color):
    tess.fillcolor(color)
    tess.begin_fill()
    tess.circle(radius)
    tess.end_fill()

# Base of UFO
def draw_ufo_body(tess):
    move_to(tess, -120, -50)
    tess.setheading(0)
    tess.fillcolor("#7F8C8D")
    tess.begin_fill()
    tess.forward(240)
    tess.left(90)
    # I figured out I could just make a half circle to make
    # the body instead of making a curve function and doing
    # it manually
    tess.circle(120, 180)
    tess.left(90)
    tess.forward(240)
    tess.end_fill()

    # Dome on top of UFO
    move_to(tess, 0, 10)
    tess.setheading(0)
    tess.fillcolor("#5DADE2")
    tess.begin_fill()
    tess.circle(60)
    tess.end_fill()


def draw_ufo_windows(tess):
    move_to(tess, -80, -20)
    tess.setheading(0)

    for i in range(5):
        draw_circle(tess, 10, "#F7DC6F")
        tess.penup()
        tess.forward(40)
        tess.pendown()

# Draws the yellow light beam coming from UFO
def draw_beam(tess):
    move_to(tess, -40, -50)
    tess.fillcolor("#F4D03F")
    tess.begin_fill()
    tess.goto(40, -50)
    tess.goto(120, -200)
    tess.goto(-120, -200)
    tess.goto(-40, -50)
    tess.end_fill()

# Adds 'stars' varying in size on random spots
# across the window
def draw_stars(tess):
    tess.pencolor("white")
    for i in range(80):
        x = random.randint(-300, 300)
        y = random.randint(-250, 250)
        move_to(tess, x, y)
        # This is what creates different sizes
        tess.dot(random.randint(3, 6))

def main():
    wn = turtle.Screen()
    wn.bgcolor("#0B1C2D")
    tess = turtle.Turtle()
    tess.speed(0)
    draw_stars(tess)
    draw_ufo_body(tess)
    draw_ufo_windows(tess)
    draw_beam(tess)
    tess.hideturtle()
    wn.exitonclick()


main()