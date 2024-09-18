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


def draw_bg(t):
    """
    Creates the required colored background.
    """
    t.fillcolor('#00BFFF') # Blue
    t.penup() # To prevent random lines
    t.goto (-100, -100) # Goes to bottom left corner of future square
    t.begin_fill() # Begins filling the square
    t.left(90)
    t.forward(200)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(200)
    t.end_fill() # Ends filling the square
    t.right(180) # Faces to original position


def draw_duck(t):
    """
    Draws the duck.
    """
    # Draws the duck's body
    t.goto(0, -50)
    t.color('#FFFF00') # Yellow
    t.begin_fill()
    t.circle(50)
    t.end_fill()

    # Draws the duck's bill
    t.goto(50, 30)
    t.color('#FFA500')  # Orange
    t.begin_fill()
    t.goto(50, 38)
    t.goto(70, 30)
    t.goto(50, 26)
    t.goto(50, 38)
    t.end_fill()

    # Draws the duck's head
    t.goto(40, 20)
    t.color('#FFFF00')  # Yellow
    t.begin_fill()
    t.circle(20)
    t.end_fill()

    # Draws the duck's beady black eyeball
    t.goto(50, 40)
    t.color('#000000')  # Black
    t.begin_fill()
    t.circle(5)
    t.end_fill()

    t.hideturtle() # Hides the turtle because it looks ugly at the end



def main():
    """
    The main function that calls the other two functions, which draw the background and then the duck.
    """
    wn = turtle.Screen()
    t = turtle.Turtle()
    draw_bg(t)
    draw_duck(t)
    wn.exitonclick() # Waits until the user clicks to exit the drawing so you can admire the pretty duck


main()  # The beginning of something great