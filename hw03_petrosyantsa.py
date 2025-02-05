#################################################################################
# Author: Alina Petrosyants
# Username: petrosyantsa
#
# Assignment: HW03 coding part
# Purpose: to be able to structure the code and use functions
# Google Doc Link: https://docs.google.com/document/d/1DpBnaFCUQfxH7ogekAsqEz43IugeimAfZu72GTLsSbk/edit?tab=t.0
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################


import turtle

def big_square(the_drawing_turtle):
    #Draws a big square which is the house

    the_drawing_turtle.penup()
    the_drawing_turtle.goto(-100,-100)
    the_drawing_turtle.pendown()
    the_drawing_turtle.pensize(10)
    the_drawing_turtle.color("#550913")

    for i in range(2):
     the_drawing_turtle.forward(250)
     the_drawing_turtle.left(90)
     the_drawing_turtle.forward(250)
     the_drawing_turtle.left(90)

def draw_window(window):
    """
    Drawing a window inside the house
    """
    window.penup()
    window.goto(-25, -25)
    window.pendown()
    window.pensize(3)
    window.color("#483D8B")

    for i in range(2):
     window.forward(100)
     window.left(90)
     window.forward(100)
     window.left(90)

    window.left(45)
    window.forward(140)
    window.left(135)
    window.forward(100)
    window.left(135)
    window.forward(140)

def roof(build):
    #Build a roof on the top of the house

    build.penup()
    build.goto(155,155)
    build.pendown()
    build.pensize(5)
    build.color("#3CB371")

    build.left(190)
    build.forward(160)
    build.left(71)
    build.forward(155)

def main():
    """
    Calls all the functions and built the house, also introduces the turtle
    """
    wn = turtle.Screen()
    # Function calls to scott
    #bigsquare()
    #draw_window()
    #roof()
    turtle.bgcolor('#FFC0CB')
    scott = turtle.Turtle()

    big_square(scott)
    draw_window(scott)
    roof(scott)

    wn.exitonclick()

main()
