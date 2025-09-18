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
# Python Random Dictionary : https://docs.python.org/3/library/random.html#module-random
# Research on how to create Turtle constellations: https://holypython.com/python-turtle-tutorial/turtle-constellations/
#################################################################################

import turtle
import random


def setup_scene():
    wn = turtle.Screen()  # Makes a new turtle screen
    wn.bgpic("GalaxyBG.gif")  # Sets background to a gif
    wn.title("Night Sky")

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    return wn, t


def draw_star(t, x, y, size, color):
    t.penup()
    t.goto(x, y)
    t.pendown()

    t.color(color)
    t.begin_fill()
    for i in range(5):
            t.forward(size)
            t.right(144)
    t.end_fill()
# moon function
def draw_moon(t, x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()

    t.color('#F5F5DC')
    t.begin_fill()
    t.circle(size)
    t.end_fill()

#  using the random functions to create random stars all over the background
def draw_random_stars(t, num_stars, width, height):
    star_colors = ["#FFFFFF", "#FFFFAA", "#FFD700",
                   "#ADD8E6", "#FFC0CB", "#E6E6FA"]
    # creating random stars on the turtle screen
    for i in range(num_stars):
        rand_x = random.randint(-width // 2, width // 2)
        rand_y = random.randint(-height // 2, height //2)
        rand_size = random.randint(10, 25)
        rand_color = random.choice(star_colors)

        draw_star(t, rand_x, rand_y, rand_size, rand_color)

# A list of (x, y) coordinates for the stars we can use in the Big Dipper by random
BIG_DIPPER_CORDS = [
    (100, 100), (150, 120), (190, 110), (220, 80),
    (270, 70), (280, 120), (230, 130)
]

def draw_constellation(t, star_points):
    # First we draw all the stars for the constellation
    for point in star_points:
        # We make constellation stars smaller and white
        draw_star(t, point[0], point[1], 15, "white")

    # Second, connect the stars with faint lines
    t.penup()
    t.goto(star_points[0]) # Goes to the first star
    t.pendown()
    t.color("#FFFFFF",) # Sets line color to a faint white
    t.width(1)

    for point in star_points:
        t.goto(point)

def main():
    wn = turtle.Screen()
    wn.bgpic("GalaxyBG.gif")
    wn, artist = setup_scene()

    screen_width = wn.window_width()
    screen_height = wn.window_height()

# This function call draws 40 stars in random locations
    draw_random_stars(artist, 40, screen_width, screen_height)

# Draw a single moon in the top-left area of the screen
    draw_moon(artist, -200, 90, 70)

    draw_constellation(artist, BIG_DIPPER_CORDS)

    wn.exitonclick()

main()
