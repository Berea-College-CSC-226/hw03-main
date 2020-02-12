################################################################################
# Author: Sreynit Khatt
# Username: khatts
#
# Assignment: A03-  A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Continue practicing creating and using functions.
# More practice on using the turtle library.
# Learn about how computers represent colors.
# Learn about source control and git.
# Google Doc Link: https://docs.google.com/document/d/1n2OCQ609UmhUfsZfULFk00n2J-0kORAOPWE7uw0DzRI/edit#
#
#################################################################################
# Acknowledgements:
# Scott Heggen
#
#################################################################################

import turtle

wn = turtle.Screen()

def draw_backyard(back):
    back.penup()
    back.color("#00FF00")
    back.goto(-341.5, -288)
    back.pendown()
    back.begin_fill()
    for i in range(2):
        back.forward(683)
        back.left(90)
        back.forward(300)
        back.left(90)
    back.end_fill()
def draw_roof(r):
    r.color("#800000")
    r.penup()
    r.goto(-150, 50)
    r.pendown()
    r.begin_fill()
    r.forward(300)
    r.left(120)
    r.forward(100)
    r.left(60)
    r.forward(200)
    r.left(60)
    r.forward(100)
    r.end_fill()
    r.hideturtle()


def draw_body(b):
    b.color("#A9A9A9")
    b.penup()
    b.goto(-150, 50)
    b.pendown()
    b.begin_fill()
    for i in range(4):
        b.forward(300)
        b.right(90)
    b.end_fill()
    b.hideturtle()

def draw_windows(w):
    w.penup()
    w.goto(-125,-50)
    w.pendown()
    w.color("#8B4513")
    w.begin_fill()
    for i in range(4):
        w.forward(50)
        w.left(90)
    w.end_fill()
    w.penup()
    w.goto(75, -50)
    w.pendown()
    w.color("#8B4513")
    w.begin_fill()
    for i in range(4):
        w.forward(50)
        w.left(90)
    w.end_fill()
    w.hideturtle()



def draw_doors(d):
    d.penup()
    d.goto(-50, -250)
    d.pendown()
    d.color("#8B4513")
    d.begin_fill()
    for i in range(2):
        d.forward(100)
        d.left(90)
        d.forward(150)
        d.left(90)
    d.end_fill()
    d.hideturtle()

def draw_chick(chic):
    wn.register_shape("chick-transparent-yellow2.gif")
    chic.penup()
    chic.goto(200,-230)
    chic.pendown()
    chic.shape("chick-transparent-yellow2.gif")

def draw_hen(hen):
    wn.register_shape("chicken_PNG2172.gif")
    hen.penup()
    hen.goto(250,-200)
    hen.pendown()
    hen.shape("chicken_PNG2172.gif")
def add_title(title):
    title.color("#FF00FF")
    title.penup()
    title.goto(0,0)
    title.write("Sreynit's Countryside House", align = 'center', font = ("Arial", 17, ("bold", "normal")))
    title.hideturtle()

def main():

    back = turtle.Turtle()
    draw_backyard(back)
    r = turtle.Turtle()
    draw_roof(r)
    b = turtle.Turtle()
    draw_body(b)
    w = turtle.Turtle()
    draw_windows(w)
    d = turtle.Turtle()
    draw_doors(d)
    chic = turtle.Turtle()
    draw_chick(chic)
    hen = turtle.Turtle()
    draw_hen(hen)
    title = turtle.Turtle()
    add_title(title)
main()

wn.exitonclick()
