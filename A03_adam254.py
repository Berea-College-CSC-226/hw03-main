######################################################################
# Author: Adam Kinyua
# Username: adam254
#
# Assignment: A03: A Pair of Fully Functional Gitty Psychedelic  Robotic Turtles
# Purpose: To very simply demonstrate use of functions to organize my code
######################################################################
# Acknowledgements:
# Original: http://openbookproject.net/thinkcs/python/english3e/hello_little_turtles.html
# Google doc link: https://docs.google.com/document/d/17O7B0N_S3BY3BcRQUWubq5Tzo0S8eUoqEwEutIYOzSw/edit?usp=sharing
#################################################################################
import turtle


def create_turtle():
    """
    This function creates my initial turtle that will carry out all the drawing in the assignment
    :return: a Turtle Object
    """

    alex = turtle.Turtle()
    alex.pensize(2)
    alex.hideturtle()
    alex.pencolor("#000000")
    alex.speed(0)
    alex.up()
    alex.setpos(-300,0)
    alex.pd()
    alex.lt(60)
    return alex


def draw_trapezium(alex):
    """
    This function constructs a roof.

    :param alex: a Turtle object
    :return: None
    """
    alex.fillcolor('#8B2323')
    alex.begin_fill()
    alex.fd(90)
    alex.rt(60)
    alex.fd(200)
    alex.rt(120)
    alex.fd(90)
    alex.rt(60)
    alex.fd(200)
    alex.end_fill()
    alex.pu()
    alex.fd(-200)
    alex.rt(180)
    alex.pd()
    alex.lt(20)
    alex.pu()
    alex.fd(80)
    alex.pd()
    alex.lt(100)
    alex.fd(60)
    alex.fd(-60)
    alex.lt(60)
    alex.fd(20)
    alex.rt(60)
    alex.fd(40)
    alex.pu()


def draw_wall_1(alex):
    """
    This function draws then main wall.

    :param alex: a turtle object
    :return: None
    """
    alex.setpos(-290,0)
    alex.pd()
    alex.lt(150)
    alex.fillcolor("#8B7500")
    alex.begin_fill()
    alex.fd(100)
    alex.lt(90)
    alex.fd(185)
    alex.lt(90)
    alex.fd(100)
    alex.end_fill()
    alex.fd(-100)


def draw_second_wall(alex):
    """
    This function draws the second wall.

    :param alex: a turtle object
    :return: None
    """
    alex.fillcolor("#8B7500")
    alex.begin_fill()
    alex.rt(70)
    alex.fd(70)
    alex.lt(70)
    alex.fd(104)
    alex.pu()
    alex.end_fill()


def draw_flowerbed(alex):
    """
    This function draws the flower beds

    :param alex: a turtle object
    :return: None
    """
    alex.setpos(-290,-100)
    alex.lt(110)
    alex.fillcolor("#90EE90")
    alex.begin_fill()
    alex.pd()
    alex.fd(30)
    alex.lt(160)
    alex.fd(40)
    alex.lt(20)
    alex.fd(30)
    alex.end_fill()
    alex.fillcolor("#0000FF")
    alex.begin_fill()
    alex.fd(-30)
    alex.rt(20)
    alex.fd(40)
    alex.lt(20)
    alex.fd(30)
    alex.end_fill()
    alex.fillcolor("#FF0000")
    alex.begin_fill()
    alex.fd(-30)
    alex.rt(20)
    alex.fd(40)
    alex.lt(20)
    alex.fd(30)
    alex.end_fill()
    alex.fillcolor("#000000")
    alex.begin_fill()
    alex.fd(-30)
    alex.rt(20)
    alex.fd(40)
    alex.lt(20)
    alex.fd(30)
    alex.end_fill()
    alex.fillcolor("#90EE90")
    alex.begin_fill()
    alex.fd(-30)
    alex.rt(20)
    alex.fd(70)
    alex.lt(145)
    alex.fd(20)
    alex.end_fill()
    alex.fillcolor("#0000FF")
    alex.begin_fill()
    alex.fd(-20)
    alex.rt(120)
    alex.fd(40)
    alex.lt(120)
    alex.fd(16)
    alex.end_fill()
    alex.fillcolor("#FF0000")
    alex.begin_fill()
    alex.fd(-16)
    alex.rt(120)
    alex.fd(28)
    alex.lt(123)
    alex.fd(16)
    alex.end_fill()
    alex.pu()


def draw_doors(alex):
    """
    This function draws patterns inside the square.

    :param alex: a turtle object
    :return: None
    """
    alex.pensize(1)
    alex.pu()
    alex.setpos(-210,-99)
    alex.rt(59)
    alex.fillcolor("#FF0000")
    alex.begin_fill()
    alex.fd(60)
    alex.rt(90)
    alex.fd(25)
    alex.rt(90)
    alex.fd(60)
    alex.end_fill()


def draw_window_1(alex):
    """
    This function draws windows.

    :param alex: a turtle object
    :return: None
    """
    alex.pensize(1)
    alex.pu()
    alex.setpos(-270,-40)
    alex.lt(90)
    alex.fillcolor("#B03060")
    alex.begin_fill()
    alex.fd(25)
    alex.rt(90)
    alex.fd(25)
    alex.rt(90)
    alex.fd(25)
    alex.end_fill()


def draw_window_2(alex):
    """
    This function draws patterns inside the square.

    :param alex: a turtle object
    :return: None
    """
    alex.pensize(1)
    alex.pu()
    alex.setpos(-130,-40)
    alex.lt(90)
    alex.fillcolor("#B03060")
    alex.begin_fill()
    alex.fd(25)
    alex.rt(90)
    alex.fd(25)
    alex.rt(90)
    alex.fd(25)
    alex.end_fill()


def main():
    """
    This is the main function of our assignment where execution begins and ends
    :return: None
    """

    screen = turtle.Screen()
    screen.bgcolor("#FFFFF0")
    alex = create_turtle()
    draw_trapezium(alex)
    draw_wall_1(alex)
    draw_second_wall(alex)
    draw_flowerbed(alex)
    draw_doors(alex)
    draw_window_1(alex)
    draw_window_2(alex)
    screen.exitonclick()


main()

