######################################################################
# Author: Jairus Harriso
# Username: harrisonj2
#
# Assignment: Hw03
######################################################################
import turtle

t = turtle.Turtle()
t.speed(10)
screen = turtle.Screen()
screen.bgcolor("black")

def draw_house():
    t.penup()
    t.goto(-100, -100)
    t.pendown()
    t.color("brown")
    for _ in range(4):
        t.forward(200)
        t.left(90)

def draw_roof():
    t.penup()
    t.goto(-120, 100)
    t.pendown()
    t.color("brown")
    for _ in range(3):
        t.forward(240)
        t.left(120)
    t.penup()

def draw_door():
    t.goto(-30, -100)
    t.pendown()
    t.begin_fill()
    t.color("white")
    for _ in range(2):
        t.forward(60)
        t.left(90)
        t.forward(100)
        t.left(90)
    t.end_fill()

def draw_windows():
    t.penup()
    t.goto(-80, 0)
    t.pendown()
    t.begin_fill()
    t.color("blue")
    for _ in range(4):
        t.forward(40)
        t.left(90)
    t.end_fill()
    t.penup()
    t.goto(40, 0)
    t.pendown()
    t.begin_fill()
    t.color("red")
    for _ in range(4):
        t.forward(40)
        t.left(90)
    t.end_fill()

def draw_tree():
    t.penup()
    t.goto(-250, -100)
    t.pendown()
    t.begin_fill()
    t.color("saddlebrown")
    for _ in range(2):
        t.forward(40)
        t.left(90)
        t.forward(100)
        t.left(90)
    t.end_fill()
    t.penup()
    t.goto(-270, 0)
    t.pendown()
    t.begin_fill()
    t.color("forest green")
    for _ in range(3):
        t.forward(120)
        t.left(120)
    t.end_fill()

# Call functions to draw the house and sky
def main():
   draw_house()
   draw_roof()
   draw_door()
   draw_windows()
   draw_tree()
   t.hideturtle()
   screen.exitonclick()

main()

