#################################################################################
# Author: Mauricha Davis
# Username: davism5
#
# Assignment: HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose:
# Google Doc Link: https://docs.google.com/document/d/1GffD-r3WjBjP_JdkNARFkIGOf5sZ6pIk-gUKqU8K7fQ/edit?usp=sharing
#
#################################################################################

import turtle

def house(t):
    for i in range(4):
        t.forward(300)
        t.left(90)
    return t

def roof(t):
    for i in range(1):
         t.left(140)
         t.forward(250)
         t.left(77)
         t.forward(260)
         t.left(143)
         t.forward(390)

    return t


def tree(t):
    for i in range(2):
        t.forward(100)
        t.left(90)
        t.forward(200)
        t.left(90)

    return t

def window_door(t):
    for i in range(2):
        t.forward(120)
        t.left(90)


    return t

def create_turtle(pensize, color):
    t_turtle=turtle.Turtle()
    t_turtle.pensize(pensize)
    t_turtle.color(color)

    return t_turtle

def main():
    wn=turtle.Screen()
    wn.bgcolor('lightblue')
    wn.screensize(canvwidth=600, canvheight=600)

    t_house= create_turtle(pensize=10, color="hotpink")
    t_house.penup()
    t_house.setposition(-280, -280)
    t_house.pendown()

    t_house.color('hotpink')
    t_house.begin_fill()
    for n in range(4):
        t_house.forward(400)
        t_house.left(90)
    t_house.end_fill()

    t_roof= create_turtle(pensize=10, color="purple")
    t_roof.penup()
    t_roof.setposition(123,123)
    t_roof.pendown()

    t_roof.color('purple')
    t_roof.begin_fill()
    for n in range(1):
        t_roof.left(140)
        t_roof.forward(250)
        t_roof.left(77)
        t_roof.forward(260)
        t_roof.left(143)
        t_roof.forward(390)
    t_roof.end_fill()

    t_tree= create_turtle(pensize=5, color="brown")
    t_tree.penup()
    t_tree.setposition(280,-280)
    t_tree.pendown()

    t_tree.color('brown')
    t_tree.begin_fill()

    for side in range(2):
        t_tree.forward(100)
        t_tree.left(90)
        t_tree.forward(200)
        t_tree.left(90)
    t_tree.end_fill()

    t_tree.color('green')
    t_tree.begin_fill()
    t_tree.penup()
    t_tree.setposition(335,-90)
    t_tree.pendown()
    t_tree.color("green")
    t_tree.circle(120)
    t_tree.end_fill()

    t_window_door = create_turtle(pensize=2, color="brown")
    t_window_door.penup()
    t_window_door.setposition(-130,-30)
    t_window_door.pendown()


    t_window_door.color('black')
    for i in range(4):
        t_window_door.forward(120)
        t_window_door.left(90)


    wn.exitonclick()

main()









