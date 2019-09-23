#################################################################################
# Author: Thy H. Nguyen
# Username: nguyent2
#
# Assignment: A03: A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Learning Objectives
# Grow to appreciate pair programming a little more.
# Continue practicing creating and using functions.
# More practice on using the turtle library.
# Learn about how computers represent colors.
# Learn about source control and git.
# Google Doc Link: https://docs.google.com/document/d/1ESXaEmAVPOV7Git4coeOZfVLM6Tuy64xYXGSnApyoww/edit?usp=sharing
#
#################################################################################
# Acknowledgements: Berea College
# Citation:
# https://www.w3schools.com/colors/colors_groups.asp (get color for the turtle)
# https://docs.python.org/3.3/library/turtle.html?highlight=turtle#
#################################################################################

import turtle
from time import sleep

def pythagore_triangle(c, b):
    """
    This function calculate the side of a right triangle using the Pythagore Theorem
    :param c:
    :param b:
    :return:
    """
    return ((c ** 2 - b ** 2) ** (0.5))


def draw_rectangle(thy,x,y):
    """
    This function draws a rectangle. As a swing will look like a rectangle
    :param thy:
    :param x:
    :param y:
    :return:
    """
    for i in range(2):
        thy.right(90)
        thy.forward(x)
        thy.right(90)
        thy.forward(y)

def draw_swing(thy):
    """
    This function draws a swing.
    :param thy:
    :param sides:
    :return:
    """
    #Construct tne swing with nearly a trapezoid
    thy.left(60)
    thy.forward(80)

    thy.right(60)
    thy.forward(100)

    thy.right(60)
    thy.forward(80)

    thy.penup()
    thy.right(120)
    thy.forward(180)

    thy.right(180)
    thy.forward(40)
    thy.left(90)
    sides = int((pythagore_triangle(80, 40)))
    thy.forward(sides / 4)

    thy.pendown()
    thy.forward(sides - sides / 4)

    thy.penup()
    thy.right(90)
    thy.forward(100)

    thy.pendown()
    thy.right(90)
    thy.forward(sides - sides / 4)
    thy.color("#800000")
    thy.begin_fill()
    draw_rectangle(thy, 100, 10)
    thy.end_fill()

def write_word(maithy, ask_color):
    """
    This function writes this is a swing
    :param maithy:
    :return:
    """
    maithy.penup()
    maithy.left(90)
    maithy.forward(75)
    maithy.right(90)
    maithy.forward(95)
    maithy.pendown()
    maithy.write("This is a " + ask_color + " swing", move=False, align="center", font=("Helvetica", 30, "bold"))
    #Print the color of the swing
def main():
    """
    Call all of the functions and set up all of the turtles as well as the background
    """
    ask_color = input("Enter a color: [pink], [red], [blue], [yellow]")
    sleep(2)
    wns = turtle.Screen()
    wns.setworldcoordinates(-5, -5, 200, 100)
    wns.bgcolor("#b3ffe6")
    thy = turtle.Turtle()
    if ask_color == "pink" or ask_color == "red" or ask_color == "blue" or ask_color == "yellow":
        thy.color(ask_color)
    else:
        ask_color = "purple"
        thy.color("purple")
    thy.pensize(3)
    maithy = turtle.Turtle()
    maithy.color("#000099")
    draw_swing(thy)
    write_word(maithy, ask_color)
    wns.exitonclick()

main()


