########################################################################################################################
# HEADER BLOCK #
########################################################################################################################

import turtle
def makeGUI():
    """This function creates the GUI, instantiates then hides
    the turtle object and will return a variable that can be called into main."""
    wn=turtle.Screen()
    wn.bgcolor("blue") #Make cycle black, red, orange, yellow, green, blue, indigo, violet.
    porchTurtle = turtle.Turtle() #PyCharm indicates that the variable assignment is not
    porchTurtle.hideturtle() #hides the cursor immediately.
    return wn


def drawPorch(turtle):
    """ This function draws and colors the porch in the GUI."""
    turtle.begin_fill()
    turtle.fillcolor("red")
    turtle.forward(250)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(350)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.end_fill()


def drawPillarOne(turtle):
    """This function is responsible for creating and coloring
    a black pillar in the GUI. It is called by the main function."""
    turtle.fillcolor = "white"
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.end_fill()

def drawPillarTwo(turtle):
    """This function is responsible for creating and coloring
    a black pillar in the GUI."""
    turtle.fillcolor = "black"
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.end_fill()

def main():
    """The main function calls wn from makeGUI() **this was
    partly a solution for order of execution problems I was having**
    ,and to hide the porchTurtle cursors.
    It calls the two other functions in the program.
    The main function is a bit heavy in the sense that it also
    creates the two turtle objects, and performs some modification to
    the objects.
    I think it's possible to refactor this main() function to only
    have 3-5 lines, if I can get the understanding of returning
    arguments.
    """

    wn = makeGUI()
    pillarTurtleOne = turtle.Turtle()
    pillarTurtleTwo = turtle.Turtle()
    pillarTurtleOne.hideturtle()
    pillarTurtleTwo.color("white")
    pillarTurtleTwo.goto(200, 0)
    pillarTurtleTwo.hideturtle()
    porchTurtle = turtle.Turtle()
    porchTurtle.hideturtle()
    drawPorch(porchTurtle)
    drawPillarOne(pillarTurtleOne)
    drawPillarTwo(pillarTurtleTwo)
    wn.exitonclick()


main()