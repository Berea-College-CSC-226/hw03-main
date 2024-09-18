

#################################################################################
# Author: Dylan Roland
# Username: rolandd
#
# Assignment: HW03
# Purpose: To draw a giraffe
# Google Doc Link:https://docs.google.com/document/d/1A-STS7gX_5MVm1CM2mSFn-NCOdlrcuB4ouTSuaZ2fhc/edit
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################


import turtle




def drawbackground(giraffe):
    """
    draws a safari background for mr giraffe (sun and a tree)
    """
    giraffe.penup()
    giraffe.goto(-200, 150)
    giraffe.pendown()
    giraffe.color("yellow")
    giraffe.begin_fill()
    giraffe.circle(50)
    giraffe.end_fill()

    # Draw the trunk
    giraffe.penup()
    giraffe.goto(160, -150)   #starting position
    giraffe.pendown()
    giraffe.color("brown")
    giraffe.begin_fill()
    for _ in range(2):
        giraffe.forward(30)  # wide trunk
        giraffe.left(90)
        giraffe.forward(150)  # Tall trunk
        giraffe.left(90)
    giraffe.end_fill()

    # Draw the first layer of leaves (large circle)
    giraffe.color("darkgreen")
    giraffe.penup()
    giraffe.goto(160, -10)  # Shift left for centering
    giraffe.pendown()
    giraffe.begin_fill()
    giraffe.circle(60)  # first layer of leaves
    giraffe.end_fill()

    # Draw the second layer of leaves (medium circle)
    giraffe.penup()
    giraffe.goto(160, 70)  # Adjusted for height
    giraffe.pendown()
    giraffe.begin_fill()
    giraffe.circle(45)  # second layer of leaves
    giraffe.end_fill()


def drawgiraffe(giraffe):
    """
    Draws a simple giraffe using basic shapes.
    """
    # Draw body
    giraffe.penup()
    giraffe.goto(-50, -100)
    giraffe.pendown()
    giraffe.color("orange")
    giraffe.begin_fill()
    for i in range(2):
        giraffe.forward(100)
        giraffe.left(90)
        giraffe.forward(60)
        giraffe.left(90)
    giraffe.end_fill()

    # Draw legs
    giraffe.penup()
    giraffe.goto(-40, -160)
    giraffe.pendown()
    giraffe.color("orange")
    giraffe.begin_fill()
    for i in range(2):
        giraffe.forward(20)
        giraffe.left(90)
        giraffe.forward(60)
        giraffe.left(90)
    giraffe.end_fill()

    giraffe.penup()
    giraffe.goto(20, -160)
    giraffe.pendown()
    giraffe.begin_fill()
    for i in range(2):
        giraffe.forward(20)
        giraffe.left(90)
        giraffe.forward(60)
        giraffe.left(90)
    giraffe.end_fill()

    # Draw neck
    giraffe.penup()
    giraffe.goto(-50, -40)
    giraffe.pendown()
    giraffe.begin_fill()
    for i in range(2):
        giraffe.forward(20)
        giraffe.left(90)
        giraffe.forward(110)
        giraffe.left(90)
    giraffe.end_fill()

    # Draw head
    giraffe.penup()
    giraffe.goto(-40, 60)
    giraffe.pendown()
    giraffe.begin_fill()
    giraffe.circle(30)  # Head as a circle
    giraffe.end_fill()

    # Draw ears
    giraffe.penup()
    giraffe.goto(-55, 115)
    giraffe.pendown()
    giraffe.begin_fill()
    giraffe.circle(10)  # Left ear
    giraffe.end_fill()

    giraffe.penup()
    giraffe.goto(-25, 115)
    giraffe.pendown()
    giraffe.begin_fill()
    giraffe.circle(10)  # Right ear
    giraffe.end_fill()

    # Draw spots on body
    giraffe.penup()
    giraffe.goto(-40, -80)
    giraffe.pendown()
    giraffe.color("brown")
    giraffe.begin_fill()
    giraffe.circle(10)  # Spot 1
    giraffe.end_fill()

    giraffe.penup()
    giraffe.goto(0, -70)
    giraffe.pendown()
    giraffe.begin_fill()
    giraffe.circle(10)  # Spot 2
    giraffe.end_fill()

    giraffe.penup()
    giraffe.goto(-40, -45)
    giraffe.pendown()
    giraffe.begin_fill()
    giraffe.circle(10)  # Spot 3
    giraffe.end_fill()

    giraffe.penup()
    giraffe.goto(-40, 10)
    giraffe.pendown()
    giraffe.begin_fill()
    giraffe.circle(10)  # Spot 4
    giraffe.end_fill()


def main():
    """
    draws the picture of the safari background and mr giraffe
    """
    giraffe = turtle.Turtle()
    wn = turtle.Screen()
    wn.bgcolor('green')
    giraffe.speed(0.1)
    # Function calls to function_1 and function_2.
    drawbackground(giraffe)
    drawgiraffe(giraffe)
    wn.exitonclick()


main()  # Starts the program!
