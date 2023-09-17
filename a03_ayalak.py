
#################################################################################
# Author: Katherine Ayala
# Username: ayalak
#
# Assignment:HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose:Continue practicing creating and using functions.
# More practice on using the turtle library.
# Learn about how computers represent colors.
# Learn about source control and Git.
# Google Doc Link:
# https://docs.google.com/document/d/1yX21Qx8PuccPRjeSoPx5JTthVSf3EOnR6XgCUS1IQII/edit?usp=sharing
#
#################################################################################
# Sources:
# hw02_ayalak.py
# https://docs.python.org/3.3/library/turtle.html?highlight=turtle#methods-of-turtlescreen-screen
# https://docs.python.org/3.3/library/turtle.html?highlight=turtle#overview-of-available-turtle-and-screen-methods
#
#################################################################################
import turtle

def petal(t, r, angle):
    for i in range(2):
        t.circle(r, angle)
        t.left(180-angle)
def flower(t, n,  r, angle):
    for i in range(n):
        petal(t, r, angle)
        t.left(360.0/n)
def move(t, lenght):
    t.pu()
    t.fd(lenght)
    t.pd()
def setup_window(rosa):
    rosa.color('orchid') #aje
    rosa.shape('turtle')
    move(rosa,150)
    rosa.begin_fill()
    flower(rosa, 7, 100.0, 60.0)
    rosa.end_fill()
def setup_window1(azul):
    azul.color('blue')
    azul.shape('circle')
    move(azul, 150)
    flower(azul, 7, 60.0, 60)

def main ():
    wn = turtle.Screen()
    wn.bgcolor('pink')
    rosa = turtle.Turtle()
    setup_window(rosa)
    azul = turtle.Turtle()
    setup_window1(azul)



    wn.exitonclick()
main()