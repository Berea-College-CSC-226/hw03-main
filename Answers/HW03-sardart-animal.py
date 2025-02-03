#################################################################################
# Author: Tafreed
# Username: sardart
#
# Assignment: hw03
# Purpose:
#################################################################################
# Acknowledgements:
#https://www.google.com/search?q=animal+drawing+using+linear+geometry&sca_esv=2621f7b39c394d4e&sxsrf=AHTn8zqDrZ2F47DfYotIfoYEv91Ad_P98Q%3A1738566728932&ei=SGygZ-DQOKSbwbkP0oq1-AE&ved=0ahUKEwjglK_i-aaLAxWkTTABHVJFDR8Q4dUDCBE&uact=5&oq=animal+drawing+using+linear+geometry&gs_lp=Egxnd3Mtd2l6LXNlcnAiJGFuaW1hbCBkcmF3aW5nIHVzaW5nIGxpbmVhciBnZW9tZXRyeTIFECEYoAEyBRAhGKABMgUQIRigATIFECEYoAEyBRAhGKABSLkQULMEWPwJcAF4AJABAJgBaKAB9AOqAQMyLjO4AQPIAQD4AQGYAgagAogEwgIOEAAYgAQYsAMYhgMYigXCAgUQIRirApgDAIgGAZAGApIHAzIuNKAH-h8&sclient=gws-wiz-serp
#
#################################################################################

import turtle

def draw_hexagon(t,sz):        # Make a face shape
    """
    Creates a hexagon

    :param t: a Turtle object
    :param sz: size of a side of a square
    :return: None (void function)
    """
    t.left(30)
    for i in range(6):
        t.forward(150)
        t.left(60)




def draw_mouth():
    """draws the mouth and noes of panda
    :return: None (void function)"""

    s = turtle.Turtle()
    s.pensize(10)
    s.color("black")
    s.penup()
    s.setposition(-30, -100)
    s.pendown()
    s.left(30)
    s.forward(80)
    s.left(150)
    s.forward(70)
    s.left(150)
    s.forward(80)
    s.left(90)
    s.forward(60)
    s.left(60)
    s.forward(80)
    s.penup()
    s.setposition(-30,-100)
    s.pendown()
    s.forward(60)
    s.right(60)
    s.forward(80)

def draw_eyes():
    """ draws the eyes and ears of panda
    :return: None (void function)"""
    r = turtle.Turtle()
    r.color("black")
    r.pensize(10)
    r.penup()
    r.setposition(85, 130)
    r.pendown()
    r.begin_fill()
    r.circle(40)
    r.end_fill()
    r.penup()
    r.setposition(-90,130)
    r.pendown()
    r.begin_fill()
    r.circle(40)
    r.end_fill()

    r.penup()
    r.setposition(55,30)
    r.pendown()
    r.begin_fill()
    r.circle(20)
    r.end_fill()
    r.penup()
    r.setposition(-50,30)
    r.pendown()
    r.begin_fill()
    r.circle(20)
    r.end_fill()




def main():
    wn = turtle.Screen()
    wn.bgcolor('grey')
    t = turtle.Turtle()
    t.pensize(10)
    t.pencolor("black")
    t.penup()
    t.setposition(0,-120)
    t.pendown()
    draw_hexagon(t,500)
    draw_mouth()
    draw_eyes()







    wn.exitonclick()

main()