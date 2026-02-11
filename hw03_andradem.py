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
ws.bgcolor("white")

koopa = turtle.Turtle()

# pattern(koopa, 40,10,5)
koopa.pensize(5)

lozenge(koopa, 25, 50, 1)
koopa.up()
koopa.forward(20)
koopa.down()
lozenge(koopa, 15, 30, 1)
ws.exitonclick()

