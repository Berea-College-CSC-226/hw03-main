#################################################################################
# Author:Jaela Smith
# Username:smithj5
#
# Assignment:HW03
# Purpose:Homework
# Google Doc Link:https://docs.google.com/document/d/13CGHi_koGhI8SePSLn2inpXajzkOhXyslGOPkxyufRA/edit
#
#################################################################################
# Acknowledgements:I am creating a house with windows and flowers
#
#
#################################################################################


import turtle



def drawTriangle(sally):
    sally.penup()
    sally.forward(-150)
    sally.pendown()
    sally.forward(200)
    sally.left(127)
    sally.forward(200)
    sally.goto(-150,0)









def drawRectangle(ted):
    ted.penup()
    ted.forward(-150)
    ted.right(90)
    ted.pendown()
    ted.forward(250)
    ted.left(90)
    ted.forward(200)
    ted.right(90)
    ted.forward(-250)
    ted.penup()
    ted.goto(-100,-250)
    ted.pendown()
    ted.right(180)
    ted.forward(100)
    ted.right(90)
    ted.forward(75)
    ted.right(90)
    ted.forward(100)

def drawFlower(teddy):
    teddy.penup()
    teddy.goto(-200, -250)
    teddy.pendown()
    teddy.right(-90)
    teddy.forward(30)
    teddy.circle
    for i in range(20):
        # moving turtle 100 units forward
        teddy.forward(30)

        # rotating turtle 144 degree right
        teddy.right(30)

def main() :
    wn = turtle.Screen()

    sally = turtle.Turtle()
    ted = turtle.Turtle()
    teddy = turtle.Turtle()
    drawTriangle(sally)   #call to drawSquare
    drawRectangle(ted)          #drawRectangle
    drawFlower(teddy)                  #drawFlower

    wn.exitonclick()


main()