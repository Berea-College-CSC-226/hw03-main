# Author: Jeremy Campbell

# Username: campbellj3

# Assignment: a03

# Purpose: Design a moderately complex image that utilizes a rgb color range.

# Modeled after the house code in t03. Credit to Dr. Scott Heggen and Emily Lovell
########################################################################################################################

# Author: Jeremy Campbell

# Username: campbellj3

# Assignment: a03

# Purpose: Design a moderately complex image that utilizes a rgb color range.

# Acknowledgements: Received assistance from Aziz, and Dr. Heggen.

# Modeled after the house code in t03. Credit to Dr. Scott Heggen and Emily Lovell.
# Source: https://www.mouseplanet.com/12222/Disney_Goes_to_Hell_for_Halloween
########################################################################################################################

import turtle  # opens the turtle library


def make_main_house(bob):
    """
    Will construct the main body of the house

    :param bob: the specified turtle object.
    :return: N/A
    """
    bob.penup()
    bob.setpos(35, 47)
    bob.pendown()
    bob.color('dark red')
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
    bob.setpos(75, -42)
    bob.pendown()
    bob.color('black')
    bob.begin_fill()
    for side in range(2):
        bob.forward(20)
        bob.right(90)
        bob.forward(50)
        bob.right(90)
    bob.end_fill()


def make_text(bob, txt):
    """
    Will display text on the screen.

    :param bob: turtle object we defined.
    :param txt: intended text to be displayed.
    :return: N/A.
    """
    bob.penup()
    bob.color('black')
    bob.setpos(70, 200)
    bob.write(txt, move=False, align='center', font=("Arial", 25, ("bold", "normal")))


def main():
    """
    Will draw a house on the intended screen.

    :return: N/A.
    """
    #turtle.colormode(255)

    wn = turtle.Screen()
    wn.bgpic("DHRoof6.png")
    bob = turtle.Turtle()
    bob.hideturtle()

    # Will call the defined functions
    # make_roof(wn, bob)
    make_main_house(bob)
    make_window(bob, 50, 0)
    make_window(bob, 93, 0)
    make_door(bob)
    make_text(bob, "At least the rents cheap...")   # Leaves text on the screen.

    wn.exitonclick()  # allows user to exit the ran program as wanted.


main()  # Calling the function.
