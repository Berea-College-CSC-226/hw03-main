
# Author: Hira Karim
# Username: karimh
#
# Assignment: HW03-Fully Functional Gitty Psychedelic Robotic Turtle
# Purpose: To create a code using functions, and submit a pull request.
# Google Doc Link: https://docs.google.com/document/d/12MLXaEkr6jyzp5jVL2UXoEJTj2VyV12LwCJIk-eW6fs/edit?usp=sharing


import turtle

# Assigning name to the turtle
Heer = turtle.Turtle()


def tyre_1(rad, th, H):
    "rad = radius of the circle"
    "th = thickness of the tyre"
    "Makes the left tyre of the car"

    # Gives black color to the tyre
    H.fillcolor("black")
    H.begin_fill()

    # Attributes of the tyre
    H.pensize(th)
    H.circle(rad)
    H.end_fill()


def tyre_2(rad, th, H):
    "rad = radius of the circle"
    "th = thickness of the tyre"

    H.fillcolor("black")
    H.begin_fill()

    H.pensize(th)
    H.circle(rad)
    H.end_fill()


def lower_body(l, w, H):
    "l = length of the lower rectangular body of car"
    "w = width of the lower rectangular body of car"
    "Makes the lower body of the car which looks like a big rectangle"

    # Colors the lower body blue
    H.fillcolor("blue")
    H.begin_fill()

    # Gives movement directions to the turtle
    H.left(180)
    H.forward(l)
    H.right(90)
    H.forward(w)
    H.right(90)
    H.forward(l)
    H.right(90)
    H.forward(w)
    H.end_fill()


def upper_body(ul,uw, H):
    "ul = length of the upper rectangular body"
    "uw = width of the upper rectangular body"

    H.fillcolor("grey")
    H.begin_fill()

    H.left(180)
    H.forward(ul)
    H.right(90)
    H.forward(uw)
    H.right(90)
    H.forward(ul)
    H.right(90)
    H.forward(uw)
    H.end_fill()


def main ():
    # Creates method for the screen
    wn = turtle.Screen()
    wn.bgpic("chitral-valley.gif")     # Adds a background picture

    wn.colormode(255)
    wn.bgcolor("lightblue")
    Heer.speed(0)

    # Moves the turtle head from the center to the porper starting place
    Heer.penup()
    Heer.goto(-150, -200)
    Heer.pendown()

    # call functions
    tyre_1(50, 5, Heer)   # calls function 1 (making tyre 1)

    Heer.penup()
    Heer.goto(150, -200)
    Heer.pendown()

    tyre_2(50,5, Heer)    # calls function 2 (making tyre 2)

    Heer.penup()
    Heer.goto(300, -100)
    Heer.pendown()

    lower_body(600,130, Heer)     # call function 3 (making the lower body of car)

    Heer.setheading(180)
    Heer.penup()
    Heer.goto(-180,180)
    Heer.pendown()

    upper_body(350,150, Heer)        # calls function 4 (making the upper body of the car)

    Heer.penup()
    Heer.goto(0,60 )
    Heer.pendown()

    Heer.write("Hira's flying car!", align="center", font=("Verdana", 18, "normal"))

    wn.exitonclick()


main()
