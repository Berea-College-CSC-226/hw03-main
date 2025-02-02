import turtle
def makeGUI():
    wn=turtle.Screen()
    wn.exitonclick

def drawPorch():
     Turtle.forward(50)

def main():
     porchTurle = turtle.Turtle()
     makeGUI()
     drawPorch(porchTurtle)