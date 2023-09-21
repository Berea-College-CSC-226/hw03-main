

#################################################################################
# Author:Claudia Pulido
# Username: pulidoc
#
# Assignment:Hw3
# Purpose: Draw a house and 2 flowers.
# Google Doc Link:
# https://docs.google.com/document/d/1AogX32QRhDn63KLXeTTo4sUARmfhCANY6IuMRZVQCpo/edit
#################################################################################
# Acknowledgements: Dr. Scott Heggen.
#
#
#################################################################################

import turtle


def create_roof(circle):
    """
    making the roof
    """
    circle.penup()
    circle.setpos(-50, 100)
    circle.pendown()
    circle.begin_fill()
    for i in range(3):             # loop for the roof
        circle.forward(160)
        circle.left(120)
    circle.end_fill()
    circle.stamp()

    # ....


def create_house(bunny):
    """
    making the actual house
    """
    bunny.penup()
    bunny.setpos(-50, 100)
    bunny.forward(5)
    bunny.pendown()
    bunny.begin_fill()
    for i in range(2):                   # loop to make the house
        bunny.forward(150)
        bunny.right(-270)
        bunny.forward(150)
        bunny.right(-270)
    bunny.end_fill()
    bunny.stamp()
    # ...


def create_window(dolphin):
    """
    making the first window
    """
    dolphin.penup()
    dolphin.setpos(-15, 50)
    dolphin.color("#D04D70")
    dolphin.begin_fill()
    for side in range(2):                    # loop to make the window
        dolphin.forward(30)
        dolphin.right(90)
        dolphin.forward(20)
        dolphin.right(90)
    dolphin.end_fill()


def create_windows(oso):
    """
    making the second window
    """
    oso.penup()
    oso.setpos(40, 50)
    oso.color("#D04D70")
    oso.begin_fill()
    for side in range(2):
        oso.forward(30)
        oso.right(90)
        oso.forward(20)
        oso.right(90)
    oso.end_fill()


def make_door(tiger):
    """
    making the door
    """
    tiger.penup()
    tiger.setpos(15,0)
    tiger.pendown()
    tiger.color("#9E0419")
    tiger.begin_fill()
    for side in range(2):                       # loop for the door
        tiger.forward(20)
        tiger.right(90)
        tiger.forward(50)
        tiger.right(90)
    tiger.end_fill()


def make_flower(flower):
    """
    Drawing the first flower
    """
    flower.shape("circle")
    flower.color("#67AC2B")
    flower.pensize(16)
    flower.penup()
    flower.setpos(-200, 50)
    for i in range(6):           # loop for my flower
        flower.pendown()
        flower.forward(80)
        flower.right(40)
        flower.forward(80)
        flower.right(110)
        flower.forward(80)
        flower.right(40)
        flower.forward(80)
        flower.right(110)


def make_other(petals):
    """
    Drawing the second flower
    """
    petals.shape("circle")
    petals.color("#67AC2B")
    petals.pensize(16)
    petals.penup()
    petals.setpos(130, 50)
    for i in range(6):           # loop for my second flower
        petals.pendown()
        petals.forward(80)
        petals.right(40)
        petals.forward(80)
        petals.right(110)
        petals.forward(80)
        petals.right(40)
        petals.forward(80)
        petals.right(110)


def main():
    """
    Draws a house and some flowers.
    :return:none
    """
    turtle.colormode(255)
    wn = turtle.Screen()  # Makes a new turtle screen
    wn.bgcolor("black")  # Sets background to an image
    circle = turtle.Turtle()
    circle.speed(1)
    circle.color("purple")

    bunny = turtle.Turtle()     # second turtle
    bunny.speed(1)
    bunny.color("blue")

    dolphin = turtle.Turtle()      # third turtle
    dolphin.speed(1)
    dolphin.color("#D04D70")

    oso = turtle.Turtle()            # fourth turtle
    turtle.speed(1)
    turtle.color("#D04D70")

    tiger = turtle.Turtle()            # fifth turtle
    tiger.speed(1)
    tiger.color("#9E0419")

    flower = turtle.Turtle()         # sixth turtle
    flower.speed(1)
    flower.color("#67AC2B")

    petals = turtle.Turtle()         # seventh turtle
    petals.speed(1)
    petals.color("#67AC2B")

    create_roof(circle)      # Function call to function_1
    create_house(bunny)  # Function call to function_2
    create_window(dolphin)  # Function to call to function_3
    create_windows(oso)     # function to call
    make_door(tiger)        # function to call
    make_flower(flower)     # function to call
    make_other(petals)      # function to call

    wn.exitonclick()


main()
