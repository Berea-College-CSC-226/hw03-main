###############################################
# Name: Ben Maynard
# Username: maynardb

# assignment: A03 A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
# google doc link:https://docs.google.com/document/d/1KhrAcX_s6xYsGnLjPLaGLGwKJPQA00j1x-yZnrc9Mcg/edit?usp=sharing
###############################################

import turtle


def floating_house(x=-50, y=-40):
    """
    Draws a little house with balloons

    :return: none
    """
    home = turtle.Turtle()                  # create my house turtle
    home.penup()
    home.setpos(x, y)
    home.pendown()
    home.pensize(10)
    home.color("red")                       # set color schemes
    home.fillcolor("yellow")
    home.begin_fill()
    for roof in range(3):
        home.forward(100)                   # create the roof
        home.left(120)

    home.right(90)

    for box in range(4):
        home.forward(100)                   # create my box of a home
        home.left(90)
    home.end_fill()

    balloon = turtle.Turtle()               # create my balloon turtle
    balloon.shape("circle")
    balloon.penup()
    balloon.setpos(x + 50, y + 90)          # the position at the top of the house
    balloon.pendown()
    balloon.left(90)
    balloon.hideturtle()                    # hide my turtle
    for bunch in (x, x, x+20):
        balloon.forward(100)
        balloon.pensize(50)                 # Create my bloons
        balloon.color("green")
        balloon.stamp()
        balloon.pensize(1)
        balloon.color("black")
        balloon.penup()
        balloon.setpos(x+50, y+90)
        balloon.pendown()
        balloon.left(20)


def main():
    """
    all the main code and calling of my function
    :return:
    """
    wn = turtle.Screen()
    wn.colormode(255)                           # window screen and color
    wn.bgcolor(94, 209, 255)

    floating_house()

    wn.exitonclick()


main()
