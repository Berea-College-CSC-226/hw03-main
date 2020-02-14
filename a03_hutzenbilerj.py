######################################################################
# Author: James Hutzenbiler
# Username: hutzenbilerj
#
# Assignment: hutzenbiler - A03: A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: further our knowledge of functions
######################################################################
# Acknowledgements:

#################################################################################

# snail drawing

import turtle

# draw the ground

def ground():
    """
    this function creates the ground of the picture
    :return:
    """
    dirt = turtle.Turtle()
    dirt.color("#bc5a16")
    dirt.penup()
    dirt.setpos(-400, -80)
    dirt.pendown()
    dirt.speed(0)
    dirt.begin_fill()
    for i in range(2):
        dirt.fd(800)
        dirt.right(90)
        dirt.fd(200)
        dirt.right(90)
    dirt.end_fill()
    pass
# draw background (look main)
# draw the snail shell

def snail_shell():
    """
    This function creates the shell of the snail
    :return:
    """
    shell = turtle.Turtle()
    shell.pensize(10)
    shell.speed(0)
    shell.color("#35c58e")
    go_fd = .5
    shell.penup()
    shell.setpos(150, -75)
    shell.pendown()
    shell.begin_fill()
    for i in range(100):
        go_fd = go_fd + .5
        shell.fd(go_fd)
        shell.right(20)
    shell.end_fill()
    shell.pencolor("black")
    shell.penup()
    shell.setpos(150, -75)
    shell.pendown()
    go_fd2 = .5
    shell.setheading(0)
    for i in range(100):
        go_fd2 = go_fd2 + .5
        shell.fd(go_fd2)
        shell.right(20)
    shell.right(90)
    shell.fd(25)
    shell.hideturtle()
    pass
# draw the snail head + body


def snail_head():
    head = turtle.Turtle()
    head.pensize(5)
    head.speed(0)
    head.color("#d4e410")
    head.penup()
    head.setpos(150, -100)
    head.pendown()
    head.left(180)
    head.begin_fill()
    for i in range(2):
        head.fd(200)
        for n in range(45):
            head.left(2)
            head.fd(1)
        head.fd(50)
        for n in range(45):
            head.left(2)
            head.fd(1)
    head.end_fill()

def snail_eyes():
    """
    This Function creates both the first and the second eye of the snail
    :return:
    """
    # First Eye
    eyes1 = turtle.Turtle()
    eyes1.pensize(25)
    eyes1.penup()
    eyes1.setposition(-60, -110)
    eyes1.pendown()
    eyes1.left(130)
    eyes1.fd(100)
    eyes1.pensize(75)
    eyes1.fd(1)
    # Second Eye
    eyes2 = turtle.Turtle()
    eyes2.pensize(25)
    eyes2.penup()
    eyes2.setposition(-40, -110)
    eyes2.pendown()
    eyes2.left(85)
    eyes2.fd(100)
    eyes2.pensize(75)
    eyes2.fd(1)

# main function


def main():
    """
    this function calls all the other functions in the code, as well as creating the screen and the background
    :return:
    """
    wn = turtle.Screen()
    wn.bgcolor("#19a1f9")

    ground()
    snail_eyes()
    snail_head()
    snail_shell()
    wn.exitonclick()


main()


