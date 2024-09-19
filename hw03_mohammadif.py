# Author: Feda Mohammadi
# Username: mohammadif
#Description: This program is intended to draw a car with a man on top of it using turtle. I want to acknowledge that I wrote the initial code for this program but asked ChatGPT to debug it and find the errors with the code.
# Google Doc Link: https://docs.google.com/document/d/1qTWr4piK7tfv3tEWBzQmfMGjncuCZ-eiIB3OlwvXbfw/edit?usp=sharing

import turtle

def draw_car_body():
    turtle.colormode(255)
    turtle.fillcolor(0, 130, 130)
    turtle.begin_fill()

    turtle.forward(200)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)

    turtle.end_fill()

def draw_wheels():
    turtle.colormode(255)

    turtle.penup()
    turtle.goto(-75, -50)
    turtle.pendown()
    turtle.fillcolor(0, 0, 0)
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(75, -50)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()

def draw_windows():
    turtle.colormode(255)

    turtle.penup()
    turtle.goto(25, 25)
    turtle.pendown()
    turtle.fillcolor(255, 255, 255)
    turtle.begin_fill()

    for _ in range(2):
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(25)
        turtle.left(90)

    turtle.end_fill()

    turtle.penup()
    turtle.goto(-75, 25)
    turtle.pendown()
    turtle.begin_fill()

    for _ in range(2):
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(25)
        turtle.left(90)

    turtle.end_fill()

def draw_a_man():
    turtle.penup()
    turtle.goto(0, 80)
    turtle.pendown()

    turtle.penup()
    turtle.goto(0, 100)
    turtle.pendown()
    turtle.fillcolor("peachpuff")
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(0, 90)
    turtle.pendown()
    turtle.pensize(2)
    turtle.goto(0, 70)

    turtle.penup()
    turtle.goto(-10, 85)
    turtle.pendown()
    turtle.goto(10, 85)

    turtle.penup()
    turtle.goto(0, 85)
    turtle.pendown()
    turtle.goto(-10, 75)

    turtle.penup()
    turtle.goto(0, 70)
    turtle.pendown()
    turtle.goto(-10, 50)

    turtle.penup()
    turtle.goto(0, 70)
    turtle.pendown()
    turtle.goto(10, 50)

    turtle.penup()
    turtle.goto(-10, 50)
    turtle.pendown()
    turtle.goto(-10, 45)

    turtle.penup()
    turtle.goto(10, 50)
    turtle.pendown()
    turtle.goto(10, 45)

def main():
    wn = turtle.Screen()
    wn.bgcolor("orange")

    turtle.speed(1)
    turtle.penup()
    turtle.goto(-100, 0)
    turtle.pendown()
    draw_car_body()
    draw_wheels()
    draw_windows()
    draw_a_man()

    turtle.hideturtle()
    wn.exitonclick()

main()
