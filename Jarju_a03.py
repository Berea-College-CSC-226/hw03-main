######################################################################
# Author: Gaston Jarju
# Username: gastonjarju
#
# Assignment: A03
# Purpose: To create any complex thing using functions.
#Google_Doc_Link: https://docs.google.com/document/d/1oGxUbCQ5Iy3_CQMwEsv24rQ2Iv9Zp0Yx4B-DzuLtlhI/edit#

# Acknowledgements: Christson

###################################################################################################

import turtle              # Imports turtle from the python Library


def draw_base(cup):
    """
    draws the base of a cup

    :param cup: a Turtle object
    :return: None (void function)
    """

    cup.hideturtle()
    cup.color('#61d4b3')
    cup.pensize(10)
    cup.begin_fill()
    for i in range(4):
        cup.forward(45)
        cup.right(90)

    cup.penup()
    cup.forward(45)
    cup.right(90)
    cup.forward(20)
    cup.circle(15)
    cup.end_fill()


def curve(love):
    """
       draws the love sign on the table
       :param love: a Turtle object
       :return: None (void function)
       """
    love.hideturtle()
    love.begin_fill()
    love.setpos(0, 10)
    for i in range(50):    # Setting up a loop
        love.right(1)
        love.forward(1)

        love.speed(0)
        love.color('#c81912')   # First color is the border color and second color is the fill color.
        love.begin_fill()
        love.left(140)             # Turns the turtle left at an angle of 140 degrees.
        love.forward(95)
        love.color('#c81912')
    love.end_fill()


def draws_table(table):
    """""
        draws a table
         :param table: a Turtle object
       :return: None (void function)
       """
    table.hideturtle()

    table.pensize(18)
    table.penup()
    table.setpos(-45, -59)
    table.pendown()
    table.begin_fill()
    table.color('#00ff22')
    table.forward(100)
    table.right(45)
    table.forward(100)
    table.right(125)
    table.forward(30)
    table.right(45)
    table.forward(65)
    table.left(35)
    table.forward(125)
    table.left(53)
    table.forward(62)
    table.right(90)
    table.forward(30)
    table.right(94)
    table.forward(98)
    table.right(55)
    table.forward(50)
    table.end_fill()


def make_text(txt):
    """
    Writes text to the screen.

    :param txt: a Turtle object
    :return: None
    """

    txt.hideturtle()
    txt.penup()
    txt.color("#ffcc00")
    txt.setpos(0, 120)
    txt.write('Computer Science Is Life!', move=False, align='center', font=("Algerian", 20, ("bold", "normal")))


def main():

    wn = turtle.Screen()
    wn.bgcolor('#ffffff')  # Sets background color.
    cup = turtle.Turtle()
    table = turtle.Turtle()
    love = turtle.Turtle()
    txt = turtle.Turtle()

    # Call Functions
    draw_base(cup)
    draws_table(table)
    make_text(txt)
    curve(love)

    wn.exitonclick()


main()       #call main()