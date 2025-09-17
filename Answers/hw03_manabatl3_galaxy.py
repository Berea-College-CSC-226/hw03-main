#################################################################################
# Author: Lindsay Manabat
# Username: manabatl3
#
# Assignment: HW03 Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Creating a drawing that uses the Turtle and different functions
# Google Doc Link: https://docs.google.com/document/d/10XcYavKaIG4UW2GclXvAIx7bxvm5gf_umBmn10wX8CQ/edit?usp=sharing

#
#################################################################################
# Acknowledgements:
# Galaxy Picture Gif : https://news.cgtn.com/news/2024-08-28/Stunning-starry-sky-above-central-China-s-Xihuang-Mountain-1wqPWOZmCfC/p.html
#
#################################################################################


import turtle


def main():
    wn = turtle.Screen()  # Makes a new turtle screen
    wn.bgpic("GalaxyBG.gif")  # Sets background to a gif

    wn.exitonclick()


def draw_star(size):
    for _ in range(5):
        star = turtle.Turtle()
        turtle.pendown()
        turtle.forward(size)
        turtle.right(144)


main()


