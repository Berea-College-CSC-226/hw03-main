#################################################################################
# Author: MAHAK KUMAWAT
# Username:MAHAK1729
# Assignment: HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: TO BUILD COOL STUFF AND LEARN FUNCTIONS
# Google Doc Link: https://docs.google.com/document/d/1XCSB1JgXj2vmlOMzZ0txzvQJ5EK_cw7_2M5RI1vVwaM/edit]\
#################################################################################
# Acknowledgements:
# Used My own code for starter code from HW02
#################################################################################
import turtle


def sml_circle(shape):
    """
      Creates a small circle
    """
    shape.color("#c5dfd6")  # Sets circle color to light blue gray
    shape.goto(50, - 70)
    shape.pendown()
    shape.begin_fill()
    shape.circle(9)  # Draws small circle
    shape.end_fill()
    shape.penup()


def big_circle(shape):
    """
      Creates a big circle
    """
    shape.color('#BDBDBD')  # Sets circle color to medium silver gray
    shape.goto(50, - 70)
    shape.pendown()
    shape.begin_fill()
    shape.circle(18)  # Draws big circle
    shape.end_fill()
    shape.penup()


def triangle(shape):
    """
      Creates a triangle
    """
    for side in range(3):  # Makes triangle(s)
        shape.forward(100)
        shape.left(120)
    shape.end_fill()
    shape.penup()


def flame(shape):
    """
         Creates a flame
    """
    shape.goto(63, -140)  # Drawing flame
    shape.pendown()
    shape.color("#FF9800")  # Sets flame color to bright orange
    shape.fillcolor("#FF9800")
    shape.width(4)
    shape.right(90)
    shape.left(50)
    shape.forward(40)
    shape.right(125)
    shape.forward(30)
    shape.left(50)
    shape.forward(30)
    shape.right(125)
    shape.forward(30)
    shape.left(50)
    shape.forward(30)
    shape.right(125)
    shape.forward(45)
    shape.penup()


def rectangle(shape):
    """
            Creates a rectangle
    """
    shape.color('#CFD8DC')  # Sets triangle turtle color to light bluish gray
    shape.pendown()
    shape.width(2)
    shape.begin_fill()
    for side in range(2):
        shape.forward(100)
        shape.right(90)
        shape.forward(140)
        shape.right(90)
    shape.end_fill()
    shape.penup()


def title(shape):
    """
            Creates a title
    """
    shape.color("#5B69BB")  # Sets flame color to dark bluish
    shape.setpos(- 60, - 125)  # Gives position to write
    shape.write("To the moon!", align='right', font=("georgia", 44, "bold normal"), move=False)


def main():
    """
            Main Code
    """
    wn = turtle.Screen()  # Initiates turtle window
    turtle.colormode(255)  # Gives a color range to choose the rgb from / limits to
    wn.bgcolor('#ffb06d')  # Sets background color to light orange

    shape = turtle.Turtle()  # Initiates turtle shape
    shape.width(2)
    shape.color('#B0BEC5')  # Sets initial turtle color to light grayish blue
    shape.begin_fill()  # Fills with color

    triangle(shape)      # Calling function that helps us draw multiple triangles

    rectangle(shape)     # Calling function that helps us draw multiple triangles

    big_circle(shape)    # Calling function that helps us draw big circle

    sml_circle(shape)    # Calling function that helps us draw small circle

    flame(shape)         # Calling function that draws really cool flame

    title(shape)         # Writes to the moon on our screen

    wn.exitonclick()


main()
