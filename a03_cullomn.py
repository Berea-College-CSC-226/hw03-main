######################################################################
# Author: Egypt Cullom
# Username: Cullomn
#
# Assignment: A03: A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: To practice in the homework assignment
# Google Doc: https://docs.google.com/document/d/1wk0P0rvhLUB784h54Wj2_DiV8qFMQrsLRJ1kUItCQCI/edit?usp=sharing
######################################################################
# Acknowledgements:
# https://www.w3schools.com/colors/colors_picker.asp
# I used source to pick my colors.  I used it throughout high school and I find
# that it is easier for me to use.
#################################################################################

import turtle

wn = turtle.Screen()
wn.bgcolor('green')

# eye turtle
joe = turtle.Turtle()
joe.shape('turtle')
joe.speed(20)

# facial structure turtle
jeff = turtle.Turtle()
jeff.shape('circle')
jeff.speed(20)
jeff.pencolor('#b37700')

# nose turtle
fred = turtle.Turtle()
fred.shape('square')
fred.speed(20)
fred.pencolor('#b37700')

# mouth turtle
pam = turtle.Turtle()
pam.shape('triangle')
pam.speed(20)
pam.pencolor('#f425af')


# head
def head():
    """
    Drawing the circle for the head
    :return: Big circle
    """
    jeff.pensize(20)
    jeff.penup()
    jeff.setheading(270)
    jeff.forward(90)
    jeff.pendown()
    jeff.left(90)
    jeff.circle(180, 360, 30)


def positioning():
    """
    moving turtles to begin the facial features
    :return: None
    """
    joe.penup()
    joe.setheading(115)
    joe.forward(150)
    joe.setheading(0)
    joe.pendown()
    # fred moves to the nose position
    fred.pensize(5)
    fred.penup()
    fred.setheading(90)
    fred.forward(125)
    fred.setheading(130)
    fred.pendown()


def eyes():    # Eyes
    """
    Loop build to draw the cornea and pupil of the eyes
    :return: White Cornea and black pupil
    """
    joe.pendown()
    for j in range(3):  #cornea
        joe.color('white')
        joe.pensize(5)
        joe.circle(20, 120, 5)
    for j in range(3):   #pupil
        joe.color('black')
        joe.pensize(5)
        joe.circle(10, 120, 5)
    joe.penup()


# nose
def nose():
    """
    Drawing the curve of the nose
    :return: Nose
    """
    fred.circle(20, 220, 10)


def transition():
    """
    Moving to the new eye position
    :return: None
    """
    joe.setheading(0)
    joe.forward(100)


#   Ear
def ear():
    """
    Puts a curve along the head to form the ear
    :return: Ear
    """
    jeff.penup()
    jeff.setheading(90)
    jeff.forward(200)
    jeff.setheading(0)
    jeff.forward(180)
    jeff.setheading(270)
    jeff.forward(60)
    jeff.pendown()
    jeff.setheading(0)
    jeff.circle(30, 180, 4)


def mouth():  #lips are being formed
    """
    Drawing the curvature of the lips
    :return: Lip outline
    """
    pam.penup()
    pam.setheading(90)
    pam.forward(20)
    pam.setheading(180)
    pam.forward(30)
    pam.pendown()
    pam.pensize(10)
    pam.setheading(0)
    pam.circle(15, 90, 3)
    pam.setheading(270)
    pam.circle(15, 180, 3)
    pam.setheading(270)
    pam.circle(15, 90, 3)
    pam.setheading(270)
    pam.circle(-30, 180, 3)


# clearing shapes out of the picture
def pen_shapes_move():
    """
    Clearing the image of the stray shapes
    :return: None
    """
    joe.penup()
    joe.setheading(270)
    joe.forward(300)
    jeff.penup()
    jeff.setheading(270)
    jeff.forward(300)
    fred.penup()
    fred.setheading(270)
    fred.forward(300)
    pam.penup()
    pam.setheading(270)
    pam.forward(300)


def main():
    """
    Puts the face together
    :return: Lil Bill's Girlfriend
    """
    head()
    positioning()
    eyes()
    nose()
    transition()
    eyes()
    ear()
    mouth()
    pen_shapes_move()


main()
wn.exitonclick()
