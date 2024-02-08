#################################################################################
# Author: Andrew Carnes
# Username: Carnesa
#
# Assignment: HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: To understand RGB colors and their application to the turtle library.
# To understand and implement both general functions and the main function and follow the order of operations depicted
# in the homework.
# To understand GitHub and Git terminology, how to create branches, committing, pushing, pulling, and merging.
# Google Doc Link: https://docs.google.com/document/d/1vnz_cg1XCmgXAm4LlyNUGNvoOjfZNXkhbUEyUmNuhYs/edit?usp=sharing
#################################################################################
# Acknowledgements:
# Block header and function outline copied from hw03_stub.py by Scott Heggan
# Advice for mirroring drawing from Scott Heggan
# rgb color wheel URL: https://colorspire.com/rgb-color-wheel/
# Legend of Zelda Royal Crest reference image URL:
# https://zelda.fandom.com/wiki/Royal_Crest?file=TLoZ_Series_Royal_Crest_Artwork.png
# The Legend of Zelda is owned by Nintendo.
#################################################################################

import turtle


def crest_triangles(tri):
    """
    Doc string for crest_triangle function. Calls the triforce turtle and draws the associated image.
    """
    # Draw Triangle 1
    tri.pendown()
    tri.begin_fill()
    for i in range(3):
        tri.forward(150)
        tri.left(120)
    tri.right(120)
    tri.end_fill()
    # Draw Triangle 2
    tri.begin_fill()
    for i in range(3):
        tri.forward(150)
        tri.left(120)
    tri.left(120)
    tri.forward(150)
    tri.right(120)
    tri.end_fill()
    # Draw Triangle 3
    tri.begin_fill()
    for i in range(3):
        tri.forward(150)
        tri.left(120)
    tri.end_fill()
    # Hide Turtle
    tri.hideturtle()


def crest_left_wing(clw):
    """
    Doc string for crest_left_wing function. Calls the crescent_left turtle and draws the associated image.
    """
    clw.right(120)
    clw.forward(30)
    clw.pendown()
    clw.begin_fill()
    clw.right(90)
    clw.forward(220)
    clw.left(120)
    clw.forward(120)
    clw.left(70)
    clw.forward(200)
    clw.right(100)
    clw.circle(50, 50)
    clw.right(100)
    clw.forward(190)
    clw.left(130)
    clw.forward(120)
    clw.left(70)
    clw.forward(130)
    clw.right(120)
    clw.circle(30, 50)
    clw.right(90)
    clw.forward(90)
    clw.left(90)
    clw.forward(70)
    clw.left(90)
    clw.forward(80)
    clw.right(100)
    clw.circle(20, 50)
    clw.right(90)
    clw.forward(50)
    clw.left(90)
    clw.forward(50)
    clw.left(90)
    clw.forward(50)
    clw.right(70)
    clw.circle(100, 40)
    clw.left(50)
    clw.circle(70, 50)
    clw.circle(1, 40)
    clw.left(5)
    clw.circle(-80, 140)
    clw.forward(160)
    clw.left(165)
    clw.forward(130)
    clw.right(80)
    clw.forward(30)
    clw.end_fill()
    clw.hideturtle()


def crest_right_wing(crw):
    """
    Doc string for crest_right_wing function. Calls the crescent_right turtle and draws the associated image.
    """
    # Mirrored to left wing on the opposite side of the Triforce.
    crw.right(-120)
    crw.forward(-30)
    crw.pendown()
    crw.begin_fill()
    crw.right(-90)
    crw.forward(-220)
    crw.left(-120)
    crw.forward(-120)
    crw.left(-70)
    crw.forward(-200)
    crw.right(-100)
    crw.circle(50, -50)
    crw.right(-100)
    crw.forward(-190)
    crw.left(-130)
    crw.forward(-120)
    crw.left(-70)
    crw.forward(-130)
    crw.right(-120)
    crw.circle(30, -50)
    crw.right(-90)
    crw.forward(-90)
    crw.left(-90)
    crw.forward(-70)
    crw.left(-90)
    crw.forward(-80)
    crw.right(-100)
    crw.circle(20, -50)
    crw.right(-90)
    crw.forward(-50)
    crw.left(-90)
    crw.forward(-50)
    crw.left(-90)
    crw.forward(-50)
    crw.right(-70)
    crw.circle(100, -40)
    crw.left(-50)
    crw.circle(70, -50)
    crw.circle(1, -40)
    crw.left(-5)
    crw.circle(-80, -140)
    crw.forward(-160)
    crw.left(-165)
    crw.forward(-130)
    crw.right(-80)
    crw.forward(-30)
    crw.end_fill()
    crw.hideturtle()


def crest_crystal(cry):
    """
    Doc string for crest_crystal function. Calls the crest_cry turtle and draws the associated image.
    """
    cry.left(68)
    # Triangle
    cry.pendown()
    cry.begin_fill()
    cry.forward(150)
    cry.right(135)
    cry.forward(150)
    cry.right(113)
    cry.forward(117)
    cry.end_fill()
    # Rhombus
    cry.begin_fill()
    cry.backward(57)
    cry.left(115)
    cry.forward(100)
    cry.right(47)
    cry.forward(100)
    cry.right(135)
    cry.forward(100)
    cry.right(47)
    cry.forward(100)
    cry.left(114)
    cry.end_fill()
    # Arc Right
    cry.fillcolor("#C3C91B")
    cry.begin_fill()
    cry.backward(50)
    cry.right(7)
    cry.circle(25, 111)
    cry.forward(60)
    cry.end_fill()
    # Arc Left
    cry.begin_fill()
    cry.right(168)
    cry.forward(99)
    cry.left(64)
    cry.forward(46)
    cry.circle(25, -100)
    cry.backward(58)
    cry.right(13)
    cry.forward(90)
    cry.end_fill()
    cry.hideturtle()


def crest_left_leg(ll):
    """
    Doc string for crest_left_leg function. Calls the crest_ll turtle and draws the associated image.
    """
    ll.pendown()
    ll.begin_fill()
    ll.right(175)
    ll.circle(25, -131)
    ll.backward(50)
    ll.left(90)
    ll.backward(20)
    ll.right(120)
    ll.backward(50)
    ll.left(50)
    ll.forward(50)
    ll.left(100)
    ll.forward(70)
    ll.left(120)
    ll.forward(70)
    ll.right(160)
    ll.forward(120)
    ll.right(140)
    ll.forward(130)
    ll.left(75)
    ll.forward(54)
    ll.end_fill()


def crest_right_leg(rl):
    """
    Doc string for crest_right_leg function. Calls the crest_rl turtle and draws the associated image.
    """
    rl.pendown()
    rl.begin_fill()
    rl.right(-175)
    rl.circle(25, 131)
    rl.backward(-50)
    rl.left(-90)
    rl.backward(-20)
    rl.right(-120)
    rl.backward(-50)
    rl.left(-50)
    rl.forward(-50)
    rl.left(-100)
    rl.forward(-70)
    rl.left(-120)
    rl.forward(-70)
    rl.right(-160)
    rl.forward(-120)
    rl.right(-140)
    rl.forward(-130)
    rl.left(-75)
    rl.forward(-54)
    rl.end_fill()


def main():
    """
    Docstring for main. Creates the screen, turtles, and calls functions.
    """
    # Create Screen
    wn = turtle.Screen()
    # Background color setup.
    wn.bgcolor("lightblue")
    # Create and provide attributes for the three triangles (triforce).
    triforce = turtle.Turtle()
    triforce.pensize(5)
    triforce.teleport(-100, 200)
    triforce.fillcolor('#EDF51B')
    # Create and provide attributes for the left crescent (crescent_left).
    crescent_left = turtle.Turtle()
    crescent_left.pensize(5)
    crescent_left.teleport(-270, 200)
    crescent_left.fillcolor('#EDF51B')
    crescent_left.penup()
    # Create and provide attributes for the right crescent (crescent_right).
    crescent_right = turtle.Turtle()
    crescent_right.pensize(5)
    crescent_right.teleport(225, 200)
    crescent_right.fillcolor('#EDF51B')
    crescent_right.penup()
    # Create and provide attributes for crest_crystal (lower center triangle and rhombus).
    crest_cry = turtle.Turtle()
    crest_cry.pensize(5)
    crest_cry.teleport(-80, -100)
    crest_cry.fillcolor('#EDF51B')
    crest_cry.penup()
    # Create and provide attributes for the design left of crest_crystal (crest_ll).
    crest_ll = turtle.Turtle()
    crest_ll.pensize(5)
    crest_ll.teleport(-120, -150)
    crest_ll.fillcolor('#EDF51B')
    crest_ll.penup()
    # Create and provide attributes for the design right of crest_crystal (crest_lr).
    crest_rl = turtle.Turtle()
    crest_rl.pensize(5)
    crest_rl.teleport(80, -150)
    crest_rl.fillcolor('#EDF51B')
    crest_rl.penup()
    # Function calls to all listed functions.
    crest_triangles(triforce)
    crest_left_wing(crescent_left)
    crest_right_wing(crescent_right)
    crest_crystal(crest_cry)
    crest_left_leg(crest_ll)
    crest_right_leg(crest_rl)

    # Click to exit the screen.
    wn.exitonclick()


main()  # Starts the program (Calls variable main).
