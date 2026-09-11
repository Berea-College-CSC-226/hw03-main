#################################################################################
# Author: Michael Damdinsuren
# Username: damdinsurenm2
#
# Assignment: Turtle Project
# Purpose: Make design using turtles
# Google Doc Link: https://docs.google.com/document/d/1gIlcfwIxLvQ4U5u7RQEEqbjnZf8J-Sm4ciO3QzV_nLE/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################


import turtle, random


def draw_grass(shape):
    """
    Example docstring for function_1. function_1 is not a good function name and should be changed.
    """
    shape.color("green")
    shape.teleport(-330, -300)
    shape.fillcolor("green")

    shape.begin_fill()

    shape.left(90)
    shape.forward(220)
    shape.right(90)
    shape.forward(700)
    shape.right(90)
    shape.forward(220)

    shape.end_fill()
    shape.setheading(0)

def draw_house_frame(shape):
    """
    Example docstring for function_1. function_1 is not a good function name and should be changed.
    """
    shape.color("white")
    shape.teleport(-100,-100)
    shape.fillcolor("white")

    shape.begin_fill()

    shape.left(90)
    shape.forward(150)
    shape.right(90)
    shape.forward(200)
    shape.right(90)
    shape.forward(150)
    shape.right(90)
    shape.forward(200)

    shape.end_fill()
    shape.setheading(0)

def draw_roof(wn, shape):
    """
        Example docstring for function_1. function_1 is not a good function name and should be changed.
    """
    wn.register_shape("./Bricks.gif")
    shape.penup()
    shape.setpos(0, 110)
    shape.pendown()
    shape.shape("./Bricks.gif")
    shape.stamp()

def draw_door(shape):

    shape.color("red")
    shape.teleport(-30, -100)
    shape.fillcolor("red")

    shape.begin_fill()

    shape.left(90)
    shape.forward(100)
    shape.right(90)
    shape.forward(60)
    shape.right(90)
    shape.forward(100)
    shape.right(90)
    shape.forward(60)

    shape.end_fill()
    shape.setheading(0)

def draw_door_handle(shape):

    shape.color("yellow")
    shape.teleport(20, -50)
    shape.shape("circle")
    shape.shapesize(0.5, 0.5)

    shape.stamp()

    shape.setheading(0)

def draw_window(shape, x, y):

    shape.teleport(x, y)
    shape.shape("circle")
    shape.shapesize(2.5, 2.5, 2)
    shape.pencolor("red")
    shape.fillcolor("yellow")
    shape.stamp()

    shape.pensize(2)
    shape.color("black")
    shape.shapesize(1, 1)
    shape.teleport(x - 23, y)
    shape.forward(46)
    shape.teleport(x, y + 23)
    shape.right(90)
    shape.forward(46)
    shape.pensize(1)

    shape.setheading(0)

def draw_sun(wn, shape):
    """
        Example docstring for function_1. function_1 is not a good function name and should be changed.
    """
    shape.color("yellow")
    shape.teleport(-210, 190)
    shape.shape("circle")
    shape.shapesize(5, 5)
    shape.stamp()

    shape.pensize(2)
    angle = 20
    for i in range(8):
        shape.teleport(-210, 190)
        shape.setheading(angle)
        shape.forward(100)
        angle = angle + 45

    shape.setheading(0)

def draw_cloud(wn, shape):
    """
        Example docstring for function_1. function_1 is not a good function name and should be changed.
    """
    for i in range(40):
        x = random.randint(50, 250)
        y = random.randint(200, 240)
        size = random.randint(20, 70)
        shape.teleport(x, y)
        shape.dot(size, "white")

def draw_bush(wn, shape):
    """
        Example docstring for function_1. function_1 is not a good function name and should be changed.
    """
    a = [-200, 200]
    b = [-200, -180]
    wn.register_shape("./bush.png")

    for i in range(2):
        shape.penup()
        shape.setpos(a[i], b[i])
        shape.pendown()
        shape.shape("./bush.png")
        shape.stamp()

def main():
    """
    Docstring for main. Should describe the main functionality of this file.
    """
    wn = turtle.Screen()
    wn.colormode(255)
    wn.bgcolor(144,213,255)

    shape = turtle.Turtle()
    shape.hideturtle()

    draw_grass(shape)
    draw_house_frame(shape)
    draw_roof(wn, shape)
    draw_door(shape)
    draw_door_handle(shape)
    draw_window(shape, 65, -20)
    draw_window(shape, -65, -20)
    draw_sun(wn, shape)
    draw_cloud(wn, shape)
    draw_bush(wn, shape)

    wn.exitonclick()

main()