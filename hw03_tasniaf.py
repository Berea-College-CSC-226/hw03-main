#################################################################################
# Author: Fairooz Farzana Tasnia
# Username: tasniaf
#
# Assignment:
# Purpose:
# Google Doc Link: https://docs.google.com/document/d/1SaIw01vDZgL-o3BGhJgf6-AvSBewDN-p92_YVbNMM50/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################



import turtle
def draw_house():
    """
    This function draws a square house.
    """
    house = turtle.Turtle()

    house.penup()

    house.goto(-100, -100)

    house.pendown()

    house.color("#B8860B")

    house.begin_fill()

    for _ in range(4):
        house.forward(200)
        house.left(90)

    house.end_fill()



def draw_door():
    """
    This function draws a door.
    """

    door = turtle.Turtle()

    door.penup()

    door.goto(-25, -100)

    door.pendown()

    door.color("#5F9EA0")

    door.begin_fill()

    for _ in range(2):
        door.forward(50)
        door.left(90)
        door.forward(80)
        door.left(90)

    door.end_fill()

def draw_roof():
    """
    This function draws a roof.
    """
    roof = turtle.Turtle()

    roof.penup()

    roof.goto(-100,100)

    roof.pendown()

    roof.color("#5F9EA0")

    roof.begin_fill()
    roof.forward(200)
    roof.left(120)
    roof.forward(200)
    roof.left(120)
    roof.forward(200)
    roof.left(120)
    roof.end_fill()

def write_text():
    """
    This function draws a text.
    """
    text = turtle.Turtle()

    text.penup()
    text.goto(-200, 200)
    text.write("My Shaky House:)")



def main():
    """
    This is the main function where all the functions are in. It decides if the program
    runs or not when it is called.
    """

    # Function calls to function_1 and function_2.
    screen = turtle.Screen()
    screen.bgcolor("#DEB887")

    draw_house()
    draw_door()
    draw_roof()
    write_text()

    screen.exitonclick()

main()