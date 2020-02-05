
#################################################################################
# Author: Henry Camacho
# Username: Camachoh
#
# Assignment: A03
# Purpose: Draw a fish
# Google Doc Link: https://docs.google.com/document/d/1kbk_Az9m1RqgzW0h4crdURhLN8WtmHXcarHSI_897FU/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################


import turtle

# screen = turtle.Screen()


bg = turtle.Screen()
bg.bgcolor("blue")


def fish_drawing():
    fish = turtle.Turtle
    # fish.penup()
    # fish.forward(100)
    # fish.pendown()
    # fish.pencolor("yellow")
    # fish.shape("circle")
    # fish.shapesize(50,40,10)
    # fish.fillcolor("orange")
    fish.up()
    fish.goto(-140, -75)
    fish.down()
    fish.seth(-45)
    fish.color('yellow')
    fish.circle(200, 90)

    fish.cirlce(100, 90)
    fish.circle(-100, -90)
    fish.circle(-200, -90)


turtle.exitonclick()