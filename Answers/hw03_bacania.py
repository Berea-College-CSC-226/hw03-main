import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
flower_turtle = turtle.Turtle()
flower_turtle.shape("turtle")
flower_turtle.color("yellow")
flower_turtle.speed(0)
flower_turtle.pensize(30)
flower_turtle.right(90)
flower_turtle.forward(1)

def drawFlowerStem():
    flower_turtle.color("green")
    flower_turtle.pensize(10)

    flower_turtle.penup()
    flower_turtle.goto(0, -0)
    flower_turtle.pendown()

    flower_turtle.forward(175)

def drawFlowerLeaves():
    flower_turtle.color("green")
    flower_turtle.pensize(10)

    flower_turtle.penup()
    flower_turtle.goto(0, 3)
    flower_turtle.pendown()

    flower_turtle.right(360)
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

def drawFlowerTurtle():
    for i in ["red", "green", "blue"]:
        flower_turtle.color(i)
        flower_turtle.pensize(10)
        flower_turtle.penup()
        flower_turtle.left(90)

def drawFlowerPetals():
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

    # original code
    # flower_turtle.penup()
    # flower_turtle.color("red")
    # for i in range (18):
    #     flower_turtle.pensize(10)
    #     flower_turtle.penup()
    #     flower_turtle.forward(25)
    #     flower_turtle.pendown()
    #     flower_turtle.right(180)
    #     flower_turtle.right(90)
    #     flower_turtle.forward(10)
    #     flower_turtle.left(18)
    #     flower_turtle.forward(10)



def main():
    drawFlowerStem()
    drawFlowerLeaves()
    drawFlowerTurtle()
    drawFlowerPetals()

main()
wn.exitonclick()


