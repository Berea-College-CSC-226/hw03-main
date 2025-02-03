######################################################################
# Author: Abdou Diop             TODO: Change this to your name, if modifying
# Username: diopa                      TODO: Change this to your username, if modifying
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

def main():
    """
    draw a colorful flower using turtles
    """
    turtle.colormode(255)

    flower_origin = (0,-250) # where the stem of the flower will start from, upwards
    flower_stem_height = 250 # how tall the flower stem is
    flower_stem_size = 8 # how wide the stem is
    flower_pistil_size = 75 # size of the middle of the flower
    flower_petals = 16 # how many petals the flower will have
    flower_petal_length = 40 # how long each petal is

    screen = turtle.Screen()
    screen.setup(500,500)
    screen.bgcolor(110,209,252)

    stem = turtle.Turtle()
    stem.color(48, 185, 107)
    stem.pensize(flower_stem_size)

    stem.up()
    stem.goto(flower_origin)
    stem.left(90)
    stem.forward(flower_stem_height)
    stem.down()
    stem.right(180)
    stem.forward(flower_stem_height)
    stem.turtlesize(flower_stem_size/2)

    pistil =turtle.Turtle()

    pistil.goto(flower_origin[0], flower_origin[1] + flower_stem_height)
    # the pistil will be visible later on

    for i in range(flower_petals):
        petal = turtle.Turtle()
        petal.color(rand.randrange(100,255),rand.randrange(100,255),rand.randrange(100,255))
        petal.pensize(int(360/flower_petals))
        petal.speed(0)

        petal.up()
        petal.goto(flower_origin[0], flower_origin[1] + flower_stem_height)
        petal.left(90)
        petal.right(i*(360/flower_petals)) # turn petal facing outwards
        petal.forward(flower_pistil_size/2)
        petal.down()
        petal.forward(flower_petal_length)

    pistil.dot(flower_pistil_size) # put the pistil on top of the petals

    screen.exitonclick()

main()