######################################################################
# Author: Concepta Njolima
# Username: njolimac
#
# Assignment: a03: A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: To draw a guitar
# Google link: https://docs.google.com/document/d/11YvbLzDSJ61SnGrrocbZ9Yq0Z_p5AJKAuERopqjMpi4/edit?usp=sharing


# Acknowledgements:
# Liberty Mupotsa during Computer Science Lab hours
# image:https://www.needpix.com/photo/174306/spotlight-limelight-lighting-lights-stage-show-spot-yellow-focus
######################################################################
def draw_string(turtle):
    """
        This function draws the strings to the guitar
       :param turtle: The name of the turtle
       :return: None
       """

    turtle.penup()
    length = 35

    turtle.setpos(60, -45)
    for i in range(5):
        turtle.penup()
        turtle.left(90)
        turtle.pendown()
        turtle.forward(300)
        turtle.left(90)
        turtle.penup()
        length = length - 6
        turtle.forward(length - 6)


def draw_rectangle(turtle):
    """
        This function draws the Guitar handle
       :param turtle: The name of the turtle
       :return: None
       """
    turtle.color(139,69,19)
    turtle.penup()
    turtle.setpos(30, -45)
    turtle.begin_fill()
    turtle.pendown()
    for i in range(2):
        turtle.forward(40)
        turtle.left(90)
        turtle.forward(300)
        turtle.left(90)
    turtle.end_fill()

def draw_upper_curve(turtle):
    """
    This draws the upper curving of the guitar
    :param turtle: The name of the turtle
    :return: None
    """


    turtle.circle(-40, 100)
    turtle.seth(0)
    turtle.forward(90)
    turtle.circle(-44, 80)
    turtle.forward(4)



def draw_left_lower_curve(turtle):
    """
    This functions draws the left lower curve of the guitar
    :param turtle: The name of the turtle
    :return:None
    """

    turtle.penup()
    turtle.setpos(-100, -145)
    turtle.pendown()
    turtle.speed(0)
    for i in range(8):
        turtle.forward(10)
        turtle.left(10)
    turtle.seth(90)
    turtle.forward(100)



def draw_right_lower_curve(turtle):
    """
    This functions draws the left lower curve of the guitar
    :param turtle: The name of the turtle
    :return:None
    """

    turtle.penup()
    turtle.setpos(200, -195)
    turtle.pendown()
    turtle.speed(0)

    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    for i in range(8):
        turtle.forward(10)
        turtle.right(10)
    turtle.seth(90)
    turtle.forward(100)



def draw_circle(turtle):
    """
    This draw the inner circle of the guitar
    :param turtle: this is the name of the turtle to be used in the drawing
    :return: None
    """
    turtle.penup()
    turtle.setpos(50, -80)
    turtle.pendown()
    turtle.circle(radius=19)


def draw_bottom(turtle):
    """
    This function draws the 2D representation of a guitar
    :param turtle: The name of the turtle to be used
    :return: None
    """


    turtle.penup()
    turtle.setpos(200, -195)
    turtle.pendown()
    turtle.right(90)
    turtle.circle(radius=-150, extent=180)
    turtle.forward(50)
    # print(turtle.pos())


def main():
    """"This is where everything begins
    """
    import turtle
    wn = turtle.Screen()
    wn.colormode(255)
    wn.bgcolor(205,133,63)
    wn.bgpic(picname="spotlight.png")
    # Set the turtle variables and maximum speed
    circle_pen = turtle.Turtle()
    circle_pen.speed(0)
    pencil = turtle.Turtle()
    pencil.speed(0)
    curving = turtle.Turtle()
    curving.speed(0)
    rect = turtle.Turtle()
    rect.speed(0)
    string = turtle.Turtle()
    string.speed(0)
    # Function calls
    draw_circle(circle_pen)
    draw_bottom(pencil)
    draw_left_lower_curve(curving)
    draw_right_lower_curve(circle_pen)
    draw_upper_curve(curving)
    draw_rectangle(rect)
    draw_string(string)
    pencil.write("MY GUITAR", move=False, align='right', font=("Arial", 30, ("bold", "normal")))

    wn.exitonclick()


main()
