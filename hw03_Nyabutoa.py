
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
    """
    we will be drawing the head using a circle, which serves as a foundational shape for the illustration.
    The command "nyabutoa.goto(0, 0)" sets the starting point at the center of the circle.The circle will be drawn outwards.
    In this function, 'r' stands for radius, which determines the size of the circle.
    The larger the radius, the bigger the circle will be; this directly affects the size of the head being drawn.
    """

    nyabutoa.goto(0,0)
    r=180
    nyabutoa.pensize(10)
    nyabutoa.circle(r)
    nyabutoa.left(90)
    nyabutoa.penup()
    #nyabutoa.forward(r+50)
    #nyabutoa.left(90)
    #nyabutoa.forward(100)
    #nyabutoa.pendown()
    #Draw_eyes(nyabutoa)
    #nyabutoa.right(90)
    #nyabutoa.penup()
    #nyabutoa.forward(20)
    #nyabutoa.right(90)
    #nyabutoa.forward(200)
    #nyabutoa.left(180)
    #nyabutoa.pendown()
    #Draw_eyes(nyabutoa)



def Draw_eyes(eye1, x, y ):
    eye_radius=30
    """
     The variable 'eye_radius' stands for eye radius.
     It defines the size of the eyes to be drawn in relation to the other elements of the drawing
    """

    eye1.goto(x,y)
    eye1.pensize(4)
    for i in range(5):
        eye1.pendown()
        eye1.circle(eye_radius)
        eye1.left(90)
        eye1.penup()
        eye1.forward(4)
        eye1.right(90)
        eye1.pendown()
        eye_radius=eye_radius-4
    eye1.penup()

def make_mouth(Mouth):
    """
        This is the function to create the mouth.
        I used the name "make_mouth" in order to kno what this function will do.
        using a for loop we will create the mouth into a rectangle.
        """

    #
    Mouth.goto(-50,90)
    Mouth.stamp()
    Mouth.pensize(15)
    for i in range(2):
        Mouth.pendown()
        Mouth.forward(20)
        Mouth.right(90)
        Mouth.forward(100)
        Mouth.right(90)
        # Mouth.forward(20)
        # Mouth.right(90)
        # Mouth.forward(100)










def main():
    Nyabutoa=turtle.Turtle()
    wn = turtle.Screen()
    wn.bgcolor("Purple")
    draw_circle(Nyabutoa)
    Draw_eyes(Nyabutoa , -70, 200)
    Draw_eyes(Nyabutoa, 120,200)
    make_mouth(Nyabutoa)
    wn.exitonclick()


main()  # Starts the program!