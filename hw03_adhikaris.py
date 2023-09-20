# Drawing a cat.
#Acknowlege:

import turtle


# Draw the cat's head

def draw_head(cat, x,y):
    """ This function is suppose to draw the head of a cat"""
    cat.penup()
    cat.goto(0, -100)
    cat.pendown()
    cat.begin_fill()
    cat.color("black")
    cat.circle(100)
    cat.end_fill()

def draw_body(x,y):
    """ This function is suppose to draw the body of a cat"""
    cat.penup()
    cat.goto(0, -140)
    cat.pendown()
    cat.begin_fill()
    cat.color("black")
    cat.circle(120)
    cat.end_fill()



def triangle(x,y):
    cat.begin_fill()
    cat.color("black")
    cat.forward(50)
    for i in range(3):
        cat.forward(side_length)
        cat.left(120)
    cat.end_fill()


def draw_eyes(cat, x,y):
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
    #cat.forward(120)
    #cat.right(-85)
    cat.end_fill()

def draw_ear(cat, x,y):
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
    cat.penup()
    cat.goto(-55, -55)  # Position the turtle
    cat.pendown()
    cat.circle(radius=60, extent=80)
    cat.right(20)
    cat.left(-20)
    cat.pendown()
    cat.right(120)
    cat.circle(radius=60, extent=80)


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
    #cat.forward(-85)
    #cat.right(80)
    #cat.circle(radius=80,extent=170)
    # triangle(70,70)
    # triangle(-70, 70)
    # draw_body(0,0)























    """
    Docstring for main
    """
    # ...
    #cat.hideturtle()
    wn.exitonclick()

main()



