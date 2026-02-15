import turtle
import math
import random
from math import hypot

def lozenge (turt, thickness, interval, times):
    for i in range(times):
        angle = 2 * math.degrees(math.atan(thickness / interval))
        length = hypot(thickness, interval)
        print(angle)
        turt.left(angle/2)
        turt.forward (length)
        turt.right(angle)
        turt.forward (length)
        turt.right(180-angle)
        turt.forward(length)
        turt.right(angle)
        turt.forward(length)
        turt.right(180-angle*.5)

#####################################################
# SETUP VARIABLES
ws = turtle.Screen()
ws.bgcolor("lightskyblue1")

koopa = turtle.Turtle()
koopa.pensize(10)
koopa.speed(0)

colorsStoneBase = ["maroon", "saddlebrown", "tan3", "tan4", "red4"]
colorsResort = ["firebrick4", "maroon"]
colorsRoof = ["azure", "azure1", "lavender"]
colorsRoof2 = ["lightsalmon", "lightsalmon", "lightsalmon3"]
colorsBackground = ["lightsteelblue1", "lightsteelblue2", "lightsteelblue", "lightsteelblue3"]

def bostro (turt, x, y, palette, triangle):
    random.seed(226)
    direction = 1
    for i in range(y//turt.pensize()):
        lengthTaken = 0
        x -= triangle # decrease size (only triangle)
        while lengthTaken < x:
            step = 10*random.randint(3, 7)
            if lengthTaken + step >= x:
                step = x-lengthTaken
            turt.pencolor(palette[random.randint(0,  len(palette)-1)])
            turt.fd(step)
            lengthTaken += step
        turt.up()
        turt.left(90*direction)
        turt.forward(turt.pensize())
        turt.left(90*direction)

        x -= triangle # decrease size (triangle only)
        turt.forward(triangle) # same here

        turt.down()
        direction *= -1

def background (turt, thickness, palette):
    bg_width = 500
    turt.pensize(thickness)
    for i in range (len(palette)):
        turt.pencolor(palette[i])
        color = [palette[i]]
        bostro(turt, bg_width, 50, color, False)
    turt.pensize(10)

def colordemo(palette):
    for i in palette:
        koopa.pencolor(i)
        koopa.fd(20)

def rectangle (turt, x, y, pen, fill):
    turt.pencolor(pen)
    turt.fillcolor(fill)
    turt.begin_fill()
    for i in range(0,4):
        turt.fd(y * (i%2) + x * ((i+1)%2))
        turt.right(90)
    turt.end_fill()

def main():

    #background(koopa, 50, colorsBackground)
    koopa.goto(-500, 100)
    thick = 150
    for i in range(0,4):
        koopa.pencolor(colorsBackground[i])
        koopa.pensize(thick)
        koopa.fd(1000)
        koopa.fd(-1000)
        koopa.right(90)
        koopa.fd(thick)
        koopa.left(90)

    koopa.up()
    koopa.goto(0,0)
    koopa.down()
    koopa.pensize(10)

    koopa.goto(-50,-400)
    bostro(koopa, 550, 300, colorsStoneBase, False)

    koopa.right(180)
    rectangle(koopa, 20, 90, "burlywood", "burlywood")
    koopa.right(180)

    bostro(koopa, 300, 100, colorsResort, False)

    koopa.fd(-10)
    bostro(koopa, 320, 140, colorsRoof, 7)
    bostro(koopa, 123, 100, colorsRoof2, 7)

    for i in range(0,2):
        koopa.up()
        koopa.right(90)
        koopa.fd(130)
        koopa.left(90)
        koopa.fd(20)
        koopa.down()
        rectangle(koopa, 30, 50, "lavender", "skyblue4")
        koopa.up()
        koopa.fd(-70)
        koopa.down()
        rectangle(koopa, 30, 50, "lavender", "skyblue4")
        koopa.up()
        koopa.fd(55)

    ws.exitonclick()


main()