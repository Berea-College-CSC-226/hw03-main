#################################################################################
# Username:woodd
# Google Doc Link: https://docs.google.com/document/d/1hR3vQZg9h3VkzSt2vV9erAGYUh89hPb0rmL-ib4MJRc/edit?usp=sharing
################################################################################

import turtle
wn = turtle.Screen()
wn.bgcolor("lightblue")

wn.colormode(255)



def draw_grass():
    greg = turtle.Turtle()
    greg.speed(100)
    greg.pencolor(20,235,90)
    greg.fillcolor(20,235,90)
    greg.penup()
    greg.setpos(-350,-90)
    greg.pendown()
    greg.begin_fill()
    for i in range(2):
        greg.forward(680)
        greg.right(90)
        greg.forward(680)
    greg.end_fill()
    """
    I am drawing a grass on the screen
    """
    pass
    # ....


def draw_house():
    david = turtle.Turtle()
    david.speed(100)
    david.pencolor(180,0,0)
    david.fillcolor(180,0,0)
    david.begin_fill()
    for i in range(2):
        david.forward(90)
        david.right(90)
        david.forward(90)
        david.right(90)
    david.end_fill()
    david.pencolor(80, 0, 255)
    david.fillcolor(80, 0, 255)
    david.begin_fill()
    for i in range(3):
        david.forward(90)
        david.left(120)
    david.end_fill()
    """
    draws a house on the grass
    """
    pass
    # ...
def draw_tree():
    tree = turtle.Turtle()
    tree.speed(100)
    tree.pencolor(140,70,10)
    tree.fillcolor(140,70,10)
    tree.penup()
    tree.setpos(-250,-90)
    tree.pendown()
    tree.begin_fill()
    for i in range(2):
        tree.forward(20)
        tree.left(90)
        tree.forward(200)
        tree.left(90)
    tree.end_fill()
    tree.left(90)
    tree.forward(200)
    tree.right(90)
    tree.forward(20)
    tree.pencolor(10, 140, 50)
    tree.fillcolor(10, 140, 50)
    tree.begin_fill()
    tree.circle(100) #draws a circle for the tree top
    tree.end_fill()
'''
A function that draws the tree on the grass 
'''

def main():
    """
    The main function of the program. I have it set to where when its called it calls the other functions.
    """
    # Main is calling the other functions
    draw_grass()
    draw_house()
    draw_tree()


main()  # Starts the program
wn.exitonclick() # makes it to where you can click on the screen to close it