####################################################################################
# Author: Kylea Hughes
# Username: hughesk2
# Assignment: A03:Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Use multiple functions to create something. In this case, a sandcastle
######################################################################

import turtle  # allows us to use the turtles library

#Going to be creating a sandcastle

def draw_first_base(shape):
    """
    The first base of the sandcastle
    :param shape: a Turtle object
    """
    shape.penup()
    shape.setpos(-200, -30)
    shape.color('black', 'moccasin')        #This is pencolor and fillcolor
    shape.pendown()
    shape.pensize(2)                        #Outlining the shape
    shape.begin_fill()
    shape.speed(8)
    for side in range(2):
        shape.forward(400)
        shape.right(90)
        shape.forward(140)
        shape.right(90)
    shape.end_fill()
    shape.penup()


def draw_second_base(shape):
    """
    Second base of the sand castle
    :param shape: turtle object
    :return:
    """
    shape.setpos(-125, 70)
    shape.color('black', 'moccasin')               #This is pencolor and fillcolor
    shape.pendown()
    shape.pensize(2)                               #Outlining the shape
    shape.begin_fill()
    shape.speed(8)
    for side in range(2):
        shape.forward(250)
        shape.right(90)
        shape.forward(100)
        shape.right(90)
    shape.end_fill()
    shape.penup()


def draw_third_base(shape):
    """
    Third base of the sandcastle
    :param shape: turtle object
    :return:
    """
    shape.setpos(-50, 180)
    shape.color("black", "moccasin")                #This is pencolor and fillcolor
    shape.pendown()
    shape.pensize(2)                                #Outlining the shape
    shape.begin_fill()
    shape.speed(8)
    for side in range(2):
        shape.forward(100)
        shape.right(90)
        shape.forward(110)
        shape.right(90)
    shape.end_fill()
    shape.penup()

# Creating towers on the side of the sandcastle

def base_one(shape):
    """
    Tower One
    :param shape: turtle object
    :return:
    """
    shape.setpos(-200, 10)
    shape.color("black", "#DEB887")            #This is pencolor and fillcolor
    shape.pendown()
    shape.pensize(2)                           #Outlining the shape
    shape.begin_fill()
    shape.speed(8)
    for side in range(2):
        shape.forward(95)
        shape.right(90)
        shape.forward(180)
        shape.right(90)
    shape.end_fill()
    shape.penup()



def base_two(shape):
    """
    Tower Two
    :param shape: turtle object
    :return:
    """
    shape.setpos(110, 10)
    shape.color("black", "#DEB887")           #This is pencolor and fillcolor
    shape.pensize(2)                          #Outlining the shape
    shape.pendown()
    shape.begin_fill()
    shape.speed(8)
    for side in range(2):
        shape.forward(95)
        shape.right(90)
        shape.forward(180)
        shape.right(90)
    shape.end_fill()
    shape.penup()

def draw_merlon_one(shape, a, b):
    """
    Creating Merlons for Tower Two
    :param shape: turtle object
    :param a: coordinates for merlon #1
    :param b: coordinates for merlon #2
    """
    shape.penup()
    shape.setpos(a, b)                        #Can be found in main function
    shape.pendown()
    shape.color('black', '#DEB887')           #This is pencolor and fillcolor
    shape.pensize(2)                          #Outlining the shape
    shape.pendown()
    shape.begin_fill()
    for side in range(6):
        shape.forward(30)
        shape.right(90)
        shape.forward(30)
        shape.right(90)
    shape.end_fill()

def draw_merlon_two(shape, c, d):
    """
    Creating merlons for Tower One
    :param shape: turtle object
    :param c: coordinates for merlon #1
    :param d: coordinates for merlon #2
    """
    shape.penup()
    shape.setpos(c, d)                        #Can be found in main function
    shape.pendown()
    shape.color('black','#DEB887')            #This is pencolor and fillcolor
    shape.pensize(2)                          #Outlining the shape
    shape.begin_fill()
    for side in range(6):
        shape.forward(30)
        shape.right(90)
        shape.forward(30)
        shape.right(90)
    shape.end_fill()

def draw_merlon_three(shape, e ,f,):
    """
    Creating merlons for Base 2
    :param shape: turtle object
    :param e: coordinates for merlon #1
    :param f: coordinates for merlon #2
    :return:
    """
    shape.penup()
    shape.setpos(e, f, )                      #Can be found in main function
    shape.pendown()
    shape.color('black', 'moccasin')          #This is pencolor and fillcolor
    shape.pensize(2)                          #Outlining the shape
    shape.begin_fill()
    for side in range(6):
        shape.forward(30)
        shape.right(90)
        shape.forward(30)
        shape.right(90)
    shape.end_fill()

def draw_merlon_four(shape, g, h):
    """
    Creating merlons for Base 3
    :param shape: turtle object
    :param g: coordinates for merlon #1
    :param h: coordinates for merlon #2
    :return:
    """
    shape.penup()
    shape.setpos(g, h)                        #Can be found in main function
    shape.pendown()
    shape.color('black', 'moccasin')          #This is pencolor and fillcolor
    shape.pensize(2)                          #Outlining the shape
    shape.begin_fill()
    for side in range(6):
        shape.forward(30)
        shape.right(90)
        shape.forward(30)
        shape.right(90)
    shape.end_fill()



def draw_hole(shape):
    """
    Creating the door for the sandcastle
    :param shape: a Turtle object

    """
    shape.penup()
    shape.setpos(-15, -90)
    shape.pendown()
    shape.color('black')
    shape.begin_fill()
    for side in range(2):
        shape.forward(40)
        shape.right(90)
        shape.forward(80)
        shape.right(90)
    shape.end_fill()
    shape.penup()

def draw_second_hole(shape):
    """
    Creating a window for the third base
    :param shape: turtle object
    :return:
    """
    shape.setpos(-10, 160)
    shape.pendown()
    shape.color('black')
    shape.begin_fill()
    for side in range(2):
        shape.forward(20)
        shape.right(90)
        shape.forward(60)
        shape.right(90)
    shape.end_fill()
    shape.penup()

def draw_starfish(shape):
    """
    Creating a little starfish
    :param shape: turtle object
    :return:
    """
    shape.setpos(50,-130)
    shape.color("orange")
    shape.pendown()
    shape.begin_fill()
    for side in range(5):
        shape.forward(50)
        shape.right(144)
    shape.end_fill()




def main():
    """
    main function calling all of the other functions
    """

    turtle.colormode(255)  # change color modes

    wn = turtle.Screen()  # Makes a new turtle screen
    wn.bgcolor("#008087")
    shape = turtle.Turtle()
    shape.hideturtle()



    draw_first_base(shape)
    draw_second_base(shape)
    draw_third_base(shape)
    base_one(shape)
    base_two(shape)
    draw_merlon_one(shape, 110, 40)
    draw_merlon_one(shape, 174, 40)
    draw_merlon_two(shape, -136, 40)
    draw_merlon_two(shape, -200, 40)
    draw_merlon_three(shape, 95, 100)
    draw_merlon_three(shape, -125, 100)
    draw_merlon_four(shape, -50, 210)
    draw_merlon_four(shape, 20, 210)
    draw_hole(shape)
    draw_second_hole(shape)
    draw_starfish(shape)



    wn.exitonclick()  # wait for a user click on the canvas


main()  # call main()
