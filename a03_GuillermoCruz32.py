######################################################################
# Author: Guillermo Cruz
# Username: GuillermoCruz32
#
# Assignment: T03: Boustrophedon Turtles
# Purpose: To get more practice using turtle library, and to learn how computers represent colors
######################################################################
# Acknowledgements:
# Original: http://openbookproject.net/thinkcs/python/english3e/hello_little_turtles.html
# Google Doc Link: https://docs.google.com/document/d/1-oSksfApYVTg6nTMdsSBAIEQVH-xe0YlDPra-Ng_edY/edit?usp=sharing
#
# Dr. Jan Pearce - this file is modified from her original work

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
#################################################################################
import turtle


def draw_rectangle(turt):
    """
    This function will draw the square shape of my house
    :param turt: A turtle
    :return: none
    """
    turt.setposition(0,-50)
    turt.color('#00ff22')
    turt.begin_fill()
    for i in range (2):  #This will draw the rectangle for our house, and also fill it in
        turt.forward(120)
        turt.left(90)
        turt.forward(160)
        turt.left(90)
    turt.end_fill()


def make_roof(turt):
    """
    This function will draw the triangle shape of our roof
    :param turt: A turtle
    :return:
    """
    turt.penup()
    turt.setposition(125,110)
    turt.pendown()
    turt.left(120)
    turt.color('#3333FF')
    turt.begin_fill()  #This will draw the triangle shaped roof for our house, and also fill it in
    for i in range(3):
        turt.forward(130)
        turt.left(120)
    turt.end_fill()


def fire_place(turt):
    """
    This function will draw a fire place for the house
    :param turt:
    :return:
    """
    turt.penup()
    turt.setposition(40,190)  #Sets the position to be right above the roof, and draws a quadrilateral shape to make the fire place
    turt.right(30)
    turt.pendown()
    turt.color('#222222')
    turt.begin_fill()
    turt.forward(50)
    turt.left(90)
    turt.forward(30)
    turt.left(90)
    turt.forward(105)
    turt.end_fill()


def fire_smoke(turt,x,y):
    """
    This function will draw the smoke coming out of the fireplace
    :param turt: A turtle object
    :param x: the x coordinate of the window
    :param y: the y coordinate of the window
    :return:
    """
    turt.penup()
    turt.setposition(x,y)
    turt.left(180)
    turt.pensize(10)
    turt.pendown()
    turt.color('grey')
    for i in range (4):  #Draws curvy-ish lines to make it appear smoke it coming out of the fire place
        turt.forward(10)
        turt.left(24)
        turt.forward(10)
        turt.right(48)
    turt.right(96)  #This action makes the turtle face up again after making all of those left and right turns to make
    turt.pensize(1)


def draw_door(turt):
    """
    This function will draw the door to the house
    :param turt: A turtle object
    :return:
    """
    turt.penup()
    turt.setposition(80,-50)
    turt.pendown()
    turt.right(144)  #This action will make the turtle face up again after making all of those left and right turns to make the smoke
    turt.begin_fill()
    for i in range (2):  #This will create a rectangular door for our house, and then fill the shape in
        turt.forward(110)
        turt.left(90)
        turt.forward(40)
        turt.left(90)
    turt.end_fill()
    turt.penup()
    turt.shape('circle')
    turt.setposition(51,5)
    turt.pensize(1)
    for i in range(1): #This will make our tutrle stamp his position while he is a circle, to create a door knob for our door
        turt.color('black')
        turt.pendown()
        turt.stamp()
    turt.penup()


def snow(turt,x,y):
    """
    This function will create a neat design
    :param turt: A turtle object
    :param x: the x coordinate of the window
    :param y: the y coordinate of the window
    :return:
    """
    turt.penup()
    turt.setposition(x,y)
    for i in ['red','blue','purple','yellow','orange','green','red','blue','purple','yellow','orange','green']:  #This will create a circular design, and will change the color of the turtle each time the loop completes for a total of 12 times
        turt.color(i)
        turt.stamp()
        turt.right(30)
        turt.forward(40)
        turt.stamp()
        turt.right(120)
        turt.forward(40)
        turt.stamp()
        turt.left(120)
        turt.forward(40)


def make_text(turt,txt,x,y):
    """
    This function will draw text inside of the design we made
    :param turt: A turtle object
    :param txt: The text we want to display
    :param x: the x coordinate of the window
    :param y: the y coordinate of the window
    :return:
    """
    turt.penup()
    turt.setposition(x,y)
    turt.pendown()
    turt.write(txt, font=("Arial", 35))  #This will allow us to write text on the screen, and sets our font style to Arial, and our font size to 35


def main():

    wn = turtle.Screen()  #Makes a new turtle screen
    alex = turtle.Turtle()  #Names our turtle alex
    wn.bgcolor('lightgreen')  #Sets the color of the window screen to lightgreen

    # Calls the functions to build each part of the house
    draw_rectangle(alex)  #Calls the function to draw a rectangle for out house, using Alex the turtle
    make_roof(alex)  #Calls the function to draw a roof for our house, using Alex the turtle
    fire_place(alex)  #Calls the function to draw a fire place, using Alex the turtle
    fire_smoke(alex,12,245)  #Calls the function to draw smoke coming out of fire place, using Alex the turtle, and making the starting position at (12,245)
    fire_smoke(alex,20,245)  #Calls the function to draw smoke coming out of fire place, using Alex the turtle, and making the starting position at (20, 245)
    fire_smoke(alex,28,245)  #Calls the function to draw smoke coming out of fire place, using Alex the turtle, and making the starting position at (28,245)
    draw_door(alex)  #Calls the function to draw a door for our house, using Alex the turtle
    snow(alex,-270,220)  #Calls the function to make a unique design, and making the starting position at (-270,220)
    make_text(alex,"MTV",-220,130)  #Calls the function to write the text "MTV" inside the design, and making the starting position at (-220,130)
    make_text(alex,"My Cribs",-260,90)  #Calls the function to write the text "My Cribs" inside the design, and making the starting position at (-260,90)

    wn.exitonclick()  #wait for a user to click on screen to end

main() #call main()
