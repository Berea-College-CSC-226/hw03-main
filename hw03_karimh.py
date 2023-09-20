
# Author: Hira Karim
# Username: karimh
#
# Assignment: HW03-Fully Functional Gitty Psychedelic Robotic Turtle
# Purpose: To create a code using functions, and submit a pull request.
# Google Doc Link: https://docs.google.com/document/d/12MLXaEkr6jyzp5jVL2UXoEJTj2VyV12LwCJIk-eW6fs/edit?usp=sharing

import turtle

def tyres(rad, th):
    "rad = radius of the circle"
    "th = thickness of the tyre"
    turtle.pensize(th)
    turtle.circle(rad)



def function_2():
    "docstring"

def function_3():
    "docstring"

def fucntion_4():
    "docstring"

def main ():
    wn = turtle.Screen()
    wn.colormode(255)
    wn.bgcolor("purple")

    #call functions
    tyres(100, 10)
    wn.exitonclick()
main()