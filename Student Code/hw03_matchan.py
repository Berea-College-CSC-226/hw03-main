# Name: Neelima Matcha
# HW03 Turtle House
#Google link: https://docs.google.com/document/d/1eD6oPSwToj9XL7h4-obYFuxXiut22ZA9a_kja4AJ3dQ/edit?usp=sharing

import turtle
Screen=turtle.Screen()

def draw_house(matcha):
    """simple house"""
    matcha.fillcolor(200,100,100)
    matcha.begin_fill()
    for i in range(4):
        matcha.forward(100)
        matcha.left(90)
    matcha.end_fill()

def roof_window(nee):
    """roof window"""
    nee.left(45)
    nee.forward(70)
    nee.right(90)
    nee.forward(70)
    nee.right(135)
    nee.forward(100)
    nee.penup()
    nee.goto(20,20)
    nee.pendown()
    nee.fillcolor(255,255,150)
    nee.begin_fill()
    for i in range(4):
        nee.forward(20)
        nee.left(90)
    nee.end_fill()

def main():
    """Set up the turtle screen, create the turtle and draw the house with a roof."""
    screen = turtle.Screen()
    screen.colormode(255)
    screen.bgcolor(180,220,255)

    matcha = turtle.Turtle()
    matcha.speed(3)

    draw_house(matcha)
    roof_window(matcha)

    turtle.done()

main()
Screen.exitonclick()

