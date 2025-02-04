

#################################################################################
# Author: Hope Michael
# Username: michaelh
#
# Assignment: HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Draw a house with a tree next to it
# Google Doc Link: https://docs.google.com/document/d/1lhv3-v5w_d1k4s5Q-C-Qu92dv-KYypOBRtJEx8BTQ8A/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
# Sami (Partner)
#
#################################################################################


import turtle


def make_turtle(size, color,shape):
    """
    makes a turtle
    :param size: size of the turtle
    :param color: color of the turtle
    :param shape: shape of the turtle
    """
    t = turtle.Turtle()
    t.hideturtle()
    t.color(color)
    t.shape(shape)
    t.pensize(size)
    t.speed(0)
    return t

def setpos(turtle, x, y):
    '''
    set turtle object position
    :param turtle: turtle object
    :param x: x position
    :param y: y position
    '''
    turtle.penup()
    turtle.setpos(x, y)
    turtle.pendown()

def draw_rectangle(turtle,filcol,width,height):
    '''
    draws a rectangle
    :param turtle: turtle object
    :param filcol: color of the rectangle
    :param width: width of the rectangle
    :param height: height of the rectangle
    '''
    turtle.setheading(270)
    turtle.fillcolor(filcol)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(height)
        turtle.right(90)
        turtle.forward(width)
        turtle.right(90)
    turtle.end_fill()
    return turtle

def draw_tree(turtle,filcol):
    """
    draws tree head
    :param turtle: turtle object
    :param filcol: color of the tree
    """
    turtle.fillcolor(filcol)
    turtle.begin_fill()
    for i in range(6):
        turtle.circle(80,140,30)
        turtle.left(-80)
    turtle.end_fill()

def draw_trapezoid(turtle,filcol):
    '''
    draws a trapezoid
    :param turtle: turtle object
    :param filcol: color of the trapezoid
    '''
    turtle.fillcolor(filcol)
    turtle.begin_fill()
    turtle.forward(350)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(60)
    turtle.forward(250)
    turtle.left(60)
    turtle.forward(100)
    turtle.end_fill()

def main():
    """
    creates screen and draws house and tree
    """
    wn = turtle.Screen()
    wn.bgcolor("lightblue")
    wn.setup(width=1000, height=700)

    #call make_turtle function to create turtle named Sami
    sami = make_turtle(size=10, color="darkgreen", shape="classic")

    #call make_turtle function to create turtle called hope
    hope = make_turtle(size=10, color='#4B2E08', shape="classic")

    # call make_turtle function to create turtle called faith
    faith = make_turtle(size=5, color='#870A59', shape="classic")

    # call make_turtle function to create turtle called michael
    michael = make_turtle(size=5, color='#390325', shape="classic")

    # call make_turtle function to create turtle called ground
    ground = make_turtle(size=10, color='black', shape="square")

    #set position of sami
    setpos(sami,-210,0)

    #set position of hope
    setpos(hope,-250,0)

    # set position of faith
    setpos(faith,300,0)

    # set position of michael
    setpos(michael,0,0)

    #set position of ground
    setpos(ground,500,-260)

    # call draw_rectangle function to draw ground
    draw_rectangle(ground, '#585050', 1100, 100)

    # call draw_rectangle function to draw tree trunk
    draw_rectangle(hope, '#69400B',100,250)

    #call draw_tree function to create tree top
    draw_tree(sami,'green')

    #calls draw_rectangle function to draw base of house
    draw_rectangle(faith, '#DA088D',250,250)

    #call draw_trapezoid function to draw roof of house
    draw_trapezoid(michael,'#680644')

    wn.exitonclick()

main()  # Starts the program!