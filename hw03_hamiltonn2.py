#################################################################################
# Author: Nicholas Hamilton
# Username: hamiltonn
#
# Assignment: hw03
# Purpose:
#################################################################################
# Acknowledgements:
#Google doc: https://docs.google.com/document/d/18IElYRwRfN-P-x0M-GQ27qRxASZecZzvfqua16UC-pw/edit?usp=sharing
#
#EXTRA SOURCE OUTSIDE OF CLASS - https://docs.google.com/document/d/1y0ie1nRm1TkirENH6K2FC378MozYTd-zCFCgBa2Cv_0/edit?usp=sharing
#################################################################################

#Add any important statements here
import turtle

def square(t):
    """draws water at bottom of screen"""
    t.speed(0)
    t.penup()
    t.goto(-270,-1000)
    t.pendown()
    t.color("blue")

    for sides in range(4):
        t.forward(700)
        t.left(90)

def sunset(t):
    """creates gradient background"""
   # first attempt- colors = ['#FFDF00' '#FFA500', 'FF5733', '#E63462', 'A300D6', '0E0F4E']
    colors = [
        '#FFD700', '#FFD700', '#FFD700', '#FFD700', '#FFD700', '#FFD700', '#FFD700',
        '#FFA500', '#FFA500', '#FFA500', '#FFA500',
        '#FF4500', '#FF4500', '#FF4500', '#FF4500',
        '#FF6347', '#FF6347', '#FF6347', '#FF6347',
        '#FF7F50', '#FF7F50', '#FF7F50', '#FF7F50',
        '#FFA07A', '#FFA07A', '#FFA07A', '#FFA07A',
        '#FFB6C1', '#FFB6C1', '#FFB6C1'
    ] # (internet source for colors, check citations)



    t.penup()
    t.speed(0)
    t.goto(-400,-50)
    t.pendown()

    for lines in range(30):
        t.color(colors[lines])
        t.forward(800)
        t.left(90)
        t.forward(5)
        t.left(90)
        t.forward(800)
        t.right(90)
        t.forward(5)
        t.right(90)

def boat(t):
    "draws a super cute brown boat"
    t.penup()
    t.speed(0)
    t.goto(-100,0)
    t.right(90)
    t.pendown()
    t.color("#8B2424")
    t.begin_fill()
    t.circle(50,180)
    t.end_fill()
    t.penup()
    t.left(90)
    t.forward(50)
    t.pendown()
    t.right(90)
    t.forward(100)
    t.right(45)
    t.begin_fill()
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.end_fill()
    t.hideturtle()
def main():
    """to draw pic"""
    wn = turtle.Screen()
    wn.bgcolor("#FFB6C1")
    alex = turtle.Turtle()
    alex.shape("square")
    alex.pensize(500)
    boatturtle = turtle.Turtle()
    boatturtle.shape("turtle")
    boatturtle.pensize(10)
    boatturtle.hideturtle()
    sunsetturtle = turtle.Turtle()
    sunsetturtle.shape("square")
    sunsetturtle.pensize(5)
    sunsetturtle.color("#E49835") # R 228 G 152 B 53


    square(alex)
    sunset(sunsetturtle)
    boat(boatturtle)
    wn.exitonclick()

main()