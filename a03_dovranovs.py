#################################################################################
# Author: Sahet Dovranov
# Username: dovranovs
#
#  Google doc link: https://docs.google.com/document/d/1UTlp6YcwC-boyDoaReInx6aPR799BLI_faPDoaez2n0/edit?usp=sharing
#############################################################################################
#
# Assignment: A03: A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Draw some fun things using turtle and also learn about git!
#################################################################################

import turtle


def draw_outside_circle(t, x, y, color):
    """
    Draws a circle with given color on the (x,y) coordinate.
    (Intended to make it look like outer circle of a tyre).

    :param t: Turtle to use a circle
    :param x: value of coordinates of x-axis
    :param y: value of coordinates of y-axis
    :param color: color of the circle
    :return:
    """
    t.color(color)
    t.fillcolor(color)
    t.up()
    t.setposition(x,y)
    t.down()
    t.begin_fill()
    t.circle(60)
    t.end_fill()


def draw_inner_circle(t, x, y, color):
    """
    Draws a square with given color on the (x,y) coordinate.
    (Intended to make it look like inner circle of a tyre )

    :param t: Turtle to use drawing a square
    :param x: value of coordinates of x-axis
    :param y: value of coordinates of y-axis
    :param color: color of the circle.
    :return:
    """
    t.color(color)
    t.fillcolor(color)
    t.up()
    t.setposition(x,y)
    t.down()
    t.begin_fill()
    t.circle(30)
    t.end_fill()


def draw_rectangle(t, x, y, color):
    """
    Draws a rectangle with given color on the (x,y) coordinates.
    (Intended to make it look like car's part which looks like a rectangle)

    :param t: Turtle to use drawing a rectangle
    :param x: value of coordinates of x-axis
    :param y: value of coordinates of y-axis
    :param color: color of the rectangle.
    :return:
    """
    t.color(color)
    t.fillcolor(color)
    t.up()
    t.setposition(x,y)
    t.down()
    t.begin_fill()
    for i in range(2):
        t.forward(600)
        t.right(90)
        t.forward(90)
        t.right(90)
    t.end_fill()


def draw_trapezoid_without_below_side(t, x, y, color):
    """
    Draws a trapezoid without below side with given color on the (x,y) coordinates.
    (Intended to make it look like car's side windows)

    :param t: Turtle to use drawing a trapezoid
    :param x: value of coordinates of x-axis
    :param y: value of coordinates of y-axis
    :param color: color of the trapezoid
    :return:
    """
    t.color(color)
    t.fillcolor(color)
    t.up()
    t.setposition(x,y)
    t.down()
    t.begin_fill()
    t.left(45)
    t.forward(100)
    t.right(45)
    t.forward(250)
    t.right(70)
    t.forward(75)
    t.end_fill()
    t.hideturtle()


def draw_line(t, x, y, color):
    """
    Draws a line.
    (Intended to make it look like a line which separates car's side windows)

    :param t: Turtle to use drawing a line
    :param x: value of coordinates of x-axis
    :param y: value of coordinates of y-axis
    :param color: color of the line
    :return:
    """
    t.color(color)
    t.up()
    t.setposition(x,y)
    t.down()
    t.setheading(0)
    t.right(90)
    t.forward(162)


def write_title(t, x, y, m, color):
    """
    Draws a title using t to present message m
    :param t: Turtle to use drawing a message.
    :param x: value of coordinates of x-axis.
    :param y: value of coordinates of y- axis.
    :param m: message for to present as a title
    :param color: color of message
    :return:
    """
    t.color(color)
    t.up()
    t.setposition(x,y)
    t.down()
    t.write(m, move=False, align='center', font=("Arial", 30, ("italic", "normal")))


def main():
    """
    Creates a turtle with name alex, gives its attributes and calls all methods properly to draw a car and draws a title
    :return:
    """

    wn = turtle.Screen()

    wn.colormode(255)
    wn.bgcolor("#191970")
    alex = turtle.Turtle()
    alex.shape("turtle")

    color_white = (255, 255, 255)
    color_black = (0, 0, 0)
    color_yellow = (255, 255, 0)
    color_light_black = (160, 160, 160)
    color_red = "#FF0000"
    color_green = "#00CC00"

    write_title(alex, 0, 200, "This is my present for your birthday", color_red)

    draw_outside_circle(alex, -120, -200, color_black)
    draw_inner_circle(alex, -120, -170, color_white)

    draw_outside_circle(alex, 160, -200, color_black)
    draw_inner_circle(alex, 160, -170, color_white)

    draw_rectangle(alex, -300, -50, color_yellow)

    draw_trapezoid_without_below_side(alex, -150, -50, color_light_black)

    draw_line(alex, 30, 20, color_black)

    write_title(alex, 0, 150, "A brand new car", color_green)

    wn.mainloop()


main()
