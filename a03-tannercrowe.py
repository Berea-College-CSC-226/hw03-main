#################################################################################
# Author: Tanner Crowe
# Username: TannerCrowe
#
# Assignment: Homework a03
# Purpose: Designing objects and using different colors.
#################################################################################
# Google Document: https://docs.google.com/document/d/1pdOD4_06ODrgqR11LQO3PXbS2jpj591w86SUGjg6deU/edit?usp=sharing
#################################################################################

import turtle                                                                 #imported my turtle

wn=turtle.Screen()
wn.bgcolor('#DDDDDD')
alex = turtle.Turtle()                                                        # alex is the name of my turtle
alex.hideturtle()


def function_1():
    """
    This function draw the main base of my house.
    :return:
    """
    alex = turtle.Turtle()                                                    # main base of my house
alex.color('black')
alex.fillcolor('black')
alex.begin_fill()
for side in range(2):
    alex.forward(160)
    alex.right(90)
    alex.forward(200)
    alex.right(90)
alex.end_fill()


def function_2():
    """
    This function draws the roof to my house.
    :return:
    """
    alex.turtle.Turtle()                                                       # roof of my house
alex.color('red')
alex.begin_fill()
for sides in range (3):
    alex.forward(159)
    alex.left(120)
    alex.penup()
alex.end_fill()


def function_3():
    """
    This function draws the door to my house.
    :return:
    """
    alex = turtle.Turtle()                                                     # door for my house
alex.setpos(105,-134)
alex.pendown()
alex.color('white')
alex.begin_fill()
for shape in range(2):
    alex.forward(-50)
    alex.left(90)
    alex.forward(-60)
    alex.left(90)
alex.end_fill()


def function_4():
    """
    This function draws the first window in my house.
    :return:
    """
    alex.turtle.Turtle()                                                        # window 1 for my house
alex.penup()
alex.setpos(35,-75)
alex.pendown()
alex.begin_fill()
for shape in range (2):
    alex.forward(-25)
    alex.right(90)
    alex.forward(-25)
    alex.right(90)
alex.end_fill()


def function_5():
    """
    This function draws the second window in my house.
    :return:
    """
    alex = turtle.Turtle()                                                     # window 2 for my house
alex.penup()
alex.forward(80)
alex.pendown()
alex.begin_fill()
for shape in range(2):
    alex.forward(25)
    alex.left(90)
    alex.forward(25)
    alex.left(90)
alex.end_fill()
alex.hideturtle()


def main():
    function_1()                                                               # my def main function
    function_2()
    function_3()
    function_4()
    function_5()


wn.exitonclick()





