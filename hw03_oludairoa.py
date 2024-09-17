#################################################################################
# Author: Ayomide Oludairo
# Username: oludairoa
#
# Assignment: HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Learn how to use git push and pull requests
# Google Doc Link: https://docs.google.com/document/d/1yX8V99iRkV56ZTmNQmI9XwANLQ7LLj5dzj0nO0i1hgw/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################


import turtle

def draw_rect(t, sz, sz2):
    """
    The draw square function creates the 4 sides of a rectangle (can be a square).
    """

    if int(sz) > 200:
        return "That value is too large try something smaller"

    for i in range(2):
        t.forward(sz)
        t.left(90)
        t.forward(sz2)
        t.left(90)

    t.right(90)
    # ....

def draw_parallelogram(t, sz, sz2):
    """
    The parallelogram will create a shap that will be the sides of the walls
    """
    t.left(45)
    t.forward(sz)
    t.left(45)
    t.forward(sz2)
    t.left(135)
    t.forward(sz)
    # ...

def draw_roof(t, sz):
    """"
    This function will create a triangle that will serve as a roof for this shed
    """
    t.right(90)
    t.forward(sz)
    t.left(90)
    t.forward(sz)

def main():
    """
    Create two separate turtles to create the body of the shed and a door.
    """
    wn = turtle.Screen()
    wn.bgcolor("lightblue")
    james = turtle.Turtle()
    james.color("orange")

    suzie = turtle.Turtle()
    suzie.color("black")

    james.penup()
    james.backward(150)
    james.left(90)
    james.backward(150)
    james.pendown()

    # Function calls to function_1 and function_2.
    draw_rect(james, 100, 100)
    draw_parallelogram(james, 150, 100)
    draw_roof(james, 70)
    james.backward(70)
    james.right(180)
    james.forward(150)
    james.right(90)
    james.forward(70)

    suzie.penup()
    suzie.backward(185)
    suzie.left(90)
    suzie.backward(150)
    suzie.pendown()

    draw_rect(suzie, 50, 25)
    james.hideturtle()
    suzie.hideturtle()

    wn.exitonclick()

main()  # Starts the program!