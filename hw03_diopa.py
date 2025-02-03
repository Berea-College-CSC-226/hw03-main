######################################################################
# Author: Abdou Diop
# Username: diopa
#
# Assignment: HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Draw a colorful flower using turtle and random colors
######################################################################
# Acknowledgements:

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
#################################################################################

import turtle
import random as rand

def flower_stem(pos,height,thickness,color):
    stem = turtle.Turtle()
    stem.color(color)
    stem.pensize(thickness)

    stem.up()
    stem.goto(pos)
    stem.left(90)
    stem.forward(height)
    stem.down()
    stem.right(180)
    stem.forward(height)
    stem.turtlesize(thickness / 2)

def flower_bud(pos,pistil_size,petals,petal_length):
    pistil = turtle.Turtle()

    pistil.goto(pos)
    # the pistil will be visible later on

    for i in range(petals):
        petal = turtle.Turtle()
        petal.color(rand.randrange(100, 255), rand.randrange(100, 255), rand.randrange(100, 255))
        petal.pensize(int(360 / petals))
        petal.speed(0)

        petal.up()
        petal.goto(pos)
        petal.left(90)
        petal.right(i * (360 / petals))  # turn petal facing outwards
        petal.forward(pistil_size / 2)
        petal.down()
        petal.forward(petal_length)

    pistil.dot(pistil_size)  # put the pistil on top of the petals

def main():
    """
    draw a colorful flower using turtles
    """
    turtle.colormode(255)

    flower_origin = (0,-250) # where the stem of the flower will start from, upwards
    flower_stem_height = 250 # how tall the flower stem is
    flower_stem_thickness = 8 # how wide the stem is
    flower_pistil_size = 75 # size of the middle of the flower
    flower_petals = 16 # how many petals the flower will have
    flower_petal_length = 40 # how long each petal is

    screen = turtle.Screen()
    screen.setup(500,500)
    screen.bgcolor(110,209,252)

    flower_stem(flower_origin,flower_stem_height,flower_stem_thickness,(48, 185, 107))

    flower_bud((flower_origin[0],flower_origin[1] + flower_stem_height),flower_pistil_size,flower_petals,flower_petal_length)

    screen.exitonclick()

main()