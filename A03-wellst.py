######################################################################
# Author: Taran Wells
# Username: wellst

# Assignment: A03

# Google Doc: https://docs.google.com/document/d/1uj7Hv_qp2zfqIw7q3sqYZJOlEyW1dOsclKZS3rBcXlM/edit?usp=sharing

######################################################################

import turtle               # allows us to use the turtles library

wn = turtle.Screen()


def house_grass(t, sz):
    """Grass of house"""

    t.color(124, 252, 0)     # grass green
    t.pendown()
    t.begin_fill()
    for side in range(2):
        t.forward(sz)
        t.right(90)             # square grass patches
        t.forward(sz)
        t.right(90)
    t.end_fill()
    t.penup()


def house_base(t, sz):
    """Base of house"""

    t.color(255, 69, 0)     # house orange
    t.pendown()
    t.begin_fill()
    for side in range(2):
        t.forward(sz)
        t.right(90)             # square house
        t.forward(sz)
        t.right(90)
    t.end_fill()
    t.penup()


def house_roof(t1, sz):
    """Roof of house"""
    t1.color(135, 30, 160)       # roof purple
    t1.begin_fill()
    for side in range(3):
        t1.forward(sz)           # shape roof
        t1.left(120)
    t1.end_fill()
    t1.penup()


def house_window(t3):
    """window on house"""
    t3.color(0, 0, 0)
    t3.begin_fill()
    for side in range(4):
        t3.fd(35)
        t3.right(90)
    t3.fillcolor(30, 135, 160)      # make window light blue
    t3.end_fill()


def main():
    wn.colormode(255)

    # setup turtles
    base = turtle.Turtle()
    base.hideturtle()
    roof = turtle.Turtle()
    roof.hideturtle()
    glass = turtle.Turtle()
    glass.hideturtle()
    wn.bgcolor("blue")

    roof.penup()
    roof.back(30)
    roof.pendown()

    house_base(base, 140)

    house_roof(roof, 200)

    glass.penup()
    glass.fd(70)
    glass.right(90)
    glass.fd(70)
    glass.pendown()
    house_window(glass)
    glass.left(90)
    house_window(glass)
    glass.left(90)
    house_window(glass)
    glass.left(90)
    house_window(glass)

    base.lt(90)
    base.bk(140)
    base.rt(90)
    house_grass(base, 1000)
    base.rt(90)
    house_grass(base, 1000)

    roof.penup()
    roof.bk(200)
    roof.color(255, 255, 0)
    roof.pendown()
    roof.begin_fill()
    roof.circle(75)        # makes the sun
    roof.end_fill()


main()     # calls on main function
wn.exitonclick()
