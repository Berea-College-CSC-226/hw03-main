#################################################################################
# Author: Bao Hoang
# Username: hoangb
#
# Assignment: HW03
# Purpose: Draw a picture
# Google Doc Link: https://docs.google.com/document/d/1v5S_iozpfFFcLiALl1o0GkXpPh7SeRWzM0E0mI2bAmI/edit?usp=sharing
#
#################################################################################


import turtle


def draw_rectangle(t, width, height, color):
    """
    Function to draw a rectangle on the screen.
    """
    t.fillcolor(color)
    t.begin_fill()
    for i in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

def draw_root(t, color):
    """
    Function to draw a root of the house.
    """
    t.fillcolor(color)
    t.begin_fill()
    t.left(45)
    t.goto(-120,80)
    t.right(45)
    t.goto(120,80)
    t.right(45)
    t.goto(150,50)
    t.end_fill()

def draw_circle(t, radius, color):
    """
    Function to draw a circle on the screen.
    """
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def main():
    """
    Draw a house including a body, a root, a door, and 2 windows. Then draw a tree on the left
    """
    wn = turtle.Screen()
    wn.bgcolor("pink")
    wn.colormode(255)

    #Draw house
    house = turtle.Turtle()

    #Draw house body
    house.penup()
    house.goto(-150, -150)
    house.pendown()
    draw_rectangle(house, 300, 200, (100, 246, 255))

    #Draw root
    house.penup()
    house.goto(-150, 50)
    house.pendown()
    draw_root(house, (144,77,0))

    #Draw door
    house.penup()
    house.goto(-30, -150)
    house.setheading(0)
    house.pendown()
    draw_rectangle(house, 60, 100, "yellow")

    #Draw windows
    house.penup()
    house.goto(-100,-25)
    house.pendown()
    draw_rectangle(house, 50, 50, "pink")

    house.penup()
    house.goto(50,-25)
    house.pendown()
    draw_rectangle(house, 50, 50, "pink")

    #Draw a tree
    tree = turtle.Turtle()

    #Draw tree trunk
    tree.penup()
    tree.goto(-210, -150)
    tree.pendown()
    draw_rectangle(tree, 40, 150, "brown")

    #Draw tree leaves
    tree.penup()
    tree.goto(-230, -30)
    tree.pendown()
    draw_circle(tree, 40, "green")

    tree.penup()
    tree.goto(-190, 0)
    tree.pendown()
    draw_circle(tree, 40, "green")

    tree.penup()
    tree.goto(-150, -30)
    tree.pendown()
    draw_circle(tree, 40, "green")

    tree.penup()
    tree.goto(-190, -40)
    tree.pendown()
    draw_circle(tree, 40, "green")

    house.hideturtle()
    tree.hideturtle()

    wn.exitonclick()

main()  # Starts the program!

