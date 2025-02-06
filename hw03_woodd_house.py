#################################################################################
# Username:woodd
from turtle import Turtle


# Google Doc Link: https://docs.google.com/document/d/1hR3vQZg9h3VkzSt2vV9erAGYUh89hPb0rmL-ib4MJRc/edit?usp=sharing
################################################################################


def draw_grass(greg):
    """
    draws a green box at the bottom of the screen for grass
    """
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



def draw_house(david):
    """
    draws a house on the grass
    """
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

def draw_tree(tree):
    '''
    A function that draws the tree on the grass
    '''
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


def main():
    import turtle
    wn = turtle.Screen()
    wn.bgcolor("lightblue")

    wn.colormode(255)
    """
    The main function of the program. Draws a house and tree on the grass.
    """
    # Main is creating the turtle and screen then runs the other functions.

    tree = turtle.Turtle()
    david = turtle.Turtle()
    greg = turtle.Turtle()
    draw_grass(greg)
    draw_house(david)
    draw_tree(tree)
    wn.exitonclick() # makes it to where you can click on the screen to close it

main()  # Starts the program
