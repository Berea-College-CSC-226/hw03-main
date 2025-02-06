

#################################################################################
# Author: Cade Allen
# Username: allenc2
#
# Assignment: hwo3
# Purpose: Understand turtle
# Google Doc Link: https://docs.google.com/document/d/1N0XwnuqSnXDgXACy2mfIxjvdEtDLY_Oj65v_rSDfHEk/edit?tab=t.0
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################




import turtle


def ground():
    red = turtle.Turtle()
    red.pensize(50)
    red.color("skyblue")
    red.speed(50)
    red.setpos(-250, -250)
    red.color("green")
    red.shape("square")
    red.forward(500)
    red.left(90)
    red.left(90)
    red.forward(500)
    red.right(90)
    red.right(90)
    red.forward(500)




def house():
    thouse = turtle.Turtle()
    thouse.pencolor("red")
    thouse.pensize(5)
    thouse.forward(250)
    thouse.right(90)
    thouse.forward(220)
    thouse.right(90)
    thouse.forward(500)
    thouse.right(90)
    thouse.forward(220)
    thouse.right(90)
    thouse.forward(250)
    thouse.color("brown")
    thouse.setpos(-5, -250)


def roof():
    troof = turtle.Turtle()
    troof.pencolor("red")
    troof.pensize(5)
    troof.setpos(-250, 0)
    troof.setpos(0, 250)
    troof.setpos(250, 0)



def main():
    wn = turtle.Screen()
    wn.bgcolor("skyblue")
    ground()
    house()
    roof()
    wn.exitonclick()

main()





