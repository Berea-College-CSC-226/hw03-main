#################################################################################
# Author: Matheus Bender
# Username:benderm
#
# Assignment:HW03
# Purpose: Create a complex drawing
# Google Doc Link: https://docs.google.com/document/d/1ZDXYSPh8PVUAUzLGM9COmB1yINPiZCu7JMtE9JghUMg/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle

def draw_circles(t,x,y):
    """
    draw the circles within the cap of the mushroom
    :param t: turtle
    :param x: starting point for x
    :param y: starting point for y
    :return:
    """
    t.speed(0)
    t.penup()
    x= x-10
    y = y+70
    t.color(1,1,1)
    for circles in range (2):
        t.begin_fill()
        t.goto(x+13*circles,y+(24*circles+1))
        t.pendown()
        t.circle(10*(circles+.6))
        t.penup()
        t.end_fill()
    for circle in range(1):
        t.begin_fill()
        x=x+72
        t.goto(x,y+5)
        t.pendown()
        t.circle(12)
        t.penup()
        t.end_fill()
    t.penup()

def draw_cap(t, x, y):
    """
    Function to draw the cap of the mushroom
    :param t: turtle
    :param x: x-coordinate to start the mushroom
    :param y: y-coordinate to start the mushroom
    """
    t.speed(0)
    t.hideturtle()
    t.goto(x,y+70)
    t.color(1, 0, 0)
    t.begin_fill()
    t.pendown()
    t.left(180)  # start of upper part
    t.forward(40)
    t.right(90)
    t.circle(-60, 180)
    t.right(90)
    t.forward(100)
    t.end_fill()
    t.penup()  # Lift the pen to move without drawing

def draw_root(t,x,y):
    """
    draw the root of the mushroom
    :param t: turtle
    :param x: starting point for x
    :param y: starting point for y
    """
    t.penup()
    t.goto(x,y)
    t.right(180)
    for sides in range (2):
        t.begin_fill()
        t.pendown()
        t.color(1,1,1)
        t.forward(40)
        t.left(90)
        t.forward(70)
        t.left(90)
        t.penup()
        t.end_fill()

def main():
    wn = turtle.Screen()
    t = turtle.Turtle() #turtle starting point
    wn.bgcolor(0, 0, 0)
    x = 10 #starting point to x
    y = 10 #starting point to y

    draw_cap(t, x, y)
    draw_root(t,x,y)
    draw_circles(t,x,y)


    wn.exitonclick()

main()
