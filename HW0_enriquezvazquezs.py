#################################################################################
# Author: Sandy Enriquez Vazquez
# Username: enriquezvazquezs
#
# Assignment:HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Draw something complex
# Google Doc Link: https://docs.google.com/document/d/16tdyTo7Va4O3NHu80p5LXP_pasdFz-eTVAOKTULSqdg/edit?tab=t.0#heading=
# h.j4414z2ufr72
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle

def draw_grass(g):
    """
    draws grass
    :param g:
    """

#run
def draw_circle(c):
    """
    draws a circle and stem
    :param c:
    """
    c.penup()
    c.setposition(100,35)
    c.pendown()
    c.begin_fill()
    c.circle(25)
    c.fillcolor("yellow")
    c.end_fill()
    c.right(90)
    c.penup()
    c.forward(45)
    c.pendown()
    c.color("light green")
    c.pensize(8)
    c.forward(300)
    c.backward(250)
    c.begin_fill()
    c.circle(80, 80)
    c.left(120)
    c.forward(35)
    c.circle(40, 40)
    c.left(120)
    c.end_fill()



#run flower petals
def main():
    wn = turtle.Screen()
    wn.bgcolor("lightblue")
    petal = turtle.Turtle()
    c = turtle.Turtle()
    c.color("yellow")
    g = turtle.Turtle()
    g.color("green")
    wn.colormode(255)
    petal.color(210, 140, 232)
    petal.fillcolor(210, 140, 232)
    petal.speed(0)
    for flower_petals in range(9):
        petal.begin_fill()
        petal.circle(180,80)
        petal.left(120)
        petal.end_fill()
    draw_circle(c)
    draw_grass(g)





    wn.exitonclick()

main()