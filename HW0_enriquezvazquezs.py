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
# Acknowledgements:OpenAI's ChatGPT. (2025). Example of Python code to draw a flower with five petals using turtle.
# Retrieved from: https://chat.openai.com
# Example given:
#import turtle

# Set up the turtle screen
#screen = turtle.Screen()
#screen.bgcolor("white")

# Create the turtle object
#flower = turtle.Turtle()
#flower.shape("turtle")
#flower.speed(10)  # Fast drawing speed

# Function to draw a single petal
#def draw_petal():
#   flower.color("red")
#   flower.circle(100, 60)  # Draw a circle with 100 radius and 60 degrees arc
#   flower.left(120)  # Turn the turtle to the left by 120 degrees
#   flower.circle(100, 60)
#   flower.left(120)

# Draw five petals
#for _ in range(5):
#    draw_petal()
#    flower.left(72)  # Turn the turtle to make space for the next petal

# Hide the turtle after drawing
#flower.hideturtle()

# Keep the window open until it is closed by the user
#turtle.done()

# *I couldn't figure out how to get the exact link to the page*
#
#################################################################################

import turtle

def draw_grass(g):
    """
    draws grass
    :param g: a turtle object
    """
    g.penup()
    g.setposition(-318, -220)
    g.pendown()
    g.begin_fill()
    for grass in range(2):
        g.forward(630)
        g.right(90)
        g.forward(150)
        g.right(90)
    g.end_fill()

#run circle in the middle of the flower and then draw flower stem with another petal
def draw_circle(c):
    """
    draws a circle and stem
    :param c: a turtle object
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
    """
    draws flower petals
    """
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
