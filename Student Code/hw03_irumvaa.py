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
    alain.color("black")
    alain.speed(5)
    alain.penup()
    alain.goto(-220,140)
    for i in range (3):
        alain.pendown()
        alain.fd(300)
        alain.left(120)
        alain.fd(120)
        alain.left(140)
        alain.fd(120)
        alain.fillcolor("brown")
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
#     # Function calls to function_1 and function_2.
#     function_1()            # TODO  Remove when you replace it with your function
#     function_2()            # TODO  Remove when you replace it with your function
#
#
# main()  # Starts the program!
# shape.write("My House",move=False,align='center',font=("Arial",30,("bold","normal")))