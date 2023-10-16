################################################################################################
# Assignment:HW03
# Purpose:
# Google Doc Link: https://docs.google.com/document/d/1SKEFGlECnO_k3vato51CFXwIfE1R-YFxNRainXu82Ug/edit


#################################################################################################

import turtle


def drawbase(sqdraw):
    """
    the following strings purpose is to create the base of the house
    """
    sqdraw.penup()
    sqdraw.goto(-100, -100)
    sqdraw.pendown()
    sqdraw.begin_fill()
    sqdraw.fillcolor(
        "pink")  # I was confused at first about how to execute this but after some practice it became easier
    sqdraw.forward(200)
    sqdraw.left(90)
    sqdraw.forward(200)
    sqdraw.left(90)
    sqdraw.forward(200)
    sqdraw.left(90)
    sqdraw.forward(200)
    sqdraw.end_fill()
    pass


def drawroof(sqdraw):
    """
    The following string is intended to create the roof of the house
    """
    sqdraw.penup()
    sqdraw.goto(-100, 100)
    sqdraw.pendown()
    sqdraw.begin_fill()
    sqdraw.fillcolor("red")
    sqdraw.left(90)
    sqdraw.forward(200)
    sqdraw.left(135)
    sqdraw.forward(141.4213562)  # An exact calculation made it easier to close the triangle.
    sqdraw.left(90)
    sqdraw.forward(141.4213562)
    sqdraw.end_fill()

    pass


def drawdoor(sqdraw):
    """
    The following string is intended to create the door of the house.
    """
    sqdraw.penup()
    sqdraw.goto(-80, -100)
    sqdraw.pendown()
    sqdraw.begin_fill()
    sqdraw.fillcolor("white")
    sqdraw.left(135)
    sqdraw.forward(60)
    sqdraw.left(90)
    sqdraw.forward(100)
    sqdraw.left(90)
    sqdraw.forward(60)
    sqdraw.left(90)
    sqdraw.forward(100)
    sqdraw.end_fill()

    pass


def drawwindow(sqdraw):
    """
    The following string is intended to create the roof of the house
    """
    sqdraw.penup()
    sqdraw.goto(10, 10)
    sqdraw.pendown()
    sqdraw.begin_fill()
    sqdraw.fillcolor("cyan")
    sqdraw.left(90)
    sqdraw.forward(70)
    sqdraw.left(90)
    sqdraw.forward(80)
    sqdraw.left(90)
    sqdraw.forward(70)
    sqdraw.left(90)
    sqdraw.forward(80)
    sqdraw.end_fill()
    sqdraw.left(180)
    sqdraw.forward(40)
    sqdraw.right(90)
    sqdraw.forward(70)
    sqdraw.right(180)
    sqdraw.forward(35)
    sqdraw.right(90)
    sqdraw.forward(40)
    sqdraw.left(180)
    sqdraw.forward(80)
    # the string is longer than I expected for it to be. The window panes were hard since I had to run the tracer back and forth.
    pass


def drawtree(sqdraw):
    """
    The following string is intended to create the base of the tree
    """
    sqdraw.penup()
    sqdraw.goto(200, -100)
    sqdraw.pendown()
    sqdraw.begin_fill()
    sqdraw.fillcolor("brown")
    sqdraw.left(180)
    sqdraw.forward(75)
    sqdraw.right(90)
    sqdraw.forward(10)
    sqdraw.right(90)
    sqdraw.forward(75)
    sqdraw.right(90)
    sqdraw.forward(10)
    sqdraw.end_fill()
    # the following code was easy since it was just 90 degree turns and extending lines.

    pass


def drawleaves(sqdraw):
    """
    The following string is intended to create the leaves of the tree
    """
    sqdraw.penup()
    sqdraw.goto(160, -60)
    sqdraw.pendown()
    sqdraw.begin_fill()
    sqdraw.fillcolor("#00FF2B")
    sqdraw.left(180)  # forming the triangle was hard. Thankfully my math major came in handy.
    sqdraw.forward(90)
    sqdraw.left(124)
    sqdraw.forward(80)
    sqdraw.left(112)
    sqdraw.forward(80)
    sqdraw.end_fill()


def main():
    """
    the following string is the basis of the code. It creates the turtle pen as well as other subjects in the code.
    """
    wn = turtle.Screen()

    sqdraw = turtle.Turtle()
    sqdraw.pensize(1)
    sqdraw.pencolor("black")
    sqdraw.speed(10)
    wn.bgcolor("cyan")

    drawbase(sqdraw)
    drawroof(sqdraw)
    drawdoor(sqdraw)
    drawwindow(sqdraw)
    drawtree(sqdraw)
    drawleaves(sqdraw)

    wn.exitonclick()


main()

