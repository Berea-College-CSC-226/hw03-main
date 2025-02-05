#################################################################################
# Author: Iuliia Likhacheva
# Username: likhachevai
#
# Assignment: HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Continue practicing creating and using functions
# Google Doc Link: https://docs.google.com/document/d/15qyuQtdjdngzL3tsy7WfdTvD6DsEjUjCGyTBroGVKq4/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle
import random

def spaceship():
    ship = turtle.Turtle()
    ship.speed(0)
    ship.pensize(3)
    ship.penup()

    # Draw main body
    ship.color('#9c9e91')
    ship.goto(0, -180)
    ship.begin_fill()
    ship.pendown()
    for i in range(2):
        ship.circle(100, 90)
        ship.circle(40, 90)
    ship.end_fill()
    ship.penup()

    # Draw window
    ship.color('#99c2c8')
    ship.goto(60, -90)
    ship.begin_fill()
    ship.circle(20)
    ship.end_fill()

    # Draw left fin
    ship.color('#7a7d73')
    ship.goto(-60, -180)
    ship.begin_fill()
    ship.pendown()
    ship.goto(-120, -220)
    ship.goto(-60, -200)
    ship.goto(-60, -180)
    ship.end_fill()
    ship.penup()

    # Draw right fin
    ship.goto(60, -180)
    ship.begin_fill()
    ship.pendown()
    ship.goto(120, -220)
    ship.goto(60, -200)
    ship.goto(60, -180)
    ship.end_fill()
    ship.penup()

    # Draw base
    ship.color('#4d4d4d')
    ship.goto(-30, -180)
    ship.begin_fill()
    ship.pendown()
    ship.goto(-50, -230)
    ship.goto(50, -230)
    ship.goto(30, -180)
    ship.goto(-30, -180)
    ship.end_fill()
    ship.penup()

    # Draw flames
    ship.color('#ff6600')
    ship.goto(-20, -230)
    ship.begin_fill()
    ship.pendown()
    ship.goto(0, -270)
    ship.goto(20, -230)
    ship.goto(-20, -230)
    ship.end_fill()
    ship.penup()

    ship.hideturtle()



def sun():
    s = turtle.Turtle()
    s.speed(0)
    s.penup()
    s.goto(-250, 20)
    s.pendown()
    s.color("#FFA501")  # Orange color
    s.begin_fill()
    s.circle(100)  # Sun size
    s.end_fill()
    s.hideturtle()

def ray():
    r = turtle.Turtle()
    r.speed(0)
    r.pensize(6)
    r.color("#FF4505")  # Bright orange
    r.penup()
    r.goto(-250, 120)


    for i in range(36): # 36 sun rays
        r.penup()
        r.forward(120)
        r.pendown()
        r.forward(20)
        r.penup()
        r.forward(-140)
        r.right(10)
    r.penup()
    r.hideturtle()


def stars():
    st = turtle.Turtle()
    st.speed(0)
    st.pensize(20)
    st.color("white")

    for i in range(50):  # 50 stars
        x = random.randint(-800, 500)
        y = random.randint(-300, 700)
        st.penup()
        st.goto(x, y)
        st.dot(random.randint(1, 8))
    st.hideturtle()


def saturn():
    turtle.colormode(255)
    sat = turtle.Turtle()
    sat.speed(0)
    sat.goto(250, -182)
    sat.pendown()
    sat.fillcolor((215, 185, 110))
    sat.begin_fill()
    sat.circle(60)  # Planet size
    sat.end_fill()
    sat.penup()
    sat.hideturtle()


def rings():
    turtle.colormode(255)
    rin = turtle.Turtle()
    rin.speed(0)
    rin.color((220, 220, 201))
    rin.pensize(3)
    rin.penup()
    rin.goto(250, -220)
    rin.pendown()
    rin.circle(100)
    rin.penup()
    rin.goto(250,-215)
    rin.pendown()
    rin.color((240, 240, 40))
    rin.circle(95)
    rin.penup()
    rin.hideturtle()

def main():
    screen = turtle.Screen()
    screen.setup(800, 600)  # Set window size
    screen.bgpic("background_2.png")  # Load background image
    spaceship()
    sun()
    ray()
    saturn()
    rings()
    stars()
    screen.exitonclick()


main()