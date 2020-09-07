######################################################################
# Author: Dante Stewart
# Username: stewartd
#
# Assignment: A03: The Psychedelic Turtles
# Purpose: We make a pizza and let the turtle out to CONSUME
#
#Google Doc Link: https://docs.google.com/document/d/1FRP7XIrJwgSZ2RkAU54NKXRRwmjCID5sE_6Mmh4Y0eg/edit?usp=sharing
#
######################################################################

import turtle


def pizza_pie():
    """
    Uses a turtle to draw a circle resembling that moment when the moon hits your eye like a big pizza pie
    :return: none
    """
    paintbrush = turtle.Turtle()                   #establishing attributes
    paintbrush.shape("classic")
    paintbrush.pencolor("orange")
    paintbrush.pensize(25)
    paintbrush.setpos(0, -250)
    paintbrush.speed(0)
    #
    paintbrush.fillcolor("orange")                 #mapping out our methods
    paintbrush.begin_fill()
    paintbrush.pendown()
    paintbrush.circle(250)
    paintbrush.end_fill()
    paintbrush.penup()

def cheese_baby():
    """
    it ain't a pizza without cheese, baby
    :return: none
    """
    paintbrush = turtle.Turtle()           #establishing our painting turtle's attributes
    paintbrush.shape("classic")
    paintbrush.pencolor("yellow")
    paintbrush.pensize(10)
    paintbrush.setpos(0, -240)
    paintbrush.speed(0)
    #
    paintbrush.fillcolor("yellow")         #drawing a circle with turtle methods
    paintbrush.begin_fill()
    paintbrush.pendown()
    paintbrush.circle(240)
    paintbrush.end_fill()
    paintbrush.penup()


def toppings():
    """
    we making pepperonis in this house tonight with another turtle
    :return: none
    """
    paintbrush = turtle.Turtle()                     #setting up our painting turtle's attributes
    paintbrush.shape("classic")
    brown = (0.12, 0.9, 0.45)
    paintbrush.color("brown")
    paintbrush.pensize(25)
    paintbrush.speed(0)
        #
    # a = paintbrush.setpos()
    # b = paintbrush.setpos()
    # c = ... so on, so on
    # positions = [a, b, c]
    #for i in range [positions] loop??????????      # i can't figure out how to make this work :(
        #
    paintbrush.penup()                        #each of these draws a pepperoni at the specified setpos()
    paintbrush.setpos(-100, 110)
    paintbrush.begin_fill()
    paintbrush.circle(50)
    paintbrush.end_fill()
    paintbrush.penup()
    #
    paintbrush.penup()
    paintbrush.setpos(100, 100)
    paintbrush.begin_fill()
    paintbrush.circle(50)
    paintbrush.end_fill()
    paintbrush.penup()
    #
    paintbrush.setpos(-150, -100)
    paintbrush.begin_fill()
    paintbrush.circle(50)
    paintbrush.end_fill()
    paintbrush.penup()
    #
    paintbrush.setpos(150, -100)
    paintbrush.begin_fill()
    paintbrush.circle(50)
    paintbrush.end_fill()
    paintbrush.penup()
    #
    paintbrush.setpos(0, -225)
    paintbrush.begin_fill()
    paintbrush.circle(50)
    paintbrush.end_fill()
    paintbrush.penup()
    #
    paintbrush.setpos(0, -50)
    paintbrush.begin_fill()
    paintbrush.circle(50)
    paintbrush.end_fill()
    paintbrush.penup()


def turtle_munch():
    """
    we letting this big dog out to hunt and THAT's amore
    :return: none
    """
    amore = turtle.Turtle()
    amore.shape("turtle")
    amore.write("NOM NOM NOM NOM NOM", align= ("center"), font=(50))
    amore.color("green")
    amore.shapesize(5)
    #
    amore.penup()
    amore.speed(1)
    amore.circle(100)               #this is what makes the figure 8 pattern...
    amore.circle(-100)              #one circle @100, and the next set at the exact mirror opposite
    amore.ht()
    turtle_munch()


def main():
    #
    wn = turtle.Screen()
    wn.title("Turtle Pizza Eating Simulator")
    gold = (0.255, 0.215, 0.0)
    wn.bgcolor(gold)
    #
    pizza_pie()              #calling each of our functions in proper order so none of them are hidden
    cheese_baby()
    toppings()
    turtle_munch()
    wn.exitonclick()


main()