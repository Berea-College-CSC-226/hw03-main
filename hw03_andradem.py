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
ws.bgcolor("lightskyblue")

koopa = turtle.Turtle()
koopa.pensize(10)
#koopa.speed(0)

colorsStoneBase = ["maroon", "saddlebrown", "tan3", "tan4", "red4"]
colorsResort = ["firebrick4", "maroon"]

def bostro (turt, x, y, palette):
    random.seed(226)
    for i in range(y//turt.pensize()):
        lengthTaken = 1
        while lengthTaken <= x:
            step = 10*random.randint(3, 7)
            # TODO: continue from here
            step -= x%lengthTaken
            print( x," % ",  lengthTaken, " = ", step)
            turt.pencolor(palette[random.randint(0,  len(palette)-1)])
            turt.fd(step)
            lengthTaken += step
        turt.up()
        turt.fd(-lengthTaken)
        turt.left(90)
        turt.forward(turt.pensize())
        turt.down()
        turt.right(90)

def colordemo(palette):
    for i in palette:
        koopa.pencolor(i)
        koopa.fd(20)


def main():
    #koopa.goto(-50,-400)
    #bostro(koopa, 550, 300, colorsStoneBase)

    bostro(koopa, 300, 200, colorsResort)

    ws.exitonclick()


main()