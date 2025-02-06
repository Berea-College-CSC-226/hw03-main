# Ku Htoo
#htook
#https://docs.google.com/document/d/14T5BiVZLmSIamvte978sTi6nW3gfJmRvPe6sXbFPgks/edit?usp=sharing

import turtle

kh1 = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor('lightblue')

def person():
    kh3 = turtle.Turtle()
    kh3.setposition(0,0)
    kh3.color('#D2B48C')
    kh3.pensize(20)
    kh3.circle(5)
    kh3.color('black')
    kh3.penup()
    kh3.setposition(0,-10)
    kh3.pendown()
    kh3.pensize(5)
    kh3.right(90)
    kh3.forward(60)
    kh3.color('blue')
    kh3.right(15)
    kh3.forward(70)
    kh3.back(70)
    kh3.left(35)
    kh3.forward(70)
    kh3.back(70)
    kh3.color('black')
    kh3.left(-20)
    kh3.back(30)
    kh3.right(130)
    kh3.color('#D2B48C')
    kh3.forward(70)
    kh3.back(70)
    kh3.right(-260)
    kh3.forward(70)




def ground():
    kh2 = turtle.Turtle()
    kh2.color('green')
    kh2.speed(10)
    kh2.penup()
    kh2.setposition(-400,-150)
    kh2.pendown()
    kh2.pensize(25)
    kh2.forward(750)
    kh2.begin_fill()
    for i in range(4):
        kh2.right(90)
        kh2.forward(750)
    kh2.end_fill()






def main():


    kh1.penup()
    kh1.setposition(200, 140)
    kh1.pendown()
    kh1.color('yellow')
    kh1.pensize(100)
    kh1.circle(5)
ground()
person()

main()
wn.exitonclick()