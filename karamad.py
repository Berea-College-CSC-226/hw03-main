#################################################################################
# Author: Dalmar Karama
# Username: Karamad
#
# Assignment: HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: to make a complex thing or drawing with thr turtle and to use functions
# Google Doc Link: https://docs.google.com/document/d/1UE4I8z1nentPUVQXBxLQUVmLlg7akMKOjNG3yos4x_k/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
##############################################################################


import turtle


def drawSquare(bob, sz):
    """Make turtle t draw a square with side sz."""
    for _ in range(4):
        bob.forward(sz)
        bob.left(90)


def window(bob):
    drawSquare(bob, 80)
    bob.forward(40)
    bob.left(90)
    bob.forward(80)
    bob.backward(40)
    bob.left(90)
    bob.forward(40)
    bob.backward(80)


def roof(bob):
    bob.fillcolor("gray")
    bob.begin_fill()
    bob.left(45)
    bob.forward(350)  # makes roof
    bob.right(89.4)
    bob.forward(355)
    bob.end_fill()


def door(bob):
    bob.penup()  # makes the door
    bob.right(130)
    bob.forward(300)
    bob.left(85)
    bob.forward(370)
    bob.pendown()
    bob.forward(100)
    bob.left(90)
    bob.forward(70)
    bob.left(90)
    bob.forward(100)
    bob.left(90)
    bob.forward(70)


def makes_windows(bob):
    bob.penup()
    bob.goto(-210, 60)
    bob.pendown()
    window(bob)
    bob.penup()  # makes windows
    bob.goto(30, -23)
    bob.pendown()
    window(bob)


def grass(bob):
    bob.left(45)
    bob.forward(30)
    bob.right(90)
    bob.forward(30)
    bob.backward(30)
    bob.left(90)
    bob.backward(30)


def main():
    turtle.screensize(10000, 10000)

    wn = turtle.Screen()
    wn.bgcolor("light blue")

    bob = turtle.Turtle()
    bob.speed(15)

    bob.penup()
    bob.goto(-340, -340)
    bob.pendown()

    bob.fillcolor("light yellow")
    bob.begin_fill()
    drawSquare(bob, 500)
    bob.end_fill()

    bob.penup()
    bob.goto(-340, 160)  # moves bob
    bob.pendown()

    roof(bob)
    door(bob)
    makes_windows(bob)

    bob.penup()
    bob.goto(-800, -358)
    bob.pendown()
    bob.color("green")

    # for _ in range(2):
    #     grass(bob)
    #     bob.right(45)
    #     bob.forward(20)
    #     bob.left(90)
    #     bob.forward(20)

    wn.exitonclick()


if __name__ == "__main__":
    main()