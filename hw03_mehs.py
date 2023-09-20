#################################################################################
# Author: Su Meh
# Username: mehs
#
# Assignment: HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: To get a better grasp of how Git works.
# Google Doc Link: https://docs.google.com/document/d/11qWG8MLGUfP-ofBRrbgEXcZg3TRbhSOh5YrcnjNUAkg/edit?usp=sharing
#
#################################################################################
# Acknowledgements: Dr Scotts Heggens for the layout.
#
#
#################################################################################

import turtle


def draw_roof(rf):
    """
    This will create the outline of the roof
    """
    pass
    # ....
    rf.penup()
    rf.fd(200)
    rf.left(145)

    for i in range(1):
        rf.speed(2)
        rf.pendown()
        rf.pensize(5)
        rf.pencolor("white")
        rf.fd(200)
        rf.left(35)
        rf.forward(200)
        rf.left(35)
        rf.fd(200)
        rf.left(145)
        rf.fd(530)



def fill_rfred(filr):
    """
    This will draw in the red line for the roof
    """
    pass
    # ....
    filr.penup()
    filr.fd(189)
    filr.left(145)
    filr.fd(10)
    filr.color("red")

    for i in range(1):
        filr.pendown()
        filr.pensize(8)
        filr.fd(184)
        filr.left(35)
        filr.fd(190)
        filr.left(35)
        filr.fd(184)
        filr.left(145)
        filr.fd(496)

def fill_rfor(filr1):
    """
    This will draw in the lighter red line for the roof
    """
    pass
    # ....
    filr1.penup()
    filr1.fd(174)
    filr1.left(145)
    filr1.fd(21)
    filr1.color("#FF0000")

    for i in range(1):
        filr1.pendown()
        filr1.pensize(8)
        filr1.fd(160)
        filr1.left(35)
        filr1.fd(181)
        filr1.left(35)
        filr1.fd(158)
        filr1.left(145)
        filr1.fd(443)

def fill_rfye(filry):
    """
    This will draw in the lighter red line than above for the roof
    """
    pass
    # ....
    filry.penup()
    filry.fd(160)
    filry.left(145)
    filry.fd(36)
    filry.color("#FF6666")

    for i in range(1):
        filry.pendown()
        filry.pensize(8)
        filry.fd(132)
        filry.left(35)
        filry.fd(173)
        filry.left(35)
        filry.fd(133)
        filry.left(145)
        filry.fd(392)

def fill_rfre1(filrd1):
    """
    This will draw in the lighter red line than the one above for the roof
    """
    pass
    # ....
    filrd1.penup()
    filrd1.fd(145)
    filrd1.left(145)
    filrd1.fd(48)
    filrd1.color("#FF9999")

    for i in range(1):
        filrd1.pendown()
        filrd1.pensize(8)
        filrd1.fd(107)
        filrd1.left(35)
        filrd1.fd(163)
        filrd1.left(35)
        filrd1.fd(106)
        filrd1.left(145)
        filrd1.fd(338)

def fill_rfor1(filror1):
    """
    This will draw in the lightest red line for the roof
    """
    pass
    # ....
    filror1.penup()
    filror1.fd(131)
    filror1.left(145)
    filror1.fd(61)
    filror1.color("#FFCCCC")

    for i in range(1):
        filror1.pendown()
        filror1.pensize(8)
        filror1.fd(81)
        filror1.left(35)
        filror1.fd(156)
        filror1.left(35)
        filror1.fd(81)
        filror1.left(145)
        filror1.fd(288)

def fill_rfye1(filrye1):
    """
    This will draw in the lightest pink line for the roof
    """
    pass
    # ....
    filrye1.penup()
    filrye1.fd(118)
    filrye1.left(145)
    filrye1.fd(70)
    filrye1.color("#FFCCE5")

    for i in range(1):
        filrye1.pendown()
        filrye1.pensize(8)
        filrye1.fd(60)
        filrye1.left(35)
        filrye1.fd(151)
        filrye1.left(35)
        filrye1.fd(55)
        filrye1.left(145)
        filrye1.fd(233)
        filrye1.left(145)
        filrye1.fd(47)
        filrye1.left(35)
        filrye1.fd(144)
        filrye1.left(35)
        filrye1.fd(38)
        filrye1.left(145)
        filrye1.fd(193)
        filrye1.left(145)
        filrye1.fd(26)
        filrye1.left(35)
        filrye1.fd(150)
        filrye1.left(35)
        filrye1.fd(19)
        filrye1.left(145)
        filrye1.fd(163)
        filrye1.left(35)
        filrye1.fd(5)
        filrye1.left(145)
        filrye1.fd(150)

def draw_house(hse):
    """
    This will draw the outline of the house
    """
    pass
    # ...'
    hse.penup()
    hse.fd(200)
    hse.right(90)

    for i in range(2):
        hse.pendown()
        hse.pensize(5)
        hse.pencolor("white")
        hse.fd(200)
        hse.right(90)
        hse.fd(528)
        hse.right(90)

def fill_house(filhse):
    """
    This will fill in the house with very light pastel brown
    """
    pass
    # ....
    filhse.penup()
    filhse.fd(194)
    filhse.right(90)
    filhse.fd(7)

    for i in range(52):
        filhse.pendown()
        filhse.pencolor("#FFE5CC")
        filhse.speed(0)
        filhse.pensize(10)
        filhse.fd(186)
        filhse.right(90)
        filhse.fd(5)
        filhse.right(90)
        filhse.fd(186)
        filhse.left(90)
        filhse.fd(5)
        filhse.left(90)

def door(dr):
    """
    This will draw the door light brown
    """
    pass
    # ....
    dr.penup()
    dr.right(90)
    dr.fd(90)
    dr.right(90)

    for i in range(4):
        dr.pendown()
        dr.pencolor("#FFB266")
        dr.pensize(8)
        dr.fd(100)
        dr.left(90)

    for i in range(5):
        dr.pendown()
        dr.pencolor("#FFB266")
        dr.pensize(8)
        dr.fd(96)
        dr.left(90)
        dr.fd(10)
        dr.left(90)
        dr.fd(96)
        dr.right(90)
        dr.fd(10)
        dr.right(90)

def window(wd):
    """
    This will draw the window brown and fill in the window light yellow
    """
    pass
    # ....
    wd.penup()
    wd.fd(130)
    wd.right(90)
    wd.fd(70)
    wd.right(90)

    for i in range(4):
        # outline the right window brown
        wd.pendown()
        wd.pencolor("#FFB266")
        wd.pensize(8)
        wd.fd(70)
        wd.left(90)

    wd.penup()
    wd.left(90)
    wd.fd(7)
    wd.right(90)
    wd.fd(5)

    for i in range(6):
        # fill in the right window light yellow
        wd.pendown()
        wd.pencolor("#FFFFCC")
        wd.pensize(8)
        wd.fd(60)
        wd.left(90)
        wd.fd(5)
        wd.left(90)
        wd.fd(60)
        wd.right(90)
        wd.fd(5)
        wd.right(90)

def window1(wd1):
    """
    This will draw the second window brown and fill it in very light yellow
    """
    pass
    # ....
    wd1.penup()
    wd1.right(180)
    wd1.fd(180)
    wd1.left(90)
    wd1.fd(70)
    wd1.right(90)

    for i in range(4):
        # this will outline the second window brown
        wd1.pendown()
        wd1.pencolor("#FFB266")
        wd1.pensize(8)
        wd1.fd(70)
        wd1.left(90)

    wd1.penup()
    wd1.left(90)
    wd1.fd(7)
    wd1.right(90)
    wd1.fd(5)

    for i in range(6):
        # fill in the right window with very light yellow
        wd1.pendown()
        wd1.pencolor("#FFFFCC")
        wd1.pensize(8)
        wd1.fd(60)
        wd1.left(90)
        wd1.fd(5)
        wd1.left(90)
        wd1.fd(60)
        wd1.right(90)
        wd1.fd(5)
        wd1.right(90)


def main():
    """
    Listed all the functions that are needed to build the house and fill it in with colors.
    """
    # ...

    wn = turtle.Screen()
    rf = turtle.Turtle()
    hse = turtle.Turtle()
    filr = turtle.Turtle()
    filhse = turtle.Turtle()
    filror = turtle.Turtle()
    filry = turtle.Turtle()
    filrd1 = turtle.Turtle()
    filror1 = turtle.Turtle()
    filrye1 = turtle.Turtle()
    dr = turtle.Turtle()
    wd = turtle.Turtle()
    wd1 = turtle.Turtle()

    wn.bgcolor("light blue")

    draw_roof(rf)  # Function call to outline the roof.
    draw_house(hse)  # Function call to outline the house.
    fill_rfred(filr)  # Function call to fill roof red
    fill_house(filhse)  # Function call to fill house
    fill_rfor(filror)  # Function call to fill roof a shade of red
    fill_rfye(filry)  # Function call to fill roof a lighter shade of red
    fill_rfre1(filrd1)  # Function call to fill in the light shade of red
    fill_rfor1(filror1)  # Function call to fill in the lightest shade of red
    fill_rfye1(filrye1)  # Function call to fill in the lightest shade of pink
    door(dr)  # Function call to draw the door
    window(wd)  # Function call to draw the right window
    window1(wd1)  # Function call to draw the left window
    wn.exitonclick()

main()


