###########################################################
# Author: Nancy Landeros
# Username: landerosn
#
# Assignment: A03: Fully Functional Gitty Psychedelic Robotic Turtles
#Google Doc link: https://docs.google.com/document/d/1CYlhf3IDJj0o6fuSB3hL0P7r1iG9gkNlMxqnPZ6EySM/edit?usp=sharing
#############################################################

import turtle

def sun(garret):

    """Drawing a circle for the shape of the sun"""
    garret.penup()
    garret.color("Yellow")
    garret.setposition(-160, 205)
    garret.pendown()
    garret.pensize(3)

    garret.begin_fill()
    garret.circle(70)
    garret.end_fill()

def sun_rays(garret):
    """
    Draw the sun rays
    """
    garret.hideturtle()
    garret.pensize(2)
    garret.color('#FF5733')
    garret.setposition(-130, 160)
    garret.pendown()

    for move in range(45):         # the rays on the sun
        garret.speed(80)
        garret.forward(150)
        garret.back(100)
        garret.penup()
        garret.right(8)
        garret.back(60)
        garret.pendown()

def a_roof(garret):
    """
    makes a roof, triangle
    : param garret: a Turtle object
    : return: None
    """
    garret.home()
    garret.hideturtle()
    garret.color('#783f04')
    garret.begin_fill()
    garret.forward(150)
    garret.left(120)
    garret.forward(60)
    garret.left(60)
    garret.forward(90)


    garret.end_fill()

def a_main_house(t,sz):
    """
    Makes the main house square
    : param garret: a Turtle object
    : return: None
    """

    t.setpos(0, -150)
    t.color('#F5B041')
    t.begin_fill()

    for side in range(4):          # Making the main house as a square
        t.forward(sz)
        t.left(90)
    t.end_fill()

def a_door(garret):
    """
    Make door inside house
    """
    garret.penup()
    garret.setpos(90, -150)
    garret.pendown()
    garret.color('#800000')
    garret.begin_fill()
    for side in range(2):             # drawing a door which is rectangular
        garret.forward(30)
        garret.right(90)
        garret.forward(80)
        garret.right(90)
    garret.end_fill()

def a_text(garret, txt):
    """
    Writes test to screen.
    : param shape: a Turtle object
    : return: None
    """
    garret.color('white')
    garret.penup()
    garret.setpos(70, 120)
    garret.pendown()
    garret.write(txt, move=False, align='center', font=("Times New Roman", 30, ("bold", "normal")))

def grass(garret):
    """
    Makes grass
    """
    garret.penup()
    garret.setposition(0, -150)
    garret.pendown()
    garret.pensize(5)
    garret.pencolor('Green')

    garret.forward(30)
    garret.right(60)
    for move in range(10):
        garret.forward(40)
        garret.left(120)
        garret.forward(40)
        garret.right(120)



def main():
    """
    Draws a house on screen.
    : return: None
    """

    wn = turtle.Screen()
    wn.bgcolor("light blue")
    garret = turtle.Turtle()                             # named my turtle garret
    garret.hideturtle()

    ##### Function call for each part ###################
    a_roof(garret)
    a_main_house(turtle.Turtle(), 150)
    a_door(garret)
    grass(garret)
    sun(garret)
    sun_rays(garret)
    a_text(garret, "My House")

    wn.exitonclick()

main()
