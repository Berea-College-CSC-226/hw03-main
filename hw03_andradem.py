import turtle
import math
from math import hypot


def pattern (turt, thickness, interval, times):
    for i in range(times):
        shouldIturn = i % 2 * 2 - 1
        turt.right(shouldIturn * 90)

        turt.forward(thickness)
        turt.left(shouldIturn * 90)

        turt.fd(interval)
        print(shouldIturn)

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

ws = turtle.Screen()
ws.bgcolor("darkslategray")

koopa = turtle.Turtle()
koopa.pensize(10)

# pattern(koopa, 40,10,5)

def unused():
    lozenge(koopa, 25, 50, 1)
    koopa.up()
    koopa.forward(20)
    koopa.down()
    lozenge(koopa, 15, 30, 1)
    ws.exitonclick()

def angleFinder(x,y):
    return math.atan(y/x)

def leaf (x, y, thickness):
    koopa.right(angleFinder(x, y))
    #extraAngle =
    #adjustAngle =
    koopa.forward(math.hypot(x, y))

def bostro (turt, x, y):
    direction = 1
    for i in range(y//turt.pensize()):
        turt.fd(x)
        turt.left(direction*90)
        turt.up()
        turt.forward(turt.pensize())
        turt.down()
        turt.left(direction*90)
        direction *= -1


def main():
    # The starter pinapple
    #koopa.begin_fill()
    #koopa.forward(-50)
    #for i in range(0,4):
    #    koopa.forward(100+i%2*50)
    #    koopa.right(45)
    #    koopa.forward(50)
    #    koopa.right(45)

    #koopa.fillcolor("goldenrod")
    #koopa.end_fill()
    bostro(koopa, 50, 50)



    ws.exitonclick()
main()