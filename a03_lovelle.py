#################################################################################
# Author: Emily Lovell
# Username: lovelle
#
# Assignment: A03: A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Draw some fun things using turtle and also learn about git!
#################################################################################

import turtle


def draw_ball(t, clr):
    """
    Draws a ball given turtle t, size sz, and color clr.
    :param t: Turtle used to draw the ball.
    :param clr: Color of the ball.
    :return:
    """
    t.fillcolor(clr)
    t.shape("circle")
    t.goto(100, -150)
    t.stamp()


def draw_sun(t, sz, clr):
    """
    Draws a sun given turtle t, size sz, and color clr.

    :param t: Turtle used to draw the sun.
    :param sz: Size (diameter) of the sun.
    :param clr: Color of the sun.
    :return:
    """

    t.fillcolor(clr)
    t.goto(-200, 75)
    t.pendown()
    t.begin_fill()
    for i in range(360):
        t.left(1)
        t.fd(1)
    t.end_fill()
    t.penup()

def draw_caption(t, m):
    """
    Draws a caption using turtle t to present message m.

    :param t: Turtle to use to draw the message.
    :param m: Message to be displayed.
    :return:
    """
    t.goto(0, 200)
    t.pendown()
    t.color("#000000")
    t.write(m, move=False, align='center', font=("Arial", 30, ("italic", "normal")))
    t.penup()


def main():
    """
    Adds a sun and a ball to a beach scene featuring Lyra.

    :return: None
    """
    turtle.colormode(255)

    wn = turtle.Screen()
    wn.bgpic("Lyra.gif")

    doggo = turtle.Turtle()
    doggo.penup()
    doggo.hideturtle()

    ball_color = (50, 205, 50)
    draw_ball(doggo, ball_color)

    sun_size = 100
    sun_color = (255, 215, 0)
    draw_sun(doggo, sun_size, sun_color)

    message = "Lyra at the beach!"
    draw_caption(doggo, message)

    wn.exitonclick()


main()
