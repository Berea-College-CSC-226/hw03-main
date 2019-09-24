
#################################################################################
# Author:bertrina iransi
# Username:iransib
#
# Assignment:
# Purpose:makes a picture of a house
# Google Doc Link:https://docs.google.com/document/d/1csqfSeKFdvdwuUWO0RpT5v3up4grXiecCx_WBqux4jg/edit#
#
#################################################################################


import turtle



def buildHouse(turtle):
   turtle.color("black", "brown")
   turtle.begin_fill()
   for i in range(4):
    turtle.forward(160)
    turtle.left(90)
    turtle.left(180)
   turtle.end_fill()
def buildRoof(turtle):
    """
        makes the roof

     """
    turtle.color("black", "red")
    turtle.begin_fill()
    turtle.left(45)
    turtle.forward(113)
    turtle.left(-90)
    turtle.forward(115)
    turtle.end_fill()
def buildChimney(turtle):
    """
     makes the chimney
     """
    turtle.color("grey")
    turtle.penup()
    turtle.right(135)
    turtle.forward(45)
    turtle.right(90)
    turtle.forward(45)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(60)
    turtle.end_fill()

def buildWindows(turtle):
    """
     make the windows
     """
    turtle.color("blue")
    turtle.penup()
    turtle.forward(90)
    turtle.right(90)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(4):
         turtle.forward(30)
         turtle.right(90)
    turtle.penup()
    turtle.forward(90)
    turtle.end_fill()
    turtle.pendown()
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(30)
        turtle.right(90)
    turtle.end_fill()


def makeSun(turtle):
    """
     makes the sun
     """
    turtle.penup()
    turtle.color('yellow')

    turtle.goto(-80, 80)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(36):
        turtle.forward(160)
        turtle.left(190)
    turtle.end_fill()
    turtle.penup()
def grass(turtle):
    """
     makes some grass
     """
    turtle.color("#86eb34")
    turtle.goto(0, -160)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(650)

    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(1000)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(350)
    turtle.end_fill()
def makeTree(turtle):
    """
    makes a tree
     """
    turtle.penup()
    turtle.forward(30)
    turtle.pendown()
    turtle.color('#402929')
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(20)
        turtle.right(90)
        turtle.forward(70)
        turtle.right(90)
    turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(-13, -60)
    turtle.pendown()
    turtle.color("#2e631d")
    turtle.begin_fill()
    for i in range(6):
        turtle.right(10)
        turtle.circle(30, 80)
    turtle.end_fill()


def main():
    turtle.speed(0)
    win = turtle.Screen()
    win.bgcolor("light blue")

    buildHouse(turtle)

    buildRoof(turtle)

    buildChimney(turtle)

    buildWindows(turtle)

    makeSun(turtle)

    grass(turtle)
    makeTree(turtle)
    win.exitonclick()
main()