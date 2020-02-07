######################################################################
# Author: Maya Rosener          ****** TODO: CHANGE THIS!! ******
# username: rosenerm            ****** TODO: CHANGE THIS!! *****
#
# Purpose: Designed to
# google doc link: https://docs.google.com/document/d/1av0ghPojqKQlRCck1p-s1Gq7s17fXfmKDOB5s4CZFnU/edit?usp=sharing
######################################################################
import turtle                           # allows us to use the turtles library

wn = turtle.Screen()                    # creates a graphics window




def draw_square(square_turtle):
    '''

    :param square_turtle: square turtle object
    :return: None (void function)
    '''
    # draws the square structure of the house

    for i in range(4):
        square_turtle.forward(300)
        square_turtle.right(90)




def draw_roof(square_turtle):
    '''

    :param square_turtle: square turtle object
    :return: None (void function)
    '''
    # draws the roof structure of the house

    square_turtle.left(45)
    square_turtle.forward(215)
    square_turtle.right(90)
    square_turtle.forward(215)



def draw_door(square_turtle):
    '''

    :param square_turtle: square turtle object
    :return: None (void function)
    '''
    # draws the structure of the door of the house

    for i in range(3):
        square_turtle.forward(100)
        square_turtle.right(90)




def draw_window(square_turtle):
    '''

    :param square_turtle: square turtle object
    :return: None (void function)
    '''
    # draws structure of window

    for i in range(4):
        square_turtle.forward(75)
        square_turtle.left(90)



def draw_panel(square_turtle):
    '''

    :param square_turtle: the square turtle object
    :return: None (void function)
    '''
    # draws panel inside of window

    for i in range(4):
        square_turtle.forward(37.5)
        square_turtle.left(90)
        square_turtle.forward(37.5)
        square_turtle.left(180)





def main():
    '''

    :return: None (void function)
    '''

    # defines the turtle and its attributes

    square_turtle = turtle.Turtle()
    wn.bgcolor("blue")
    square_turtle.penup()
    square_turtle.goto(-150, 150)
    square_turtle.pendown()
    square_turtle.pencolor("black")
    square_turtle.pensize(20)
    draw_square(square_turtle)    # function call to draw_square(square_turtle)


    square_turtle.penup()
    square_turtle.goto(-150, 150)
    square_turtle.pencolor("yellow")
    square_turtle.pendown()
    draw_roof(square_turtle)        # function call to draw_roof(square_turtle)

    square_turtle.penup()
    square_turtle.goto(-75, -150)
    square_turtle.left(135)
    square_turtle.pendown()
    draw_door(square_turtle)        # function call to draw_door(square_turtle)


    square_turtle.penup()
    square_turtle.goto(-125, 75)
    square_turtle.left(90)
    square_turtle.pendown()
    draw_window(square_turtle)       # function call to draw_window(square_turtle)

    square_turtle.penup()
    square_turtle.goto(50, 75)
    square_turtle.pendown()
    draw_window(square_turtle)      # function call to draw_window(square_turtle)

    square_turtle.penup()
    square_turtle.goto(-90, 75)
    square_turtle.pendown()
    draw_panel(square_turtle)       # function call to draw_panel(square_turtle

    square_turtle.penup()
    square_turtle.goto(90, 75)
    square_turtle.pendown()
    draw_panel(square_turtle)       # function call to draw_panel(square_turtle)




main()
wn.exitonclick()                    # exits screen when screen is clicked
