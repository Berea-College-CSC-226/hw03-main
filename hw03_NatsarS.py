#################################################################################
# Author: Salaam Natsar
# Username: NatsarS
#
# Assignment: Homework 03
# Purpose: Created a sun flower
# Google Doc Link: https://docs.google.com/document/d/1gRRxdAQvTMhQ6pwa0BwnBMu09rZ2cglwKLnd5j2zvpg/edit?usp=sharing
#################################################################################
# Acknowledgements:
# https://stackoverflow.com/questions/32804572/how-to-hide-a-turtle-icon-pointer-in-python
#
#################################################################################

import turtle
sunflower = turtle.Turtle()
sunflower.speed(0)
s=turtle.Screen()
s.bgcolor('light green')

def main():
        """
        Create the center bulb to our flower!
        """
flowercenter = turtle.Turtle()
flowercenter.hideturtle()
flowercenter.speed(0)
flowercenter.goto(-5,-65)
flowercenter.color("#503D02")
flowercenter.begin_fill()
flowercenter.circle(50)  # draws a circle of radius 20
flowercenter.end_fill()

def petals():
    """
    Creates the petals to our sunflower!
    """
sunflower.penup()
sunflower.goto(0,20)
sunflower.pendown()
for i in range(17):
        sunflower.color('gold')
        sunflower.begin_fill()
        sunflower.circle(190, 90)
        sunflower.left(98)
        sunflower.end_fill()
        sunflower.color("yellow")
        sunflower.begin_fill()
        sunflower.circle(190, 90)
        sunflower.left(18)
        sunflower.end_fill()

def make_text():
    """
    Writes text about fav flower on the screen.
    """
sunflower.penup()
sunflower.goto(0,-200)
sunflower.pendown()
sunflower.color("#086054")
sunflower.write("Sunflowers are my favourite!",move=False,align='center',font=("Arial",30,("bold","normal")))

main()  # Starts the program!
s.exitonclick()


