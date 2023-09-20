#################################################################################
# Author:Jaela Smith
# Username:smithj5
#
# Assignment:HW03
# Purpose:Homework
# Google Doc Link:https://docs.google.com/document/d/13CGHi_koGhI8SePSLn2inpXajzkOhXyslGOPkxyufRA/edit
#
#################################################################################
# Acknowledgements:I am creating a house with windows and flowers
#
#
#################################################################################


import turtle


def draw_triangle(sally):
    sally.pensize(5)
    sally.penup()
    sally.forward(-150)
    sally.pendown()
    sally.fillcolor("#808080")
    sally.begin_fill()
    for i in range(2):
        sally.forward(200)
        sally.left(120)
    sally.end_fill()
    # sally.forward(200)
    # sally.left(127)
    # sally.forward(200)
    sally.goto(-150, 0)
# draws the triangle for the top of the house #


def draw_rectangle(ted):
    ted.pensize(5)
    ted.penup()
    ted.forward(-150)
    ted.right(90)
    ted.pendown()
    ted.fillcolor("#808080")
    ted.begin_fill()
    for i in range(2):
        ted.forward(250)
        ted.left(90)
        ted.forward(200)
        ted.left(90)
    ted.end_fill()
    # ted.forward(250)
    # ted.left(90)
    # ted.forward(200)
    # ted.right(90)
    # ted.forward(-250)
    ted.penup()
    ted.goto(-100, -250)
    ted.pendown()
    ted.right(180)
    ted.forward(100)
    ted.right(90)
    ted.forward(75)
    ted.right(90)
    ted.forward(100)
# draws the rectangle for the bottom of the house #


def draw_square(patty):
    patty.pensize(2)
    patty.penup()
    patty.goto(40, -45)
    patty.pendown()
    patty.right(90)
    patty.forward(70)
    patty.right(90)
    patty.forward(70)
    patty.right(90)
    patty.forward(70)
    patty.right(90)
    patty.forward(70)
    patty.penup()
    patty.goto(40, -80)
    patty.pendown()
    patty.right(180)
    patty.forward(70)
    patty.penup()
    patty.goto(5, -45)
    patty.pendown()
    patty.left(90)
    patty.forward(70)
# draws the window and lines in the window#


def draw_flower(teddy):
    teddy.pensize(5)
    teddy.penup()
    teddy.color("#FF0000")
    teddy.goto(-200, -250)
    teddy.pendown()
    teddy.right(-90)
    teddy.forward(30)

    for i in range(18):
        teddy.forward(70)
        teddy.left(170)
# draw flower#


def main():
    wn = turtle.Screen()
    sally = turtle.Turtle()
    turtle.Screen().bgcolor("light blue")
    ted = turtle.Turtle()
    teddy = turtle.Turtle()
    patty = turtle.Turtle()
    draw_triangle(sally)                       # call to drawSquare#
    draw_rectangle(ted)                        # drawRectangle
    draw_square(patty)
    draw_flower(teddy)                          # drawFlower
    wn.exitonclick()


main()
