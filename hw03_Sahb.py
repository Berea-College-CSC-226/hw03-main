
#################################################################################
# Author: Bhushan Sah
# Username: sahb
#
# Assignment:
# Purpose:
# Google Doc Link: https://docs.google.com/document/d/13LpqSuu0xWqY5J5O9_mMFV0U0kW8zII-87wZm04kL9c/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################


import turtle
def setup():
    """Set up screen and turtle."""
    screen = turtle.Screen()
    screen.setup(800, 500)
    screen.title("UFO Beam")
    screen.colormode(255)
    screen.bgcolor(15, 15, 40)  # non-white background (RGB)

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()
    return screen, t
def jumpTo(t,x,y):
    """This function will jump to another place without mark """
    t.penup()
    t.goto(x, y)
    t.pendown()
def box(t,x,y,w,h,color):
    """This function will draw a box around the circle"""
    jumpTo(t, x, y)
    t.setheading(0)
    t.fillcolor(color)
    t.begin_fill()
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
    t.end_fill()

def circle(t, x, y, r, color):
    """This function will draw the circle with radius r"""
    jumpTo(t, x, y-r)
    t.setheading(0)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

def drawUFO(t, x, y):
    """This will make a UFO from circle and box"""
    circle(t, x, y, 40, (180, 180, 200))
    box(t, x - 50, y - 10, 100, 20, (80, 80, 100))
    for z in [-20, 0, 20]:
        circle(t, x + z, y - 10, 5, (255, 255, 0))

def draw_stars(t):
    """A few stars."""
    t.pencolor(255, 255, 200)
    for (x, y) in [
        (-350, 220), (-300, 200), (-250, 230), (-200, 150), (-150, 210),
        (-100, 180), (-50, 220), (0, 200), (50, 230), (100, 160),
        (150, 180), (200, 220), (250, 190), (300, 140), (350, 210)]:
        jumpTo(t, x, y)
        t.dot(10)



def main():
    """
    Docstring for main. Should describe the main functionality of this file.
    """
    screen, t = setup()
    drawUFO(t,0,120)
    drawUFO(t, 120, 120)
    drawUFO(t, -50, -50)
    draw_stars(t)
    screen.exitonclick()



main()  # Starts the program!