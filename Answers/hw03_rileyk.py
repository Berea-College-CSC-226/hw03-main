#################################################################################
# Author: Boone Riley
# Username: rileyk
#
# Assignment: HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Creative drawing of a UFO
# Google Doc Link: https://docs.google.com/document/d/1Rr4vIPVRLXlNXfkz7AHrMYtzlTRI_a0lpDhTECapNCE/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle


def ufo(alien):
    alien.pensize(20)
    alien.pencolor('green')
    alien.forward(50)

def main():
    alien = turtle.Turtle()
    wn = turtle.Screen()
    wn.bgcolor('purple')
    ufo(alien)
    wn.exitonclick()


main()