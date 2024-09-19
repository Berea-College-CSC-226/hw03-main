#################################################################################
# Author: Ayomide Oludairo
# Username: oludairoa
#
# Assignment: HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Learn how to use github push and pull requests
# Google Doc Link: https://docs.google.com/document/d/1yX8V99iRkV56ZTmNQmI9XwANLQ7LLj5dzj0nO0i1hgw/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle

def draw_rect(t, sz, sz2):
    """
    The draw square function creates the 4 sides of a rectangle (can be a square).
    Takes 3 inputs, the turtle t and the length of sides with 2 being parallel to each other on each side sz and sz2.
    """

    if int(sz) > 200:
        return "That value is too large try something smaller"

    # The code inside the for loop creates one right angle of a rectangle, so the loop is used to do it twice.
    for i in range(2):
        t.forward(sz)
        t.left(90)
        t.forward(sz2)
        t.left(90)

    # Puts the turtle back in its natural eastward facing position
    t.right(90)

def draw_parallelogram(t, sz, sz2):
    """
    Creates a parallelogram that will be the sides of the walls.
    This function must be called after the rectangle function as it begins where the rectangle ends.
    """
    t.left(45)
    t.forward(sz)
    t.left(45)
    t.forward(sz2)
    t.left(135)
    t.forward(sz)

def draw_roof(t, sz):
    """"
    This function will create a triangle that will serve as a roof for this shed
    Must be called after the parallelogram as it begins where the parallelogram ends.
    """
    t.right(90)
    t.forward(sz)
    t.left(90)
    t.forward(sz)

# Defining the main function where the code will run
def main():
    """
    Initialize two separate turtles that will create the body of the shed and a door.
    """
    wn = turtle.Screen()
    wn.colormode(225) # Enables the use of RGB color identification mode
    wn.bgcolor((173/255, 216/255, 230/255)) # Colors in rgb mode are represented in bits (0-1)

    james = turtle.Turtle()             # Creating the james turtle and changing its color
    james.color((255/255, 165/255, 0))

    suzie = turtle.Turtle()             # Creating the suzie turtle and changing its color
    suzie.color((0, 0, 0))

    # Move James more to the bottom left corner of the screen
    james.penup()
    james.backward(150)
    james.left(90)
    james.backward(150)
    james.pendown()

    # Function calls to function_1 and function_2.
    draw_rect(james, 100, 100)
    draw_parallelogram(james, 150, 100)
    draw_roof(james, 70)

    # Creating an extension of the roof to give it that 3d look
    james.backward(70)
    james.right(180)
    james.forward(150)
    james.right(90)
    james.forward(70)

    # Moving suzie to the correct location to place a door
    suzie.penup()
    suzie.backward(185)
    suzie.left(90)
    suzie.backward(150)
    suzie.pendown()

    # calling the function rect which will allow suzie draw a door
    draw_rect(suzie, 50, 25)

    # Hiding both turtles for a better viewing experience
    james.hideturtle()
    suzie.hideturtle()

    wn.exitonclick()

main()  # Starts the program.