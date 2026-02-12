import turtle

"""
this code starts us off by centering our
turtle for further code.
"""

def drawStart(flower_turtle):
    flower_turtle.penup()
    flower_turtle.goto(0, 0)
    flower_turtle.setheading(90)
    flower_turtle.pendown()

"""
this code draws our stem
"""

def drawFlowerStem(flower_turtle):
    flower_turtle.color("green")
    flower_turtle.pensize(10)

    flower_turtle.penup()
    flower_turtle.goto(0, -250)
    flower_turtle.pendown()

    flower_turtle.forward(175)

"""
Because we are drawing a flower, 
we want our flower to also have small leaves. 
This code does exactly that.
"""

def drawFlowerLeaves(flower_turtle):
    flower_turtle.color("green")
    flower_turtle.pensize(10)

    flower_turtle.penup()
    flower_turtle.goto(0, 3)
    flower_turtle.setheading(90)
    flower_turtle.pendown()

    flower_turtle.right(180)
    flower_turtle.forward(50)
    flower_turtle.left(90)
    flower_turtle.forward(15)
    flower_turtle.left(180)
    flower_turtle.forward(15)
    flower_turtle.left(90)
    flower_turtle.forward(25)
    flower_turtle.right(90)
    flower_turtle.forward(25)
    flower_turtle.left(180)
    flower_turtle.forward(25)
    flower_turtle.left(90)
    flower_turtle.forward(50)

"""
This code is a loop. The reason why I made 
it into a loop was so that I don't have to 
keep rewriting turtle functions. 
"""

def drawFlowerTurtle(flower_turtle):
    for i in ["red", "green", "blue"]:
        flower_turtle.color(i)
        flower_turtle.pensize(10)
        flower_turtle.left(90)

def drawFlowerPetals(flower_turtle):
    """
    please note that this section
    was edited by chatgpt with the prompt:
    "help me make this to a petal" and is only
    being kept as a example code.
    """

    flower_turtle.penup()
    flower_turtle.goto(0, 10)
    flower_turtle.setheading(0)
    flower_turtle.pendown()

    flower_turtle.color("red")
    flower_turtle.pensize(5)

    for i in range(18):
        flower_turtle.circle(40, 60)
        flower_turtle.left(120)
        flower_turtle.circle(40, 60)
        flower_turtle.left(20)

def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    flower_turtle = turtle.Turtle()
    flower_turtle.shape("turtle")
    flower_turtle.speed(0)


    drawStart(flower_turtle)
    drawFlowerStem(flower_turtle)
    drawFlowerLeaves(flower_turtle)
    drawFlowerTurtle(flower_turtle)
    drawFlowerPetals(flower_turtle)

    wn.exitonclick()

main()



