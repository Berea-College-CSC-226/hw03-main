# Drawing the cat.
#Acknowlege:

import turtle
cat = turtle.Turtle()
wn = turtle.Screen()
side_length= 50

# Draw the cat's head

def draw_head(x,y):
    """ This function is suppose to draw the head of a cat"""
    cat.penup()
    cat.goto(0, -100)
    cat.pendown()
    cat.begin_fill()
    cat.color("black")
    cat.circle(100)
    cat.end_fill()

def draw_body(x,y):
    """ This function is suppose to draw the head of a cat"""
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
    cat.forward(120)
    cat.right(-85)
    cat.end_fill()


def draw_eyes(x,y):
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












def main():
    cat.speed(7)
    draw_head(0,-100)
    wn.bgcolor("orange")
    cat.speed(10)
    cat.goto(0,50)
    draw_eyes(70,70)
    cat.goto(0,0)
    cat.forward(-85)
    cat.right(80)
    cat.circle(radius=80,extent=170)
    triangle(70,70)
    triangle(-70, 70)
    draw_body(0,0)























    """
    Docstring for main
    """
    # ...


main()
cat.hideturtle()
wn.exitonclick()


