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


def flowercenter(sunflower):
    """
    Create the center bulb to our flower!
    """
    sunflower.hideturtle()
    sunflower.speed(0)
    sunflower.goto(-15, -65)
    sunflower.color("#503D02")
    sunflower.begin_fill()
    sunflower.circle(50)  # draws a circle of radius 20
    sunflower.end_fill()


def petals(sunflower):
    """
    Creates the petals to our sunflower!
    """
    sunflower.penup()
    sunflower.goto(0, 20)
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


def make_text(sunflower):
    """
    Writes text about fav flower on the screen.
    """
    sunflower.penup()
    sunflower.goto(0, -200)
    sunflower.pendown()
    sunflower.color("#086054")
    sunflower.write("Sunflowers are my favourite!", move=False, align='center', font=("Arial", 30, ("bold", "normal")))


def main():
    """
    Let's create a sunflower using python turtle features!
    """
    sunflower = turtle.Turtle()
    sunflower.speed(0)
    s = turtle.Screen()
    s.bgcolor('light green')

    petals(sunflower)
    flowercenter(sunflower)
    make_text(sunflower)

    s.exitonclick()


main()  # Starts the program!