######################################################################
# Author: Bekzodjon Rakhimov
# Username: rakhimovb
# Assignment: A03: A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
######################################################################

import turtle


def draw_rectangle(t, h, c):
    """
    This function draws a rectangle
    :param t: turtle name
    :param h: height of the rectangle
    :param c: turtle color
    :return:
    """
    for i in range(2):
        t.color(c)
        t.begin_fill()
        t.forward(h)
        t.left(90)
        t.forward(480)
        t.left(90)
        t.end_fill()


def draw_flag(t):
    """
    This function draws two third of the flag
    :param t: turtle name
    :return:
    """
    for i in ["#6fff01", "white"]:
        draw_rectangle(t, 80, i)
        t.fd(-15)
        draw_rectangle(t, 15, "red")
        t.fd(-80)


def moon(t):
    """
    This function draws a moon on the top left corner of the flag
    :param t: turtle name
    :return:
    """
    t.begin_fill()
    t.circle(20, 180)
    t.circle(20, -130)
    t.end_fill()


def change_pos(t, x, y):
    """
    This function changes the position of the turtle
    :param t: turtle name
    :param x: x coordinate
    :param y: y coordinate
    :return:
    """
    t.penup()
    t.setpos(x, y)
    t.pendown()


def star_line(t, n, y):
    """
    This function draws one line of stars in front of the moon
    :param t: turtle name
    :param n: number of stars on the line
    :param y: y coordinate to move the stars
    :return:
    """
    x = -115
    for b in range(n):
        t.begin_fill()
        for i in range(5):
            t.fd(10)
            t.right(144)
        change_pos(t, x, y)
        x = x - 15
        t.end_fill()


def draw_stars(t):
    """
    This function draws three lines of stars with different number of stars in each line
    :param t: turtle name
    :return:
    """
    y = 110
    n = 3
    for i in [95, 80, 65]:
        star_line(t, n, y)
        change_pos(t, -100, i)
        y = y - 15
        n = n + 1


def main():

    wn = turtle.Screen()
    wn.bgpic("samarkand-196923_1920.png")
    ttl1 = turtle.Turtle()

    change_pos(ttl1, -250, -50)          # Change position of the turtle to start drawing
    ttl1.setheading(-90)

    draw_flag(ttl1)                      # Draw the whole flag
    draw_rectangle(ttl1, 80, "#0abeff")

    ttl1.color("white")                  # Draw a moon in white on the top left corner of the flag
    ttl1.pensize(3)
    change_pos(ttl1, -200, 115)
    ttl1.right(80)
    moon(ttl1)

    change_pos(ttl1, -100, 110)          # Draw stars in front of the moon
    ttl1.pensize(1)
    ttl1.right(170)
    draw_stars(ttl1)

    change_pos(ttl1, -250, -210)         # Write "UZBEKISTAN" under the flag
    ttl1.color("#ff1100")
    ttl1.write("UZBEKISTAN", font=("Blackadder ITC", 45, "normal"))

    wn.exitonclick()


main()
