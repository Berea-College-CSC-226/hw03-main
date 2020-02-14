######################################################################
# Author: Christopher Rice
# Username: ricec3
#Google Doc Link: https://docs.google.com/document/d/1ANmSHhQXJY3ZONwnDIuHhWrGQpVYf9lQNOcYVucKYdo/edit?usp=sharing

# Assignment: A03
# Purpose: To very simply demonstrate the turtle library to demo shapes
######################################################################

import turtle


def making_box(alpha):
    """
    Function draws a filled square
    """
    alpha.pendown()
    alpha.pencolor(169,169,169)     #making the color of pen
    alpha.left(180)
    alpha.begin_fill()
    alpha.fillcolor(169,169,169)    #making the color of fill
    for i in range(4):
        alpha.forward(100)
        alpha.left(90)
    alpha.end_fill()

    pass
    # ...


def making_roof(alpha):
    """
   This function sends the turtle to (-50,50) and uses a loop to make some of the triangle and then finishes it.
   Also uses a fill
    """
    alpha.begin_fill()
    alpha.fillcolor("red")
    alpha.pencolor("red")
    alpha.setpos(-50,50)
    for i in range(2):
        alpha.right(120)
        alpha.forward(100)
    alpha.right(120)
    alpha.forward(50)
    alpha.end_fill()
    alpha.penup()
    pass
    # ...

def creating_door(alpha):
    """
   This function makes a zigzag pattern of lines that go right to left and then go down and then start a line left to
   right and then go down again
    """
    #Door
    alpha.setpos(-15,-60)
    alpha.pensize(5)
    alpha.pendown()
    alpha.begin_fill()
    alpha.pencolor("purple")
    alpha.fillcolor("purple")
    alpha.right(90)
    alpha.forward(50)
    alpha.right(90)
    alpha.forward(30)
    alpha.right(90)
    alpha.forward(50)
    alpha.end_fill()
    alpha.penup()


def creating_windows(alpha):
    """
   This function draws the last lines for the program to fill the box
    """
    #First Window
    alpha.setpos(25,25)
    alpha.pencolor("purple")
    alpha.fillcolor("purple")
    alpha.begin_fill()
    alpha.pendown()
    for x in range(4):  #making square
        alpha.forward(20)
        alpha.left(90)
    alpha.end_fill()
    alpha.penup()

    #Second Window
    alpha.setpos(-45, 25)
    alpha.pendown()
    alpha.begin_fill()
    for y in range(4):      #making square
        alpha.forward(20)
        alpha.left(90)
    alpha.end_fill()
    alpha.penup()


def making_ground_and_fence(alpha):
    """
    This function draws the last lines for the program to fill the box
    """
    #Ground
    alpha.setpos(-100, -60)
    alpha.pencolor("gray")
    alpha.pensize(12)
    alpha.pendown()
    alpha.left(90)
    alpha.forward(200)
    #Fence 1
    alpha.pencolor(162,42,42)
    alpha.left(90)
    alpha.forward(20)
    alpha.left(90)
    alpha.forward(40)
   #Fence 2
    alpha.penup()
    alpha.setpos(-65, -40)
    alpha.pendown()
    alpha.forward(40)
    alpha.left(90)
    alpha.forward(20)
    alpha.fillcolor("gray")

def makingearth(alpha):
    """
    This function draws the last lines for the program to fill the box
    """
    alpha.penup()
    alpha.setpos(-250, -70)
    alpha.begin_fill()
    alpha.pendown()
    alpha.fillcolor(165,42,42)
    alpha.pencolor(165,42,42)
    alpha.forward(250)
    alpha.left(90)
    alpha.forward(500)
    alpha.left(90)
    alpha.forward(250)
    alpha.left(90)

    #making grass
    alpha.pencolor("green")
    alpha.forward(500)
    alpha.end_fill()
    alpha.penup()
def windowbar_doorknob(alpha):
    """
    This function draws the last lines for the program to fill the box
    """

    #Windows
    alpha.pencolor(184,134,11)
    alpha.left(90)
    alpha.setpos(35,25)
    alpha.pensize(5)
    alpha.pendown()
    alpha.forward(22.5)
    alpha.penup()
    alpha.setpos(-35,25)
    alpha.pendown()
    alpha.forward(22.5)
    alpha.penup()
    alpha.setpos(-45,15)
    alpha.left(90)
    alpha.pendown()
    alpha.forward(22.5)
    alpha.penup()
    alpha.setpos(25,15)
    alpha.pendown()
    alpha.forward(22.5)
    alpha.penup()

    #Doorknob
    alpha.setpos(5,-30)
    alpha.shape("circle")
    alpha.shapesize(.5)
    alpha.stamp()
    alpha.penup

def sun(alpha):
    """
    This func
    """
    alpha.setpos(175,175)
    alpha.fillcolor("yellow")
    alpha.color("orange")
    alpha.shapesize(10)
    alpha.stamp()

def main():
    """
    This is the main function, it makes an house out of basic shapes with a yard,fence, the earth beneath it and the sun
    """
    alpha =turtle.Turtle()
    wn = turtle.Screen()
    wn.bgcolor('lightblue')
    wn.colormode(255)
    alpha.pensize(20)
    alpha.speed(250)
    alpha.penup()
    alpha.setpos(50,50)
    alpha.shape("arrow")
    alpha.color("black")

    # ...
    making_box(alpha)            # Function call to function_1
    making_roof(alpha)            # Function call to function_2
    creating_door(alpha)
    creating_windows(alpha)
    making_ground_and_fence(alpha)
    makingearth(alpha)
    windowbar_doorknob(alpha)
    sun(alpha)
    wn.exitonclick()
main()

