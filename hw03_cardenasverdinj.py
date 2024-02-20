################################################################################
# Author: Jonathan Cardenas Verdin
# Username: cardenasverdinj
#
# Assignment:HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Draws a checkerboard that is unfair
# Google Doc Link:https://docs.google.com/document/d/17gThgtnci2bNcu_HRuWUme-Kz3chDmeEpRvLUbDW_10/edit
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################
import turtle
def draw_square(x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor("red")
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.end_fill()
def draw_triangle(x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor((0.6, 0.3, 0.0))
    turtle.setheading(60)
    turtle.forward(size)
    turtle.right(120)
    turtle.forward(size)
    turtle.right(120)
    turtle.forward(size)
    turtle.right(120)
    turtle.end_fill()
def draw_circle(x, y, radius):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor("yellow")
    turtle.circle(radius)
    turtle.end_fill()
def main():
    wn = turtle.Screen()
    wn.bgcolor("light blue")
    turtle.speed(0)
    draw_square(-50, -100, 100)
    draw_square(-200, -100, 100)
    draw_square(-350, -100, 100)
    draw_triangle(-50, 0, 100)
    draw_triangle(-200, 0, 100)
    draw_triangle(-350, 0, 100)
    draw_circle(200, 200, 80)
    turtle.hideturtle()
    wn.exitonclick()

main()
