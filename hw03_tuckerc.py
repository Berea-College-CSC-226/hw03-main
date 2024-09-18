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
    turtle.penup() # To prevent random lines
    turtle.goto (-100, -100) # Goes to bottom left corner of future square
    turtle.begin_fill() # Begins filling the square
    turtle.left(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(200)
    turtle.end_fill() # Ends filling the square
    turtle.right(180) # Faces to original position


def draw_duck():
    """
    Draws the duck.
    """
    # Draws the duck's body
    turtle.goto(0, -50)
    turtle.color('#FFFF00') # Yellow
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()

    # Draws the duck's bill
    turtle.goto(50, 30)
    turtle.color('#FFA500')  # Orange
    turtle.begin_fill()
    turtle.goto(50, 38)
    turtle.goto(70, 30)
    turtle.goto(50, 26)
    turtle.goto(50, 38)
    turtle.end_fill()

    # Draws the duck's head
    turtle.goto(40, 20)
    turtle.color('#FFFF00')  # Yellow
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()

    # Draws the duck's beady black eyeball
    turtle.goto(50, 40)
    turtle.color('#000000')  # Black
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()

    turtle.hideturtle() # Hides the turtle because it looks ugly at the end



def main():
    """
    The main function that calls the other two functions, which draw the background and then the duck.
    """
    draw_bg()
    draw_duck()
    turtle.exitonclick() # Waits until the user clicks to exit the drawing so you can admire the pretty duck


main()  # The beginning of something great