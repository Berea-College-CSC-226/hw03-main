#################################################################################
# Author: Ela Jamali
# Username: Jamalie
#
# Google Doc: https://docs.google.com/document/d/1-tCZSE_ifI0Q9IcZ3osAFNl59Ois0sxHh9bdSrzI_Bo/edit?usp=sharing
# Assignment: A03: A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Practicing creating and using functions and using the turtle library.
#################################################################################
# Attribution:
# Website used: https://docs.python.org/2/library/turtle.html#turtle.write
# https://docs.python.org/3.0/library/turtle.html#turtle.color
# Got help from TAs: Aaron Christian and Giorgi Lomia
#################################################################################

import turtle


def draw_rectangle_screen(t, l, wid, x, y):
    """
    A function to draw two triangles for the Screen of our laptop

    :param t: a turtle object
    :param l: the length of the triangle
    :param wid: the width of the triangle
    :param x: the point on x-axis on the screen
    :param y: the point on y-axis on the screen
    :return: None
    """
    t.speed(5)       # our speed to draw the triangle
    t.pensize(5)      # the pensize our turtle uses
    t.penup()          # penup so the position change is not recorded
    t.setpos(x, y)       # setting the position on the screen
    t.pendown()
    for i in range(2):    # for loop to repeat the commands to draw a rectangle
        t.left(90)        # turning for the 90 degree angle
        t.forward(wid)    # drawing the width of the triangle
        t.left(90)
        t.forward(l)      # drawing the length of the triangle


def draw_rectangle_keyboard(t, x, y, l, wid, ang):
    """
    A function that will draw a rectangle for the keyboard

    :param: t: a turtle object
    :param: x: the point on x-axis on the screen
    :param: y: the point on y-axis on the screen
    :param: l: the length of the triangle
    :param: wid: the width of the triangle
    :param: ang: the angle degree we want to turn
    :return: None
    """
    t.speed(5)      # setting the speed of the turtle
    t.pensize(5)    # setting the pensize
    t.penup()       # penup so the position change is not recorded
    t.setpos(x, y)  # setting the position on the screen
    t.pendown()
    for i in range(1):   # for loop to have the commands to draw a rectangle
        t.right(80)       # turning for 80 degrees
        t.forward(wid)    # drawing the width of the triangle
        t.right(ang)      # turning with a specific degree
        t.forward(l)     # drawing the angle of the triangle
        t.right(ang)
        t.forward(wid)


def draw_rectangle_keyboard_inside(t, x, y, l, wid, ang1):
    """
    A function that will draw a rectangle for the keyboard

    :param: t: a turtle object
    :param: x: the point on x-axis on the screen
    :param: y: the point on y-axis on the screen
    :param: l: the length of the triangle
    :param: wid: the width of the triangle
    :param: ang1: the angle degree we want to turn at the bottom
    :return: None
    """
    t.speed(5)      # setting the speed of the turtle
    t.pensize(5)    # setting the pensize
    t.penup()       # penup so the position change is not recorded
    t.setpos(x, y)  # setting the position on the screen
    t.pendown()
    for i in range(1):    # for loop to draw a rectangle
        t.right(160)      # turning right for 160 degrees
        t.forward(wid)    # drawing the width of the triangle
        t.right(ang1)     # turning based on the angle given
        t.forward(l)      # drawing the length of the triangle
        t.right(ang1)
        t.forward(wid)
        t.right(80)
        t.forward(260)


def draw_circle_camera(t, x, y):
    """
    A function that will draw a circle for the camera of the laptop

    :param: t: a turtle object
    :param: x: the point on x-axis on the screen
    :param: y: the point on y-axis on the screen
    :return: None
    """
    t.speed(5)      # setting the speed of the turtle
    t.pensize(2)    # setting the pensize
    t.penup()       # penup so the position change is not recorded
    t.setpos(x, y)  # setting the position on the screen
    t.pendown()
    t.circle(5)     # we want to draw a circle with a radius of 5


def draw_circle_buttons(t, x, y, w, r, g, b):
    """
    A function that will draw three circle buttons

    :param: t: a turtle object
    :param: x: the point on x-axis on the screen
    :param: y: the point on y-axis on the screen
    :param: w: the Screen
    :param: r: the value of R
    :param: g: the value of G
    :param: b: the value of B
    :return: None
    """
    t.speed(5)      # setting the speed of the turtle
    t.pensize(5)    # setting the pensize
    t.penup()       # penup so the position change is not recorded
    t.setpos(x, y)  # setting the position on the screen
    t.pendown()
    w.colormode(255)   # setting the screen for a colormode to use RGB colors
    t.color(r, g, b)   # specifying the percentage of the colors
    t.begin_fill()     # begin filling the circle with the given color
    t.circle(40)       # drawing circle with the given radius
    t.end_fill()       # stop filling the circle


def word_on_screen(t, x, y):
    """
    A function that will write a word inside the screen of our laptop

    :param: t: a turtle object
    :param: x: the point on x-axis on the screen
    :param: y: the point on y-axis on the screen
    :return: None
    """
    t.speed(5)      # setting the speed of the turtle
    t.pensize(3)    # setting the pensize
    t.penup()       # penup so the position change is not recorded
    t.setpos(x, y)  # setting the position on the screen
    t.pendown()
    t.pencolor("purple")   # setting the color of the pencil
    t.shape("blank")       # setting the shape of the turtle
    t.write("Python", False, align="center", font=("Arial", 40, "normal"))
    # setting the turtle to write a word without moving a pen in the center of its position with the given font


def main():
    """
    the main function of the program where the laptop, buttons, camera and text will be executed

    :return: None
    """
    wn = turtle.Screen()
    wn.bgcolor("lightblue")

    alex = turtle.Turtle()

    draw_rectangle_screen(alex, 300, 175, 150, 0)   # this calls the function to have the bigger triangle
    draw_rectangle_screen(alex, 260, 135, 130, 20)  # this calls the function to draw the smaller triangle
    draw_rectangle_keyboard(alex, 150, 0, 352, 150, 100)       # this calls the function to draw the keyboard triangle
    draw_rectangle_keyboard_inside(alex, 130, -20, 300, 110, 100)    # this calls the function to draw the smaller triangle for keyboard
    draw_circle_camera(alex, 0, 160)                               # this calls the function to draw a circle as the camera
    draw_circle_buttons(alex, -90, -110, wn, 143, 188, 143)        # this calls the function to draw a circle and paint it xanadu
    draw_circle_buttons(alex, 0, -110, wn, 255, 255, 0)            # this calls the function to draw a circle and paint it yellow
    draw_circle_buttons(alex, 90, -110, wn, 220, 20, 60)           # this calls the function to draw a circle and paint it crimson
    word_on_screen(alex, 0, 60)        # this calls the function to write a word on the screen
    wn.exitonclick()


main()
