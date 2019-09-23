###############################################################
# Author: Mason Richardson
# Username: Richardsonmas
# For CSC 226 with Scott Heggen (Fall 2019)
# This program uses the Turtles library to draw a complex image.

# Google Doc Link: https://docs.google.com/document/d/1aHajIag9yXOQFwHwXaT4hE5cj7AmsKLXGQaBAiAACRg/edit#
################################################################
import turtle
import random

def draw_frame(picasso):                # the lines before the for loop are there to get the turtle in place.
    picasso.forward(200)
    picasso.right(-90)
    picasso.forward(200)
    picasso.pendown()
    picasso.color(152, 158, 205)
    picasso.begin_fill()

    for i in range(4):                   # this for loop draws a box and fills it with a pleasant periwinkle color
        picasso.right(-90)
        picasso.forward(400)
    picasso.end_fill()


def perspective_lines(picasso):        # makes the lines that show that the square is a tunnel
    picasso.color(143, 37, 239)
    coordinates = [[200,200], [-200, 200], [200, -200], [-200, -200]]
    for point in coordinates:
        picasso.penup()
        picasso.setpos(point)
        picasso.pendown()
        picasso.setpos(0,0)


def train(picasso):                  # draws the body of the train
    picasso.penup()
    picasso.begin_fill()
    picasso.color(172, 104, 104)
    picasso.right(180)
    picasso.setpos(30, 40)
    picasso.pendown()
    picasso.forward(80)
    picasso.right(90)
    picasso.forward(60)
    picasso.right(90)
    picasso.forward(80)
    picasso.right(90)
    picasso.forward(60)
    picasso.end_fill()


def tracks(picasso):                   # draws the tracks (basically long skinny triangles)
    picasso.penup()
    picasso.color(143, 117, 159)
    picasso.setpos(-160, -200)
    picasso.pendown()
    picasso.begin_fill()
    picasso.setpos(0,0)
    picasso.setpos(-140, -200)
    picasso.setpos(-160, -200)
    picasso.end_fill()
    picasso.penup()
    picasso.setpos(160, -200)
    picasso.pendown()
    picasso.begin_fill()
    picasso.setpos(0, 0)
    picasso.setpos(140, -200)
    picasso.setpos(160, -200)
    picasso.end_fill()

def train_details(picasso):
    picasso.penup()                             # draws the details on the train
    picasso.color(244, 228, 32)
    picasso.setpos(0, 10)
    picasso.pendown()
    picasso.begin_fill()
    picasso.circle(10)
    picasso.end_fill()
    picasso.penup()
    picasso.color(172, 104, 104)
    picasso.setpos(0, 30)
    picasso.pendown()
    picasso.begin_fill()
    picasso.setpos(20, 80)
    picasso.setpos(-20, 80)
    picasso.setpos(0, 30)
    picasso.end_fill()
    picasso.penup()
    picasso.color(142, 64, 64)
    picasso.pendown()
    picasso.begin_fill()
    picasso.setpos(0, -5)
    picasso.setpos(-45, -40)
    picasso.setpos(45, -40)
    picasso.setpos(0, -10)
    picasso.end_fill()


def train_light(picasso):
    picasso.penup()
    picasso.setpos(0, 20)
    for i in range(15):
        color = [(random.randint(125,255)), (random.randint(125,255)), (random.randint(100,255))]
        picasso.pendown()
        picasso.setpos(0, (20 - (2 * i)))
        picasso.color(color)
        picasso.circle(i*i)
        picasso.penup()

def main():
    wn = turtle.Screen()
    wn.colormode(255)
    wn.bgcolor(109, 167, 119)
    picasso = turtle.Turtle()
    picasso.hideturtle()
    picasso.penup()
    draw_frame(picasso)
    perspective_lines(picasso)
    tracks(picasso)
    train(picasso)
    train_details(picasso)
    train_light(picasso)
    wn.exitonclick()


main()


