#################################################################################
# Author: Abdul-Hakim Adam
# Username: adama
#
# Assignment: HW03
# Purpose: To get more familiar with Git
# Google Doc Link: https://docs.google.com/document/d/1YXFZxbLGXzFVEYKEQaQeSxvyGnDFdqLH4iHtMqZ9kCQ/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
# Image adapted from
# https://cadbull.com/img/product_img/original/all_sides_sectional_view_of_house_file_25072019045223.jpg
#
#################################################################################

import turtle


def draw_figure(t, width, height):
    """
    This function draws the rectangular figures using the given parameters.
    """
    for i in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)


def dissect_window(t):
    """
    This function divides the windows
    """
    t.forward(50)
    t.left(90)
    t.forward(45)


def draw_gable(left_part):
    """
    This function draws the gable roof on the left
    """
    left_part.goto(-250, 0)
    left_part.left(30)
    left_part.forward(144)
    left_part.right(60)
    left_part.forward(144)
    left_part.left(30)
    left_part.penup()
    left_part.goto(-240, 0)
    left_part.pendown()
    left_part.left(30)
    left_part.forward(133)
    left_part.right(60)
    left_part.forward(145)


def adjust_position(t_pos, x, y):
    """
        This function sets the turtle to a given position so that it performs the next action
    """
    t_pos.penup()
    t_pos.goto(x, y)
    t_pos.pendown()


def left_windows(left_part):
    """
        This function draws the windows on the left
    """
    adjust_position(left_part, -170, -70)
    left_part.left(30)
    left_part.fillcolor("#50EE8A")
    left_part.begin_fill()
    draw_figure(left_part, 100, 45)
    left_part.end_fill()
    dissect_window(left_part)
    adjust_position(left_part, -170, -170)
    left_part.right(90)
    left_part.fillcolor("#50EE8A")
    left_part.begin_fill()
    draw_figure(left_part, 100, 45)
    left_part.end_fill()
    dissect_window(left_part)


def right_windows(right_part):
    """
        This function draws the windows on the right
    """
    right_part.goto(0, -170)
    right_part.penup()
    right_part.forward(275)
    right_part.pendown()
    right_part.fillcolor("#50EE8A")
    right_part.begin_fill()
    draw_figure(right_part, 100, 45)
    right_part.end_fill()
    dissect_window(right_part)

    adjust_position(right_part, 275, -70)
    right_part.right(90)
    right_part.fillcolor("#50EE8A")
    right_part.begin_fill()
    draw_figure(right_part, 100, 45)
    right_part.end_fill()
    dissect_window(right_part)


def middle_windows(middle_part):
    """
            This function draws the windows in the middle section
    """
    adjust_position(middle_part, 35, -170)
    middle_part.right(90)
    middle_part.fillcolor("#50EE8A")
    middle_part.begin_fill()
    draw_figure(middle_part, 100, 45)
    middle_part.end_fill()
    dissect_window(middle_part)

    adjust_position(middle_part, 35, -70)
    middle_part.right(90)
    middle_part.fillcolor("#50EE8A")
    middle_part.begin_fill()
    draw_figure(middle_part, 100, 45)
    middle_part.end_fill()
    dissect_window(middle_part)


def main():
    """
    This python program draws a simple side elevation of my dream home.
    """
    window = turtle.Screen()
    window.bgcolor("#5BF0FF")
    window.setup(width=1000, height=750)

    # Here are the three wonderful turtles that did all the hard work to bring my dream home to reality.
    left_part = turtle.Turtle()
    left_part.pencolor("black")
    left_part.speed(10)

    middle_part = turtle.Turtle()
    middle_part.pencolor("black")
    middle_part.speed(10)

    right_part = turtle.Turtle()
    right_part.pencolor("black")
    right_part.speed(10)
    #####################################################

    # left_part couldn't wait to start his duties
    adjust_position(left_part, -250, -250)
    draw_figure(left_part, 250, 400)
    draw_figure(left_part, 10, 250)
    draw_figure(left_part, 250, 405)

    # Gable roof on the left
    draw_gable(left_part)
    #####################

    # windows on the left
    left_windows(left_part)
    ######################

    # middle section
    draw_figure(middle_part, 450, 140)
    middle_part.goto(0, -5)
    draw_figure(middle_part, 450, 140)
    middle_part.goto(0, -250)
    draw_figure(middle_part, 440, 250)

    middle_part.penup()
    middle_part.goto(0, -125)
    middle_part.forward(170)
    middle_part.pendown()
    middle_part.fillcolor("#7550EE")
    middle_part.begin_fill()
    draw_figure(middle_part, 283, 10)
    middle_part.end_fill()

    # middle wall
    adjust_position(middle_part, 170, -250)
    middle_part.left(90)
    middle_part.forward(245)
    ############################

    # right_part has waited so long. It's desperate to be released!
    # windows on the right
    right_windows(right_part)
    ##########################

    # windows in the middle
    middle_windows(middle_part)
    ############################

    window.exitonclick()


main()  # Starts the program!
