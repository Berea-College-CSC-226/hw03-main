import turtle
import random

#####################################################
# SETUP VARIABLES
ws = turtle.Screen()
ws.bgcolor("lightskyblue1")

koopa = turtle.Turtle()
koopa.pensize(10)
koopa.speed(0)

colorsStoneBase = ["maroon", "saddlebrown", "tan3", "tan4", "red4"]
colorsResort = ["firebrick4", "maroon"]
colorsRoof = ["azure", "azure1", "lavender"]
colorsRoof2 = ["lightsalmon", "lightsalmon", "lightsalmon3"]
colorsBackground = ["lightsteelblue1", "lightsteelblue2", "lightsteelblue", "lightsteelblue3"]

def bostro (x, y, palette, triangle):
    """
    Draws a boustrophedon rectangle. Randomly switches colors using input palette.
    Triangle decreases the tip of the rectangle to turn it into an isosceles trapezoid, or triangle if it ends up
    surpassing x.
    x and y are not pensize dependant, but Triangle unfortunately is

    Args:
        x: x distance of rectangle
        y: y distance of rectangle
        palette: randomly switches pencolors using this array of colors
        triangle: decrease the x of the rectangle for what amount for each line, effectively turning the rectangle into
            an isosceles trapezoid or triangle
    """
    random.seed(226)
    direction = 1
    for i in range(y//koopa.pensize()):
        lengthTaken = 0
        x -= triangle # decrease size (only triangle)
        while lengthTaken < x:
            step = 10*random.randint(3, 7)
            if lengthTaken + step >= x:
                step = x-lengthTaken
            koopa.pencolor(palette[random.randint(0,  len(palette)-1)])
            koopa.fd(step)
            lengthTaken += step
        koopa.up()
        koopa.left(90*direction)
        koopa.forward(koopa.pensize())
        koopa.left(90*direction)

        x -= triangle # decrease size (triangle only)
        koopa.forward(triangle) # same here

        koopa.down()
        direction *= -1

def background (thickness, palette):
    bg_width = 500
    koopa.pensize(thickness)
    for i in range (len(palette)):
        koopa.pencolor(palette[i])
        color = [palette[i]]
        bostro(bg_width, 50, color, False)
    koopa.pensize(10)

def colordemo(palette):
    for i in palette:
        koopa.pencolor(i)
        koopa.fd(20)

def rectangle (x, y, pen, fill):
    koopa.pencolor(pen)
    koopa.fillcolor(fill)
    koopa.begin_fill()
    for i in range(0,4):
        koopa.fd(y * (i%2) + x * ((i+1)%2))
        koopa.right(90)
    koopa.end_fill()
def main():

    #background(koopa, 50, colorsBackground)
    koopa.goto(-500, 100)
    thick = 150
    for i in range(0,4):
        koopa.pencolor(colorsBackground[i])
        koopa.pensize(thick)
        koopa.fd(1000)
        koopa.fd(-1000)
        koopa.right(90)
        koopa.fd(thick)
        koopa.left(90)

    koopa.up()
    koopa.goto(0,0)
    koopa.down()
    koopa.pensize(10)

    koopa.goto(-50,-400)
    bostro(550, 300, colorsStoneBase, False)

    koopa.right(180)
    rectangle(20, 90, "burlywood", "burlywood")
    koopa.right(180)

    bostro(300, 100, colorsResort, False)

    koopa.fd(-10)
    bostro(320, 140, colorsRoof, 7)
    bostro(123, 100, colorsRoof2, 7)

    for i in range(0,2):
        koopa.up()
        koopa.right(90)
        koopa.fd(130)
        koopa.left(90)
        koopa.fd(20)
        koopa.down()
        rectangle(30, 50, "lavender", "skyblue4")
        koopa.up()
        koopa.fd(-70)
        koopa.down()
        rectangle(30, 50, "lavender", "skyblue4")
        koopa.up()
        koopa.fd(55)

    ws.exitonclick()


main()