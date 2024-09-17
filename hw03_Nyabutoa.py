
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


def draw_circle(nyabutoa):

#we will be drawing the head using a circle, which serves as a foundational shape for the illustration.

    nyabutoa.goto(0,0)    # The command "nyabutoa.goto(0, 0)" sets the starting point at the center of the circle.The circle will be drawn outwards.
    r=180

# In this function, 'r' stands for radius, which determines the size of the circle.
 # The larger the radius, the bigger the circle will be; this directly affects the size of the head being drawn.

    nyabutoa.pensize(10)
    nyabutoa.circle(r)
    nyabutoa.left(90)
    nyabutoa.penup()
    nyabutoa.forward(r+50)
    nyabutoa.left(90)
    nyabutoa.forward(100)
    nyabutoa.pendown()
    Draw_eyes(nyabutoa)
    nyabutoa.right(90)
    nyabutoa.penup()
    nyabutoa.forward(20)
    nyabutoa.right(90)
    nyabutoa.forward(200)
    nyabutoa.left(180)
    nyabutoa.pendown()
    Draw_eyes(nyabutoa)



def Draw_eyes(eye1):
    e_r=30

# The variable 'e_r' stands for eye radius.
# It defines the size of the eyes to be drawn in relation to the other elements of the drawing

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
    draw_circle(Nyabutoa)
   # eyez(Nyabutoa)
    wn.exitonclick()


main()  # Starts the program!