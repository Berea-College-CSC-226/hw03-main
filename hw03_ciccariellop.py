#################################################################################
# Author: Pier Ciccariello
# Username: ciccariellop
#
# Assignment: HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Practice w/ functions, turtles, and python in general
# Google Doc Link: https://docs.google.com/document/d/1GoGJoL2peNQtOe6GWwlO17fe6I_66j5E4ZYtaTG-Bw0/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################


import turtle

def draw_window1(t):
    """Draws the first window at (120,20)"""
    t.penup()
    t.setpos(120,20)
    t.pendown()
    t.pencolor("grey")
    for i in range(4):
        t.forward(75)
        t.left(90)

def draw_window2(t):
    """Draws the second window at (-150,20)"""
    t.penup()
    t.setpos(-150, 20)
    t.pendown()
    t.pencolor("grey")
    for i in range(4):
        t.forward(75)
        t.left(90)

def draw_house(t):
    """Draws the house"""
    t.penup()
    t.setpos(-200, -200)
    t.pendown()
    t.pencolor("grey")
    t.forward(450)
    t.left(90)
    t.forward(350)
    t.left(90)
    t.forward(450)
    t.left(90)
    t.forward(350)

def draw_roof_chimney(t):
    """Draws the house's roof and the chimney on the roof, then fills chimney with a specific shade of brown"""
    t.setpos(-200,150)
    t.left(135)
    t.forward(319)
    t.right(90)
    t.forward(319)
    t.backward(100)
    t.begin_fill()
    t.fillcolor((155,75,0))
    t.left(135)
    t.forward(70)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(90)
    t.end_fill()

def draw_head(t):
    """Draws my characters head circle"""
    t.setpos(0,0)
    t.fillcolor((255,100,100))
    t.begin_fill()
    t.circle(30)
    t.end_fill()

def draw_body(t):
    """Draws a stick body down from the filled circle"""
    t.setpos(0,0)
    t.right(90)
    t.forward(100)
    t.left(45)
    t.forward(65)
    t.backward(65)
    t.right(90)
    t.forward(65)
    t.penup()

def draw_arms(t):
    """Draws arms branching from the body"""
    t.setpos(0,0)
    t.pendown()
    t.forward(65)
    t.backward(65)
    t.left(90)
    t.forward(65)
    t.left(45)

def draw_flower(t):
    """Draws a flower at (200,-180)"""
    t.penup()
    t.setpos(200,-180)
    t.pendown()
    t.pencolor("hot pink")
    t.begin_fill()
    for i in range (8):
        t.circle(10)
        t.left(45)
    t.end_fill()

def draw_stem(t):
    """Draws a stem underneath the flower"""
    t.penup()
    t.forward(20)
    t.pendown()
    t.pencolor("green")
    t.forward(50)
    t.backward(15)

def draw_leaf(t):
    """Draws a leaf on the stem"""
    t.penup()
    t.right(135)
    t.forward(20)
    t.fillcolor("green")
    t.shape("circle")
    t.shapesize(stretch_wid=1, stretch_len=2)
    t.stamp()

def draw_eyes(t):
    """Gives the created character googly eyes"""
    t.setpos(12,40)
    t.color("black")
    t.turtlesize(1,1,1)
    t.stamp()
    t.penup()
    t.setpos(-12,40)
    t.stamp()

def main():
    """Main function"""
    wn = turtle.Screen()
    wn.bgcolor("#87CEEB")
    wn.colormode(255)
    wn.setup(600, 600)
    t = turtle.Turtle()
    t.color("purple")
    t.pensize(5)
    t.speed(0)

    draw_head(t)
    draw_body(t)
    draw_arms(t)
    draw_window1(t)
    draw_window2(t)
    draw_house(t)
    draw_roof_chimney(t)
    draw_flower(t)
    draw_stem(t)
    draw_leaf(t)
    draw_eyes(t)

    wn.exitonclick()

main()