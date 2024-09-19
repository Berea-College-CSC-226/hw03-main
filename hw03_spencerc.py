#################################################################################
# Author:CJ Spencer
# Username:spencerc
#
# Assignment:HW03
# Purpose:Draw picture and learn collaborative Github
# Google Doc Link:https://docs.google.com/document/d/152Rw1JpNvbbuw87RRWGGLysXNf_UNEKe0uls69uLH50/edit?usp=sharing
#
#################################################################################
# Acknowledgements:https://docs.python.org/3/library/turtle.html#turtle.fillcolor, RGB Color Wheel
#
#
#################################################################################

import turtle

def draw_wall(goober):
    """draws and fills the square that will be the walls/base of the house"""
    goober.fillcolor('beige')
    goober.begin_fill()
    for i in range(4):
        goober.forward(100)
        goober.right(90)
    goober.end_fill()
    goober.left(45)

def draw_roof(goober):
    """draws the roof atop the house"""
    goober.fillcolor('red')
    goober.begin_fill()
    goober.forward(71.5)
    goober.right(90)
    goober.forward(71.5)
    goober.right(135)
    goober.forward(100)
    goober.end_fill()
    goober.right(45)
    goober.penup()
    goober.right(90)
    goober.forward(71.5)
    goober.right(90)
    goober.forward(20.5)
    goober.pendown()

def draw_chimney(goober):
    """Draws a chimney. Every house could use a chimney for those cold winter night by the fire"""
    goober.fillcolor('grey')  #it's a rock chimney
    goober.begin_fill()
    goober.left(135)
    goober.forward(20)
    goober.right(90)
    goober.forward(10)
    goober.right(90)
    goober.forward(30.5)
    goober.end_fill()
    goober.left(45)
    goober.forward(20)

def draw_door(goober):
    """creates a door so people aren't trapped inside"""
    goober.penup()
    goober.right(45)
    goober.forward(110)
    goober.right(90)
    goober.forward(40)
    goober.pendown()
    goober.right(90)
    goober.pendown()
    goober.fillcolor('brown')
    goober.begin_fill()
    goober.forward(35)
    goober.left(90)
    goober.forward(20)
    goober.left(90)
    goober.forward(35)
    goober.left(90)
    goober.forward(20)
    goober.end_fill()

def draw_grass(goober):
    """draws the landscape"""
    goober.fillcolor('lightgreen')
    goober.begin_fill()
    goober.forward(300)
    goober.right(90)
    goober.forward(200)
    goober.right(90)
    goober.forward(900)
    goober.right(90)
    goober.forward(200)
    goober.right(90)
    goober.forward(700)
    goober.end_fill()

def draw_sun(goober):
    """draws the sun to brighten everyone's day"""
    goober.penup()
    goober.left(135)
    goober.forward(550)
    goober.pendown()
    goober.fillcolor('yellow')
    goober.begin_fill()
    goober.circle(80)
    goober.end_fill()
    goober.penup()
    goober.left(90)
    goober.forward(80)
    goober.pendown()
    goober.color('orange')
    x = 1
    for i in range(60):
        goober.forward(1)
        goober.right(45)
        goober.forward(x+i)

def main():
    """it's main... it's where the main stuff goes like functionality calls go"""
    wn = turtle.Screen()
    goober = turtle.Turtle()
    turtle.bgcolor('lightblue')
    goober.speed(9)
    draw_wall(goober)
    draw_roof(goober)
    draw_chimney(goober)
    draw_door(goober)
    draw_grass(goober)
    draw_sun(goober)
    wn.exitonclick()

main()