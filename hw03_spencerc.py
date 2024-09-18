import turtle


def wall(goober): #draws and fills the square that will be the walls/base of the house
    goober.fillcolor('beige') #beige walls
    goober.begin_fill()
    for i in range(4):
        goober.forward(100)
        goober.right(90)
    goober.end_fill()
    goober.left(45)

def roof(goober):         #draws the roof atop the house
    goober.fillcolor('red')  #trying to make the roof red
    goober.begin_fill()
    goober.forward(71.5)
    goober.right(90)
    goober.forward(71.5)
    goober.right(135)
    goober.forward(100)
    goober.end_fill()
    goober.right(45)
    goober.penup()
    goober.right(90)
    goober.forward(71.5)
    goober.right(90)
    goober.forward(20.5)
    goober.pendown()

def chimney(goober): #every house could use a chimney for those cold winter night by the fire
    goober.fillcolor('grey')  #it's a rock chimney
    goober.begin_fill()
    goober.left(135)
    goober.forward(20)
    goober.right(90)
    goober.forward(10)
    goober.right(90)
    goober.forward(30.5)
    goober.end_fill()
    goober.left(45)
    goober.forward(20)

def door(goober):  #creates a door so people aren't trapped inside
    goober.penup()
    goober.right(45)
    goober.forward(110)
    goober.right(90)
    goober.forward(40)
    goober.pendown()
    goober.right(90)
    goober.pendown()
    goober.fillcolor('brown')  #wooden door color
    goober.begin_fill()
    goober.forward(35)
    goober.left(90)
    goober.forward(20)
    goober.left(90)
    goober.forward(35)
    goober.left(90)
    goober.forward(20)
    goober.end_fill()

def grass(goober):
    goober.fillcolor('lightgreen') #not quite kentucky bluegrass, but it'll do
    goober.begin_fill()
    goober.forward(300)
    goober.right(90)
    goober.forward(200)
    goober.right(90)
    goober.forward(900)
    goober.right(90)
    goober.forward(200)
    goober.right(90)
    goober.forward(700)
    goober.end_fill()

def sun(goober):   #draws the sun to brighten everyone's day
    goober.penup()
    goober.left(135)
    goober.forward(550)
    goober.pendown()
    goober.fillcolor('yellow') #sets the sun to that warm hugh
    goober.begin_fill()
    goober.circle(80)
    goober.end_fill()
    goober.penup()
    goober.left(90)
    goober.forward(80)
    goober.pendown()
    goober.color('orange')
    x = 1
    for i in range(60):
        goober.forward(1)
        goober.right(45)
        goober.forward(x+i)

def main():  #it's main... it's where the main stuff goes like functionality calls
    wn = turtle.Screen()
    goober = turtle.Turtle()
    turtle.bgcolor('lightblue')
    goober.speed(9)  #faster means less time spent waiting on certain parts of testing
    wall(goober)
    roof(goober)
    chimney(goober)
    door(goober)
    grass(goober)
    sun(goober)

    wn.exitonclick() #Game over man!!! This just closes the program

main()