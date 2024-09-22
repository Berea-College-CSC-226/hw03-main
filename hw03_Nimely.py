#################################################################################
# Author: Joyce Nimely
# Username: Nimely
#
# Assignment:Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose:
# Google Doc Link:https://docs.google.com/document/d/1e2HxfEvyB-SdWBs9_G7ZBRoc6QCUzZAmlhiQFXjMTxE/edit

#################################################################################
# Acknowledgements:
#Cemah Turboh: Helped with showing me how to use parameters.
#
#################################################################################


import turtle

#define function to draw background
def  draw_background(screen: turtle.TurtleScreen ):
    """Set up the background for the screen"""
    screen.colormode(255)
    screen.bgcolor(127,103,103)

def draw_house(house: turtle.Turtle):
    """Draw a square house with a roof."""
    house.penup()
    house.pensize(4)
    house.goto(-50,-50) #move turtle to a starting position
    house.pendown()

    house.color(136, 166, 99)
    house.begin_fill()
    for i in range(4):
        house.forward(100)
        house.right(90)
        house.end_fill()

    # Draw the roof on top of  the house
    house.left(45)
    house.forward(70)
    house.right(90)
    house.forward(70)
    house.left(90+45)
    house.forward(70)

def draw_flower(flower:turtle.Turtle, stem: turtle.Turtle):
    """ Draw a flower with petal and stem."""
    flower.color(239, 255, 0)
    flower.speed(20)
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
        flower.right(90)
        flower.pendown()

    # Draw the stem
    stem.penup()
    stem.goto(-150, -100)  # Adjusted position for the stem
    stem.pendown()
    stem.right(90)
    stem.forward(100)

def main():
    """Set up the screen and draw the house and flower."""
    house = turtle.Turtle()
    screen = turtle.Screen()
    turtle.speed('fast')
    draw_background(screen)

    draw_house(house)

    flower = turtle.Turtle()
    stem = turtle.Turtle()
    draw_flower(flower, stem)

    screen.exitonclick()


main()







