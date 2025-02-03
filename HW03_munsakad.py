################################################
# Name: Dingani Munsaka
#Title: Fully Functional Gitty Psychedelic Robotic Turtles
#Google doc link: https://docs.google.com/document/d/1_QtOsvS1fWH7XksrLDKD0NqiDHW8SSyqDkNQlqv7ePw/edit?usp=sharing
#Acknoledgements: None for this code, I made it on my own.
#
#######################################################

import turtle


w = turtle.Turtle()
s=turtle.Turtle()


def draw_rectangle(t,s):
    """
    This function draws the recurring rectangle with the length of the side being i increment.
    """
    for i in range(100):
        t.forward(i)
        t.left(90)


def triangle():
    """
    This function does the same as the rectangle only that this time is triangles
    """
    for i in range(50):
        w.forward(i * 5)
        w.left(120)


def sun_rays():
    """
    This function draws the sun rays besides the triangles and rectangles for decoration purposes
    """
    t = turtle.Turtle()
    t.speed(8)
    t.color('red', 'blue')
    t.begin_fill()
    for i in range(100):
        t.penup()
        t.forward(100)
        t.left(90)
        t.pendown()
        t.forward(100)
        t.left(169)


def flower():
    """
    This function draws a flower on the other side of the rectangles and triangles for decorative purposes
    """
    s.pencolor('orange')
    s.penup()
    s.fd(-100)
    s.left(90)
    s.pendown()
    for i in range(100):

        s.forward(100)
        s.left(169)


def main():
    """
    Here in the main is where I defined all my turtles and calling the functions above
    """
    wn = turtle.Screen()
    wn.bgcolor('blue')
    tess = turtle.Turtle()
    tess.color('green')
    w.pencolor("black")
    w.pensize(1)
    w.penup()
    w.forward(200)
    w.pendown()
    tess.pensize(0)
    w.penup()
    w.bk(200)
    w.pendown()
    draw_rectangle(tess, 50)
    triangle()
    sun_rays()
    flower()
    wn.exitonclick()

main()








