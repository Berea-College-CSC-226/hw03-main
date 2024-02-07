#################################################################################
# Author: Giovanny Ortiz
# Username: ortizg
#
# Assignment: HW03: "Fully Functional Gitty Psychedelic Robotic Turtles"
# Purpose:
# Google Doc Link: https://docs.google.com/document/d/1OJ2Gq9T8-_tipjT83M_Q2aLOkE_8c5aM-uYcQoyR1oc/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle

def tierra_ciel(t):
    t.speed(6)
    t.penup()
    t.setposition(-385, -80)
    t.pendown()
    for i in range(4):
        t.forward(900)
        t.right(90)
        t.forward(30)
        t.right(90)
        t.forward(900)
        t.left(90)
        t.forward(30)
        t.left(90)
    t.forward(900)
    t.penup()
    t.home()
    t.hideturtle()
    pass
    # ....

def monte(t):

    pass
    # ...

def filled_circle(turtle, radius, color):
    turtle.color(color, color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def cloud(turtle, radius, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    filled_circle(turtle, radius, "white")
    turtle.penup()
    turtle.forward(radius)
    turtle.pendown()
    filled_circle(turtle, radius, "white")
    turtle.penup()
    turtle.hideturtle()


def heat(t, radio, x, y):
    t.penup()
    t.setposition(x, y)
    t.penup()
    t.begin_fill()
    t.circle(radio)
    t.end_fill()
    t.hideturtle()


def main():
    pantalla = turtle.Screen()
    pantalla.bgcolor('#80B9E5')
    t_c = turtle.Turtle()
    #montana = turtle.Turtle()
    #rio=turtle.Turtle()
    #t_c attributes
    t_c.pensize(30)
    cl = ('#0A8623')
    t_c.pencolor(cl)
    # t_c.
    # t_c.

   #######################

   #montana attributes
    # montana.
    # montana.
    # montana.

    #El sol
    sun = turtle.Turtle()
    sun.fillcolor('yellow')
    radio = 85
    ##############

    #Cloud
    cloud_turtle = turtle.Turtle()
    cloud_turtle.penup()
    ##############


    tierra_ciel(t_c)
    #monte(montana)

    radius = 50
    cloud(cloud_turtle, radius, -155, 130)
    heat(sun, radio, 370, 245)

    pantalla.exitonclick()


main()  # Starts the program!


