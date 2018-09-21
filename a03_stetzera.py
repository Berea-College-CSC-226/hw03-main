######################################################################
# Author: Heidi Stetzer
# Username: Stetzera
#
# Assignment: A03
# Purpose: Creates a picture using lots of functions.
######################################################################
# Acknowledgements:
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
#################################################################################

import turtle ###Imports the turtle library


def draw_grass(pen, color):
    """
    A function to draw the block of grass at the bottom.

    :param pen: The turtle.
    :param color: Variable for color of grass.
    :return: None (void function)
    """
    pass
    pen.penup()
    pen.setpos(-350, -250)
    pen.pendown()
    pen.pensize(20)
    pen.color(color)
    pen.begin_fill()
    for side in range (2):
        pen.forward(700)
        pen.right(90)
        pen.forward(100)
        pen.right(90)
    pen.end_fill()



def draw_horse(pen, x, y):
    """

    :param pen: Turtle object.
    :param x: Coordinate for starting leg.
    :param y: Coordinate for starting leg.
    :return: None.
    """
    pass
    pen.penup()
    pen.setpos(x, y)
    pen.pendown()
    pen.color("#d2a679")
    pen.pensize(10)

    pen.begin_fill()  #Draws first leg
    for side in range(2):
        pen.forward(30)
        pen.left(90)
        pen.forward(100)
        pen.left(90)
    pen.end_fill()

    pen.penup()  #Draws second leg
    pen.setpos(x+150, y)
    pen.pendown()
    pen.begin_fill()
    for side in range(2):
        pen.forward(30)
        pen.left(90)
        pen.forward(100)
        pen.left(90)
    pen.end_fill()

    pen.penup()  #Draws body
    pen.setpos(x, y+100)
    pen.pendown()
    pen.begin_fill()
    for side in range(2):
        pen.forward(210)
        pen.left(90)
        pen.forward(100)
        pen.left(90)
    pen.end_fill()

    pen.setpos(x + 160, -50)  #Draws neck
    pen.begin_fill()
    for side in range(2):
        pen.forward(50)
        pen.left(90)
        pen.forward(100)
        pen.left(90)
    pen.end_fill()

    pen.setpos(x + 160, 0)
    pen.begin_fill()
    for side in range(2):
        pen.forward(70)
        pen.left(90)
        pen.forward(30)
        pen.left(90)
    pen.end_fill()

    pen.color("#000066")
    pen.pensize(20)
    pen.up()
    pen.setpos(-10, 20)
    pen.stamp()
    pen.setpos(10, 20)
    pen.stamp()



def draw_fence(pen, x, y):

    """
    A function to draw the fence.
    :param pen: The turtle named pen.
    :param x: The beginning x-coordinate of the first fence post.
    :param y:  The beginning y-coordinate of the first fence post.
    :return: None.
    """

    pen.color("#ffffff")
    pen.setpos(x, y)
    for i in range(10):   #Makes the slats of the fence and repeats them so that they fill the whole screen.
        pen.penup()
        pen.forward(100)
        pen.pendown()
        pen.begin_fill()
        for side in range(2): #The rectangular slat.
            pen.forward(35)
            pen.left(90)
            pen.forward(150)
            pen.left(90)
        pen.end_fill()


    pen.penup()
    pen.setpos(-350, -150)
    pen.pendown()
    pen.begin_fill()
    for side in range(2):  #The bar across the top of the fence.
        pen.forward(700)
        pen.right(90)
        pen.forward(15)
        pen.right(90)
    pen.end_fill()

def speech_bubble(pen, bubblex, bubbley):
    pen.pensize(5)
    pen.color("#000066")
    pen.penup()
    pen.setpos(bubblex, bubbley)
    pen.pendown()
    for side in range (2):
        pen.forward (500)
        pen.left(90)
        pen.forward(100)
        pen.left(90)
    pen.forward(500)
    pen.right(120)
    pen.forward(150)
    pen.setpos(bubblex+450, bubbley)

def speech_in_bubble(pen, txt):
    """

    :param pen: Turtle object.
    :param txt: Variable as to what the text says.
    :return: None.
    """

    pen.penup()
    pen.color("#0F00F0")
    pen.setpos(-100, 175)
    pen.pendown()
    pen.write(txt, move=False, align='center', font=("Arial", 30, ("bold", "normal")))


def main():
    """
    Makes a llama, or loose approximation thereof, with a fence, grass and speech-bubble.

    :return: None
    """

    wn = turtle.Screen()        # Set up the window and its attributes
    wn.colormode(255)
    wn.bgcolor("#cce6ff")
    wn.title("Sunny Fields")

    pen = turtle.Turtle()      # Create the pen and sets attributes.
    pen.hideturtle()
    pen.shape('circle')
    pen.speed(100)

    draw_grass(pen, "#4dff88")   #Calls for the functions to draw the various parts of the horse.
    draw_horse(pen, -200, -250)
    draw_fence(pen, -375, -300)
    speech_bubble(pen, -300, 150)
    speech_in_bubble(pen, "I'm a drama-llama!")  #Adds the totally fun totally quirky text. What is this, 2008?

    wn.exitonclick()


main()                          # Calls the main function
