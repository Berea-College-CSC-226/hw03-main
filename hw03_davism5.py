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

def draw_house(t):
    """
        draw_house creates is the named function for the square of the hosuse.
        """
    for i in range(4):
        t.forward(300)
        t.left(90)

    return t

def draw_roof(t):
    """
        draw_roof is the name the turtle that is to create the roof of the house.
            """
    for i in range(1):
         t.left(140)
         t.forward(250)
         t.left(77)
         t.forward(260)
         t.left(143)
         t.forward(390)

    return t


def draw_tree(t):
    """
        draw_tree creates the truck of the tree and in main I use the same name to create the top.
        """
    for i in range(2):
        t.forward(100)
        t.left(90)
        t.forward(200)
        t.left(90)

    return t


def draw_door(t):
    for i in range(2):
        t.forward(100)
        t.left(90)
        t.forward(200)
        t.left(90)
    return t





def create_turtle(pensize, color):
    """
        Helps create customs settings for the turtles and is used to create a new turtle.
            """
    t_turtle=turtle.Turtle()
    t_turtle.pensize(pensize)
    t_turtle.color(color)

    return t_turtle

def main():
    """
        jdhkchof
        """
    wn=turtle.Screen()     #Set up the window and it's attributes
    wn.bgcolor('lightblue')
    wn.screensize(canvwidth=600, canvheight=600)

    t_draw_house= create_turtle(pensize=10, color="hotpink")
    t_draw_house.penup()
    t_draw_house.setposition(-280, -280)
    t_draw_house.pendown()

    t_draw_house.color('hotpink')
    t_draw_house.begin_fill()

    draw_house(t_draw_house)

    t_draw_house.end_fill()

    t_draw_roof= create_turtle(pensize=10, color="purple")
    t_draw_roof.penup()
    t_draw_roof.setposition(70,25)
    t_draw_roof.pendown()

    t_draw_roof.color('purple')
    t_draw_roof.begin_fill()

    draw_roof(t_draw_roof)

    t_draw_roof.end_fill()

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

    t_draw_door = create_turtle(pensize=2, color="black")
    t_draw_door.penup()
    t_draw_door.setposition(-180, -280)
    t_draw_door.pendown()
    t_draw_door.color('black')
    t_draw_door.begin_fill()

    draw_door(t_draw_door)

    t_draw_door.end_fill()


    wn.exitonclick()

main()









