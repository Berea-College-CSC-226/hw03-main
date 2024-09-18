#################################################################################
# Author: Sonam Tsering
# Username: Sonam867
#
# Assignment: HW03
# Purpose: Create a colorful house using functions.
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle


def create_house(turtle_instance, size, house_color):
    """
    Constructs the main structure of the house.
    """
    turtle_instance.fillcolor(house_color)
    turtle_instance.begin_fill()
    for _ in range(4):
        turtle_instance.forward(size)
        turtle_instance.right(90)
    turtle_instance.end_fill()


def create_roof(turtle_instance, size, roof_color):
    """
    Constructs the roof of the house.
    """
    turtle_instance.fillcolor(roof_color)
    turtle_instance.begin_fill()
    for _ in range(3):
        turtle_instance.forward(size)
        turtle_instance.left(120)
    turtle_instance.end_fill()


def create_door(turtle_instance, door_width, door_height, door_color):
    """
    Constructs the door of the house.
    """
    turtle_instance.fillcolor(door_color)
    turtle_instance.begin_fill()
    for _ in range(2):
        turtle_instance.forward(door_width)
        turtle_instance.right(90)
        turtle_instance.forward(door_height)
        turtle_instance.right(90)
    turtle_instance.end_fill()


def create_window(turtle_instance, window_size, window_color):
    """
    Constructs a window for the house.
    """
    turtle_instance.fillcolor(window_color)
    turtle_instance.begin_fill()
    for _ in range(4):
        turtle_instance.forward(window_size)
        turtle_instance.right(90)
    turtle_instance.end_fill()

    turtle_instance.forward(window_size / 2)
    turtle_instance.right(90)
    turtle_instance.forward(window_size)
    for _ in range(2):
        turtle_instance.right(90)
        turtle_instance.forward(window_size / 2)
    turtle_instance.right(90)
    turtle_instance.forward(window_size)


def main():
    """
    Configures the turtle screen and initiates the drawing process.
    """
    screen = turtle.Screen()
    screen.colormode(255)
    screen.bgcolor((200, 240, 255))  # Light sky blue background

    artist = turtle.Turtle()  # Turtle named artist
    artist.pensize(5)

    artist.penup()
    artist.goto(-150, 100)  # Position for the house base
    artist.pendown()
    create_house(artist, 300, (102, 204, 255))  # Light blue house base
    create_roof(artist, 300, (255, 128, 0))  # Orange roof

    artist.penup()
    artist.goto(-30, -100)  # Position for the door
    artist.pendown()
    create_door(artist, 60, 120, (139, 69, 19))  # Brown door

    artist.penup()
    artist.goto(-100, -30)  # Position for the first window
    artist.pendown()
    create_window(artist, 60, (255, 255, 0))  # Yellow window

    artist.penup()
    artist.goto(40, -30)  # Position for the second window
    artist.pendown()
    create_window(artist, 60, (255, 255, 0))  # Matching yellow window

    artist.hideturtle()  # Hide the turtle for better view

    screen.exitonclick()


main()  # Start the drawing process
