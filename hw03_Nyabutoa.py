
#################################################################################
# Author: Alpha Nyabutop
# Username: Nyabutoa
#
# Assignment:HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose:
# Google Doc Link:https://docs.google.com/document/d/1A_q6VWbkQ8u_noD3prdv25tmySfbxk-JVBYkq4vUlPI/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################


import turtle


def circlec(nyabutoa):
    nyabutoa.goto(0,0)
    r=180
    nyabutoa.pensize(10)
    nyabutoa.circle(r)
    nyabutoa.left(90)
    nyabutoa.penup()
    nyabutoa.forward(r+50)
    nyabutoa.left(90)
    nyabutoa.forward(100)
    nyabutoa.pendown()
    eyez(nyabutoa)
    nyabutoa.right(90)
    nyabutoa.penup()
    nyabutoa.forward(20)
    nyabutoa.right(90)
    nyabutoa.forward(200)
    nyabutoa.left(180)
    nyabutoa.pendown()
    eyez(nyabutoa)



def eyez(eye1):
    e_r=30
    eye1.pensize(4)
    for i in range(5):
        eye1.circle(e_r)
        eye1.left(90)
        eye1.penup()
        eye1.forward(4)
        eye1.right(90)
        eye1.pendown()
        e_r=e_r-4




def main():
    Nyabutoa=turtle.Turtle()
    wn = turtle.Screen()
    wn.bgcolor("Purple")
    circlec(Nyabutoa)
   # eyez(Nyabutoa)
    wn.exitonclick()


main()  # Starts the program!