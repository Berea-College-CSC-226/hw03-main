#########################################################################################
# Author: Kristiana Nakaj
# Username: nakajk
# Assignment A03: Fully Functional Gitty Psychedelic Robotic Turtles (DE)
# Purpose: Continue using functions; More practice on turtle library; Colors; Source control and Git.
# Google Doc link: https://docs.google.com/document/d/1rADE_2iU1ZrSHtEymZ3lj9RiJ8Puzofms9Im9B578WY/edit?usp=sharing

########################################################################################

import turtle


def the_waves(r):
    """Drawing the waves of the sea"""
    r.right(90)
    r.speed(0)
    r.setposition(-700, -200)
    r.pendown()
    r.showturtle()
    for row in range(40):
        r.circle(20, -180)
        r.left(180)
    r.penup()
    r.setposition(-700, -240)
    r.pendown()
    for row in range(40):
        r.circle(20, -180)
        r.left(180)
    r.penup()


def the_base_of_the_boat(k):
    """Drawing the base of the boat"""
    k.setposition(-200, -150)
    k.showturtle()
    k.pendown()
    k.forward(350)
    k.left(45)
    k.forward(150)
    k.left(140)
    k.forward(480)
    k.left(100)
    k.forward(70)
    k.hideturtle()


def sail(i):
    """Drawing the sail of the boat"""
    i.setposition(-50, -70)
    i.showturtle()
    i.pendown()
    i.left(90)
    i.forward(350)
    i.left(180)
    i.forward(10)
    i.right(45)
    i.forward(40)
    i.left(95)
    i.forward(350)
    i.right(120)
    i.forward(260)
    i.hideturtle()


def sun(t):
    """Drawing a circle for the shape of the sun"""
    t.setposition(-160, 90)
    t.pendown()
    t.pensize(3)

    t.begin_fill()
    t.circle(60)
    t.end_fill()


def rays(sun_rays):
    """Draw the sun rays by repetition of the same lines 45 times"""
    sun_rays.pendown()
    for move in range(45):
        sun_rays.speed(35)
        sun_rays.forward(200)
        sun_rays.back(140)
        sun_rays.penup()
        sun_rays.right(8)
        sun_rays.back(60)
        sun_rays.pendown()


def bird(b):
    """Draw a small simple bird right under the sun"""
    b.pendown()
    for row in range(2):
        b.circle(15, -180)
        b.left(180)
    b.hideturtle()


def main():
    wn = turtle.Screen()
    wn.title("A03-A cute little boat")
    turtle.colormode(255)
    turtle.bgcolor(15, 60, 180)

    k = turtle.Turtle()  # the turtle used to draw the base of the boat
    k.hideturtle()
    k.shape("classic")
    k.penup()
    k.color((170, 60, 25), (139, 69, 19))
    k.pensize(4)

    r = turtle.Turtle()  # the turtle used to draw the waves
    r.hideturtle()
    r.penup()
    r.shape("classic")
    r.color("white")
    r.pensize(5)

    i = turtle.Turtle()  # the turtle used to draw the sail
    i.hideturtle()
    i.penup()
    i.shape("classic")
    i.pensize(3)
    i.color((170, 60, 25), (245, 222, 179))

    the_waves(r)

    k.begin_fill()
    the_base_of_the_boat(k)
    k.end_fill()

    i.begin_fill()
    sail(i)
    i.end_fill()

    a = turtle.Shape("compound")  # draw the small detail on the boat
    poly1 = ((-40, -50), (-40, -10), (-50, -10), (-50, -50))
    a.addcomponent(poly1, (170, 60, 25), (170, 70, 10))
    turtle.register_shape("detail", a)
    turtle.shape("detail")

    t = turtle.Turtle()  # turtle used to draw the sun shape
    t.hideturtle()
    t.penup()
    t.color((255, 255, 0), (255, 191, 0))

    sun(t)

    sun_rays = turtle.Turtle()  # turtle used to draw rays of the sun
    sun_rays.hideturtle()
    sun_rays.penup()
    sun_rays.pensize(2)
    sun_rays.color(255, 101, 0)
    sun_rays.setposition(-220, 150)

    rays(sun_rays)

    b = turtle.Turtle()  # turtle used to draw the little bird
    b.penup()
    b.hideturtle()
    b.color("black")
    b.pensize(3)
    b.setposition(-290, 80)
    b.speed(10)
    b.right(130)

    bird(b)

    wn.exitonclick()


main()
