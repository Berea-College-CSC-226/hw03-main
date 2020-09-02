######################################################################
# Author: Emiliano Torres-Vera
# Username: torresverae
#
# Assignment: A03-A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Create a house
# Google Doc Link:
#####################################################################
import turtle

wn = turtle.Screen()
wn.bgcolor("lightblue")
wn.title("house")

emi = turtle.Turtle()
emi.color("black")
emi.shape("turtle")
emi.pensize(5)


def house():
    """build house
    : return: none
    """
    emi.penup()
    emi.setposition(-175, -180)  # places house in position needed
    emi.pendown()
    for i in range(2):  # creates house
        emi.forward(300)
        emi.left(90)
        emi.forward(200)
        emi.left(90)


emi.fillcolor("indigo") # colors house
emi.begin_fill()

house()

emi.end_fill()


# Build roof

def roof():
    emi.pendown()
    emi.setposition(-175, 25)
    emi.pendown()
    for i in range(3):
        emi.forward(300)
        emi.left(120)


emi.fillcolor("red")    # colors roof
emi.begin_fill()

roof()

emi.end_fill()


# build window

def window():
    """Builds window"""
    emi.penup()
    emi.setposition(-150, -100)
    emi.pendown()
    for i in range(4):
        emi.forward(50)
        emi.left(90)


emi.fillcolor("blue")   # colors window
emi.begin_fill()

window()

emi.end_fill()


# build window

def window_2():
    """Builds window 2"""
    emi.penup()
    emi.setposition(60, -100)
    emi.pendown()
    for i in range(4):
        emi.forward(50)
        emi.left(90)


emi.fillcolor("green")  # colors window 2
emi.begin_fill()

window_2()

emi.end_fill()


# build door

def door():
    """Builds Door"""
    emi.penup()
    emi.setposition(-50, -180)
    emi.pendown()
    for i in range(4):
        emi.forward(50)
        emi.left(90)
        emi.forward(100)
        emi.left(90)


emi.fillcolor("pink")   # colors door
emi.begin_fill()

door()

emi.end_fill()


# build sun

def sun():
    """Draws Sun"""
    emi.penup()
    emi.setposition(250, 150)
    emi.pendown()
    # circle for sun
    emi.circle(180)


emi.fillcolor("yellow")  # colors sun
emi.begin_fill()

sun()

emi.end_fill()


def main():
    """"All functions that are being used"""
    house()  # constructs house
    roof()  # constructs roof
    window()  # constructs window 1
    window_2()  # constructs window 2
    door()  # constructs door
    sun()  # draws sun


wn.exitonclick()

main()