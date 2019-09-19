#################################################################################
# Author: Shawn Villahermosa
# Username: villahermosas
# Google Doc Link: https://docs.google.com/document/d/1WmPhrT9UQnTNgxlrbguVLvC46vg5aPw7u2hMnHOlA9w/edit?usp=sharing
#################################################################################

import turtle


def roof(tess):
    """
    Makes the roof

    :param tess: a Turtle object
    :return: None
    """
    tess.penup()
    tess.goto(-200, 0)
    tess.pendown()
    tess.color("white")  # Makes the pencolor white
    tess.begin_fill()
    for num in range(3):
        tess.forward(180)
        tess.left(120)
    tess.end_fill()


def main_walls(tess):
    """
    Make the main walls

    param tess: a Turtle object
    :return: None
    """
    tess.penup()
    tess.goto(-190, 0)
    tess.pendown()
    tess.right(90)
    tess.color("white", "black")  # Makes the line white, fills in the shape black
    tess.begin_fill()
    for num in range(2):
        tess.fd(150)
        tess.left(90)
        tess.fd(160)
        tess.left(90)
    tess.end_fill()


def windows(tess):
    """
    Makes the windows

    :param tess: a Turtle object
    :return: None
    """
    # First window
    tess.penup()
    tess.goto(-170, -20)
    tess.pendown()
    tess.left(90)
    tess.color("white")
    for num in range(4):
        tess.fd(50)
        tess.right(90)
    tess.fd(25)
    tess.right(90)
    tess.fd(50)
    tess.right(90)
    tess.fd(25)
    tess.right(90)
    tess.fd(25)
    tess.right(90)
    tess.fd(50)

    # Details
    tess.penup()  # First line
    tess.goto(-152, -26)
    tess.pendown()
    tess.goto(-160, -37)
    tess.penup()  # Second line
    tess.goto(-140, -37)
    tess.pendown()
    tess.goto(-132, -26)
    tess.penup()  # Third line
    tess.goto(-124, -26)
    tess.pendown()
    tess.goto(-132, -37)
    tess.penup()  # Fourth line
    tess.goto(-130, -54)
    tess.pendown()
    tess.goto(-135, -60)
    tess.penup()  # Fifth line
    tess.goto(-150, -54)
    tess.pendown()
    tess.goto(-158, -63)

    # Second window
    tess.penup()
    tess.goto(-100, -20)
    tess.pendown()
    for num in range(4):
        tess.fd(50)
        tess.right(90)
    tess.fd(25)
    tess.right(90)
    tess.fd(50)
    tess.right(90)
    tess.fd(25)
    tess.right(90)
    tess.fd(25)
    tess.right(90)
    tess.fd(50)

    # Details
    tess.penup()  # First line
    tess.goto(-80, -26)
    tess.pendown()
    tess.goto(-90, -40)
    tess.penup()  # Second line
    tess.goto(-70, -40)
    tess.pendown()
    tess.goto(-60, -26)
    tess.penup()  # Third line
    tess.goto(-58, -33)
    tess.pendown()
    tess.goto(-63, -40)
    tess.penup()  # Fourth line
    tess.goto(-60, -53)
    tess.pendown()
    tess.goto(-70, -65)
    tess.penup()  # Fifth line
    tess.goto(-83, -55)
    tess.pendown()
    tess.goto(-90, -65)


def door(tess):
    """
    Makes the door

    :param tess: a Turtle object
    :return: None
    """
    tess.penup()
    tess.goto(-135, -150)
    tess.pendown()
    tess.left(90)
    tess.color("#ffffff", "#8B4513")  # Makes the pen color white and fills in brown
    tess.begin_fill()
    for num in range(2):
        tess.fd(60)
        tess.right(90)
        tess.fd(50)
        tess.right(90)
    tess.end_fill()

    # Makes the doorknob
    tess.hideturtle()
    tess.penup()
    tess.goto(-97, -127)
    tess.dot(8)


# Writes the texts "BOO!"
def text(tess):
    tess.color("#00008b")
    tess.setpos(5, 0)
    tess.write("BOO!", font=("TimesNewRoman", 50, "bold"))


def main():
    """
    Draws a house

    :return: None
    """

    wn = turtle.Screen()
    wn.title("Happy Halloween!")
    wn.bgpic("Halloween-Background.gif")  # Sets up the background picture
    tess = turtle.Turtle()
    tess.speed(5)  # Sets up the speed to which the turtle draws
    tess.hideturtle()

    # The different parts of the house
    roof(tess)
    main_walls(tess)
    windows(tess)
    door(tess)
    text(tess)

    wn.exitonclick()


main()
