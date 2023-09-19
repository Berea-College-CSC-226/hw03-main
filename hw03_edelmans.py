#################################################################################
# Author: Sam Edelman
# Username: edelmans
#
# Assignment: hw03 Fully Functional Gitty Psychedelic Robotic Turtles
#
# Purpose:
#   Continue practicing creating and using functions.
#   More practice on using the turtle library.
#   Learn about how computers represent colors.
#   Learn about source control and Git.
#
# Google Doc Link: https://docs.google.com/document/d/1d-mX4dTe4ysHzNasPZLG1phhV-ksM9_mMCXrIqtT3wU/edit#heading=h.ju96mtye4s7l
#################################################################################
# Acknowledgements: Scott Heggen (for template)
#
#################################################################################

import turtle


def head():
    """
    Head of turtle
    """
    pass
    # ....


def body():

    """
    Docstring for function_2
    """
    shell = turtle.Turtle
    shell.pensize(10)

    # ...


def tail():
    """

    """
    pass

def main():
    """
    Drawing a alligator snapping turtle
    """
    # ...
    window = turtle.Screen()

    head()            # Function call to function_1
    body()            # Function call to function_2
    tail()

    turtle.exitonclick()


main()