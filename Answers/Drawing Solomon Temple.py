########################################################################################################################
# HEADER BLOCK #
########################################################################################################################

import turtle
def makeGUI():
    """This function creates the GUI, instantiates the turtle object
    and will be called into main."""
    wn=turtle.Screen()
    wn.bgcolor("blue") #Make cycle black, red, orange, yellow, green, blue, indigo, violet.
    porchTurtle = turtle.Turtle() #PyCharm indicates that the variable assignment is not
    # needed, and I confirmed that this works, but this is just for one turtle.
    #A=turtle.Turtle() Attempting to instantiate the turtle object in the makeGUI function
    # though, I am going to do it inside of the main() function, and pass the objects as a
    # parameter to the other functions that need it.
    #B=turtle.Turtle()
    #C=turtle.Turtle()
    porchTurtle.hideturtle() #hides the cursor immediately.
    return wn


def drawPorch(turtle): # I need a turtle object as a parameter here, using 't'.
    turtle.begin_fill()
    turtle.fillcolor("red")
    turtle.forward(250) #Line 22 refs. line 21.
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(350)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.end_fill()
    """DOCSTRING PLACEHOLDER"""
#    porchTurtle = turtle.Turtle() #Is the object properly defined?
#    turtle.forward(100)
#    return porchTurtle


def drawPillarOne(turtle):
    """DOCSTRING PLACEHOLDER"""
    turtle.fillcolor = "white"
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.end_fill()
    #turtle.forward(100)
    #turtle.left(90)
    #turtle.forward(50)
    #turtle.left(90)
    #turtle.forward(100)
    #turtle.left(90)
    #turtle.forward(70)
    #turtle.right(90)
    #turtle.forward(10)
    ##turtle.right(90)
    #turtle.forward(80)
    #turtle.right(90)
    #turtle.forward(10)
    #turtle.right(90)
    #turtle.forward(80)



def drawPillarTwo(turtle):
    """DOCSTRING PLACEHOLDER"""
    turtle.fillcolor = "black"
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.end_fill()
    #turtle.fillcolor = "black"
    #turtle.begin_fill()
    #turtle.left(90)
    #turtle.forward(100)
    #turtle.left(90)
    #turtle.forward(50)
    #turtle.left(90)
    #turtle.forward(100)
    #turtle.left(90)
    #turtle.forward(50)
    #turtle.left(90)
    #turtle.forward(100)
    #turtle.left(90)
    #turtle.forward(70)
    #turtle.right(90)
    #turtle.forward(10)
    #turtle.right(90)
    #turtle.forward(80)
    #turtle.right(90)
    #turtle.forward(10)
    #turtle.right(90)
    #turtle.forward(80)


#def drawStar(turtle):
    """DOCSTRING PLACEHOLDER"""
#    turtle.forward(50)

#def drawWindow(turtle):
    """DOCSTRING PLACEHOLDER"""
 #   turtle.forward(100)

#def colorShape():
    """DOCSTRING PLACEHOLDER"""

def main():
    """DOCSTRING PLACEHOLDER"""
    wn = makeGUI()
    pillarTurtleOne = turtle.Turtle()
    pillarTurtleTwo = turtle.Turtle()
    pillarTurtleOne.hideturtle()
    #pillarTurtleOne.pensize(10)
    pillarTurtleTwo.color("white")
    pillarTurtleTwo.goto(200, 0)
    pillarTurtleTwo.hideturtle()
    porchTurtle = turtle.Turtle()
    porchTurtle.hideturtle()
    #starTurtle = turtle.Turtle()
    #windowTurtle = turtle.Turtle()
    # makeGUI() #This function isn't needed? The program still runs when I comment it out?
    #turtle.Turtle() #Generates a turtle object using the .Turtle() method.
    drawPorch(porchTurtle) #Calls the turtle object defined in line 47 as porchTurtle, and acts on
    # the using process defined within the function drawPorch.
    #drawWindow(A) #Trying to call these unsuccessfully.
    #drawStar(A)
    #drawPillar(B)
    drawPillarOne(pillarTurtleOne)
    drawPillarTwo(pillarTurtleTwo)
    #drawStar(starTurtle)
    #drawWindow(windowTurtle)
    wn.exitonclick()


main()