######################################################################
# Author: Lydia Bodine
# Username: bodinel
# Assignment: A03 - Fully Functional Gitty Pyschedelic Robotic Turtles
# Google Doc: https://docs.google.com/document/d/1nO1j0PSvngdlDDSlSutAlc7grp_5dXbqYevRSSM-StI/edit#
# Purpose: To create something complex, like a house, animal or person.
# https://docs.python.org/3.0/library/turtle.html#turtle.pencolor helped me figure out how to incorporate r,g,b
######################################################################
import turtle

wn = turtle.Screen()
wn.bgcolor("light blue")
wn.title("Welcome Home!")


def log_cabin(): # making the structure of the log cabin
        """
        Docstring for function_1
        """
log = turtle.Turtle()
log.pencolor("brown")
tup = (0.2, 0.8, 0.55)
log.pencolor(tup)
log.pencolor()

log.pensize(20)
log.speed(20)

log.penup()
log.setx(100)
log.sety(-175)
log.pendown()

for i in range(8): # this is building the structure
    log.forward(-250)
    log.left(90)
    log.forward(25)
    log.left(-90)
    log.forward(250)

log.right(90)
log.forward(200)



def front_door(): # making the door to the cabin
    """function 2"""

door = turtle.Turtle()
door.color("black")
door.pensize(10)
door.penup()
door.setx(110)
door.sety(-80)
door.pendown()

door.color("black")
door.begin_fill()
for i in range(2):
    door.right(90)
    door.forward(100)
    door.right(90)
    door.forward(40)
door.end_fill()



def roof_top(): # Building the roof
    """Function 3"""
roof = turtle.Turtle()
roof.color("purple")
roof.pensize(20)
roof.penup()
roof.setx(90)
roof.sety(50)
roof.pendown()
roof.begin_fill()

for i in range(3):
    roof.backward(250)
    roof.left(-120)
roof.end_fill()


def main():
    """
    Docstring for main
    """
    log_cabin()
    front_door()
    roof_top()



wn.exitonclick()
