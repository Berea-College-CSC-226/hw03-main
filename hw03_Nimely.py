#################################################################################
# Author: flower stem
# Username:stem
#
# Assignment:Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose:
# Google Doc Link:https://docs.google.com/document/d/1e2HxfEvyB-SdWBs9_G7ZBRoc6QCUzZAmlhiQFXjMTxE/edit

#################################################################################
# Acknowledgements:
#
#
#################################################################################


import turtle

#define function to draw background
def  draw_background(screen: turtle.TurtleScreen ):
    screen.colormode(255)
    screen.bgcolor(127,103,103)


def draw_house(house: turtle.Turtle):
    house.penup()
    house.pensize(4)
    house.goto(-50,-50) #move turtle to a starting position
    house.pendown()


    house.color(136, 166, 99)
    house.begin_fill()
    for i in range(4):
        house.forward(100)
        house.left(90)
        house.end_fill()

    # Draw the roof on top of  the house
    house.penup()
    house.pensize(5)
    house.goto(-50,45)
    house.pendown()
    house.color(27, 14, 14)
    house.begin_fill()
    house.left(45)
    house.forward(70)
    house.right(90)
    house.forward(70)
    house.left(135)
    house.forward(100)

def draw_flower(flower:turtle.Turtle, stem: turtle.Turtle):
    """Draws a flower on the side of the house."""

    flower.color(27, 27, 14)
    flower.speed(25)
    flower.pensize(3)
    stem.color(16,27,14)
    stem.speed(15)
    stem.pensize(10)

    # Draw flower petals
    flower.penup()
    flower.goto(-150, -50)  # Adjusted position to the side of the house
    flower.pendown()
    for _ in range(50):
        flower.circle(50, 60)
        flower.left(120)
        flower.circle(50, 60)
        flower.left(160)
        flower.right(50)

    # Draw the stem
    stem.penup()
    stem.goto(-150, -100)  # Adjusted position for the stem
    stem.pendown()
    stem.right(90)
    stem.forward(100)

def main():
    wn = turtle.Turtle()
    screen = wn.screen
    turtle.speed('fastest')
    draw_background(screen)

    house = turtle.Turtle()
    draw_house(house)

    flower = turtle.Turtle()
    stem = turtle.Turtle()
    draw_flower(flower, stem)


main()





