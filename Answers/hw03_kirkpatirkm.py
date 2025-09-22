#################################################################################
# Author:Scott Kirkpatrick
# Username:Kirkpatrickm
#
# Assignment:Hw_03
# Purpose:To use the turtles to create a house and some decorations.
# Google Doc Link:https://docs.google.com/document/d/14dGwMUBC1r0ZQ34hphIV0dmghsiJ_4dG94F4nQ3bJ-A/edit?tab=t.0 .
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################


import turtle


def build_house(tess):
    """
    it builds the roof and the house
    """
    for i in range(2):
        tess.fd(410)
        tess.left(90)
        tess.fd(300)
        tess.left(90)
    tess.end_fill()
    tess.left(90)
    tess.fd(300)
    tess.color('red')
    tess.begin_fill()
    tess.right(45)
    tess.fd(290)
    tess.rt(90)
    tess.fd(295)
    tess.end_fill()
    tess.hideturtle()



def door(tedd):
    """
    Reaveals tedd and he draws a door.
    """
    tedd.showturtle()
    tedd.teleport(-50,-250)
    tedd.color('brown')
    tedd.begin_fill()
    tedd.left(90)
    for i in range(4):
        tedd.fd(100)
        tedd.rt(90)
    tedd.end_fill()
    tedd.hideturtle()



def sun(sunny):

    sunny.showturtle()
    sunny.teleport(215,100)
    sunny.color('yellow')
    sunny.begin_fill()
    sunny.circle(100)
    sunny.end_fill()
    sunny.hideturtle()

def cool(guy):
#Essentially I'm creating sunglasses on the sun
    guy.showturtle()
    guy.color('black')
    guy.teleport(125,225)
    guy.forward(25)
    guy.left(90)
    guy.forward(25)
    guy.right(90)
    guy.begin_fill()
    for i in range(4):
        guy.fd(50)
        guy.rt(90)
    guy.end_fill()
    guy.forward(50)
    guy.right(90)
    guy.fd(25)
    guy.left(90)
    guy.forward(25)
    guy.left(90)
    guy.forward(25)
    guy.right(90)
    guy.begin_fill()
    for i in range(4):
        guy.fd(50)
        guy.rt(90)
    guy.end_fill()
    guy.forward(50)
    guy.right(90)
    guy.fd(25)
    guy.left(90)
    guy.forward(50)




def main():
    """
    to initiate the turtles and fill the background .
    """
    wn = turtle.Screen()
    tess = turtle.Turtle()
    tedd = turtle.Turtle()
    sunny = turtle.Turtle()
    guy = turtle.Turtle()
    guy.hideturtle()
    tedd.hideturtle()
    sunny.hideturtle()
    guy.speed(8)
    tess.speed(0)
    tedd.speed(0)
    sunny.speed(0)
    turtle.colormode(255)
    wn.bgcolor((173, 216, 230))
    tess.color("white")
    tess.begin_fill()
    tess.teleport(-200,-250)


    build_house(tess)
    door(tedd)
    sun(sunny)
    cool(guy)

    wn.exitonclick()




main()  # Starts the program!