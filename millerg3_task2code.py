# Author: Gavin Miller
# Username: millerg3
#
# Assignment: HW03
# Purpose: Create a complicated drawing (in this case, a measured person) using clean, conside code, functions, and loops
# Google Doc Link: https://docs.google.com/document/d/1ubqCXVn_pfDmnt3cz7FQ8piWil1egG5pBuyEQEn9wbA/edit?tab=t.0
#
#################################################################################
# Acknowledgements:
# None
#
#################################################################################

import turtle

def draw_head(size, alex):
    alex.penup()
    alex.goto(0,100)
    alex.pendown()
    for i in range(size):
        alex.forward(5)
        alex.right(5)
'''
Draw the head of person
Parameter 'size' = size of head, how many times turtle moves forward and right
Parameter 'alex' = turtle
'''
def draw_body(alex):
    alex.penup()
    alex.goto(0, -15)
    alex.pendown()
    alex.right(90)
    alex.forward(150)
    alex.right(180)
    alex.forward(75)
'''
Draw body of the person
Parameter 'alex' = turtle
'''

def draw_limbs(length, limbs, alex):
    for i in range(limbs):
        alex.left(135)
        alex.forward(length)
        alex.right(180)
        alex.forward(length)
        alex.right(90)
        alex.forward(length)
        alex.left(180)
        alex.forward(length)
        alex.penup()
        alex.setheading(270)
        alex.forward(length)
        alex.pendown()
        alex.setheading(90)
    '''
    Draw the arms and legs of the body using a for loop
    Length = how far forward alex moves
    Limbs = how many limbs the person has (4)
    Parameter 'alex' = turtle
    '''
def draw_mouth(alex):
    alex.penup()
    alex.goto(10, 10)
    alex.pendown()
    print(alex.pos())
    alex.color("red")
    alex.left(90)
    alex.forward(30)
    alex.right(180)
    alex.forward(40)
    alex.penup()
    alex.goto(-20, 65)
    alex.pendown()
'''
Draw the mouth!
Parameter 'alex' = turtle
'''
def draw_eyes(size, alex):
    alex.begin_fill()
    alex.color("blue")
    alex.fillcolor(87, 142, 73)
    for i in range(size):
        alex.forward(1)
        alex.right(5)
    alex.penup()
    alex.forward(50)
    alex.pendown()
    for i in range(size):
        alex.forward(1)
        alex.right(5)
    alex.end_fill()
'''
Draw the eyes using rgb color, for loop, and filled eyes.
Parameter 'size' = how many times the commands in the for loop (moving forward and looking right) are executed;
in other words, the size of his eyes. In future, naming this something like length likely makes more sense
Parameter 'alex' = turtle
'''
def draw_ruler(alex):
    alex.penup()
    alex.goto(-75, -217)
    print(alex.pos())
    alex.pendown()
    for i in range(63):
        alex.forward(5)
        alex.right(180)
        alex.forward(5)
        alex.right(90)
        alex.forward(5)
        alex.right(90)
    print(alex.pos())
    alex.forward(100)
    print("This guy is just under 316 pixels tall!")
    alex.left(90)
    alex.forward(50)
    alex.write("This guy is just under 316 pixels tall!")
'''
Draw ruler to measure his pixel height
Parameter 'alex' = turtle
'''

def main():
    screen = turtle.Screen()
    screen.bgcolor("pink")
    screen.colormode(255)
    alex = turtle.Turtle()
    print(alex.pos())
    alex.speed(0)
    draw_head(72, alex)
    draw_body(alex)
    draw_limbs(75, 2, alex)
    draw_mouth(alex)
    draw_eyes(72, alex)
    draw_ruler(alex)
    screen.exitonclick()

main()



