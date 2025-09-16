#################################################################################
# Author: Stephen Aaron Robinson
# Username: robinsons3
#
# Assignment: HW03
# Purpose: Draws Dog
# Google Doc Link:
#
#################################################################################

import turtle
t = turtle.Turtle()
t.speed(0)
wn = t.getscreen()
t.hideturtle()

def semicircle(dir):
    #Makes a semi-circle for use in other functions like leg()
    for i in range(36):
        t.forward(1)
        if dir == 'left':
            t.left(5)
        elif dir == 'right':
            t.right(5)
    pass
    # ....


def leg(length, dir):
    #Draws leg of dog
    t.forward(length)
    semicircle(dir)
    t.forward(length)


def main():
    """
    Docstring for main. Should describe the main functionality of this file.
    """
    #First pair of legs
    t.right(90)
    leg(20, "right")
    t.right(180)
    leg(20, "right")
    t.forward(1)
    t.left(90)
    t.forward(-23)

    #Second pair of legs
    t.forward(45)
    t.left(90)
    leg(20, "right")
    t.right(180)
    leg(20, "right")
    t.forward(1)
    t.left(90)
    t.forward(-23)
    t.forward(23)

    #Left side of body
    t.right(90)
    t.forward(45)
    t.left(90)

    #Head
    for i in range(72):
        t.forward(2)
        t.right(5)
    for i in range(25):
        t.forward(2)
        t.right(5)
    t.left(45)
    t.forward(25)
    t.right(135)
    t.forward(25)
    t.left(45)
    for i in range(5):
        t.forward(2)
        t.right(5)
    t.left(45)
    t.forward(25)
    t.right(135)
    t.forward(27)
    t.left(45)

    #Back to start
    t.penup()
    t.setpos(0, 0)
    t.left(150)

    #Right Body + Tail
    t.pendown()
    t.forward(30)
    t.right(90)
    leg(30,"left")

    #Top of body
    t.forward(98)
    t.penup()

    #Mouth
    t.right(45)
    t.fd(10)
    t.pendown()
    for i in range(2):
        t.left(90)
        t.fd(10)
        t.right(90)
        t.fd(10)
    t.penup()

    #Eye 1
    t.right(45)
    t.forward(5)
    t.begin_fill()
    t.pendown()
    for i in range(6):
        t.forward(5)
        t.right(60)
    t.end_fill()
    t.penup()

    #Eye 2
    t.right(90)
    t.fd(20)
    t.left(90)
    t.pendown()
    t.begin_fill()
    for i in range(6):
        t.forward(5)
        t.right(60)
    t.end_fill()



    wn.exitonclick()


main()  # Starts the program!