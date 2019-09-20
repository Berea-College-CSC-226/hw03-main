########################################################################################################################
# Author: Samantha Schweinsberg
# Username: Schweinsbergs
#
# Assignment: A03 A Pair of Fully-Functional Gitty Psychedelic Turtles
#
# Purpose: To create a decently friendly puppy
# https://docs.google.com/document/d/1F0p1RUkWr2HRi5TaR7jY76hfCaQDz0nHv14eZImY7uw/edit?usp=sharing
########################################################################################################################


import turtle


def CreateHead(turtle):
    """
    Creates the head for the puppy we're making!
    :return: none
    """
    turtle.penup()
    turtle.speed(0)
    turtle.setpos(100,-50)
    turtle.pendown()
    turtle.color("#bd9f60")
    turtle.shape('arrow')
    turtle.begin_fill()
    for head in range(4):
        turtle.left(90)
        turtle.forward(200)
    turtle.end_fill()

def CreateEars(turtle):
    """
    Creates the ears for the puppy we're making!
    :return: none
    """
    turtle.penup()
    turtle.speed(0)
    turtle.setpos(100,150)
    turtle.pendown()
    turtle.color("#615232")
    turtle.shape('arrow')
    turtle.begin_fill()
    for ears in range(2):
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(300)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.setpos(-200,150)
    turtle.pendown()
    turtle.begin_fill()
    for earstwo in range(2):
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(300)
        turtle.right(90)
    turtle.end_fill()

def DrawEyes(turtle):
    """
    Gives eyes to the puppy we're drawing!
    :return: none
    """
    turtle.penup()
    turtle.speed(0)
    turtle.color('light blue')
    turtle.shape('arrow')
    turtle.setpos(-70,100)
    turtle.pendown()
    turtle.begin_fill()
    for eyesone in range(4):
        turtle.forward(30)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.setpos(40,100)
    turtle.pendown()
    turtle.begin_fill()
    for eyestwo in range(4):
        turtle.forward(30)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()

def DrawNose(turtle):
    turtle.penup()
    turtle.setpos(-15,40)
    turtle.shape('arrow')
    turtle.color('light pink')
    turtle.pendown()
    turtle.begin_fill()
    for nose in range(3):
        turtle.forward(30)
        turtle.left(-120)
    turtle.end_fill()

def DrawMouth(turtle):
    """
    Makes a mouth and tongue for our puppy!
    """
    turtle.penup()
    turtle.color('black')
    turtle.setpos(-50,20)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(30)

    turtle.penup()
    turtle.color('red')
    turtle.setpos(-20,-11)
    turtle.pendown()
    turtle.begin_fill()
    for tongue in range(2):
        turtle.right(90)
        turtle.forward(40)
        turtle.right(90)
        turtle.forward(90)
    turtle.penup()
    turtle.setpos(700,700)

    turtle.end_fill()





def main(turtle):
    """
    Calls all of the functions in order so that the puppy can be drawn!
    :return: none
    """
    wn = turtle.Screen()
    wn.bgcolor('light green')
    CreateHead(turtle)
    CreateEars(turtle)
    DrawEyes(turtle)
    DrawNose(turtle)
    DrawMouth(turtle)
    wn.exitonclick()

main(turtle)
