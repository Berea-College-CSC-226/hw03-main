#################################################################################
# Author: Tyler Barnes
# Username: tylerbarnes70
# Assignment: A03 A Pair of Fully Functional Gitty Psychedellic Robotic Turtles
# Purpose: The purpose of this piece was to make a drawing expressing my knowledge of functions and to learn how to
# upload my work to Github
# Google Doc Link: https://docs.google.com/document/d/14x1obxTxnOAusPypyGGnFPovBs_ScAmhieBzGT052TQ/edit?usp=sharing
#################################################################################
# Acknowledgements: I wrote all of this. I used the knowledge that was given to me by professor Scott Heggen.
#################################################################################
import turtle
import random
import time


def setup(adrian, leslie, patience, tyler):
    #This is quite the handfull, but it is necessary to creating the house shape that I ended up with.
    adrian.penup()
    adrian.right(90)
    adrian.forward(30)
    adrian.pendown()
    adrian.right(90)
    patience.penup()
    patience.forward(30)
    patience.right(180)
    patience.forward(90)
    patience.right(-270)
    patience.pendown()
    leslie.penup()
    leslie.right(90)
    leslie.forward(30)
    leslie.right(90)
    leslie.forward(120)
    leslie.right(90)
    leslie.pendown()
    tyler.penup()
    tyler.right(90)
    tyler.forward(40)
    tyler.right(90)
    tyler.forward(683)
    tyler.right(180)
    tyler.pendown()
    tyler.pencolor(0,140,0)
    tyler.pensize(20)



def draw_barn(adrian):
    ### Makes adrian.turtle draw both the rectangle and the roof and colors the both of them
    '''

       :param turtle:  this will be the turtle that needs to draw the house
       :return:
       '''
    adrian.begin_fill()
    for i in range(2):
        adrian.forward(210)
        adrian.right(90)
        adrian.forward(100)
        adrian.right(90)
    adrian.color(125,0,0)
    adrian.end_fill()
    adrian.color(0,0,0)
    adrian.penup()
    adrian.forward(210)
    adrian.right(90)
    adrian.forward(100)
    adrian.right(45)
    adrian.pendown()
    adrian.begin_fill()
    adrian.forward(150)
    adrian.right(90)
    adrian.forward(150)
    adrian.right(135)
    adrian.forward(210)
    adrian.end_fill()





def draw_windows(patience):
    #makes patience.turtle draw both of the windows and it colors bot of them a yellow colors
    patience.begin_fill()
    patience.forward(45)
    patience.right(90)
    patience.forward(25)
    patience.right(90)
    patience.forward(45)
    patience.right(90)
    patience.forward(25)
    patience.color(218,165,32)
    patience.end_fill()
    patience.penup()
    patience.color(0,0,0)
    patience.forward(90)
    patience.pendown()
    patience.begin_fill()
    patience.right(90)
    patience.forward(45)
    patience.left(90)
    patience.forward(25)
    patience.left(90)
    patience.forward(45)
    patience.left(90)
    patience.forward(25)
    patience.color(218,165,32)
    patience.end_fill()

def draw_door(leslie):
    #This function was designed to draw a door and change its color to a shade of brown
    leslie.begin_fill()
    leslie.forward(60)
    leslie.right(90)
    leslie.forward(30)
    leslie.right(90)
    leslie.forward(60)
    leslie.color(139,69,19)
    leslie.end_fill()

def draw_grass(tyler):
    # This is the function that I created to make some boustrophedon style grass.
    for i in range(10):
        tyler.forward(1366)
        tyler.right(90)
        tyler.forward(20)
        tyler.right(90)
        tyler.forward(1366)
        tyler.left(90)
        tyler.forward(20)
        tyler.left(90)


def scatter(patience,adrian,tyler,leslie):
    #This function will make the turtles scatter off the screen after all things are drawn
    patience.penup()
    adrian.penup()
    leslie.penup()
    leslie.forward(300)
    patience.forward(1366)
    adrian.forward(1366)
















def main():
    #This is the function that will call all of the other functions when a call is made to it.
    wn = turtle.Screen()
    wn.colormode(255)
    tyler = turtle.Turtle()
    leslie = turtle.Turtle()
    patience = turtle.Turtle()
    adrian = turtle.Turtle()
    wn.bgcolor(random.randint(0,0), random.randint(130,140), random.randint(200,255))
    setup(adrian, leslie, patience, tyler)
    draw_barn(adrian)
    draw_windows(patience)
    draw_door(leslie)
    draw_grass(tyler)
    scatter(patience,adrian,tyler,leslie)
    wn.mainloop()
main()


