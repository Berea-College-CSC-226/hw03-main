#################################################################################
# Author: Brandon Atu
# Username: Atu175
#
# Assignment: A03
# Purpose: Making branches
# Google Doc Link: https://docs.google.com/document/d/1c5eu4vL2XOw1urT8wXGVSEBSlOtsq3Ih0KEi_JZgfmU/edit?usp=sharing
#
#################################################################################
# Acknowledgements: Used the code for writing labels from a02
#
#
#################################################################################

import turtle

turt = turtle.Turtle()


def write_title():    # Writing thr title under the diagram
    """
    Writing the title
    :return: None
    """
    turt.penup()
    turt.goto(0, -200)
    turt.pendown()
    turt.color('#000000')
    turt.left(-90)
    turt.write("Home Sweet Home", move=False, align='center', font=("Arial", 32, ("bold", "normal")))


def draw_tree():         # Drawing a tree beside the house
    """

    :return: None
    """
    turt.penup()
    turt.goto(-300, -100)
    turt.pendown()
    turt.right(-120)
    turt.color('#9C661F')
    turt.begin_fill()
    for i in range(2):
        turt.forward(10)
        turt.left(90)
        turt.forward(250)
        turt.left(90)
    turt.end_fill()
    turt.left(90)
    turt.forward(250)
    turt.left(-90)
    turt.forward(100)
    turt.left(90)
    turt.color('#008000')
    turt.begin_fill()
    turt.circle(100, 360)
    turt.end_fill()


def draw_moon():                 # Drawing the moon
    """

    :return: None
    """
    turt.left(60)
    turt.penup()
    turt.goto(250, 280)
    turt.pendown()
    turt.left(60)
    turt.color('#FFFFFF')
    turt.begin_fill()
    turt.circle(50, 180)
    turt.end_fill()


def draw_roof(turt):                  # Drawing the roof
    """

    :param turt: Drawing the roof
    :return: None
    """
    turt.color('#000000')
    turt.penup()
    turt.goto(-150, 100)
    turt.pendown()
    turt.begin_fill()
    turt.left(60)
    turt.forward(150)
    turt.left(-60)
    turt.forward(150)
    turt.left(-60)
    turt.forward(150)
    turt.end_fill()


def draw_window(turt):  # Drawing the window
    """

    :param turt: Drawing the window
    :return: None
    """
    turt.penup()
    turt.goto(55, 40)
    turt.pendown()
    turt.left(90)
    for i in range(4):
        turt.forward(50)
        turt.left(90)
    turt.penup()
    turt.goto(80, 40)
    turt.pendown()
    turt.right(-90)
    turt.forward(50)
    turt.right(90)


def draw_door(turt):
    """

    :param turt: Drawing the door
    :return: None
    """
    turt.color('#0000FF')
    turt.penup()
    turt.forward(120)
    turt.pendown()
    turt.begin_fill()
    turt.left(90)
    turt.forward(90)
    turt.right(90)
    turt.forward(60)
    turt.right(90)
    turt.forward(90)
    turt.end_fill()


def build_body(turt):
    """

    :param turt: Building the body
    :return: None

    """
    turt.penup()
    turt.goto(-150, -100)
    turt.pendown()
    turt.color('#FF0000')
    turt.begin_fill()
    for i in range(2):
        turt.forward(300)
        turt.left(90)
        turt.forward(200)
        turt.left(90)
    turt.end_fill()


def main():
    """
    This enables  the other functions to function

    """
    # ...
    wn = turtle.Screen()
    wn.bgcolor('#808080')
    head = 0
    turt.pensize(5)
    build_body(turt)
    draw_door(turt)
    draw_window(turt)
    draw_roof(turt)
    draw_moon()
    draw_tree()
    write_title()
    turt.hideturtle()

    wn.exitonclick()


main()



