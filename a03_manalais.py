#################################################################################
# Author: Sama Manalai
# Username:manalais
#
# Assignment: A03
# Purpose: To draw something complex, like a house, animal, or person.
# Google Doc Link: https://docs.google.com/document/d/1AN04zZWxZgyEDke2bhz2lNziQM3opjN-ZGbic-6_P1E/edit#
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################
import turtle


def the_roof(roof):
    """ draw the roof
    """
    roof.penup()
    roof.setpos(-40, 0)
    roof.pensize(5)
    roof.color('#006666')
    roof.pendown()
    roof.color('#006666')
    roof.begin_fill()
    roof.forward(200)
    roof.left(120)
    roof.forward(200)
    roof.left(120)
    roof.forward(200)
    roof.end_fill()


def the_house(house):
    """ draws the body of the house
    """
    house.penup()
    house.setpos(-40, 0)
    house.pensize(5)
    house.color('#003333')
    house.pendown()
    house.color('#003333')
    house.begin_fill()
    for i in range(2):
        house.forward(200)
        house.right(90)
        house.forward(200)
        house.right(90)
    house.end_fill()


def the_window(window1, window2):
    """ draws two circular windows, one to the left and one to the right
    """
    window1.penup()
    window1.setpos(7, -65)
    window1.color('#00CCCC')
    window1.pendown()
    window1.color('#00CCCC')
    window1.begin_fill()
    window1.circle(30)
    window1.end_fill()
    window2.penup()
    window2.setpos(120, -65)
    window2.color('#00CCCC')
    window2.pendown()
    window2.color('#00CCCC')
    window2.begin_fill()
    window2.circle(30)
    window2.end_fill()


def the_door(door):
    """ draws the door
    """
    door.penup()
    door.setpos(28, -88)
    door.color('#606060')
    door.pendown()
    door.color('#606060')
    door.begin_fill()
    for i in range(2):
        door.forward(70)
        door.right(90)
        door.forward(114)
        door.right(90)
    door.end_fill()


def the_moon(moon):
    """ draws the moon to the left of the house
    """
    moon.penup()
    moon.setpos(-150, 100)
    moon.color('#FFFFFF')
    moon.pendown()
    moon.color('#FFFFFF')
    moon.begin_fill()
    moon.circle(60)
    moon.end_fill()


def the_stars(star1, star2, star3, star4, star5, star6):
    """draws six stars that are scattered all over the house
    """
    star1.penup()
    star1.setpos(-90, 250)
    star1.color('#FFFFFF')
    star1.pendown()
    star1.color('#FFFFFF')
    star1.begin_fill()
    for i in range(5):
        star1.forward(30)
        star1.right(144)
    star1.end_fill()
    star2.penup()
    star2.setpos(-20, 200)
    star2.color('#FFFFFF')
    star2.pendown()
    star2.color('#FFFFFF')
    star2.begin_fill()
    for i in range(5):
        star2.forward(30)
        star2.right(144)
    star2.end_fill()
    star3.penup()
    star3.setpos(-60, 100)
    star3.color('#FFFFFF')
    star3.pendown()
    star3.color('#FFFFFF')
    star3.begin_fill()
    for i in range(5):
        star3.forward(30)
        star3.right(144)
    star3.end_fill()
    star4.penup()
    star4.setpos(150, 100)
    star4.color('#FFFFFF')
    star4.pendown()
    star4.color('#FFFFFF')
    star4.begin_fill()
    for i in range(5):
        star4.forward(30)
        star4.right(144)
    star4.end_fill()
    star5.penup()
    star5.setpos(90, 220)
    star5.color('#FFFFFF')
    star5.pendown()
    star5.color('#FFFFFF')
    star5.begin_fill()
    for i in range(5):
        star5.forward(30)
        star5.right(144)
    star5.end_fill()
    star6.penup()
    star6.setpos(250, 200)
    star6.color('#FFFFFF')
    star6.pendown()
    star6.color('#FFFFFF')
    star6.begin_fill()
    for i in range(5):
        star6.forward(30)
        star6.right(144)
    star6.end_fill()


def main():
    """the main function
    """
    wn = turtle.Screen()
    wn.bgcolor('#000000')
    roof = turtle.Turtle()
    house = turtle.Turtle()
    window1 = turtle.Turtle()
    window2 = turtle.Turtle()
    door = turtle.Turtle()
    moon = turtle.Turtle()
    star1 = turtle.Turtle()
    star2 = turtle.Turtle()
    star3 = turtle.Turtle()
    star4 = turtle.Turtle()
    star5 = turtle.Turtle()
    star6 = turtle.Turtle()
    the_roof(roof)
    the_house(house)
    the_window(window1, window2)
    the_door(door)
    the_moon(moon)
    the_stars(star1, star2, star3, star4, star5, star6)
    wn.exitonclick()


main()
