#################################################################################
# Author: Pier Ciccariello
# Username: ciccariellop
#
# Assignment: HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Practice w/ functions, turtles, and python in general
# Google Doc Link: https://docs.google.com/document/d/1GoGJoL2peNQtOe6GWwlO17fe6I_66j5E4ZYtaTG-Bw0/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################


import turtle

def draw_window1(t):
    """Draws a window at (120,20)"""
    t.penup()
    t.setpos(120,20)
    t.pendown()
    t.pencolor("grey")
    for i in range(4):
        t.forward(75)
        t.left(90)

def draw_window2(t):
    t.penup()
    t.setpos(-150, 20)
    t.pendown()
    t.pencolor("grey")
    for i in range(4):
        t.forward(75)
        t.left(90)

def draw_house(t):
    t.penup()
    t.setpos(-200, -200)
    t.pendown()
    t.pencolor("grey")
    t.forward(450)
    t.left(90)
    t.forward(350)
    t.left(90)
    t.forward(450)
    t.left(90)
    t.forward(350)
    t.backward(350)

def draw_roof_chimney(t):
    t.left(135)
    t.forward(319)
    t.right(90)
    t.forward(319)
    t.backward(100)
    t.left(135)
    t.forward(70)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(90)
    t.fillcolor("brown")

def draw_head(t):
    """Draws a filled circle centered at (x, y)."""
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    t.circle(30)
    t.end_fill()

def draw_body(t):
    """Draws a body down from the filled circle."""
    t.right(90)
    t.forward(100)
    t.left(45)
    t.forward(65)
    t.backward(65)
    t.right(90)
    t.forward(65)
    t.penup()
    t.setpos(0,0)

def draw_arms(t):
    """Draws arms at (x,y)"""
    t.pendown()
    t.forward(65)
    t.backward(65)
    t.left(90)
    t.forward(65)
    t.left(45)

def main():
    wn = turtle.Screen()
    wn.bgcolor("#87CEEB")
    wn.setup(600, 600)
    t = turtle.Turtle()
    t.color("purple")
    t.pensize(5)
    t.speed(0)

    draw_head(t)
    draw_body(t)
    draw_arms(t)
    draw_window1(t)
    draw_window2(t)
    draw_house(t)
    draw_roof_chimney(t)

    wn.exitonclick()




main()