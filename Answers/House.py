# **********************************************************
# Name: Your Name
# Username: yourusername
# Link to Google Doc: https://docs.google.com/...
# Homework Assignment: Turtle Drawing Project
# **********************************************************

import turtle

# function to draw a square
def draw_square(color, x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)
    turtle.end_fill()

# function to draw a triangle/roof
def draw_triangle(color, x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(size)
        turtle.left(120)
    turtle.end_fill()

# function to draw a window, This made me throw my computer out the window.
def draw_window(color, x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)
    turtle.end_fill()

def main():
    turtle.bgcolor("#87CEEB")  # background color (sky blue)
    turtle.speed(5)

    # draw the house base
    draw_square("burlywood", -50, -100, 100)

    # draw the roof
    draw_triangle("firebrick", -50, 0, 100)

    # draw a window
    draw_window("lightyellow", -30, -50, 30)

    # keep window open
    turtle.done()

main()

#not all credit goes to me what so ever, between the help of former cs majors. I couldn't get the window to work.
