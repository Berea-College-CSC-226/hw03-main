# Author: Jeremy Campbell

# Username: campbellj3

# Assignment: a03

# Purpose: Design a moderately complex image that utilizes a rgb color range.
########################################################################################################################

import turtle  # opens the turtle library


def make_roof(wn, bob):
    """
    Constructing the roof of the house.

    :param wn: the turtle screen object
    :param bob: the turtle object we'll be using
    :return: No specified return
    """
    bob.penup()
    bob.setpos(90, 90,)
    bob.pendown()
    bob.stamp()


def make_main_house(bob):
    """
    Will construct the main body of the house

    :param bob: the specified turtle object.
    :return: N/A
    """

    bob.setpos(30, 47)
    bob.color('brown')
    bob.begin_fill()
    for side in range(2):
        bob.forward(100)
        bob.right(90)
        bob.forward(140)
        bob.right(90)
    bob.end_fill()


def make_window(bob, x, y):
    """
    Will design a window on the house.

    :param bob: Names the turtle object.
    :param x: the x coordinate found on the window.
    :param y: the y coordinate found on the window.
    :return: N/A.
    """
    bob.penup()
    bob.setpos(x, y)
    bob.pendown()
    bob.color('black')
    bob.begin_fill()
    for side in range(2):
        bob.forward(30)
        bob.right(90)
        bob.forward(20)
        bob.right(90)
    bob.end_fill()


def make_door(bob):
    """
    Constructs a door on the house.

    :param bob: defined turtle object.
    :return: N/A.
    """
    bob.penup()
    bob.setpos(70, -42)
    bob.pendown()
    bob.color('black')
    bob.begin_fill()
    for side in range(2):
        bob.forward(20)
        bob.right(90)
        bob.forward(50)
        bob.right(90)
    bob.end_fill()


#def make_text(bob, txt):
    """
    Will display text on the screen.

    :param bob: turtle object we defined.
    :param txt: intended text to be displayed.
    :return: N/A.
    """
    #bob.color('red')
    #bob.setpos(70, 120)
    #bob.write(txt, move=False, align='center', font=("Times New Roman", 20, "bold," "normal"))


def main():
    """
    Will draw a house on the intended screen.

    :return: N/A.
    """
    #turtle.colormode(255)

    wn = turtle.Screen()
    wn.bgcolor('lightgreen')
    bob = turtle.Turtle()
    bob.hideturtle()

    # Will call the defined functions
    make_roof(wn, bob)
    make_main_house(bob)
    make_window(bob, 45, 0)
    make_window(bob, 88, 0)
    make_door(bob)
    #make_text(bob, "Welcome home!")

    wn.exitonclick()  # allows user to exit the ran program as wanted.


main()  # Calling the function.
