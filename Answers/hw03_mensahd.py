#################################################################################
# Author: Derrick Mensah
# Username: mensahd
#
# Assignment: HW03
# Purpose: To practice using functions,and learn more about version control
# Google Doc Link: https://docs.google.com/document/d/1T5sj3CfbJUNc7w7CJK4-0kZ4NJDZA8HCI-O98-Uq_Vs/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle

def draw_boat_hull():
    """
    Draw the bottom body base of the sailboat
    """
    hull = turtle.Turtle()
    hull.speed(3)
    hull.hideturtle()

    # Move to the starting point for the hull base
    hull.penup()
    hull.goto(-100, -90)
    hull.pendown()

    # Fill the shape with a brown color
    hull.begin_fill()
    hull.color("saddlebrown")

    hull.forward(200)
    hull.left(60)
    hull.forward(60)
    hull.left(120)
    hull.forward(260)
    hull.left(120)
    hull.forward(60)

    hull.end_fill()


def draw_mast_and_sail():
    """
    Draws a vertical black center mast and a large sky-blue triangular sail.
    """
    sail = turtle.Turtle()
    sail.speed(3)
    sail.hideturtle()

    # Drawing the vertical mast used on the boat
    sail.penup()
    sail.goto(0, -38)  # Start right at the top center of the hull base area
    sail.pendown()
    sail.pensize(5)
    sail.color("black")
    sail.left(90)
    sail.forward(130)

    #reduce pensize, and draw a triangular mast with a red color
    sail.pensize(1)
    sail.begin_fill()
    sail.color("red")
    sail.right(90)
    sail.forward(80)
    sail.goto(0, 132)
    sail.goto(0, 2)

    sail.end_fill()


def main():
    """
    This is the main function, where we run the window object, and run all other functions
    """
    wn = turtle.Screen()
    wn.setup(width=600, height=500)
    wn.title("Ghana NAVY Boat")
    wn.bgpic("background.gif")  # change background to a gif, basically an ocean

    draw_boat_hull()
    draw_mast_and_sail()
    wn.exitonclick()

main()