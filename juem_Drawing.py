######################################################################################################
#Author: May Jue
#username: juem

#Assignment: a03: A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
######################################################################################################
import turtle

def draw_house(rex): #def for drawing th house
    '''
    Drawing the house and the roof

    :param rex: a turtle
    :return: none
    '''

    rex.fillcolor(100,0,100) #drawing the house body
    rex.begin_fill()
    for i in range(4):

        rex.forward(100)
        rex.left(90)
    rex.end_fill()

    rex.penup()         #changing the pen color and setting the new position for the roof
    rex.color("brown")
    rex.fillcolor("brown")
    rex.setpos(-60,90)
    rex.pendown()

    rex.begin_fill()        #Drawing the trisngle roof
    for i in range(3):
        rex.forward(120)
        rex.left(120)
    rex.end_fill()

def draw_stars(s, x):
    '''
    drawing the stars in the sky

    :param s: the turtle to draw the star
    :param x: the position of the turtle
    :return: none
    '''
    for i in range(1):
        s.penup()           #setting up to draw the stars

        s.setpos(x)
        s.pendown()
        s.begin_fill()
        for i in range(4):      # drawing the stars
            s.forward(20)
            s.right(144)
        s.end_fill()


def moon(m, p):
    '''
    drawing the moon in the sky

    :param m: turtle to draw the moon
    :param p: turtle position
    :return: None
    '''

    m.penup()       #setting up the new position to draw the moon
    m.setpos(p)
    m.pendown()

    m.begin_fill()
    m.circle(45)        #Drawing the moon
    m.end_fill()
    m.color(0,0,80)

def other_stuff(d):
    '''
    draw the door and the road

    :param d: turtle to draw the door and road
    :return: None
    '''
    d.setpos(-10,-5)        #settign up to draw the door
    d.begin_fill()
    for i in range(2):      #Drawing the door
        d.forward(20)
        d.left(90)
        d.forward(40)
        d.left(90)
    d.end_fill()

    d.color("gray")     #setting up to draw the road by changing the colors
    d.begin_fill()
    d.setpos(-50,-320)  #drawing the road
    d.forward(100)
    d.setpos(10,-5)
    d.end_fill()

def main():
    '''
    Make the background and creating turtles
    :return: none
    '''
    wn = turtle.Screen()        #setting up the screen and screen color
    wn.colormode(255)
    wn.bgcolor(0,0,80)

    #creating turtles
    bob = turtle.Turtle()          #setting up turtle to draw the land
    bob.pencolor(0,80,0)
    bob.fillcolor(0,80,0)
    bob.speed(10)
    bob.shape()

    rex = turtle.Turtle()   #creating turtle for the house
    rex.speed(10)
    rex.color(100,0,100)
    rex.shape("blank")

    rex.penup()
    rex.setpos(-50,-5)     #setting rex's position
    rex.pendown()

    star = turtle.Turtle()      #creating turtle for drawing stars
    star.color("yellow")
    star.speed(10)
    star.shape("blank")

    door = turtle.Turtle()      #creating turtle for drawing door and rode
    door.color(100,100,225)
    door.shape("blank")


    #setting distance
    dis = [[-300,90], [-200,250], [-130,150], [95,230], [160,75], [230,190], [270,-25]]
    pos = [[-100,220], [-80,220]]


    #creating the land
    bob.fillcolor(0,80,0)
    bob.begin_fill()
    bob.circle(-400)
    bob.end_fill()


    #function calls
    draw_house(rex)
    for x in dis:
        draw_stars(star, x)
    star.color(225,225,225)
    for p in pos:
        moon(star, p)
    other_stuff(door)


    wn.exitonclick()

main()     #call function to main
