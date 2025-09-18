#################################################################################
# Author: Rafael Hermoza Freitas
# Username: hermozafreitasr
#
# Assignment: Homework 3: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Understand the use of Github in our class and practice the use of functions with the turtle library
# Objective: Draw the letter S multiple times on the same origin using different orientations and sizes to draw a symmetric rose
# Google Doc Link: https://docs.google.com/document/d/1w3na4v43X3XTtP5udqPAMPljKMYfpp-VYHJuhq2COvw/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################


import turtle


def drawing_s(tur, size):
    """
    This function receives a turtles and draws the letter s on the screen, taking the origin as a start point
    """

    for i in range(18):
        tur.stamp()
        tur.penup()
        tur.forward(size)
        tur.pendown()
        tur.right(10)
    tur.penup()
    tur.goto(0, 0)
    tur.pendown()
    for i in range(18):
        tur.stamp()
        tur.forward(size)
        tur.left(-10)


def main():
    """
    main function, defines all the variables and calls the functions for drawing.
    """

    #defining variables

    #screen:
    wn = turtle.Screen()
    wn.colormode(255)
    wn.bgcolor(137,16,100)

    #turtles:
    rafael = turtle.Turtle()
   # rafael.shape("circle")
    rafael.pensize(4)
    rafael.pencolor(18,205, 205)
    rafael.speed("fastest")

    size=8
    # Function calls
    for i in range(19):
        drawing_s(rafael,size)

        rafael.right(20)
        if i % 2 == 0:
            size+=5
        else :
            size-=5

    wn.exitonclick() #finish the program when clicking the screen
    #end of main function definition


main()  # Starts the program!