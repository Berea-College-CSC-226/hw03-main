#################################################################################
# Author: Danny Abnee
# Username: abneed
#
# Assignment: HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: It is all about GIT and not creating merge conflicts
# Google Doc Link: https://docs.google.com/document/d/1JqFxISAvIxFo8bfUmzAgvcF1u6JWtTEUi2HYTVH7C8U/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################


import turtle


def DrawChessBoard(jerome):
    """
    This function draws a chess board using turtle.
    """
    jerome.speed(0)
    jerome.pensize(2)
    jerome.color("gold")
    jerome.penup()
    jerome.goto(-200,-200)
    jerome.pendown()
    for i in range(4):
        jerome.forward(400)
        jerome.left(90)
    for i in range(4):
        jerome.forward(50)
        jerome.left(90)
        jerome.forward(400)
        jerome.right(90)
        jerome.forward(50)
        jerome.right(90)
        jerome.forward(400)
        jerome.left(90)
    jerome.left(90)
    for i in range(4):
        jerome.forward(50)
        jerome.left(90)
        jerome.forward(400)
        jerome.right(90)
        jerome.forward(50)
        jerome.right(90)
        jerome.forward(400)
        jerome.left(90)
    jerome.penup()
    jerome.shape("square")
    jerome.shapesize(2.3)
    jerome.goto(-175.5,-174.5)
    for i in range(4):
        jerome.stamp()
        jerome.forward(100)
        jerome.stamp()
        jerome.forward(100)
        jerome.stamp()
        jerome.forward(100)
        jerome.stamp()
        jerome.forward(50)
        jerome.right(90)
        jerome.forward(50)
        jerome.right(90)
        jerome.stamp()
        jerome.forward(100)
        jerome.stamp()
        jerome.forward(100)
        jerome.stamp()
        jerome.forward(100)
        jerome.stamp()
        jerome.forward(50)
        jerome.left(90)
        jerome.forward(50)
        jerome.left(90)
    jerome.goto(250,250)
    jerome.shapesize(1)

def DrawRook(jerome):
    """
    This function draws a Rook piece over top of the chess board.
    """
    jerome.pensize(20)
    jerome.color("black")
    jerome.shape("turtle")
    jerome.penup()
    jerome.goto(-75,-150)
    jerome.pendown()
    jerome.right(90)
    jerome.forward(150)
    jerome.left(110)
    jerome.forward(50)
    jerome.right(20)
    jerome.forward(170)
    jerome.right(90)
    jerome.forward(15)
    jerome.left(90)
    jerome.forward(50)
    for i in range(3):
        jerome.left(90)
        jerome.forward(20)
        jerome.left(90)
        jerome.forward(20)
        jerome.right(90)
        jerome.forward(20)
        jerome.right(90)
        jerome.forward(20)
    jerome.left(90)
    jerome.forward(20)
    jerome.left(90)
    jerome.forward(50)
    jerome.left(90)
    jerome.forward(15)
    jerome.right(90)
    jerome.forward(170)
    jerome.right(25)
    jerome.forward(50)
    jerome.left(115)

    jerome.color("white")
    jerome.pensize(10)
    jerome.forward(150)
    jerome.left(110)
    jerome.forward(50)
    jerome.right(20)
    jerome.forward(170)
    jerome.right(90)
    jerome.forward(15)
    jerome.left(90)
    jerome.forward(50)
    for i in range(3):
        jerome.left(90)
        jerome.forward(20)
        jerome.left(90)
        jerome.forward(20)
        jerome.right(90)
        jerome.forward(20)
        jerome.right(90)
        jerome.forward(20)
    jerome.left(90)
    jerome.forward(20)
    jerome.left(90)
    jerome.forward(50)
    jerome.left(90)
    jerome.forward(15)
    jerome.right(90)
    jerome.forward(170)
    jerome.right(25)
    jerome.forward(50)
    jerome.left(115)
    # ...


def main():
    """
    This function creates the screen with a background and calls the other 2 functions.
    """
    jerome = turtle.Turtle()
    wn = turtle.Screen()
    wn.bgcolor("#3C0372")
    # Function calls to DrawChessBoard and DrawKing.
    DrawChessBoard(jerome)
    DrawRook(jerome)
    wn.exitonclick()

main()  # Starts the program!