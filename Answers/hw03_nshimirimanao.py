#################################################################################
# Author: Briana Nshimirimana
# Username: Nshimirimanao
#
# Assignment: HW03_Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Learning how to write functions and using the turtle library
# Google Doc Link: https://docs.google.com/document/d/1ZtcYU7PHItUzZ4hzqbLtUHBl__7jwoWPN-NipuDiB8Q/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
# hw03_stubs_do_not_edit.py
#
#################################################################################


import turtle


def draw_sun(t):
    """
    Uses turtle to draw sun on top and below the horizon.
    """
    t.hideturtle()
    t.penup()
    t.goto(0,-40)
    t.pendown()

    t.begin_fill() #t draws a circle and fills it in.
    t.circle(40)
    t.end_fill()


def Horizon(Hz):
    """
     Uses turtle to draw a horizontal line across the screen to signify the horizon.
    """
    Hz.hideturtle()
    Hz.penup()
    Hz.goto(-700,0)
    Hz.pendown()
    Hz.fd(1400)


def draw_birds(bd,dist):
    """
         Uses turtle to draw birds off in the horizon.
    """


    bd.hideturtle()
    for i in range(2):
        bd.penup()
        bd.goto(dist)
        bd.pendown()

    # drawing the 2 birds
        bd.left(45)
        bd.fd(30)
        bd.right(45)
        bd.fd(10)
        bd.left(45)
        bd.fd(10)
        bd.right(45)
        bd.fd(30)
        dist = (120,120) #changing the distance for the second loop.






def main():
    """
    Docstring for main. Should describe the main functionality of this file.
    """
    wn = turtle.Screen()
    wn.bgcolor("blue") #making my background blue

    # making t a turtle object and making the color orangered
    t = turtle.Turtle()
    t.color("orange""red")
    t.speed(0) #fastest speed

    # making Hz a turtle object and making the color darkblue
    Hz = turtle.Turtle()
    Hz.speed(0) #fastest speed
    Hz.color("darkblue")

    # making bd a turtle object and making the color black
    bd = turtle.Turtle()
    bd.speed(0) #fastest speed
    bd.color("black")
    dist = (-100,100)



    # calling functions to run
    draw_sun(t)
    Horizon(Hz)
    draw_birds(bd,dist)

    print("Enjoy the sunset!") # prints when done drawing

    wn.exitonclick() # holding window screen open until user clicks on it to close


main()  # Starts the program!