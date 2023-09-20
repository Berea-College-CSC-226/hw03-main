# Drawing the cat.
#Acknowlege:

import turtle
cat = turtle.Turtle()
wn = turtle.Screen()

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

def draw_eyes(x,y):
    cat.begin_fill()
    cat.color("white")
    cat.penup()
    cat.forward(-50)
    cat.pendown()
    cat.circle(-15)
    cat.penup()
    cat.forward(100)
    cat.pendown()
    cat.circle(-15)
    cat.end_fill()








def main():
    cat.speed(7)
    draw_head(0,-100)
    wn.bgcolor("orange")
    cat.speed(10)
    cat.goto(0,50)
    draw_eyes(70,70)
    cat.goto(0,0)
    cat.forward(-80)
    cat.left(-90)
    cat.circle(radius=80,extent=170)











    """
    Docstring for main
    """
    # ...


main()
wn.exitonclick()


