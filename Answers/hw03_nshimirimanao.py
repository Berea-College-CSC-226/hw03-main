#################################################################################
# Author: Briana Nshimirimana
# Username: Nshimirimanao
#
# Assignment: HW03_Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose:
# Google Doc Link: https://docs.google.com/document/d/1ZtcYU7PHItUzZ4hzqbLtUHBl__7jwoWPN-NipuDiB8Q/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
# hw03_stubs_do_not_edit.py
#
#################################################################################


import turtle


def Horizon(Hz):
    """
     Uses turtle to draw a horizontal line across the screen to signify the horizon.
    """
    Hz.goto(-700,0)


def function_2():
    """
    Example docstring for function_2. function_2 is not a good function name and should be changed.
    """
    pass
    # ...


def main():
    """
    Docstring for main. Should describe the main functionality of this file.
    """
    wn = turtle.Screen()
    wn.bgcolor("blue")
    t = turtle.Turtle()
    t.color("orange""red")
    Hz = turtle.Turtle()
    Hz.speed(0)
    Hz.color("darkblue")
    # Function calls to function_1 and function_2.
    Horizon(Hz)
    function_2()
    wn.exitonclick()


main()  # Starts the program!