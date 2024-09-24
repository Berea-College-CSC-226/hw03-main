# TODO Do not edit this file directly!
# TODO Instead, create a new file called hw03_username.py and copy this code into it!

#################################################################################
# Author: Janee Amig
# Username: Amigj
#
# Assignment: HW03
# Purpose: Complex turtling
# Google Doc Link: https://docs.google.com/document/d/1ZubPrhdobqaMp-9kqOMK8lZNzvwYkhv42pZEmzof-wU/edit
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################
#Has at least one complex thing which looks like something; a building, animal,  person, etc.
#Is set against a background which is not white. You can use an image or a color as your background.
#Has some embellishments or interesting details, such as windows, text, trees, flowers in front of a house, intricate windows, smoke out of the chimney, or something; these are not all required, they are just suggestions. Be creative!
#Use an unnamed color using either RGB or Hexadecimal.
#Use creativity (such as the use of color, an intricate shape, a cool design…)


import turtle


def round (t,r):
    """
    Draws a circle and fills in with any color.
    """

    t.begin_fill()
    t.circle(radius = r)
    t.color("yellow")
    t.end_fill()

    # ....


def quad (t,l,w):
    """
        Make a qualuilatural shape (rectangle or squares can be made.
    """
    for q in range(2):
        t.forward(l)
        t.right(90)
        t.forward(w)
        t.right(90)
    # ...


def main():
    """

    """
    wn = turtle.Screen()
    jimmy = turtle.Turtle()
    round(jimmy,100)
    quad(jimmy, 150,70)



    wn.exitonclick()



main()  # Starts the program!