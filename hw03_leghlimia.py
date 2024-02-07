# Author: Mahmoud Leghlimi
# Username: Leghlimi
#
# Assignment: HW03
# Purpose:
# Google Doc Link: https://docs.google.com/document/d/1wAef8xBkCldLnTCKJWgGhmvbp0nYVJpMk71C0vCxwEs/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
################################################################################

import turtle


def draw_human(mah):
    """
    This function draws a human.
    """
    mah.goto(100, 70)
    mah.right(180)
    mah.pendown()
    mah.color("#cfd6d4")
    mah.circle(30, 360)   # Drawing human head
    mah.penup()
    mah.color("black")
    mah.left(90)
    mah.forward(60)
    mah.pendown()
    mah.forward(130)      # Drawing body
    mah.penup()
    ar = [45, -90]
    for i in ar:     # Drawing hands and feet
        mah.goto(100, -10)
        mah.right(i)
        mah.pendown()
        mah.forward(60)
        mah.penup()
        mah.goto(100, -120)
        mah.pendown()
        mah.forward(70)
        mah.penup()

def sword(mah):
    """
    This function draws a sword.
    """
    mah.pensize(2.5)
    mah.goto(142, -54.4)
    mah.left(45)
    mah.forward(10)
    mah.left(180)
    mah.pendown()
    mah.forward(25)        # Drawing sword handler
    mah.penup()
    mah.goto(140, -54.4)
    mah.right(90)
    mah.pendown()
    mah.forward(20)
    mah.penup()
    mah.right(180)

    for i in [35, -35]:       # Drawing the blade
        if i == -35:
            mah.goto(133, -54.4)
            mah.left(35)
        else:
            mah.goto(147,-54.4)
        mah.pendown()
        mah.forward(70)
        mah.right(i)
        mah.forward(14.6)
        mah.penup()


def main():
    wn = turtle.Screen()
    wn.bgpic("the-witcher-3-wild-hunt-the-witcher-3-wild-hunt-blood-and-wine-toussaint-geralt-of-rivia-the-witcher-hd-wallpaper-preview.png")
    mah = turtle.Turtle()
    mah.speed(8)
    mah.pensize(6)
    mah.penup()

    draw_human(mah)
    sword(mah)

    wn.exitonclick()


main()
