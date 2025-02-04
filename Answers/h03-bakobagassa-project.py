#################################################################################
# Author: Saratou Bako Bagassa
# Username: bakobagassas
#
# Assignment: hw03
# Purpose: Drawing a house, a sun and a person.
#################################################################################
# Acknowledgements:I went through all my previous teamworks - mostly T03 - any time I was confused about the proper way to write a function
# link to docs document: https://docs.google.com/document/d/1PRZAWkCXwyBdSHiGf_T4-6e4DEXLePajUikn0E5IDvg/edit?usp=sharing
#
#################################################################################




import turtle

#defining function to draw a square
def drawSquare(elle, sz):
    for i in range (4):
        elle.forward(sz)
        elle.left(90)

#defining function to draw a triangle
def drawTriangle(elle, size):
    for i in range(3):
        elle.forward(size)
        elle.right(120)


# defining my main function
def main():
    elle = turtle.Turtle()
    wn = turtle.Screen()
    # set the background color to xanadu
    turtle.bgcolor("#66947D")
# placing the turtle in the lower left corner
    elle.penup()
    for i in range(2):
        elle.right(90)
        elle.forward(200)
    elle.right(180)
    elle.pendown()

    #setting up my pen size and color
    elle.pensize(15)
    elle.pencolor("gray")
    #calling the drawSquare function for the base of my house
    drawSquare(elle, 150)

    #adjusting the position of the turtle after it has finished drawing the square
    elle.left(90)
    elle.forward(150)
    elle.right(30)

    #calling the function so that elle can draw the roof of the house
    drawTriangle(elle, 150)

    #positioning the sun
    elle.penup()
    elle.forward(200)
    elle.right(60)
    elle.forward(200)
    elle.pendown()

    # Setting up the color and size for the sun
    elle.pensize(5)
    elle.pencolor("yellow")
    #drawing a sun
    elle.begin_fill()
    elle.fillcolor("yellow")
    elle.circle(50)
    elle.end_fill()
    elle.right(90)

    #Placing the pen for my next drawing
    elle.penup()
    elle.forward(200)
    elle.pendown()
    elle.pencolor("black")
    elle.left(90)

    #drawing a person
    hand = 40
    length = 70
    leg = 60
    elle.circle(20)
    elle.right(90)
    elle.forward(length)
    elle.backward(40)
    elle.right(30)
    elle.forward(hand)
    elle.backward(hand)
    elle.left(60)
    elle.forward(hand)
    elle.backward(hand)
    elle.right(30)
    elle.forward(length)
    elle.left(30)
    elle.forward(leg)
    elle.backward(leg)
    elle.right(60)
    elle.forward(leg)
    elle.backward(leg)

    wn.exitonclick()

main()

