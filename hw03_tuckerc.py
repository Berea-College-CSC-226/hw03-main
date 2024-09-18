################################################################################
# Author: Caleb Tucker
# Username: tuckerc
#
# Assignment: HW03
# Purpose: To draw something complex using turtles, like a house, animal, or person
# Google Doc Link: https://docs.google.com/document/d/1Xw1e0TFWaXDlRICmIxsiKXDqgC0jr2wqghk2cMqD0TE/edit?usp=sharing
#
#################################################################################
# Acknowledgements: The Python Documentation, hw03_stubs.py
#
#
#################################################################################


import turtle


def draw_bg():
    """
    Creates the required colored background.
    """
    turtle.fillcolor('#00BFFF') # Blue
    turtle.penup() # To prevent random line
    turtle.goto (-100, -100)
    turtle.left(90)
    turtle.begin_fill() # Begins filling the shape
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(200)
    turtle.end_fill() # Ends filling the shape
    turtle.right(180) # Turns to original position


def draw_duck():
    """
    Draws the duck.
    """
    pass
    # ...


def main():
    """
    The main function that calls the other two functions, which draw the background and then the duck.
    """

    draw_bg()
    draw_duck()
    turtle.exitonclick() # Waits until the user clicks to exit the program


main()  # Starts the program!