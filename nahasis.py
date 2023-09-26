#################################################################################
# Author: Salaam Nahasi
# Username: Nahasis
#
# Assignment: HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose:
# Google Doc Link: https://docs.google.com/document/d/1DqO8WEZtaDIxztsUj6yHy_CPPnJbPVhyKno5Mi0vmyE/edit?usp=sharing

#################################################################################
# Acknowledgements:
#
#
#################################################################################
import turtle

def house(pen1):
    """
       This function creates the house
       Pen1 makes the main structure
       and the Pen2 makes the roof
     """
    pen1.speed(0)
 ##MR.BLUE SKY
    pen1.penup()
    pen1.goto(-400, -100)
    pen1.pendown()
    pen1.color("#0000FF")
    pen1.begin_fill()
    for i in range(2):
        pen1.forward(800)
        pen1.left(90)
        pen1.forward(500)
        pen1.left(90)
    pen1.end_fill()

# HERE COMES THE SUN
    pen1.penup()
    pen1.goto(-250, 225)
    pen1.pendown()
    pen1.color("#E3CF57")
    pen1.begin_fill()
    pen1.circle(35)
    pen1.end_fill()

    # ON TOP OF THE WORLD (Roof)
    pen1.penup()
    pen1.goto(-260, 70)
    pen1.pendown()
    pen1.color("#292421")  # (stroke, fill)
    pen1.begin_fill()
    for i in range(3):
        pen1.forward(225)
        pen1.left(120)
    pen1.end_fill()

# My House
    pen1.penup()
    pen1.goto(-220, -100)
    pen1.pendown()
    pen1.pensize(3)
    pen1.color("darkred")  # (stroke, fill)
    pen1.begin_fill()
    for i in range(4):
        pen1.forward(170)
        pen1.left(90)
    pen1.end_fill()

#I'VE GOT A FEELING, SOMEBODY'S WATCHIN' MEEEE (window 1)
    pen1.penup()
    pen1.goto(-200, 10)
    pen1.pendown()
    pen1.color("#8B0000", "pink")
    pen1.begin_fill()
    for i in range(4):
        pen1.forward(50)
        pen1.left(90)
    pen1.end_fill()
    pen1.penup()
    pen1.goto(-200, 30)
    pen1.down()
    pen1.color("black")
    pen1.forward(50)
    pen1.penup()
    pen1.goto(-170, 10)
    pen1.pendown()
    pen1.left(90)
    pen1.forward(50)

#I'VE GOT A FEELING, SOMEBODY'S WATCHIN' MEEEE (window 2)
    pen1.penup()
    pen1.goto(-120, 10)
    pen1.pendown()
    pen1.right(90)
    pen1.color("#8B0000", "pink")
    pen1.begin_fill()
    for i in range(4):
        pen1.forward(50)
        pen1.left(90)
    pen1.end_fill()
    pen1.penup()
    pen1.goto(-120, 30)
    pen1.pendown()
    pen1.color("#292421")
    pen1.forward(50)
    pen1.penup()
    pen1.goto(-95, 10)
    pen1.pendown()
    pen1.left(90)
    pen1.forward(50)

# I SEE YOUR RED DOOR AND I WANT IT PAINTED BLACK (door)
    pen1.penup()
    pen1.goto(-160, -100)
    pen1.pendown()
    pen1.right(90)
    pen1.color("#292421")
    pen1.begin_fill()
    for i in range(2):
        pen1.forward(50)
        pen1.left(90)
        pen1.forward(80)
        pen1.left(90)
    pen1.end_fill()

#I AM THE LORAX, I SPEAK FOR THE TREES (This is a tree)
    pen1.penup()
    pen1.color("#308014")
    pen1.goto(100, 0)
    pen1.pendown()
    pen1.begin_fill()
    for i in range(3):
        pen1.forward(150)
        pen1.left(120)
    pen1.end_fill()
    pen1.penup()
    pen1.goto(160, -95)
    pen1.pendown()
    pen1.begin_fill()
    pen1.color("#5E2612")
    for _ in range(2):
        pen1.forward(30)
        pen1.left(90)
        pen1.forward(90)
        pen1.left(90)
    pen1.end_fill()
def main():
    """
        Docstring for main
     """
    wn = turtle.Screen()
    turtle.Screen().setup(700, 700)
    wn.bgcolor("DarkGreen")

    pen1 = turtle.Turtle()
    # ...
    house(pen1)  # Function call to house
    wn.exitonclick()

main()