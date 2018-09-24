######################################################################
# Author: Hailey Barnett
# Username: barnetth
#
# Assignment: A03: A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
# Google Doc: https://docs.google.com/document/d/1b_kPuOFjk2ts8oeHPeDi9AVNJG23O5g9rXZ3Zpel5ic/edit?usp=sharing
######################################################################
# Acknowledgements:

#################################################################################

import turtle


def draw_grass(grass):
    """
    Draws the grass.

    :param grass: a Turtle object
    :return: None
    """
    grass.penup()
    grass.setpos(-500, -200)
    grass.pendown()
    grass.color("green")
    grass.begin_fill()
    for shape in range(2):
        grass.forward(1000)
        grass.right(90)
        grass.forward(500)
        grass.right(90)
    grass.end_fill()


def draw_walls(walls):
    """
    Draws the walls of the house.

    :param walls: a Turtle object
    :return: None
    """
    walls.penup()
    walls.setpos(-100, -200)
    walls.pendown()
    walls.color("white")
    walls.begin_fill()
    walls.left(90)
    for shape in range(2):
        walls.forward(200)
        walls.right(90)
        walls.forward(200)
        walls.right(90)
    walls.end_fill()


def draw_roof(roof):
    """
    Draws the roof of the house.

    :param roof: a Turtle object
    :return: None
    """
    roof.penup()
    roof.setpos(-100, 0)
    roof.pendown()
    roof.color("black")
    roof.begin_fill()
    roof.left(40)
    roof.forward(132)
    roof.right(80)
    roof.forward(131)
    roof.end_fill()


def draw_chimney(chimney):
    """
    Draws the chimney of the house.

    :param chimney: a Turtle object
    :return: None
    """
    chimney.penup()
    chimney.setpos(-100, 1)
    chimney.pendown()
    chimney.color("black")
    chimney.begin_fill()
    for shape in range(2):
        chimney.forward(50)
        chimney.left(90)
        chimney.forward(50)
        chimney.left(90)
    chimney.end_fill()


def draw_door(door):
    """
    Draws the door of the house.

    :param door: a Turtle object
    :return: None
    """
    door.penup()
    door.setpos(20, -200)
    door.pendown()
    door.color("#ff0000")
    door.begin_fill()
    for shape in range(2):
        door.forward(40)
        door.left(90)
        door.forward(75)
        door.left(90)
    door.end_fill()


def draw_window_one(window_one):
    """
    Draws the left window of the house.

    :param window_one: a Turtle object
    :return: None
    """
    window_one.penup()
    window_one.setpos(-75, -75)
    window_one.pendown()
    window_one.color("teal")
    window_one.begin_fill()
    for shape in range(4):
        window_one.forward(40)
        window_one.left(90)
    window_one.end_fill()


def draw_window_two(window_two):
    """
    Draws the right window of the house.

    :param window_two: a Turtle object
    :return: None
    """
    window_two.penup()
    window_two.setpos(30, -75)
    window_two.pendown()
    window_two.color("teal")
    window_two.begin_fill()
    for shape in range(4):
        window_two.forward(40)
        window_two.left(90)
    window_two.end_fill()


def main():
    """
    Calls all functions to draw all the features of the house together.

    :return: None
    """
    turtle.colormode(255)

    # creates and draws background
    wn = turtle.Screen()
    wn.bgcolor("sky blue")

    # creates specific turtle for each specific function
    grass = turtle.Turtle()
    grass.hideturtle()
    walls = turtle.Turtle()
    walls.hideturtle()
    roof = turtle.Turtle()
    roof.hideturtle()
    chimney = turtle.Turtle()
    chimney.hideturtle()
    door = turtle.Turtle()
    door.hideturtle()
    window_one = turtle.Turtle()
    window_one.hideturtle()
    window_two = turtle.Turtle()
    window_two.hideturtle()

    # calls each function and draws house
    draw_grass(grass)
    draw_walls(walls)
    draw_roof(roof)
    draw_chimney(chimney)
    draw_door(door)
    draw_window_one(window_one)
    draw_window_two(window_two)

    # wait for a user to click on canvas to exit
    wn.exitonclick()


main()
