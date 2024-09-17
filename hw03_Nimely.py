#################################################################################
# Author: Joyce Nimely
# Username:Nimely
#
# Assignment:Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose:
# Google Doc Link:https://docs.google.com/document/d/1e2HxfEvyB-SdWBs9_G7ZBRoc6QCUzZAmlhiQFXjMTxE/edit

#################################################################################
# Acknowledgements:
#
#
#################################################################################


import turtle

#define function to draw background
def  draw_background():
    turtle.bgcolor("sky blue")

def draw_house():
    turtle.penup()
    turtle.pensize(4)
    turtle.goto(-50,-50) #move turtle to a starting position
    turtle.pendown()
    turtle.color('brown')
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
        turtle.end_fill()

    # Draw the roof on top of  the house
    turtle.penup()
    turtle.pensize(5)
    turtle.goto(-50,45)
    turtle.pendown()
    turtle.bgcolor('sky blue')
    turtle.color('red')
    turtle.begin_fill()
    turtle.left(45)
    turtle.forward(70)
    turtle.right(90)
    turtle.forward(70)
    turtle.left(135)
    turtle.forward(100)

def draw_flower():
    """Draws a flower on the side of the house."""
    joyce = turtle.Turtle()
    nimely = turtle.Turtle()

    joyce.color('yellow')
    joyce.speed(25)
    joyce.pensize(3)
    nimely.color('green')
    nimely.speed(15)
    nimely.pensize(10)

    # Draw flower petals
    joyce.penup()
    joyce.goto(-150, -50)  # Adjusted position to the side of the house
    joyce.pendown()
    for _ in range(50):
        joyce.circle(50, 60)
        joyce.left(120)
        joyce.circle(50, 60)
        joyce.left(160)
        joyce.right(50)

    # Draw the stem
    nimely.penup()
    nimely.goto(-150, -100)  # Adjusted position for the stem
    nimely.pendown()
    nimely.right(90)
    nimely.forward(100)

def main():
    turtle.speed('fastest')
    draw_background()
    draw_house()
    draw_flower()

main()





