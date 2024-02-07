#################################################################################
# Author:Valentin Rama
# Username: ramav
#
# Assignment: HW03
# Purpose: Creating a cat
# Google Doc Link: https://docs.google.com/document/d/18V8i2I56Gj5T8IJGo4s0cEIvQE2YgXbE2uGVO0n7EVE/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################

# TESTING PUSH FEATURE IN TA HOURS

import turtle

def draw_ears(cat_turtle):
    """
    The function draw_ears allows for the drawing of the cat to draw the ears. using goto allows for the ears
    to be drawn at a certain position that allows for the ears to be drawn. The fillcolor allows so the spce where the
    ears are drawn they are filled with the color "gray" in this instance.
    """

    cat_turtle.penup()
    cat_turtle.goto(-25, 100)
    cat_turtle.pendown()
    cat_turtle.fillcolor("gray")
    cat_turtle.begin_fill()
    cat_turtle.forward(20)
    cat_turtle.right(90)
    cat_turtle.forward(20)
    cat_turtle.left(45)
    cat_turtle.end_fill()

    cat_turtle.penup()
    cat_turtle.goto(0, 100)
    cat_turtle.pendown()
    cat_turtle.fillcolor("gray")
    cat_turtle.begin_fill()
    cat_turtle.left(45)
    cat_turtle.forward(20)
    cat_turtle.right(90)
    cat_turtle.forward(20)
    cat_turtle.left(45)
    cat_turtle.end_fill()

def draw_cat(cat_turtle):

    """
    The function draw cat makes it possible for the cat to be drawn on the screen. In this function there are most of
    the components(Head,body,eyes etc.) that allow the cat to be displayed on the screen, and the for it to take shape
    as a 2d cat drawing.
    """

    #Drawing a cat
    #Body

    cat_turtle.fillcolor("gray")
    cat_turtle.begin_fill()
    cat_turtle.circle(50)
    cat_turtle.end_fill()

    #Head
    cat_turtle.fillcolor("gray")
    cat_turtle.begin_fill()
    cat_turtle.circle(30)
    cat_turtle.end_fill()

    #Eyes
    cat_turtle.penup()
    cat_turtle.goto(-15, 70)
    cat_turtle.pendown()
    cat_turtle.fillcolor("blue")
    cat_turtle.begin_fill()
    cat_turtle.circle(5)


    # Nose
    cat_turtle.penup()
    cat_turtle.goto(0, 50)
    cat_turtle.pendown()
    cat_turtle.dot(10, "pink")

    # Mouth
    cat_turtle.penup()
    cat_turtle.goto(0, 50)
    cat_turtle.pendown()
    cat_turtle.right(90)
    cat_turtle.circle(10, -180)

    # Tail
    cat_turtle.penup()
    cat_turtle.goto(60, 50)
    cat_turtle.pendown()
    cat_turtle.right(45)
    cat_turtle.forward(40)

    # Closing the turtle graphics on when clicked!

def main():

    # Turtle screen
    screen = turtle.Screen()
    screen.bgcolor("yellow")

    # creating turtle object
    cat_turtle = turtle.Turtle()

    # Setting the turtle properties
    cat_turtle.shape("turtle")
    cat_turtle.color((0,0,0))
    cat_turtle.pensize(2)



    # Function call to draw_cat
    draw_cat(cat_turtle)
    draw_ears(cat_turtle)
    screen.exitonclick()


if __name__ == "__main__":
    main()
 # Starts the program!


