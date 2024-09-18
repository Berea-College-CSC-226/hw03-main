###################################################
##  Author: Julio Jijon
##  Username: jijonj
##  Google Doc: https://docs.google.com/document/d/1lS28AuVN5m-JRi-ODe0WctUhKYdrz50QzcrktSkBx60/edit?usp=sharing
##  Purpose: create a house with a person using turtles
###################################################

import turtle

def drawSquare(t, size):
    ''' put in a for loop for a square'''
    for i in range(4):
        t.fd(size)
        t.left(90)


def drawTriangle(t):
    ''' code for the roof of the house '''
    for i in range(3):
        t.fd(125)
        t.right(120)


def drawPerson(t):
    ''' draw a stickfigure person '''
    intial_pos = t.pos()
    t.right(90)
    t.fd(100)
    t.right(45)
    t.fd(50)
    t.bk(50)
    t.left(90)
    t.fd(50)
    t.bk(50)
    t.goto(intial_pos)
    t.fd(50)
    t.bk(50)
    t.right(90)
    t.fd(50)
    t.bk(50)
    t.left(130)
    t.circle(50,360)

def main():
    ''' define the main function of the program'''
    wn = turtle.Screen()
    wn.colormode(255)
    wn.bgcolor('lightblue')
    house = turtle.Turtle()
    person = turtle.Turtle()
    house.penup()
    house.goto(100,25)
    house.pendown()

    house.color('red')
    house.fillcolor("red")
    house.begin_fill()
    drawSquare(house, 125)
    house.end_fill()
    house.fd(125)
    house.left(90)
    house.fd(125)
    house.left(90)
    house.color(115,134,120)
    house.fillcolor(115,134,120)
    house.begin_fill()
    drawTriangle(house)
    house.end_fill()
    house.penup()
    house.goto(200, 100)
    house.pendown()
    drawSquare(house,75)
    house.hideturtle()

    person.penup()
    person.goto(-50,50)
    person.pendown()
    person.color()
    drawPerson(person)

    wn.exitonclick()

if __name__ == '__main__':
    main()