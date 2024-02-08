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

# Corrected mistakes after given feedback.


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
    #  Section that draws a cat.
    #  This section of the code draws the body of the cat.
    cat_turtle.fillcolor("gray")
    cat_turtle.begin_fill()
    cat_turtle.circle(50)
    cat_turtle.end_fill()

    # This section of the code draws the head of the cat
    cat_turtle.fillcolor("gray")
    cat_turtle.begin_fill()
    cat_turtle.circle(30)
    cat_turtle.end_fill()

    # This section of the code draws the eyes of the cat.
    cat_turtle.penup()
    cat_turtle.goto(-15, 70)
    cat_turtle.pendown()
    cat_turtle.fillcolor("blue")
    cat_turtle.begin_fill()
    cat_turtle.circle(5)

    # This section of the code draws the nose of the cat.
    cat_turtle.penup()
    cat_turtle.goto(0, 50)
    cat_turtle.pendown()
    cat_turtle.dot(10, "pink")

    # This section of the code draws the mouth of the cat.
    cat_turtle.penup()
    cat_turtle.goto(0, 50)
    cat_turtle.pendown()
    cat_turtle.right(90)
    cat_turtle.circle(10, -180)

    # This section of the code draws the tail of the cat.
    cat_turtle.penup()
    cat_turtle.goto(60, 50)
    cat_turtle.pendown()
    cat_turtle.right(45)
    cat_turtle.forward(40)
    # Closing the turtle graphic on clicked.


def main():
    """
    The function main hold the important parts of the code that run through this program.
    Its use is for the controlling the drawing of the cat. This section contains creating the screen for the cat to show
    up and the background color through screen.bgcolor("yellow"), and in this section are included the functions
    that are called to draw the cat (draw_cat).
    """
    # This section allows for the turtle to appear on the screen through turtle.Screen()
    screen = turtle.Screen()
    screen.bgcolor("yellow")

    # This code allows us to create a turtle object
    cat_turtle = turtle.Turtle()

    # This section describes the properties of the cat such as the shape of the pen that draws the cat, the color of
    # the pen, and the pensize is the width of the pen to draw the cat
    cat_turtle.shape("turtle")
    cat_turtle.color((0, 0, 0))
    cat_turtle.pensize(2)

    # The function draw_cat holds the code for the cat to be drawn on the screen.
    # The function daw_ears allows to store the code that makes up the ears of the cat.
    # the pen, and the pensize is the width of the pen to draw the cat
    draw_cat(cat_turtle)
    draw_ears(cat_turtle)

    # The turtle graphics close on click
    screen.exitonclick()


if __name__ == "__main__":
    main()

# Program to draw a cat beings here.
