######################################################################
# Author: Genevieve McWilliams
# Username: mcwilliamsg
#
# Assignment: A03:Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: To draw a house
# Google Doc Link: https://docs.google.com/document/d/1LqK3C93SgweDSm81z-T2KW_Ruwtsl6kmEFbcNStc_cQ/edit#
######################################################################
# Acknowledgements:

#################################################################################
import turtle

sam = turtle.Turtle()

def house():
    sam.penup()
    sam.goto(-150,-150)
    sam.pendown()
    sam.begin_fill()
    for i in range(4):
        sam.fd(250)
        sam.left(90)
    sam.end_fill()
    sam.left(90)
    sam.fd(250)
    draw_roof()
    sam.fd(250)
    sam.right(90)
    sam.fd(100)
    draw_door()
    sam.fd(150)
    sam.pendown()
    draw_window()
    sam.penup()
    sam.right(90)
    sam.fd(100)
    sam.left(90)
    draw_window()

def draw_roof():
    '''Draw roof'''
    sam.fillcolor("black")
    sam.begin_fill()
    sam.right(67)
    sam.fd(136)
    sam.right(46)
    sam.fd(136)
    sam.right(67)
    sam.right(90)
    sam.fd(250)
    sam.end_fill()
    sam.back(250)
    sam.left(90)

def draw_door():
    '''Draws a door'''
    sam.begin_fill()
    sam.color("brown")
    sam.right(90)
    sam.fd(100)
    sam.left(90)
    sam.fd(50)
    sam.left(90)
    sam.fd(100)
    sam.left(90)
    sam.fd(50)
    sam.end_fill()

    # doornob
    sam.color("black")
    sam.penup()
    sam.left(90)
    sam.fd(50)
    sam.left(90)
    sam.fd(10)
    sam.pendown()
    sam.circle(2)
    sam.penup()
    sam.back(10)
    sam.left(90)
    sam.fd(50)
    sam.right(90)
    sam.fd(50)
    sam.right(90)

    sam.penup()
    sam.color('#cb4154')

def draw_window():
    '''Draws a window'''
    sam.pendown()
    sam.color("black")
    sam.begin_fill()
    for i in range(4):
        sam.fd(50)
        sam.left(90)
    sam.fillcolor("white")
    sam.end_fill()
    for i in range(2):
        sam.fd(25)
        sam.left(90)
        sam.fd(50)
        sam.bk(50)
        sam.right(90)
        sam.fd(25)
        sam.left(90)
    for i in range(2):
        sam.fd(50)
        sam.left(90)

    sam.color('#cb4154')



def main():
    '''Main function'''
    wn = turtle.Screen()
    wn.bgcolor("lightblue")
    sam.color('#cb4154')
    house()
    wn.exitonclick()

main()
