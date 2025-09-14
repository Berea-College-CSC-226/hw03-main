#################################################################################
# Author: Pier Ciccariello
# Username: ciccariellop
#
# Assignment: HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Practice w/ functions, turtles, and python in general
# Google Doc Link: https://docs.google.com/document/d/1GoGJoL2peNQtOe6GWwlO17fe6I_66j5E4ZYtaTG-Bw0/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################


import turtle




def draw_square():
    for i in range(4):
        turtle.forward(75)
        turtle.left(90)


def main():
    wn = (turtle.Screen()
    wn.bgcolor("purple"))
    tess = turtle.Turtle()
    tess.color("black")

main()