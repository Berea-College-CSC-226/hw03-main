#################################################################################
# Author: Elijah Babayemi
# Username: babayemie
#
# Assignment:HW03: Fully Functional Gitty Psychedelic Robotic Turtles Purpose: Continue practicing creating and using
# functions, more practice on using the turtle library, learn about how computers represent colors, and learn about
# source control and Git.
#
# Google Doc Link: https://docs.google.com/document/d/1X9d90s3RxZa3LG8GFm7Y8XtmVSOv1ai_OpNtu0xGtpk/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
# https://openbookproject.net/thinkcs/python/english3e/hello_little_turtles.html
# https://www.geeksforgeeks.org/draw-color-filled-shapes-in-turtle-python/
#################################################################################


import turtle


def make_house(house_turtle):
    """
    This function draws the main body of the house
    """

    house_turtle.penup()
    house_turtle.goto(-50, -50)
    house_turtle.pendown()

    house_turtle.fillcolor("#FF3C00")  # red color
    house_turtle.begin_fill()
    for _ in range(4):
        house_turtle.forward(100)
        house_turtle.left(90)
    house_turtle.end_fill()

    # Draws a door for house
    house_turtle.penup()
    house_turtle.fillcolor("#060D04")
    house_turtle.begin_fill()
    house_turtle.goto(-15, -50)
    for _ in range(4):
        house_turtle.forward(30)
        house_turtle.left(90)
    house_turtle.end_fill()
    house_turtle.hideturtle()


def draw_roof(shape):
    """
    This function draws a roof for the square to make it look like a house.
    """

    shape.penup()
    shape.fillcolor("#898685")
    shape.begin_fill()
    shape.goto(50, 50)
    shape.pendown()
    shape.goto(0, 100)
    shape.goto(-50, 50)
    shape.goto(50, 50)
    shape.end_fill()
    shape.hideturtle()


def draw_tree(tree_turtle):
    """
    This function draws a tree beside the house.
    """

    tree_turtle.fillcolor("#4A3209")
    tree_turtle.begin_fill()
    tree_turtle.penup()
    tree_turtle.goto(130, -50)
    tree_turtle.pendown()
    for _ in range(2):
        tree_turtle.forward(20)
        tree_turtle.left(90)
        tree_turtle.forward(40)
        tree_turtle.left(90)
        print(turtle.pos())  # Printing a location, so I can find a good place to put the green circle.
    tree_turtle.end_fill()

    # Draws a circle that represents the leaves
    tree_turtle.fillcolor("#2FA118")
    tree_turtle.begin_fill()
    tree_turtle.penup()
    tree_turtle.goto(140, -10)  # Putting the circle in a location close to coordinates I got from "print(turtle.pos(
    # ))" that's in the center of the rectangle.
    tree_turtle.pendown()
    tree_turtle.circle(30)
    tree_turtle.end_fill()
    tree_turtle.hideturtle()


def sun(sun_turtle):
    """
    This function draws a sun.
    """

    sun_turtle.penup()
    sun_turtle.goto(-150, 100)
    sun_turtle.pendown()

    sun_turtle.fillcolor("#FFDE00")  # Yellow color for sun
    sun_turtle.begin_fill()
    sun_turtle.circle(30)
    sun_turtle.end_fill()
    sun_turtle.hideturtle()


def main():
    """
    This function starts the drawing process for the house, tree, and sun.
    """

    shape = turtle.Turtle()
    sun_turtle = turtle.Turtle()
    house_turtle = turtle.Turtle()
    tree_turtle = turtle.Turtle()

    # Making turtle screen
    wn = turtle.Screen()
    wn.bgcolor("lightblue")

    # Calls Functions
    make_house(house_turtle)
    draw_roof(shape)
    draw_tree(tree_turtle)
    sun(sun_turtle)

    turtle.hideturtle()

    wn.exitonclick()


main()  # Starts the program!
