#################################################################################
# Author: Besher Kitaz
# Username: kitazb
#
# Assignment: HW03
# Purpose: Drawing a house with Turtle library
#
#
#################################################################################
# Acknowledgements:
#
# Document link: https://docs.google.com/document/d/13fdydW8mxVLdYfAWMG7x2zIYqjoSEVAWuOItJJ7VOT4/edit
#################################################################################

import turtle


def draw_house_body(t):
    """
    draws a body for the house
    :args: a turtle object
    :returns:none
    """
    t.fillcolor('green')
    t.begin_fill()
    for i in range(4):
        t.forward(250)
        t.left(90)
    t.end_fill()


def draw_rooftop(t):
    """
    draws a rooftop for the house
    :args: a turtle object
    :returns:none
    """
    t.fillcolor('red')
    t.begin_fill()
    t.right(45)
    t.forward(176)
    t.right(90)
    t.forward(176)
    t.end_fill()


def draw_window_square(t):
    """
        gets a turtle object to draw a square shape for the window
        :args: t, turtle object to draw the square
        :returns: None
    """
    t.fillcolor('yellow')
    t.begin_fill()
    for i in range(4):
        t.forward(60)
        t.left(90)
    t.end_fill()


def draw_windows(t, px, py, turn_degree):
    """
        gets a turtle object to draw a window
        :args: t, turtle object, px, for the position of the window horizontally, and py for vertical position
        :returns: None
    """
    t.penup()
    t.goto(px, py)
    t.pendown()
    t.left(turn_degree)
    draw_window_square(t)

    t.forward(30)
    t.left(90)
    t.forward(60)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(60)


def draw_door(t):
    """
    Draws a door for the house
    :args: a turtle object
    :returns:none
    """

    t.fillcolor('brown')
    t.begin_fill()
    t.left(90)
    t.forward(120)
    t.right(90)
    t.forward(80)
    t.right(90)
    t.forward(120)
    t.end_fill()

def draw_chimney(t):
    """
    Draws a chimney for the house
    :args: a turtle object
    :returns:none
    """

    t.fillcolor('brown')
    t.begin_fill()
    t.forward(80)

    t.right(90)
    t.forward(10)
    t.left(90)
    t.forward(30)

    t.left(90)
    t.forward(50)

    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(10)
    t.right(90)

    t.forward(110)
    t.end_fill()

def draw_sun(t):
    """
    Draws a sun for above the house
    :args: a turtle object
    :returns:none
    """
    t.penup()
    t.goto(200, 200)
    t.pendown()
    t.fillcolor('yellow')
    t.begin_fill()
    for i in range(90):
        t.forward(4)
        t.right(4)
    t.end_fill()


def main():
    """
    main function: includes the main body of the source code
    :args: None
    :returns: None
    """
    wn = turtle.Screen()
    t1 = turtle.Turtle()

    # go to the suitable position for the house to begin drawing and draw the body using the function
    t1.penup()
    t1.goto(-200,-200)
    t1.pendown()
    draw_house_body(t1)

    # Go to the position for the rooftop beginning and use the function to draw it
    t1.left(90)
    t1.forward(250)
    draw_rooftop(t1)

    #draw two windows
    draw_windows(t1, -50, -50, 45)
    draw_windows(t1, -160, -50, 0)

    # Go to a suitable position for the door and use the function to draw it
    t1.penup()
    t1.goto(-110, -200)
    t1.pendown()
    draw_door(t1)

    # Go to a suitable position for the chimney and use the function to draw it
    t1.left(180)
    t1.penup()
    t1.goto(-150, 100)
    t1.pendown()
    draw_chimney(t1)

    #use the function to draw the sun; the positioning will take place inside the function this time
    draw_sun(t1)

    #click to exist after finishing:
    wn.exitonclick()


main()