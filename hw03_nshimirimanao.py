#################################################################################
# Author: Briana Nshimirimana
# Username: nshimirimanao
#
# Assignment: HW03_ Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Creating a house with a shooting star behind in the background of the house.
# Google Doc Link:
#
#################################################################################
# Acknowledgements: Scott Heggen
#
#
#################################################################################


import turtle


def body_of_house(berea):
    """
    Creating the rectangle for the body of the house.
    """
    berea.setpos(100, 50)
    berea.color('brown')
    berea.begin_fill()
    for side in range(2):
        berea.forward(100)
        berea.right(90)
        berea.forward(140)
        berea.right(90)
    berea.end_fill()
    # ....


def roof_of_house():
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
    berea = turtle.Turtle()
    body_of_house()




    wn.exitonclick()

    # Function calls to function_1 and function_2.
    #function_1()            # TODO  Remove when you replace it with your function
    #function_2()            # TODO  Remove when you replace it with your function


main()  # Starts the program!