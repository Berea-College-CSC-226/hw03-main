
#Author: Tristan Razote
# Username:razotet
#
# Assignment:HW03-Fully Functional Gitty Psychedelic Robotic Turtles

# Purpose:
#Continue practicing creating and using functions.
#More practice on using the turtle library.
#Learn about how computers represent colors.
#Learn about source control and Git.

# Google Doc Link:https://docs.google.com/document/d/1o3qQdqf5zXFRLx-ZWTtfvhRjhSI-q1dkjrt7Ms-U91M/edit?usp=sharing

#################################################################################
# Acknowledgements: Dr. Scott Heggen
#
#
#################################################################################
import turtle


def house(tur_house):
    """
    This uses a turtle to create the general shape of a house.
    """
    tur_house.speed(0)
    tur_house.pensize(10)
    tur_house.penup()
    tur_house.setpos(-100,-100)

    tur_house.penup()
    tur_house.color("Gray")
    tur_house.begin_fill()
    for i in range(2):
        tur_house.forward(200)
        tur_house.left(90)
        tur_house.forward(275)
        tur_house.left(90)
    tur_house.end_fill()
    tur_house.pendown()

    tur_house.color("Black")
    for i in range(2):
        tur_house.forward(200)
        tur_house.left(90)
        tur_house.forward(275)
        tur_house.left(90)



def roof(tur_roof):
    """
    This is used to create the nice roof of the house
    """
    tur_roof.speed(0)
    tur_roof.penup()
    tur_roof.speed(0)
    tur_roof.penup()
    tur_roof.setpos(-100, 175)
    tur_roof.pensize(10)
    tur_roof.pendown()
    tur_roof.color("#BC4A3C")
    tur_roof.begin_fill()
    for i in range(3):
        tur_roof.forward(200)
        tur_roof.left(120)
    tur_roof.end_fill()
    tur_roof.color("black")
    tur_roof.forward(200)




def window(tur_win):
    """
    This is used to add a window the house. This will add details to the house.
    """
    tur_win.speed(0)
    tur_win.color("white")
    tur_win.penup()
    tur_win.setpos(-80,0)
    tur_win.pendown()
    tur_win.begin_fill()
    for i in range (4):
        tur_win.forward(50)
        tur_win.left(90)
    tur_win.end_fill()
    tur_win.color("black")
    tur_win.penup()
    tur_win.forward(25)
    tur_win.pendown()
    tur_win.left(90)
    tur_win.forward(25)
    for i in range(4):
        tur_win.forward(25)
        tur_win.back(25)
        tur_win.left(90)
    tur_win.penup()
    tur_win.back(25)
    tur_win.right(90)
    tur_win.back(25)
    tur_win.pendown()


    tur_win.color("white")
    tur_win.penup()
    tur_win.forward(100)
    tur_win.pendown()
    tur_win.begin_fill()
    for i in range (4):
        tur_win.forward(50)
        tur_win.left(90)
    tur_win.end_fill()
    tur_win.color("black")
    tur_win.penup()
    tur_win.forward(25)
    tur_win.pendown()
    tur_win.left(90)
    tur_win.forward(25)
    for i in range(4):
        tur_win.forward(25)
        tur_win.back(25)
        tur_win.left(90)
    tur_win.penup()
    tur_win.back(25)
    tur_win.right(90)
    tur_win.back(25)
    tur_win.pendown()



def main():
    """
    Docstring for main
    """
    wn = turtle.Screen()
    wn.bgcolor("#7CFC00")

    tur_house = turtle.Turtle()
    tur_roof = turtle.Turtle()
    tur_win = turtle.Turtle()





    house(tur_house)            # Function call to function_1
    roof(tur_roof)            # Function call to function_2
    window(tur_win)


    wn.exitonclick()

main()