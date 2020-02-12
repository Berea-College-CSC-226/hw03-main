######################################################################
# Author: Zach Neill
# Username: zachneill
# Assignment: A03: A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: create a small group of houses
# Google Doc Link: https://docs.google.com/document/d/1VfLZ3YZHtOkuD6xTmwszyaBVpT-0YcORDvjXixXiIDM/edit?usp=sharing
#################################################################################
# Acknowledgements:
# Everything was painstakingly typed by me.
#################################################################################
import turtle
# global variables so houses can be different locations
hx = 0
hy = 0


def roof(shape, x, y, color):
    # creates the triangular roof
    global hx
    global hy
    shape.setpos(x + 25 + hx, y + 200 + hy)
    shape.color(color)
    shape.showturtle()
    shape.stamp()
    shape.hideturtle()


def box(shape, width, height):
    # makes a rectangle of chosen sizes used in house frame, chimney, window, door
    shape.begin_fill()
    for line in range(2):
        shape.fd(width)
        shape.lt(90)
        shape.fd(height)
        shape.lt(90)
    shape.end_fill()


def make_circle(shape, r, g, b, size, x, y):
    # creates a circle used for the doorknob and for the smoke
    global hx
    global hy
    shape.hideturtle()
    shape.setpos(x + hx, y + hy)
    shape.turtlesize(size)
    shape.color(r, g, b)
    shape.showturtle()
    shape.stamp()


def fd_lt(shape):
    # used a lot in function window so call this to make it easier to read
    shape.lt(90)
    shape.fd(35)


def window(x, y, shape):
    # creates a window
    global hx
    global hy
    shape.setpos(x + hx, y + hy)
    shape.pendown()
    shape.showturtle()
    box(shape, 70, 70)
    # make inside frame of window
    fd_lt(shape)
    shape.rt(90)
    shape.fd(70)
    fd_lt(shape)
    fd_lt(shape)
    shape.lt(90)
    shape.fd(70)
    shape.penup()
    shape.hideturtle()
    # face original direction
    shape.lt(90)


def door(shape, x, y):
    # creates the door to the house
    global hx
    global hy
    shape.setpos(x + hx, y + hy)
    shape.pendown()
    box(shape, 40, 70)
    shape.penup()


def chimney(shape, x, y):
    # creates the chimney
    shape.setpos(x + 30 + hx, y + 200 + hy)
    shape.pendown()
    box(shape, 40, 70)
    shape.penup()


def building(shape, x, y, color):
    # creates a house frame
    global hx
    global hy
    shape.setpos(x + hx, y + hy)
    shape.fillcolor(color)
    shape.pendown()
    box(shape, 250, 200)
    shape.penup()
    # calls and makes the chimney
    chimney(shape, x, y)


def smoke(shape):
    # creates 3 circles of smoke out of the chimney
    global hx
    global hy
    make_circle(shape, 211, 211, 211, 1.2, -100, 91)
    make_circle(shape, 211, 211, 211, 1.6, -80, 111)
    make_circle(shape, 211, 211, 211, 2, -55, 121)


def house(wall, rf, twin, dr, shape, h_color, r_color):
    # makes a house out of previous functions
    building(wall, -150, -200, h_color)
    roof(rf, -150, -200, r_color)
    smoke(shape)
    window(-130, -100, twin)
    door(dr, 0, -200)
    make_circle(shape, 255, 255, 10, .5, 10, -180)


def main():
    # make hx and hy variables usable on main
    global hx
    global hy
    wn = turtle.Screen()  # Set up the window and its attributes
    wn.bgcolor("green")
    wn.colormode(255)
    wn.register_shape("triangle", ((-50, 0), (100, 90), (250, 0)))
    # roof variable
    rf = turtle.Turtle()
    rf.speed("fastest")
    rf.hideturtle()
    rf.penup()
    rf.shape("triangle")
    rf.lt(90)
    # window variable
    twin = turtle.Turtle()
    twin.hideturtle()
    twin.penup()
    twin.shape("square")
    twin.color(0, 234, 125)
    twin.pencolor(0, 57, 255)
    twin.speed("fastest")
    twin.pensize(5)
    # building and chimney variable
    wall = turtle.Turtle()
    wall.hideturtle()
    wall.pensize(15)
    wall.penup()
    wall.shape("square")
    wall.color("black")
    wall.speed("fastest")
    # door variable
    dr = turtle.Turtle()
    dr.hideturtle()
    dr.penup()
    dr.shape("square")
    dr.color(150, 80, 0)
    dr.pencolor(0, 0, 0)
    dr.speed("fastest")
    dr.pensize(3)
    # smoke and doorknob variable
    circle = turtle.Turtle()
    circle.hideturtle()
    circle.penup()
    circle.shape("circle")
    circle.color(180, 100, 10)
    circle.pencolor(0, 0, 0)
    circle.speed("fastest")
    circle.pensize(3)

    # make neighborhood out of houses
    house(wall, rf, twin, dr, circle, "red", "white")

    hx = 280
    hy = 200
    house(wall, rf, twin, dr, circle, "blue", "black")

    hx = -280
    hy = -210
    house(wall, rf, twin, dr, circle, "gray", "yellow")

    hx = 280
    hy = -200
    house(wall, rf, twin, dr, circle, (50, 205, 50), "white")

    hx = -280
    hy = 210
    house(wall, rf, twin, dr, circle, "orange", "gray")

    wn.exitonclick()


main()
