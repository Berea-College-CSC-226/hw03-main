#################################################################################
# Author: Destiny White
# Username: whited3
#
# Assignment:HW03- Fully Functional GItty Psychedelic Turtles
# Purpose: To learn more about git, functions, and doc strings
# Google Doc Link: https://docs.google.com/document/d/1JwFWjoXfjxo1U_hnxmwLi8dFDfw2O1sIfiP6n8Y5bWw/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle

def mb():
    """
    Creating the main building part of my house
    """
    mb = turtle.Turtle()
    mb.ht()
    mb.up()
    mb.setpos(-100, -100)
    mb.down()
    mb.fillcolor('#eb5c0d')
    mb.pencolor('#eb5c0d')
    mb.begin_fill()
    for i in range(2):      # rectangle
        mb.fd(200)
        mb.left(90)
        mb.fd(50)
        mb.left(90)
    mb.end_fill()

    mb.left(90)
    mb.fd(50)

    mb.pencolor('royal blue')
    mb.fillcolor('royal blue')
    mb.begin_fill()
    for f in range(2):      ##TODO: Change placeholder colors
        mb.fd(100)
        mb.right(90)
        mb.fd(200)
        mb.right(90)
    mb.end_fill()

    mb.pencolor('green')
    mb.fillcolor('green')
    mb.begin_fill()

    mb.fd(100)
    mb.right(45)
    mb.fd(100)
    mb.right(45)
    mb.fd(60)
    mb.right(45)
    mb.fd(100)
    mb.right(135)
    mb.fd(200)

    mb.end_fill()


def chim():
    ch = turtle.Turtle()
    ch.pencolor('yellow')
    ch.ht()
    ch.up()
    ch.setpos(50, 100)
    ch.left(90)
    ch.down()

    ch.fillcolor('yellow')
    ch.begin_fill()
    ch.fd(20)
    ch.right(90)
    ch.fd(40)
    ch.right(90)
    ch.fd(80)
    ch.right(135)
    ch.fd(60)
    ch.end_fill()






def main():
    wn = turtle.Screen()
    wn.setup(400, 400)


    chim()
    mb()
    wn.exitonclick()

main()