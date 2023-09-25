######################################################################
# Author: Beth Mason
# Username: Masone2
# Assignment: HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: To demonstrate the turtle library, funcshons, and git
# google doc link: https://docs.google.com/document/d/1uEDcJfrSPKVqRZIrBYCS930wwOhCPhb6U_Q640EEbRM/edit?usp=sharing
######################################################################
# Acknowledgements:
#HW02: Loopy Turtles, Loopy Languages and its assosiated acknowledgments
######################################################################
import turtle
import random
import math

def full_head(catpill):
    """makes the head of the full catipiller"""
    catpill.goto(0, 70)
    catpill.left(135)
    catpill.fillcolor("crimson")
    catpill.begin_fill()
    catpill.circle(45, 170)
    catpill.end_fill()
def full_mouth(catpill):
    """makes the mouth of the full catipiller"""
    catpill.goto(-47, 53)
    catpill.fillcolor("saddle brown")
    catpill.begin_fill()
    catpill.circle(5)
    catpill.end_fill()
def full_body(catpill):
    """makes the body of the full catipiller"""
    catpill.goto(-69, 12)
    catpill.right(45)
    catpill.fillcolor(random.randrange(170), random.randrange(170, 256), random.randrange(170))
    catpill.begin_fill()
    catpill.circle(70, )
    catpill.end_fill()
def full_anteni(catpill):
    """makes the anteni of the full catipiller"""
    catpill.goto(-45, 80)
    catpill.right(140)
    catpill.color("purple")
    catpill.pendown()
    for size in range(10, 20):
        catpill.pensize(size)
        catpill.forward(3)
    catpill.penup()
    catpill.left(20)
    catpill.goto(-68, 64)
    catpill.pendown()
    for size in range(10, 20):
        catpill.pensize(size)
        catpill.forward(3)
    catpill.penup()
def full_eyes(catpill):
    """makes the eyes of the full catipiller"""
    catpill.pensize(5)
    catpill.shape("circle")
    catpill.color("green")
    catpill.shapesize(.5)
    catpill.goto(-40, 70)
    catpill.stamp()
    catpill.goto(-60, 55)
    catpill.stamp()
def full_belly_button(catpill):
    """makes the belly button of the full catipiller"""
    bp = 20
    catpill.goto(bp, bp)
    catpill.pendown()
    for i in range (4):
        catpill.forward(15)
        catpill.backward(15)
        catpill.right(90)
    catpill.penup()
def full_legs(catpill):
    """makes the legs on the full catipiller"""
    catpill.goto(-29, 33)
    catpill.left(20)
    catpill.pendown()
    catpill.forward(30)
    catpill.penup()
    catpill.goto(60, -20)
    catpill.left(70)
    catpill.pendown()
    catpill.forward(20)
    catpill.penup()
    catpill.goto(59, 11)
    catpill.left(180)
    catpill.pendown()
    catpill.forward(20)
    catpill.penup()
    catpill.goto(14, 60)
    catpill.left(50)
    catpill.pendown()
    catpill.forward(20)
    catpill.penup()
def full_outcome(text, catpill):
    """ends the program by showing the catipiller must have been full and that if why he didnt eat food"""
    text.goto(0, -160)
    text.write("must have already been full!", move=False, align='center', font=("Arial", 30, ("bold", "normal")))

    catpill.speed(0)

    full_head(catpill)
    full_mouth(catpill)
    full_body(catpill)
    full_anteni(catpill)
    full_eyes(catpill)
    full_belly_button(catpill)
    full_legs(catpill)

def exsploed_outcome(text, catpill):
    """ends the program by showing that catipiller exsploed from eating to much"""
    catpill.speed(0)
    catpill.goto(-95,20)
    catpill.fillcolor("red")
    catpill.begin_fill()
    for i in range(6):
        catpill.circle(20, -210)
        catpill.right(180)
        catpill.forward(30)
        catpill.circle(20, 150)
        catpill.forward(30)
        catpill.right(180)
    catpill.end_fill()

    text.goto(0, -160)
    text.write("ate too much and exsploded!", move=False, align='center', font=("Arial", 30, ("bold", "normal")))

def normal_body(catpill, food):
    """makes a body segmint for each frute he ate"""
    x = -310
    y = -60
    for segments in range(food):
        catpill.goto(x, y)
        catpill.fillcolor(random.randrange(170), random.randrange(170, 256), random.randrange(170))
        catpill.begin_fill()
        catpill.circle(60)
        catpill.end_fill()
        catpill.pendown()
        catpill.right(68)
        catpill.forward(15)
        catpill.backward(15)
        catpill.right(45)
        catpill.forward(15)
        catpill.backward(15)
        catpill.left(113)
        catpill.penup()
        x = x + 30
        y = 12 * math.sin(x) - 60
def normal_head(catpill):
    """makes the head"""
    catpill.forward(40)
    catpill.right(90)
    catpill.forward(5)
    catpill.left(90)
    catpill.fillcolor("crimson")
    catpill.begin_fill()
    catpill.circle(70)
    catpill.end_fill()
def normal_mouth(catpill):
    """makes hte mouth"""
    catpill.color("saddle brown")
    catpill.pensize(10)
    catpill.forward(40)
    catpill.left(90)
    catpill.forward(60)
    catpill.pendown()
    catpill.circle(40, -180)
    catpill.penup()
def normal_eyes(catpill):
    """makes the eyes"""
    catpill.shape("circle")
    catpill.left(180)
    catpill.forward(30)
    catpill.right(90)
    for i in range(2):
        catpill.forward(20)
        catpill.color("gold")
        catpill.shapesize(1)
        catpill.stamp()
        catpill.shapesize(.8)
        catpill.color("green")
        catpill.stamp()
        catpill.forward(20)
def normal_anteni(catpill):
    """makes the anteni"""
    catpill.color("purple")
    catpill.backward(20)
    catpill.left(90)
    catpill.forward(30)
    catpill.pendown()
    catpill.right(23)
    for size in range(10, 20):
        catpill.pensize(size)
        catpill.forward(3)
    catpill.penup()
    catpill.backward(30)
    catpill.right(67)
    catpill.backward(40)
    catpill.left(113)
    catpill.pendown()
    for size in range(10, 20):
        catpill.pensize(size)
        catpill.forward(3)
def normal_text(text, food):
    text.goto(0, -160)
    bottom_text = 'ate ' + str(food) + ' frutes'
    text.write(bottom_text, move=False, align='center', font=("Arial", 30, ("bold", "normal")))
def normal_outcome(text, catpill, food):
    normal_body(catpill, food)
    normal_head(catpill)
    normal_mouth(catpill)
    normal_eyes(catpill)
    normal_anteni(catpill)
    normal_text(text, food)

def main():
    wn = turtle.Screen()
    wn.bgcolor("old lace")
    wn.colormode(255)

    catpill = turtle.Turtle()
    catpill.hideturtle()
    catpill.penup()

    text = turtle.Turtle()
    text.hideturtle()
    text.color("dark green")
    text.penup()

    text.goto(0, 160)
    text.write("The Very Hungry Caterpillar ", move=False, align='center', font=("Arial", 30, ("bold", "normal")))

    food = int(wn.textinput("how much he eat?!?", "how many frutes did the very hungry caterpillar eat? "))

    if food < 1:
        full_outcome(text, catpill)
    elif food >20:
        exsploed_outcome(text, catpill)
    else:
        normal_outcome(text, catpill, food)

    wn.exitonclick()


main()
