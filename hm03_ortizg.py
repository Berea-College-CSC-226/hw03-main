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
# ChatGPT for references, methods and ways to code. (No copy paste obviously)
#
#################################################################################

import turtle


def tierra_ciel(t):
    """This function makes the green surface on the bottom of the screen simulating the ground"""
    t.speed(5)
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


def filled_circle(t, radius, color):
    """This allows the circle drawn to be filled with the assigned color on the other function when called\""""
    t.color(color, color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


def cloud(t, radius, x, y):
    """This function draws the clouds (circles) on the top of the screen (sky)"""
    t.penup()
    t.goto(x, y)
    t.pendown()
    filled_circle(t, radius, "white")
    t.penup()
    t.forward(radius)
    t.pendown()
    filled_circle(t, radius, "white")
    t.penup()
    t.fd(190)
    t.pendown()
    filled_circle(t, radius, "white")
    t.penup()
    t.forward(radius)
    t.pendown()
    filled_circle(t, radius, "white")
    t.penup()
    t.hideturtle()


def heat(t, radio, x, y):
    """Draw and fill a circle that crosses the border of the screen and only shows part of the circle (Sun)"""
    t.penup()
    t.setposition(x, y)
    t.penup()
    t.begin_fill()
    t.circle(radio)
    t.end_fill()
    t.hideturtle()


def hills(t, x, y):
    """This function draws the two hills at the middle left part simulating mountains"""
    t.penup()
    t.goto(x, y)
    for i in range(2):
        t.pendown()
        t.begin_fill()
        t.left(45)
        t.fd(65)
        t.right(95)
        t.fd(35)
        t.left(95)
        t.fd(80)
        t.right(105)
        t.fd(87)
        t.end_fill()
        t.penup()
        t.left(60)
        t.fd(5)

    t.hideturtle()


def lago(t, x, y):
    """This functions draws and fills it color blue simulating a pond or a little lake"""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.right(45)
    t.begin_fill()
    for _ in range(2):
        t.circle(180, 90)  # Draw quarter circle
        t.circle(80, 90)  # Draw quarter circle
    t.end_fill()
    t.hideturtle()


def main():
    """The function where all the extra code is. Turtles, variables, attributes, etc\""""

    # Screen and its attributes
    pantalla = turtle.Screen()
    pantalla.bgcolor('#80B9E5')

    # Turtles
    t_c = turtle.Turtle()
    montana = turtle.Turtle()
    rio = turtle.Turtle()

    # t_c attributes
    t_c.pensize(30)
    cl = '#0A8623'
    t_c.pencolor(cl)

    # montana attributes
    montana.pensize(4)
    montana.fillcolor('grey')
    montana.pencolor('grey')

    # El sol
    sun = turtle.Turtle()
    sun.fillcolor('yellow')
    radio = 100

    # Cloud
    cloud_turtle = turtle.Turtle()
    cloud_turtle.penup()
    radius = 50

    # pond
    rio.pensize(2)
    rio.pencolor('darkblue')
    rio.fillcolor('darkblue')

    # Every function that is going to be called in the determined order.
    tierra_ciel(t_c)
    cloud(cloud_turtle, radius, -255, 130)
    heat(sun, radio, 355, 225)
    hills(montana, 100, -65)
    lago(rio, -280, -250)

    pantalla.exitonclick()


main()  # Starts the program!
