#################################################################################
# Author: Henry Camacho
# Username: Camachoh
#
# Assignment: A03
# Purpose: Draw a fish
# Google Doc Link: https://docs.google.com/document/d/1kbk_Az9m1RqgzW0h4crdURhLN8WtmHXcarHSI_897FU/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
# https://pythonturtle.academy/tutorial-drawing-an-oval-with-python-turtle/
#
#################################################################################


import turtle

# wn = turtle.Screen()
# wn.bgcolor("blue")
#
#
# size = 30


def draw_house(): #####draws the body of the house
    """
    draw body of house
    :return: draws house
    """
    house = turtle.Turtle()
    house.fillcolor("orange")
    # fish.begin_fill()
    for i in range(4):
        house.begin_fill()
        house.fd(100)

        house.left(90)
        house.fd(100)
        house.left(90)
        house.fd(100)
        house.left(90)
        house.fd(100)
        house.end_fill()

def draw_windows():
    """
    draws window
    :return: drawn window
    """
    window = turtle.Turtle()
    window.fillcolor("white")
    ####right window
    for i in range (1):
        window.begin_fill()
        window.fd(25)
        window.left(90)
        window.fd(50)
        window.right(90)
        window.fd(50)
        window.right(90)
        window.fd(50)
        window.right(90)
        window.fd(50)
        window.end_fill()
####Left window
        window.fd(25)
        window.begin_fill()
        window.fd(25)
        window.right(90)
        window.fd(50)
        window.left(90)
        window.fd(50)
        window.left(90)
        window.fd(50)
        window.left(90)
        window.fd(50)
        window.end_fill()

def draw_door():
    """
    draws door
    :return: drawn door
    """""


    door = turtle.Turtle()
    door.fillcolor("white")
    ####right window
    for i in range(1):

         door.right(90)
         door.fd(50)
         door.begin_fill()
         door.left(90)
         door.fd(15)
         door.left(180)
         door.fd(30)
         door.left(90)
         door.fd(50)
         door.left(90)
         door.fd(30)
         door.left(90)
         door.fd(50)

         door.end_fill()
def draw_roof():  ####draws  a red roof
    """
    draw red roof
    :return: redroof
    """
    roof = turtle.Turtle()
    roof.fillcolor("red")

    roof.left(90)
    roof.fd(100)
    roof.begin_fill()
    roof.left(90)
    roof.fd(200)
    roof.right(135)
    roof.fd(200)
    roof.right(45)
    roof.fd(100)
    roof.right(45)
    roof.fd(200)
    roof.right(135)
    roof.fd(100)
    roof.end_fill()








def main():
    wn = turtle.Screen()
    wn.bgcolor("blue")

    size = 30

    draw_house()
    draw_windows()
    draw_door()
    draw_roof()



    wn.exitonclick()
main()

