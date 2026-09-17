
#################################################################################
# Author: Makayla Jones
# Username: MakaylaJones90e4
#
# Assignment: Hw3
# Purpose:
# Google Doc Link:https://docs.google.com/document/d/1AzS2gjtqboie09I6Rc8EHFkJDg7CB9_1g6C9EeOJXIo/edit?tab=t.0
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################


import turtle

wn = turtle.Screen()
turtle.colormode(255)
wn.bgcolor(230, 34, 138)
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

def draw_circle(t, color, radius, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_ears(t):
    draw_circle(t, "#E67E22", 45, -75, 75)
    draw_circle(t, "#E67E22", 45, 75, 75)
    draw_circle(t, "pink", 22, -75, 95)
    draw_circle(t, "pink", 22, 75, 95)

def draw_face(t):
    draw_circle(t, "#E67E22", 100, 0, -85)
    draw_circle(t, "white", 35, -25, -20)
    draw_circle(t, "white", 35, 25, -20)

def draw_eyes(t):
    draw_circle(t, "white", 22, -45, 15)
    draw_circle(t, "white", 22, 45, 15)
    draw_circle(t, "black", 10, -45, 15)
    draw_circle(t, "black", 10, 45, 22)

def draw_nosemouth(t):
    t.penup()
    t.goto(-15, 15)
    t.pendown()
    t.color("black")
    t.begin_fill()
    for _ in range(3):
        t.forward(30)
        t.right(120)
    t.end_fill()
    t.penup()
    t.goto(0, -11)
    t.setheading(270)
    t.pendown()
    t.width(4)
    t.forward(25)
    t.width(1)

def draw_stripes(t):
    t.color("black")
    t.width(6)
    t.penup()
    t.goto(0, 115)
    t.setheading(270)
    t.pendown()
    t.forward(35)
    t.penup()
    t.goto(-100, 15)
    t.setheading(0)
    t.pendown()
    t.forward(30)
    t.penup()
    t.goto(100, 15)
    t.setheading(180)
    t.pendown()
    t.forward(30)
    t.width(1)
    t.setheading(0)

def draw_grass(t):
    t.color("green")
    t.width(6)
    t.penup()
    t.goto(-180, -180)
    t.pendown()
    t.goto(-150, -120)
    t.goto(-120, -180)
    t.goto(-90, -105)
    t.goto(-60, -180)
    t.penup()
    t.goto(60, -180)
    t.pendown()
    t.goto(90, -105)
    t.goto(120, -180)
    t.goto(150, -120)
    t.goto(180, -180)
    t.width(1)

draw_grass(t)
draw_ears(t)
draw_face(t)
draw_eyes(t)
draw_stripes(t)
draw_nosemouth(t)
wn.exitonclick()


# def function_2():
#     """
#     Example docstring for function_2. function_2 is not a good function name and should be changed.
#     """
#     pass
#     # ...
#
#
# def main():
#     """
#     Docstring for main. Should describe the main functionality of this file.
#     """
#
#     # Function calls to function_1 and function_2.
#     function_1()            # TODO  Remove when you replace it with your function
#     function_2()            # TODO  Remove when you replace it with your function


main()  # Starts the program!