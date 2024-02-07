#################################################################################
# Author: Javier Vazquez Soto
# Username:Vazquezsotoj
#
# Assignment:hw03
# Purpose: To create something complex like a house,animal, or person
# Google Doc Link: https://docs.google.com/document/d/1f5hiQ8grzoAFKAAftUvUoYdcgWC0BoQAqeDspi7zWOU/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#T03_Function_house.py
#Hw02-loopy-turtles-loopy-languages.py
#################################################################################

import turtle

def Ear1(x):
    """draws right ear"""
    x.pensize(10)
    x.begin_fill()
    x.fillcolor("#F9D6E3")
    x.left(45)
    x.forward(60)
    x.right(130)
    x.forward(70)
    x.end_fill()

def Ear2(y):
    """Draws left ear"""
    y.pensize(10)
    y.begin_fill()
    y.fillcolor("#F9D6E3")
    y.left(210)
    y.forward(50)
    y.left(140)
    y.forward(70)
    y.end_fill()


# Makes eye and colors the eyes
def EyeColor(z):
    """draws eyes and makes them black"""
    z.pendown()
    z.begin_fill()
    z.fillcolor('black')
    z.circle(18)
    z.end_fill()
    z.penup()

def mouth(b):
    "draws mouth and nose"
    b.penup()
    b.goto(-40, -10)
    b.pensize(5)
    b.pendown()
    b.right(90)
    b.circle(20, 180)
    b.right(180)
    b.circle(20, 180)
    b.penup()
    b.goto(10, -5)
    b.pendown()
    b.pensize(3)
    b.begin_fill()
    b.fillcolor('black')
    b.circle(10, 360)
    b.end_fill()

def whiskers1(x):
    """Draws right whiskers"""
    x.penup()
    x.goto(10, 0)
    x.pendown()
    x.right(70)
    x.forward(100)
    x.penup()
    x.goto(10, -5)
    x.pendown()
    x.right(20)
    x.forward(100)

def whiskers2(x):
    """draws left whiskers"""
    x.penup()
    x.goto(0, 0)
    x.pendown()
    x.left(165)
    x.forward(100)
    x.penup()
    x.goto(0,-5)
    x.pendown()
    x.left(20)
    x.forward(100)


def main():
    """sets window and turtles"""
    wn = turtle.Screen()
    wn.bgcolor("#65A2FD")
    Cat = turtle.Turtle()
    Tux = turtle.Turtle()
    Bob = turtle.Turtle()

    """Turtle design"""
    Cat.hideturtle()
    Tux.hideturtle()
    Bob.hideturtle()
    Cat.color('orange')
    Tux.color('orange')
    Cat.pensize(3)
    Tux.pensize(3)
    """Draws Cat's head"""
    Cat.penup()
    Cat.goto(0, -70)
    Cat.pendown()
    Cat.begin_fill()
    Cat.fillcolor("orange")
    Cat.circle(100)
    Cat.end_fill()
    """Right Ear"""
    Tux.penup()
    Tux.goto(30, 120)
    Tux.pendown()
    Ear1(Tux)

    """Left Ear"""
    Tux.penup()
    Tux.goto(-50, 120)
    Tux.pendown()
    Ear2(Tux)

    """Creates Eyes"""
    Bob.penup()
    Bob.goto(35, 40)
    EyeColor(Bob)
    Bob.goto(-35, 40)
    EyeColor(Bob)
    """Mouth and nose"""
    mouth(Bob)
    whiskers1(Bob)
    whiskers2(Bob)
    """Says meow"""
    Cat.penup()
    Cat.goto(-200, 0)
    Cat.pendown()
    Cat.color('black')
    Cat.write("Meow", font=("Arial", 20, "bold"))
    wn.exitonclick()



main()



