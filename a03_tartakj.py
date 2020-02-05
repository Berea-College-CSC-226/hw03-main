#################################################################################
# Author: Jacek Tartak
# Username: tartkj
#
# Google Docs: https://docs.google.com/document/d/1884_v8JY0_S9ndSunQ-q2NpWi_gngqWtRQI5gqQD-yg/edit?usp=sharing
#
# Assignment: A03 - A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Grow to appreciate pair programming and learn about how computers represent colors.
#################################################################################
# Acknowledgements:
# https://upload.wikimedia.org/wikipedia/en/3/39/Pokeball.PNG (picture of the Pokéball)
# https://www.online-convert.com/  (to change the Pokéball's image from a .png file to a .gif file)
# https://ezgif.com/resize/  (to resize the image of the Pokéball)
# I referenced to "t03_functions_house.py" a lot to help me
# Thanks to Audrey Craft from the TA lab for helping me figure out how to format the image properly.
#
#################################################################################

import turtle
from turtle import Turtle


def stick_figure():
    """
    Creates a stick figure person. 
    """
    baba = turtle.Turtle()
    baba.hideturtle()
    baba.pensize(10)
    baba.penup()
    baba.left(90)
    baba.forward(100)                           # Moves turtle to top of person's neck
    baba.right(90)
    baba.pendown()
    baba.fillcolor("sandy brown")
    baba.begin_fill()
    baba.circle(50)                             # Creates the person's head
    baba.end_fill()
    baba.right(90)
    baba.forward(95)                            # Creates top of torso
    baba.left(150)
    baba.fd(90)                                 # Creates right arm that is "waving"
    baba.back(90)                               # Moves turtle back to torso
    baba.left(8)
    baba.back(90)                               # Creates left arm
    baba.fd(90)                                 # Moves turtle back to torso
    baba.left(22)
    baba.back(105)                              # Creates bottom half of the torso
    baba.left(15)
    baba.back(120)                              # Creates right leg
    baba.fd(120)
    baba.right(30)
    baba.back(120)                              # Creates left leg


def create_face():
    """
    Creates the person's face
    """
    mandy: Turtle = turtle.Turtle()
    mandy.hideturtle()
    mandy.penup()
    mandy.shape("circle")
    mandy.left(90)
    mandy.fd(165)
    mandy.left(90)
    mandy.fd(20)
    mandy.stamp()                                      # Creates left eye
    mandy.back(40)
    mandy.stamp()                                      # Creates right eye
    mandy.fd(20)
    mandy.left(90)
    mandy.fd(40)
    mandy.left(90)
    mandy.fillcolor("salmon")
    mandy.pendown()
    mandy.begin_fill()
    mandy.circle(8)
    mandy.end_fill()                                   # Creates mouth and fills it with the color salmon
    mandy.penup()
    mandy.left(90)
    mandy.fd(40)
    mandy.left(90)
    mandy.fd(4)
    mandy.right(40)
    mandy.pendown()
    mandy.pensize(5)
    mandy.fd(25)                                       # Creates left eyebrow
    mandy.penup()
    mandy.back(25)
    mandy.left(40)
    mandy.back(8)
    mandy.left(40)
    mandy.pendown()
    mandy.back(25)                                     # Creates right eyebrow


def pokéball(wn):
    """
    Puts a Pokéball in the person's hand
    """
    pika = turtle.Turtle()
    pika.hideturtle()
    wn.register_shape("Pokeball2.gif")
    pika.color("white")                                 # changes color to white for debugging
    pika.penup()
    pika.left(90)
    pika.fd(5)
    pika.right(30)
    pika.fd(95)                                         # Moves turtle to the person's hand
    pika.shape("Pokeball2.gif")
    pika.stamp()                                        # Stamps the picture of the Pokéball


def text():
    """
    Writes the words "Go Pikachu!"
    """
    phrase = turtle.Turtle()
    phrase.hideturtle()
    phrase.penup()
    phrase.setpos(90, 150)
    phrase.color(255, 220, 5)
    phrase.write("Go, Pikachu!", font=("Arial", 30))


def main():
    """
    Sets the window attributes.
    Calls functions to create person's body and creates a face for the person.
    Calls function to put a Pokéball on the person's hand.
    Calls function to write the words.
    """
    wn = turtle.Screen()
    wn.colormode(255)
    wn.bgcolor(115, 139, 120)

    stick_figure()

    create_face()

    pokéball(wn)

    text()

    wn.exitonclick()



main()
