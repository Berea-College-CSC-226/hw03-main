#################################################################################
# Author: Chris Georgiev
# Username: georgievh
#
# Assignment: HW03
# Purpose: Learn version control using git, and practice using functions by drawing a house
# Google Doc Link:
#
#################################################################################
# Acknowledgements:
# learned about default arguments (used in draw_curve() function) [https://www.geeksforgeeks.org/default-arguments-in-python/]
#
#################################################################################


import turtle


def draw_curve(turty, turn_amount, iterations, direction = "right", line_length = 15):
    """
    Draws a curve by drawing a short line, turning a small amount, then repeating for the length of the curve.
    The shorter the line length the smoother the curve, the greater the turning amount the tighter the curve.
    """
    for i in range(iterations):
        turty.fd(line_length)
        if direction == "right": turty.right(turn_amount)
        if direction == "left": turty.left(turn_amount)


def white_circle(turty, radius, forward):
    '''
    Draws a filled-in white circle of the specified radius, along with a spacing distance
    '''
    turty.begin_fill()
    turty.circle(radius)
    turty.fd(forward)
    turty.end_fill()


def draw_background(turty):
    '''
    Draws the background of the picture, that being the sun, cloud, and green lawn/bushes (or maybe distant hills, art is in the eye of the beholder)
    '''
    #start on the left side of the screen
    turty.penup()
    turty.setposition(-320,-40)
    turty.pendown()

    #grass color
    turty.fillcolor("green")
    turty.begin_fill()

    #draw grassy ground
    for i in range(8):
        turty.setheading(90)
        draw_curve(turty, 20, 10)

    turty.setheading(270)
    turty.fd(300)
    turty.right(-90)
    turty.fd(-700)
    turty.setposition(-320,-40)
    turty.end_fill()

    #start in upper right
    turty.penup()
    turty.setposition(200, 200)
    turty.pendown()

    #draw sun
    turty.color("yellow")
    turty.begin_fill()
    turty.circle(40)
    turty.end_fill()

    #start in upper left
    turty.penup()
    turty.setposition(-200, 150)
    turty.pendown()

    #draw cloud
    turty.color("white")

    white_circle(turty, 15, 20)
    white_circle(turty, 20, 30)
    white_circle(turty, 20, 30)
    white_circle(turty, 15, 0)

    turty.begin_fill()
    turty.left(90)
    turty.fd(10)
    turty.left(90)
    turty.fd(88)
    turty.left(90)
    turty.fd(10)
    turty.end_fill()


def draw_square(turty, side):
    '''
    Draws square of specified side length
    '''
    for i in range(4):
        turty.fd(side)
        turty.left(90)


def draw_roof(turty):
    '''
    Draws the roof of the house.
    '''
    # reorient
    turty.penup()
    turty.home()
    turty.setposition(-120, 90)
    turty.pendown()

    #set color
    turty.fillcolor("yellow")
    turty.pencolor("orange")

    #draw roof
    turty.begin_fill()
    for i in range(7):
        pre_jump = 0             #temp var for coords
        turty.left(30)
        turty.fd(19.5)

        #draw peaks of the corrugated roof corrugations.
        pre_jump = turty.pos()   #save current coordinates so return is possible
        turty.setposition(0, 200)
        turty.setposition(pre_jump)
        turty.right(60)
        turty.fd(19.5)

        #draw trough of corrugated roof with smaller pensize, giving an illusion of depth
        turty.pensize(1)
        pre_jump = turty.pos()
        turty.setposition(0, 200)
        turty.setposition(pre_jump)
        turty.pensize(3)

        turty.left(30)

    turty.setposition(0, 200)
    turty.setposition(-120, 90)

    turty.end_fill()


def draw_window(turty):
    '''
    Draws a window.
    '''
    #setting color
    turty.pencolor("blue")
    turty.fillcolor("lightblue")

    #drawing window
    turty.begin_fill()
    draw_square(turty,60)
    turty.end_fill()

    #draw window bar things
    turty.fd(30)
    turty.left(90)
    turty.fd(60)
    turty.fd(-30)
    turty.left(90)
    turty.fd(-30)
    turty.fd(60)

    #return to original position
    turty.left(90)
    turty.fd(30)
    turty.left(90)


def draw_walls(turty):
    '''
    Draws the main body of the house, namely its walls.
    '''
    # reorient
    turty.penup()
    turty.home()
    turty.setposition(-100, -100)
    turty.pendown()

    #start drawing walls
    turty.begin_fill()
    turty.fillcolor("lightgreen")
    turty.pencolor(12,200,29)
    draw_square(turty, 200)
    turty.end_fill()


def draw_door(turty):
    '''
    Draws a door with handles.
    '''
    # reorient
    turty.penup()
    turty.setposition(-35, -100)
    turty.pendown()

    #set colors
    turty.pencolor(105,20,5)
    turty.fillcolor(172, 112, 60)

    #draw door
    turty.begin_fill()
    draw_square(turty,70)
    turty.end_fill()
    turty.fd(35)
    turty.left(90)
    turty.fd(70)

    #draw door handles
    turty.fd(-35)
    turty.penup()
    turty.color("lightgrey")
    turty.left(-90)
    turty.penup()
    turty.fd(4)
    turty.pendown()
    turty.circle(1)
    turty.penup()
    turty.fd(-8)
    turty.pendown()
    turty.circle(1)


def draw_path(turty):
    '''
    Draws the path to the door (or maybe a driveway)
    '''
    turty.penup()
    turty.setposition(-35,-100)

    #set colors
    turty.pencolor(69,69,69)
    turty.fillcolor(100,100,100)

    #draw path
    turty.begin_fill()
    turty.pendown()
    turty.setposition(-300,-400)
    turty.setposition(300, -400)
    turty.setposition(35,-100)
    turty.end_fill()


def main():
    """
    Draws whole house and background.
    """
    #setup code
    chris = turtle.Turtle()
    window = turtle.Screen()
    chris.speed("fastest")
    chris.pensize(3)
    window.colormode(255)

    #set sky color
    window.bgcolor("lightblue")

    #begin drawing
    draw_background(chris)
    draw_walls(chris)

    #drawing windows
    chris.penup()
    chris.setposition(20, 10)
    chris.pendown()
    draw_window(chris)
    #reorient
    chris.penup()
    chris.setposition(-80, 10)
    chris.pendown()
    draw_window(chris)

    #draw rest of house
    draw_roof(chris)
    draw_door(chris)
    draw_path(chris)

    #last thing in main
    turtle.exitonclick()


main()  # Starts the program!