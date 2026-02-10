#################################################################################
# Author: Alain Irumva
# Username: irumvaa
#
# Assignment: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Source Control and Git
# Google Doc Link: https://docs.google.com/document/d/1pOIbG65CpjYltCJQEnEJ-lRjg3jt2vX88Tf9P7UaTw0/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################


import turtle
alain = turtle.Turtle()
turtle.colormode(255)
wn = turtle.Screen()
wn.bgcolor('lightgreen')
turtle.pensize(4)
def build_my_roof():
    alain.color("black", "brown")
    alain.speed(0)
    alain.penup()
    alain.goto(-220,140)
    for i in range (1):
        alain.begin_fill()
        alain.pendown()
        alain.fd(300)
        alain.left(160)
        alain.fd(200)
        alain.left(50)
        alain.fd(130)
        alain.right(200)
        alain.end_fill()
        alain.penup()
        alain.color("blue")
        alain.fd(60)
        alain.right(100)
        alain.fd(15)
        alain.pendown()
        alain.fd(90)
        alain.left(90)
        for i in range(80):
            alain.color("black", "yellow")
            alain.begin_fill()
            alain.right(120)
            alain.fd(40)
            alain.left(50)
            alain.fd(40)
            alain.end_fill()
        alain.penup()
        alain.right(80)
        alain.fd(150)
        alain.right(80)
        alain.fd(280)
        alain.right(90)
        alain.fd(15)
        alain.pendown()
        alain.color("blue")
        alain.fd(100)

build_my_roof()


wn.exitonclick()







#     # """
#     # Example docstring for function_1. function_1 is not a good function name and should be changed.
#     # """
#     pass
#     # ....
#
#
# def function_2():
#     """
#     Example docstring for function_2. function_2 is not a good function name and should be changed.
#     """
#     pass
#     # ...
#
#
# def main():
#     """
#     Docstring for main. Should describe the main functionality of this file.
#     """

#
# main()  # Starts the program!
# shape.write("My House",move=False,align='center',font=("Arial",30,("bold","normal")))