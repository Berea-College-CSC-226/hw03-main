# Drawing a cat.
#Acknowlege: Used ChatGPT to ask question, used runestone textbook.

import turtle


# Draw the cat's head

def draw_head(cat, x,y):
    """ This function draws the head of a cat"""
    cat.penup()
    cat.goto(0, -100)
    cat.pendown()
    cat.begin_fill()
    cat.color("#110101")
    cat.circle(100)
    cat.end_fill()



def draw_eyes(cat, x,y):
    """This function draws the eyes of cat"""
    cat.begin_fill()
    cat.color("white")
    cat.penup()
    cat.forward(-50)
    cat.pendown()
    cat.circle(-25)
    cat.penup()
    cat.forward(100)
    cat.pendown()
    cat.circle(-25)
    cat.end_fill()

def draw_ear(cat, x,y):
    """This function draws the ear of cat."""
    cat.begin_fill()
    cat.color("white")
    cat.penup()
    cat.goto(-70, 70)  # Position the turtle
    cat.pendown()
    for i in range(3):
        cat.forward(50)
        cat.left(120)
    cat.end_fill()

def right_ear(cat, x,y):
    """This function draws the right side ear of a cat."""
    cat.begin_fill()
    cat.color("white")
    cat.penup()
    cat.goto(20, 70)
    cat.pendown()
    for i in range(3):
        cat.forward(50)
        cat.left(120)
    cat.end_fill()


def draw_mouth(cat, x,y):
    """This function is supposed to draws mustache """
    cat.penup()
    cat.goto(-55, -55)  # Position the turtle
    cat.pendown()
    cat.circle(radius=60, extent=80)
    cat.right(20)
    cat.left(-20)
    cat.pendown()
    cat.right(120)
    cat.circle(radius=60, extent=80)

def draw_body(cat,x,y):
    """ This function draws the body of a cat"""
    cat.penup()
    cat.goto(-8, -315)
    cat.pendown()
    cat.begin_fill()
    cat.color("#110101")
    cat.circle(120)
    cat.end_fill()

def draw_tail(cat,x,y):
    """ draw's triangle shape white tail"""
    cat.penup()
    cat.begin_fill()
    cat.forward(5)
    cat.color("white")
    cat.circle(radius=25, extent=180)
    cat.pendown()
    cat.forward(-200)
    cat.end_fill()





def main():
    cat = turtle.Turtle()
    wn = turtle.Screen()
    side_length = 50
    cat.speed(7)
    draw_head(cat, 0,-100)
    wn.bgcolor("orange")
    cat.speed(10)
    cat.goto(0,50)
    draw_eyes(cat, 70,70)
    draw_ear(cat, -70, 70)
    draw_mouth(cat, -40, 40)
    right_ear(cat, 20, 70)
    draw_body(cat,-8,-315)
    draw_tail(cat, 0, 0)
    cat.hideturtle()
    wn.exitonclick()


main()



