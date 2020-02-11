#################################################################################
# Author:  Jacci Boggs
# Username:jacciboggs
#
# Assignment: Something complex like a house animal or person
# Purpose: A03 Assignment
#GoogleDoc Link: https://docs.google.com/document/d/1Hl7kINQyqdksEBDVbi8g9lsvORFqICh2WLn5p8n-LKg/edit?usp=sharing
#################################################################################
# Acknowledgements: Thanks to Dr. Heggen for teaching us all this good stuff.
#
#
#################################################################################
#draw a house with windows, doors and a chimney with fire

import turtle

#make the roof made of bricks
def make_roof(wn, shape):
    """
    Draws a roof made of bricks
    :param wn:
    :param shape:
    :return:
    """
    wn.register_shape("Bricks.gif")     #registers a sh
#draw the body of the house - a rectangle

def draw_square(houseturtle):
    """

    :param houseturtle:
    :return:
    """
    houseturtle.color(50, 168, 82)
    houseturtle.penup()
    houseturtle.goto(-250, -250)
    houseturtle.pendown()
    houseturtle.fillcolor(50, 168, 82)
    for i in range (4):
        houseturtle.forward(300)
        houseturtle.left(90)

#draw the roof of the house - a triangle on top of the rectangle

def draw_roof(houseturtle):
    """
    :param houseturtle:
    :return:
    """
    houseturtle.color(50, 168, 82)
    houseturtle.penup()
    houseturtle.goto(-230, -230)
    houseturtle.pendown()
    houseturtle.left(180)
    houseturtle.forward(400)
    houseturtle.begin_fill()
    for i in range (3):
        houseturtle.right(120)
        houseturtle.forward(200)
    houseturtle.end_fill()
    houseturtle.penup()
    

#draw a chimney - a small rectangle at the top of the triangle

#draw smoke coming out of the chimney


#main
def main():
    """

    :return:
    """
    houseturtle = turtle.Turtle()
    wn = turtle.Screen()
    wn.colormode(255)
    houseturtle.pensize (10)

    draw_square(houseturtle)
    draw_roof(houseturtle)
    #draw_chimney(houseturtle)
    #draw_smoke(houseturtle)

    wn.exitonclick()

main()    