

#################################################################################
# Author: Remi White
# Username: whiter2
#
# Assignment: HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Create a stone brick house with a chimney.
# Google Doc Link: https://docs.google.com/document/d/1chCZKeHSg3kU6T27DLPU1viQg1XvQb7iwmaFCIQyrR8/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
# HW02, T03
#
#################################################################################

import turtle


def grass_background(grass):
    """
    This makes the grass at the bottom of the screen.
    It goes off the window and makes a rectangle to look like it takes up the bottom part.
    """
    grass.setpos(-600, -600)
    grass.pensize(5)
    grass.pendown()
    grass.color(122, 253, 166)
    grass.begin_fill()
    for i in range(2):
        grass.forward(1200)
        grass.left(90)
        grass.forward(360)
        grass.left(90)
    grass.end_fill()
    grass.penup()


def house_base(base):
    """
    This is the walls and brick pattern of the walls.
    It makes the rectangle and then adds the pattern after.
    """
    base.setpos(-250, -250)
    base.pensize(5)
    base.pendown()
    base.color(0, 0, 0)
    base.fillcolor(200, 200, 200)
    base.begin_fill()
    for i in range(2):
        base.forward(500)
        base.left(90)
        base.forward(350)
        base.left(90)
    base.end_fill()

    # Starts the brick pattern by making horizontal lines.
    for i in range(10):
        base.penup()
        base.setpos(-250, -250 + 35 * i)
        base.pendown()
        base.forward(500)

    #
    for a in range(5):
        base.penup()
        base.setpos(-230 + 105 * a, -250)
        base.pendown()
        for i in range(5):
            base.forward(35)
            base.left(90)
            base.forward(35)
            base.left(90)
            base.forward(35)
            base.right(90)
            base.forward(35)
    base.penup()


def house_roof(roof):
    """
    This creates the triangle roof.
    """
    roof.setpos(-250, 100)
    roof.pensize(5)
    roof.pendown()
    roof.color(0, 0, 0)
    roof.fillcolor(100, 100, 100)
    roof.begin_fill()
    roof.forward(500)
    roof.left(150)
    roof.forward(289)
    roof.left(60)
    roof.forward(289)
    roof.left(150)
    roof.end_fill()
    roof.penup()


def house_chimney(chimney):
    """
    This creates the chimney of the roof.
    It first makes the rectangle and then adds the pattern.
    Then, it has to rotate the turtle back to its original direction.
    """
    chimney.setpos(170, 100)
    chimney.pendown()
    chimney.color(0, 0, 0)
    chimney.fillcolor(210, 84, 84)
    chimney.begin_fill()

    for i in range(2):
        chimney.forward(30)
        chimney.left(90)
        chimney.forward(90)
        chimney.left(90)
    chimney.end_fill()

    # Bricks on chimney
    chimney.pensize(2)
    chimney.left(90)
    chimney.forward(10)
    chimney.right(90)

    # Creates the horizontal lines.
    for i in range(9):
        chimney.penup()
        chimney.setpos(170, 110 + 10 * i)
        chimney.pendown()
        chimney.forward(30)

    chimney.penup()
    chimney.setpos(180, 100)
    chimney.pendown()

    # Adds the pattern to the horizontal lines.
    for i in range(5):
        chimney.forward(10)
        chimney.left(90)
        chimney.forward(10)
        chimney.left(90)
        if i < 4:
            chimney.forward(10)
            chimney.right(90)
            chimney.forward(10)
            chimney.right(90)
        elif i == 4:
            chimney.right(180)
    chimney.penup()


def house_door(door):
    """
    This creates the door on the house.
    It also adds the doorknob and door window to the door.
    """
    door.setpos(-45, -250)
    door.pendown()
    door.color(0, 0, 0)
    door.fillcolor(180, 90, 60)
    door.begin_fill()

    for i in range(2):
        door.forward(90)
        door.left(90)
        door.forward(125)
        door.left(90)
    door.end_fill()

    # Door handle.
    door.shape("circle")
    door.fillcolor(0, 0, 0)
    door.shapesize(0.5)
    door.penup()
    door.setpos(25, -180)
    door.stamp()

    # Door window.
    door.setpos(30, -160)
    door.pendown()
    door.fillcolor(190, 250, 255)
    door.begin_fill()
    door.left(90)
    door.circle(30, 180)
    door.left(90)
    door.forward(60)
    door.end_fill()
    door.penup()


def house_windows(window):
    """
    Creates the windows for the house.
    Makes the windows then adds the lines.
    """
    window.setpos(-45, -250)
    window.pendown()
    window.color(0, 0, 0)
    window.fillcolor(190, 250, 255)

    # Creates window outline and fills color.
    for a in range(2):
        window.begin_fill()
        window.penup()
        window.setpos(-200 + 310 * a, -75)
        window.pendown()
        for i in range(2):
            window.forward(90)
            window.left(90)
            window.forward(125)
            window.left(90)
        window.end_fill()

    # Adds the lines 2 lines through the middle of the windows.
    for a in range(2):
        window.penup()
        window.setpos(-200 + 310 * a, -75)
        window.pendown()
        window.forward(45)
        window.left(90)
        window.forward(125)
        window.left(90)
        window.forward(45)
        window.left(90)
        window.forward(62.5)
        window.left(90)
        window.forward(90)


def main():
    """
    Makes the turtle screen and a turtle that can be used in the functions.
    Then, it calls the functions starting with the more background images and adds the others on top.
    """
    turtle.colormode(255)

    wn = turtle.Screen()
    wn.bgcolor(134, 84, 210)

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()

    grass_background(t)
    house_chimney(t)
    house_base(t)
    house_roof(t)
    house_door(t)
    house_windows(t)

    wn.exitonclick()


main()
