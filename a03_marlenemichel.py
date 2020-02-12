######################################################################
# Author: Marlene Michel
# Username: marlene_michel
# Assignment: A03 Homework
# Purpose: Grow to appreciate pair programming a little more.
# Continue practicing creating and using functions.
# More practice on using the turtle library.
# Learn about how computers represent colors.
# Learn about source control and git.
#My Google Doc: https://docs.google.com/document/d/17QTuMc8SVthGLcW6Yk_iwFCilBglBZ0AI1wx4FpWOBo/edit#
######################################################################
# Acknowledgements:
#Dr. Scott Heggen for the learning objectives for the A03 Assignments.

# original from http://openbookproject.net/thinkcs/python/english3e/functions.html
#
# Modifications by Dr. Jan Pearce
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
#################################################################################

import turtle


def draw_multicolor_square(t, sz):
    """
    Creates a multicolor square

    :param t: a Turtle object
    :param sz: size of a side of a square
    :return: None (void function)
    """

    for i in ["red", "yellow", "orange", "white"]:
        t.color(i)
        t.forward(sz)
        t.left(80)
def Fireworkshow(Maria, size, wn, mariacolor):
    for i in range(15):
        draw_multicolor_square(Maria, size)  # Calls this function each iteration of the loop
        size = size + 5  # Increase the size for next iteration
        Maria.forward(10)  # Move Maria along a bit
        Maria.right(18)  # and give her some turn
        wn.bgcolor(mariacolor)



def main():
    """
    Makes a multicolored spiralling set of squares

    :return: None
    """

    wn = turtle.Screen()        # Set up the window and its attributes
    wn.bgcolor("orange")
    wn.title("Sunshine State! From sunrise to sunset!")

    Maria = turtle.Turtle()      # Create Maria and set some attributes
    Maria.pensize(3)
    turtle.colormode(255)
    Maria.pencolor((254,254,0))

    size = 25                  # Size of the smallest square
    for i in range(15):
        draw_multicolor_square(Maria, size)  # Calls this function each iteration of the loop
        size = size + 5       # Increase the size for next iteration
        Maria.forward(10)        # Move Maria along a bit
        Maria.right(18)          # and give her some turn
        wn.bgcolor("red")
    Maria.setpos(100,100)
    size = 25  # Size of the smallest square
    Fireworkshow(Maria, size, wn, "yellow")
    Maria.setpos(-100,-100)
    Fireworkshow(Maria,size,wn,"purple")



    wn.exitonclick()



main()                          # Calls the main function

