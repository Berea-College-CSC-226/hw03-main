# Gavin Miller, millerg3
# https://docs.google.com/document/d/1ubqCXVn_pfDmnt3cz7FQ8piWil1egG5pBuyEQEn9wbA/edit?tab=t.0

# Set up turtle and it's methods

import turtle
screen = turtle.Screen()
screen.bgcolor("pink")
alex = turtle.Turtle()
print(alex.pos())
alex.speed(0)

'''
Draw the head of person
'''
def draw_head(size):
    alex.penup()
    alex.goto(0,100)
    alex.pendown()
    for i in range(size):
        alex.forward(5)
        alex.right(5)
'''
Draw body of the person
'''
def draw_body():
    alex.penup()
    alex.goto(0, -15)
    alex.pendown()
    alex.right(90)
    alex.forward(150)
    alex.right(180)
    alex.forward(75)

'''
Draw the arms and legs of the body using a for loop
'''
def draw_limbs(length, limbs):
    for i in range(limbs):
        alex.left(135)
        alex.forward(length)
        alex.right(180)
        alex.forward(length)
        alex.right(90)
        alex.forward(length)
        alex.left(180)
        alex.forward(length)
        alex.penup()
        alex.setheading(270)
        alex.forward(length)
        alex.pendown()
        alex.setheading(90)
'''
Draw the mouth!
'''
def draw_mouth():
    alex.penup()
    alex.goto(10, 10)
    alex.pendown()
    print(alex.pos())
    alex.color("red")
    alex.left(90)
    alex.forward(30)
    alex.right(180)
    alex.forward(40)
    alex.penup()
    alex.goto(-20, 65)
    alex.pendown()
'''
Draw the eyes using rgb color, for loop, and filled eyes.
'''
def draw_eyes(size):
    alex.begin_fill()
    alex.color("blue")
    screen.colormode(255)
    alex.fillcolor(87, 142, 73)
    for i in range(size):
        alex.forward(1)
        alex.right(5)
    alex.penup()
    alex.forward(50)
    alex.pendown()
    for i in range(size):
        alex.forward(1)
        alex.right(5)
    alex.end_fill()
'''
Draw stars in the background 
'''
def draw_ruler():
    alex.penup()
    alex.goto(-75, -217)
    print(alex.pos())
    alex.pendown()
    for i in range(63):
        alex.forward(5)
        alex.right(180)
        alex.forward(5)
        alex.right(90)
        alex.forward(5)
        alex.right(90)
    print(alex.pos())
    alex.forward(100)
    print("This guy is just under 316 pixels tall!")

def main():
    draw_head(72)
    draw_body()
    draw_limbs(75, 2)
    draw_mouth()
    draw_eyes(72)
    draw_ruler()

main()
screen.exitonclick()


