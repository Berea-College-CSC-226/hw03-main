######################################################################
# Author: Susan Coreas
# Username: coreass
#
#Google Doc Link: https://docs.google.com/document/d/1RnWymuMO2-mVgobY4ZoOXwxQDW97hM6K3pYyrGkwTK8/edit?usp=sharing
#
# Assignment: A03: A pair of Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: To draw a complex drawing.
######################################################################
# Acknowledgements:
#
#Scott Heggen & Emily Lovell
#################################################################################

import turtle

def make_moon(tur,size):
    '''
    Draws a moon.

    :param tur: A turtle object
    :param size: Size of sides of moon

    :return:None
    '''
    tur.speed(0) #Makes the turtle fast
    tur.fillcolor("White") #Sets the color of the interior of the moon
    tur.begin_fill() #Starts the filling
    for i in range(20): #Draws the outer circle for the moon
        tur.penup()
        tur.stamp()
        tur.forward(size)
        tur.left(20)
    tur.end_fill()  #Ends the filling

def make_ground(tur):
    '''

    Draws the ground

    :param tur: A turtle object
    :return: None
    '''
    tur.speed(0)
    tur.pendown()
    tur.forward(360) #Draws a line that is the ground
    tur.left(180)
    tur.forward(360)

def make_tree(tur):
    '''

    Draws a tree

    :param tur: A turtle object
    :return: None
    '''

    tur.pendown()
    tur.left(90)  #Makes the tree trunk
    tur.forward(200)
    tur.left(180)
    tur.forward(30)
    tur.left(150) #Makes first branch
    tur.forward(25)
    tur.left(180)
    tur.forward(25)
    tur.left(24)
    tur.forward(30)
    tur.right(150) #Makes second branch
    tur.forward(30)
    tur.left(180)
    tur.forward(30)
    tur.right(20)
    tur.forward(30)
    tur.left(120) #Makes third branch
    tur.forward(70)
    tur.left(180)
    tur.forward(70)
    tur.left(50)
    tur.forward(30)
    tur.right(150) #Makes fourth branch
    tur.forward(70)
    tur.left(180)
    tur.forward(20)
    tur.right(130) #Makes branch inside fourth branch
    tur.forward(20)
    tur.left(180)
    tur.forward(20)
    tur.right(50) #Makes bottom tree trunk
    tur.forward(60)
    tur.right(30)
    tur.forward(72)
    tur.left(90)
    tur.forward(12)
    tur.left(100)
    tur.forward(70)

def make_tombstone(tur):
    '''

    Makes the tombstone

    :param tur: A turtle object
    :return: None
    '''

    tur.speed(0) #Makes the turtle fast
    tur.pendown()
    tur.fillcolor("silver") #Sets color of tombstone
    tur.begin_fill() #Starts filling it
    tur.left(90) #Draws side of tombstone
    tur.forward(30)
    tur.circle(-20,180) #Draws arch of tombstone
    tur.forward(30) #Draws other side of tombstone
    tur.right(90)
    tur.forward(39)
    tur.end_fill() #Ends the filling

def make_text(shape):
    '''

    Makes "R.I.P"

    :param shape: A turtle object
    :return: None
    '''

    shape.color("red") #Sets color of text
    shape.setpos(10,-205) #Sets the position
    shape.write("R.I.P", move=False, align="center", font=("Arial", 10, ("bold", "normal"))) #Makes the style of the text

def make_cross(tur):
    '''

    Draws a cross

    :param tur: A turtle object
    :return:
    '''
    tur.pendown()
    tur.left(90) #Makes first line of cross
    tur.forward(10)
    tur.left(180)
    tur.forward(5)
    tur.left(90) #Makes second line of cross
    tur.forward(5)
    tur.left(180)
    tur.forward(5)
    tur.forward(5)



def main():
    '''

    Draws a cemetery.

    :return: None
    '''
    wn = turtle.Screen()
    wn.bgpic("python_sky.gif") #Sets a picture of the sky as the background

    alex = turtle.Turtle() #Sets tutles that I am going to use in the functions
    alex.shape("circle")
    alex.color("white")
    alex.pensize(25)
    alex.penup()
    alex.sety(150)
    alex.setx(-110)

    coco = turtle.Turtle()
    coco.hideturtle()
    coco.shape("square")
    wn.colormode(255)
    coco.color(0,25,0)
    coco.pensize(25)
    coco.penup()
    coco.sety(-235)
    coco.setx(-180)

    luna = turtle.Turtle()
    luna.hideturtle()
    luna.shape("square")
    luna.color(100,60,20)
    luna.pensize(8)
    luna.penup()
    luna.sety(-220)
    luna.setx(-100)

    dulce = turtle.Turtle()
    dulce.hideturtle()
    dulce.shape("circle")
    dulce.color("silver")
    dulce.pensize(3)
    dulce.penup()
    dulce.sety(-225)
    dulce.setx(-10)

    choco = turtle.Turtle()
    choco.hideturtle()
    choco.penup()

    rosa = turtle.Turtle()
    rosa.hideturtle()
    rosa.pensize(3)
    rosa.pencolor("silver")
    rosa.penup()
    rosa.setpos(9,-172)

    make_moon(alex,8) #Calls the functions that draw the different components of my drawing.

    make_ground(coco)

    make_tree(luna)

    make_tombstone(dulce)

    make_text(choco)

    make_cross(rosa)

    wn.exitonclick()

main()

