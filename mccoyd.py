################################
# Destiney McCoy
# # Username: mccoyd
# # Assignment: a03:Fully Functional Gitty Psychedelic Robotic Turtles (DE)
# google doc: https://docs.google.com/document/d/1RqEiIBNMvMeu62zFgvN_i5Zpmoj-cZ3gNBs0sozEvB8/edit?usp=sharing
# attributes: Will & Darrian
################################
import turtle


def first_square(turt,sz):
    """
    make first square for instagram logo
    """
    turtle.up()
    turtle.goto(-50, -75)
    turtle.down()
    turtle.color('white')
    turtle.begin_fill()
    for i in range(4):            # draw square with round edges
        turtle.fd(270)
        turtle.circle(100, 90)
        turtle.fd(270)
        turtle.circle(100, 90)
    turtle.end_fill()
    pass
    # ...


def small_square(turt,sz):
    """
    inside square for logo
    """
    turtle.up()
    turtle.goto(-15, -5)
    turtle.down()
    turtle.color('red')
    turtle.begin_fill()
    for i in range(4):  # draw square with round edges
        turtle.fd(200)
        turtle.circle(100, 90)
        turtle.fd(100)
        turtle.circle(100, 90)
    turtle.end_fill()
    pass
    # ...

def triangle_shape():
    """
    design sideways triangle
    """
    turtle.up()
    turtle.goto(50, 175)
    turtle.down()
    turtle.color('white')
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(100)
    for i in range(2):
        turtle.left(120)
        turtle.forward(100)
    turtle.end_fill()


def main():
    """
    Create the Youtube Logo
    """
    wn= turtle.Screen()
    wn.bgcolor('#738678')
    turtle.speed(0)
    turtle.hideturtle()
    turtle.setup(500,500)
    turtle.title('Welcome to youtube')
    turtle.speed(0)
    turtle.up()
    turtle.hideturtle()

    # ...
    first_square(turtle,2000)            # Function call to function_1
    small_square(turtle,500)
    triangle_shape()

    dee = turtle.Turtle()
    dee.pensize(1)
    dee.forward(320)
    dee.hideturtle()
    dee.clear()
    dee.color("black")
    style = ('gothic', 70, 'italic')
    dee.write('YouTube', font=style)


    wn.exitonclick()


main()