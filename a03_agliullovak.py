# Author: Karina Agliullova
# username: agliullovak

# Assignment: A03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: This program draws a dream house and the sun using turtles and functions.
######################################################################
# Acknowledgements:

# Original code by: Karina Agliullova

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
######################################################################

import turtle                               # lets us use a turtle library


def draw_sun(turt):                         # function that uses a turtle to draw sun
    """
    This function uses a turtle that draws sun on the top left and fills it in with a color

    :param: turt
    :return: None
    """
    for i in range(1):                       # repeats every method once
        turt.right(90)                       # goes to the right by 90 units
        turt.forward(45)                     # goes forward by 90 units
        turt.right(180)
        turt.forward(45)
        turt.right(60)
        turt.forward(40)
        turt.right(90)
        turt.forward(55)
        turt.right(180)
        turt.forward(55)
        turt.right(30)
        turt.forward(30)
        turt.right(90)
        turt.forward(65)
        turt.right(180)
        turt.forward(65)
        turt.right(50)
        turt.forward(40)
        turt.right(90)
        turt.forward(55)
        turt.right(180)
        turt.forward(55)
        turt.right(30)
        turt.forward(30)
        turt.right(90)
        turt.forward(65)
        turt.right(180)
        turt.forward(65)
        turt.right(40)
        turt.forward(30)
        turt.right(90)
        turt.forward(55)
        turt.right(180)
        turt.forward(55)
        turt.right(50)
        turt.forward(40)
        turt.right(80)
        turt.forward(55)
        turt.hideturtle()                       # method for hiding a turtle after its drawing


def draw_square(turt, w, h):                    # function that uses a turtle to draw a first square
    """
    This function uses a turtle that draws a first square and fills in the color the first square.

    :param: turt, w, h
    :return: None
    """
    for i in range(2):                          # repeats the given methods twice
        turt.begin_fill()                       # method that is used to start filling in the object from the inside
        turt.forward(w)
        turt.right(90)
        turt.forward(h)
        turt.right(90)
        turt.hideturtle()                       # method for hiding a turtle after its drawing
        turt.end_fill()                         # method that is used to ends filling in the object from the inside


def draw_a_square(turt, w, h):                  # function that uses a turtle to draw a second square
    """
    This function uses a turtle that draws a second square and fills it in with a color.

    :param: turt, w, h
    :return: None
    """
    for i in range(2):                          # repeats the given methods two times
        turt.begin_fill()                       # method that is used to start filling in the object from the inside
        turt.forward(w)
        turt.left(90)
        turt.forward(h)
        turt.left(90)
        turt.hideturtle()                       # method for hiding a turtle after its drawing
        turt.end_fill()                         # method that is used to end filling in the object from the inside


def draw_roof(turt):                            # function that uses a turtle to draw a rooftop
    """
    This function uses a turtle that draws a rooftop and fills it in with a color.

    :param: turt
    :return: None
    """
    turt.begin_fill()
    for i in range(3):                          # repeats the methods 3 times
        turt.forward(150)
        turt.left(120)
        turt.hideturtle()
    turt.end_fill()


def draw_window(turt):                          # function that draws a window
    """
    This function uses a turtle that draws a window and fills it in with a color.

    :param: turt
    :return: None
    """
    turt.begin_fill()
    for i in range(2):                          # repeats the methods twice
        turt.forward(50)
        turt.right(90)
        turt.forward(50)
        turt.right(90)
    for i in range(1):                          # repeats methods once
        turt.forward(25)
        turt.right(90)
        turt.forward(50)
        turt.right(90)
        turt.forward(25)
        turt.right(90)
        turt.forward(25)
        turt.right(90)
        turt.forward(50)
        turt.hideturtle()
    turt.end_fill()


def draw_a_window(turt):                            # function that draws a window
    """
    This function uses a turtle that draws a second window and fills it in with a color.

    :param: turt
    :return: None
    """
    turt.begin_fill()
    for i in range(2):
        turt.forward(50)
        turt.right(90)
        turt.forward(50)
        turt.right(90)
    for i in range(1):
        turt.forward(25)
        turt.right(90)
        turt.forward(50)
        turt.right(90)
        turt.forward(25)
        turt.right(90)
        turt.forward(25)
        turt.right(90)
        turt.forward(50)
        turt.hideturtle()
    turt.end_fill()


def draw_door(turt):                            # function that draws a door
    """
    This function uses a turtle that draws a door and fills it in with a color.

    :param: turt
    :return: None
    """
    turt.begin_fill()
    for i in range(2):
        turt.forward(50)
        turt.right(90)
        turt.forward(80)
        turt.right(90)
    for i in range(1):
        turt.forward(50)
        turt.right(90)
        turt.forward(50)
        turt.right(90)
        turt.forward(10)
        turt.circle(5)
        turt.hideturtle()
    turt.end_fill()


def main():                                     # calls all functions
    """
    The main function is intended to create and use all the turtles that are created in the program.

    :return:
    """
    wn = turtle.Screen()                        # creates a window
    wn.bgcolor("#5fc1f5")                       # sets a color to the window
    wn.title("Dream House!")                    # gives a title to the window

    gabe = turtle.Turtle()                      # creates a turtle
    gabe.pensize(10)                            # assigns a pensize of the turtle to 10
    gabe.penup()                                # puts up a pen so that the turtle won't be able to draw
    gabe.goto(-170, 180)                        # goes to a certain position
    gabe.pendown()                              # puts down a pen
    gabe.color("#FFFF00")                       # sets a color for the turtle
    gabe.begin_fill()                           # starts to fill in the turtle with a color
    gabe.circle(40)                             # draws a circle using the turtle
    gabe.end_fill()                             # ends to fill in the turtle with a color
    gabe.shape("turtle")                        # sets a shape for the turtle

    alex = turtle.Turtle()                      # creates a turtle
    alex.shape("arrow")                         # sets a shape for the turtle
    alex.pensize(15)                            # assigns a pensize of the turtle to 15
    alex.pencolor("#c2c2c2")                    # sets a color for the turtle
    alex.fillcolor("#03fc39")                   # fills in with a color

    tess = turtle.Turtle()                      # creates a turtle
    tess.shape("square")                        # sets a shape for the turtle
    tess.fillcolor("#ff73c0")                   # fills in with a color
    tess.pencolor("#c2c2c2")                    # sets a color for the turtle
    tess.pensize(15)                            # assigns a pensize of the turtle to 15
    tess.penup()                                # puts up a pen so that the turtle won't be able to draw
    tess.goto(25, 10)                           # goes to a certain position
    tess.pendown()                              # puts down a pen

    ben = turtle.Turtle()                       # creates a turtle
    ben.shape("square")
    ben.fillcolor("#a19023")
    ben.pencolor("#c2c2c2")
    ben.pensize(15)
    ben.penup()
    ben.goto(25, 160)
    ben.pendown()

    jake = turtle.Turtle()                      # creates a turtle
    jake.fillcolor("#d94cd4")
    jake.shape("circle")
    jake.pensize(5)
    jake.pencolor("#ededed")
    jake.penup()
    jake.goto(75, 100)
    jake.pendown()

    blake = turtle.Turtle()                       # creates a turtle
    blake.fillcolor("#d94cd4")
    blake.shape("circle")
    blake.pensize(5)
    blake.pencolor("#ededed")
    blake.penup()
    blake.goto(40, -80)
    blake.pendown()

    ann = turtle.Turtle()                          # creates a turtle
    ann.fillcolor("#d94cd4")
    ann.shape("turtle")
    ann.pensize(5)
    ann.pencolor("#ededed")
    ann.penup()
    ann.goto(125, -116)
    ann.pendown()

    draw_sun(gabe)                                  # calls a function

    draw_square(alex, 200, 200)                     # calls a function

    draw_a_square(tess, 150, 150)                   # calls a function

    draw_roof(ben)                                  # calls a function

    draw_window(jake)                               # calls a function

    draw_a_window(blake)                            # calls a function

    draw_door(ann)                                  # calls a function

    wn.exitonclick()                                # exits on a click from the user


main()                                              # finishes the main function
