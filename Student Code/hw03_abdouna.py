#################################################################################
# Author:Ahmed Abdoun
# Username:abdouna
#
# Assignment: hw03
# Purpose:creating house
# Google Doc Link:
#  https://docs.google.com/document/d/1KZfTUdIRz3Mj6UGTYCUxbxSI9waRUJT2TIGXhEEBugo/edit?usp=sharing
#################################################################################
# Acknowledgements:
#
#
#################################################################################
import turtle


def create_hut():
    hut = turtle.Turtle()                #Draws the shape of the hut and fills in the color
    hut.penup()
    hut.setpos(-230, -230)
    hut.left(60)
    hut.pendown()
    hut.begin_fill()
    hut.fillcolor("brown")
    hut.pensize(15)
    hut.forward(550)
    hut.right(120)
    hut.forward(550)
    hut.penup()
    hut.right(120)
    hut.forward(550)
    hut.end_fill()
    hut.hideturtle()


def create_details():
    door = turtle.Turtle()             #creates a rectangle inside of the hut shape to represent a door
    door.penup()
    door.setpos(0, -230)
    door.left(90)
    door.pendown()
    door.begin_fill()
    door.fillcolor("red")
    door.forward(200)
    door.right(90)
    door.forward(100)
    door.right(90)
    door.forward(200)
    door.penup()
    door.right(90)
    door.forward(100)
    door.end_fill()
    door.hideturtle()

def create_window():
    window= turtle.Turtle()            #creates a smaller square with crossing lines to represent a window
    window.penup()
    window.setpos(15,20 )
    window.pendown()
    window.begin_fill()
    window.fillcolor("#ADD8E6")
    for i in range(4):
        window.forward(70)
        window.left(90)
    window.end_fill()
    window.forward(35)
    window.left(90)
    window.forward(70)
    window.right(90)
    window.forward(35)
    window.right(90)
    window.forward(35)
    window.right(90)
    window.forward(70)
    window.hideturtle()

def main():
    wn = turtle.Screen() #creates screen and sets background color to sky blue, then calls the hut function,
    wn.bgcolor("#87CEEB") # the door function and the window function in succession where the program can be closed upon clicking on it
    create_hut()
    create_details()
    create_window()
    wn.exitonclick()

main()