import turtle
#################################################################################
# Author: Dakota Miller
# Username: millerd2
#
# Assignment: a03
# Purpose: figuring out git
# Google Doc Link: https://docs.google.com/document/d/1UkxQqxkQoV1aOVVqkFi86hIr6JmqKrbCbnJpEAgf408/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################
def draw_square(jon):
    jon.begin_fill()
    for j in range(4):
        jon.forward(300)
        jon.right(90)
    jon.end_fill()

def main():
    jon, wn = setup_screen()
    draw_square(jon)
    # moving to right starting position
    jon.penup()
    jon.left(90)
    jon.forward(20)
    jon.pendown()
    jon.pencolor("red")
    draw_triangle(jon)
    draw_door(jon)
    draw_doorknob(jon)
    text(jon)
    wn.exitonclick()

def setup_screen():
    # sets up the screen
    wn = turtle.Screen()
    wn.colormode(255)
    wn.bgcolor(128, 0, 128)
    jon = turtle.Turtle()
    jon.pensize(20)
    jon.penup()
    jon.setpos(-250, 50)
    jon.pendown()
    return jon, wn


def draw_triangle(jon):
    # draws the triangle
    jon.color("red")
    jon.begin_fill()
    for i in range(1):
        jon.right(90)
        jon.forward(300)
        jon.left(135)
        jon.forward(220)
        jon.left(90)
        jon.forward(200)
    jon.end_fill()
def draw_door(jon):
    # right place for the door
    jon.color("grey")
    jon.begin_fill()
    jon.penup()
    jon.setpos(-100, -240)
    jon.left(135)
    jon.pencolor("grey")
    jon.pendown()
    for i in range(4):
        jon.forward(150)
        jon.left(90)
    jon.end_fill()
def draw_doorknob(jon):
    # right place for the door knob
    jon.color("yellow")
    jon.penup()
    jon.left(90)
    jon.forward(60)
    jon.right(90)
    jon.forward(10)
    jon.pendown()
    for i in range(1):
        jon.circle(5)
def text(jon):
    jon.penup()
    jon.setpos(100, 100)
    jon.write("Mi Casa")
