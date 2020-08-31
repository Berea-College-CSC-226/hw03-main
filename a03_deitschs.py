###########################
# Name: Sierra Deitsch
# Username: deitschs
# Assignment: A03 Fully Functional Gitty Psychedelic Robotic Turtles
###########################
# Acknowledgements:
# Tardis from Doctor Who by Stevan Moffat
############################

import turtle
rose = turtle.Turtle()
# c'mon rose, did I mention it goes anywhere in the universe? Let's go

def draw_tardis_outline():
    '''
    this creates the outside outline for my tardis
    :return:
    '''
    for i in range(2):     #this draws our main rectangle... it's bigger on the inside, trust me
        rose.forward(125)
        rose.left(90)
        rose.forward(225)
        rose.left(90)
    rose.penup()
    rose.setpos(15,225)
    rose.left(90)
    rose.pendown()  #this draws top part of tardis
    rose.forward(15)
    rose.right(90)
    rose.forward(95)
    rose.right(90)
    rose.forward(15)
    rose.penup()
    rose.setpos(55,240)    #this will draw the light on top of tardis
    rose.right(180)
    rose.pendown()
    for i in range(2):
        rose.forward(20)
        rose.right(90)
    rose.forward(20)
    rose.penup()

def draw_tardis_features():
    '''
    draws the inside parts of the front of the tardis
    :return: 
    '''
    rose.setpos(10,210)
    rose.pendown()
    for i in range(2):    #draws box that should say police public call box inside
        rose.forward(20)
        rose.left(90)
        rose.forward(105)
        rose.left(90)

def draw_door():
    '''
    draws the doors for the tardis
    :return:
    '''
    for i in range(2):
        rose.forward(40)
        rose.right(90)
        rose.forward(150)
        rose.right(90)

def draw_panes():
    '''
    draws the three panes on the tardis doors
    :return:
    '''
    for i in range(4):
        rose.forward(20)
        rose.right(90)
    rose.left(90)
    rose.penup()
    rose.forward(40)
    rose.pendown()
    rose.right(90)

def police_box():
    '''
    writes police box on the tardis
    :return:
    '''
    rose.setpos(35,190)
    rose.pendown()
    rose.write("POLICE BOX")
    rose.penup()

def bad_wolf():
    '''
    shhhh, wibbly wobbly timey wimey stuff (writes a hidden Bad Wolf)
    '''
    rose.penup()
    rose.hideturtle()
    rose.setpos(65,-1)
    rose.pendown()
    rose.color(175,236,236)
    rose.write("BAD WOLF")

def main():
    '''
    this will call every function to run, causing Rose the turtle to draw the tardis
    :return:
    '''
    wn = turtle.Screen()
    wn.colormode(255)
    wn.bgcolor(176,224,230)
    rose.color(0,0,255)
    rose.pensize(5)
    draw_tardis_outline()
    draw_tardis_features()
    rose.penup()    #moves in place to draw doors
    rose.forward(45)
    rose.left(90)
    rose.forward(7)
    rose.pendown()
    draw_door()
    rose.penup()
    rose.forward(53)
    rose.pendown()
    draw_door()
    rose.penup()
    police_box()
    rose.setpos(26,60)
    rose.pendown()
    for i in range(3):  #draws left panes
        draw_panes()
    rose.penup()
    rose.setpos(80,60)
    rose.pendown()
    for i in range(3):  #draws right panes
        draw_panes()
    bad_wolf()
    wn.exitonclick()

main()