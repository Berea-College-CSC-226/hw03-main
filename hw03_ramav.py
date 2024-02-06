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
def draw_cat():

    #Turtle screen
    screen = turtle.Screen()
    screen.bgcolor("white")

    #creating turtle object
    cat_turtle = turtle.Turtle()

    #Setting the turtle properties
    cat_turtle.shape("turtle")
    cat_turtle.color("black")
    cat_turtle.pensize(2)

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
 #Ears

    cat_turtle.penup()
    cat_turtle.goto(-25, 100)
    cat_turtle.pendown()
    cat_turtle.fillcolor("gray")
    cat_turtle.begin_fill()
    cat_turtle.left(45)
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
    screen.exitonclick()

def main():
    """
    Docstring for main. Should describe the main functionality of this file.
    """

    # Function call to draw_cat
    draw_cat()

if __name__ == "__main__":
    main()
 # Starts the program!


