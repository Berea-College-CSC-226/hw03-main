# Author: Cameron Bridgeman
# Username: bridgemanc
#
# Assignment: A03 :Fully Functional Psychedelic Robotic Turtles
# Purpose: To learn how to draw something complex using RGB color values, functions, and more.
#################################################################################
# Acknowledgements:
# I learned how to make an ellipse using stack overflow and the turtle library.
#
#################################################################################
"""
https://docs.google.com/document/d/1MRXaVI8EXFYSslI0LNRlnHnRB7RjeiekIddHja_8Lks/edit?usp=sharing
Cameron Bridgeman
"""
import turtle
wn = turtle.Screen()
wn.bgcolor("gray")
turtle.pensize(8)
def function_1():
        #draws the face and hair of the alien
    turtle.penup()
    turtle.goto(0, -100)
    turtle.pendown()
    turtle.circle(130)
    turtle.penup()
    turtle.goto(0, 160)
    turtle.pendown()
    turtle.left(90)
    turtle.goto(5, 220)
    turtle.goto(20, 160)
function_1()

def function_2():
        #draws the eye of the alien
    turtle.penup()
    turtle.goto(30, 75)
    turtle.pendown()
    turtle.colormode(255)
    turtle.fillcolor(70, 50, 100)
    turtle.begin_fill()
    turtle.circle(40)
    turtle.end_fill()
function_2()


def main():
        #draws the mouth of the alien
    turtle.penup()
    turtle.right(180)
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(-70)
    turtle.right(90)
    turtle.pendown()
    turtle.circle(30, 180)
    turtle.left(90)
    turtle.forward(60)

main()

wn.exitonclick()