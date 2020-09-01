#################################################################################
# Author: Caleb Handley
# Username: handleyc
#
# Assignment: A03-Fully-Functional-Gitty-Psychodelic-Robotic-Turtles
# Purpose: Continue practicing creating and using functions
#          More practice on using the turtle library
#          Learn about how computers represent colors
#          Learn about source control and git
#################################################################################
# Acknowledgements:
#
#################################################################################

import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("My House!")

speedy = turtle.Turtle()
speedy.color("darkblue")
speedy.pensize(25)

speedy.penup()
speedy.setx(125)
speedy.sety(-125)
speedy.pendown()


def large_square():
    """
    This function is having the turtle make the square for the house
    """
    for i in range(4):
        speedy.forward(-250)
        speedy.left(-90)


speedy.fillcolor("darkblue")
speedy.begin_fill()

large_square()

speedy.end_fill()

speedy.hideturtle()

# Making the Roof
henry = turtle.Turtle()
henry.color("darkgreen")
henry.pensize(25)

henry.penup()
henry.setx(200)
henry.sety(125)
henry.pendown()

henry.fillcolor("darkgreen")
henry.begin_fill()


def green_roof():
    henry.forward(-400)
    henry.left(20)
    henry.forward(215)
    henry.left(-40)
    henry.forward(215)


henry.end_fill()

henry.hideturtle()

# Making the Door
leonard = turtle.Turtle()
leonard.color("purple")
leonard.pensize(25)

leonard.penup()
leonard.setx(50)
leonard.sety(25)
leonard.pendown()

leonard.fillcolor("purple")
leonard.begin_fill()


def building_a_door():
    for side in range(2):
        leonard.forward(60)
        leonard.right(90)
        leonard.forward(150)
        leonard.right(90)


leonard.end_fill()

leonard.hideturtle()

# Making the Door knob
bob = turtle.Turtle()
bob.color("#C3003C")
bob.pensize(10)

bob.penup()
bob.setx(100)
bob.sety(-70)
bob.pendown()

bob.fillcolor("#C3003C")
bob.begin_fill()


def making_door_knob():
    bob.circle(5, 1)


bob.end_fill()

bob.hideturtle()

# Making Windows
george = turtle.Turtle()
george.color("lightblue")

george.penup()
george.setx(-115)
george.pendown()

george.fillcolor("lightblue")
george.begin_fill()


def making_windows():
    for side in range(2):
        george.forward(60)
        george.right(90)
        george.forward(40)
        george.right(90)


george.end_fill()

george.hideturtle()


def main():
    """
    Uses all the functions to build/create a house
    :return: None
    """

    large_square()
    green_roof()
    building_a_door()
    making_door_knob()
    making_windows()


wn.exitonclick()
