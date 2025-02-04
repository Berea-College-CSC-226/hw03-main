#################################################################################
# Author: Shadaria Mickler
# Username: micklers
# Date due: 02.05.2025
# Assignment: hw03
# Purpose: draw a creative picture
# Google Doc Link: https://docs.google.com/document/d/1WEhtVTPHLMAFKKGypZ0Am1P2qpQWqLWe3E2AFbuBAX0/edit?usp=sharing
#################################################################################
# Acknowledgements:
# Stackoverflow: https://stackoverflow.com/questions/51007893/how-can-i-draw-a-nice-spiral-in-python-with-turtle
# Scheme color: https://www.schemecolor.com/psychedelic-art.php
# Pinterest: https://www.pinterest.com/pin/how-to-draw-bart-simpson-step-by-step--787989266073274494/
#################################################################################
# useless change - import the turtle module

import turtle



def fill_spaces(self):
    """
    fill_spaces fills in the spaces between the head and face.
    """

    self.goto(-5,-5)             # Go to the position x = -5, y = -5
    self.fillcolor("#FAE20B")   # Sets the fill color
    self.begin_fill()          # Starts the filling
    self.forward(310)
    self.right(90)
    self.forward(220)
    self.right(90)
    self.forward(320)
    self.right(90)
    self.forward(130)
    self.left(90)
    self.forward(50)
    self.seth(60)
    self.forward(110)
    self.end_fill()

    #fill in tiny space
    self.goto(0,0)
    self.fillcolor("#FAE20B")
    self.begin_fill()
    self.right(30)
    self.forward(150)
    self.seth(-60)
    self.forward(100)
    self.end_fill()



def draw_head(self):
    """
        draw_head draws the head and hair.
    """

    self.penup()
    self.goto(275,-60)
    self.seth(45)
    self.circle(-40,65)
    self.left(100)
    self.pendown()
    self.fillcolor("#FAE20B")
    self.begin_fill()
    self.forward(350)
    self.seth(100)


    # Draws spike on the far right
    self.forward(100)  # go up forward
    self.seth(-120)
    self.forward(100)  # go down forward
    self.left(-140)

    # Draws the spikes in between
    for hair_spike in range(6):

        self.forward(90)  # go forward up
        self.seth(-120)
        self.forward(100) # go down forward
        self.left(-140)

    # Draws spike on the far left
    self.left(170)
    self.forward(200)
    self.right(90)
    self.circle(30,130)
    self.end_fill()


def draw_jaw(self):
    """
    draw_jaw draws the jaw, lip and neck of Bart's face.
    """

    # Draw the jaw/smile
    self.penup()        # Set the pen up
    self.goto(-100,-86) # Go to x = -100, y = -75
    self.seth(-110)
    self.pendown()
    self.fillcolor("#FAE20B")
    self.begin_fill()
    self.circle(-90,30)
    self.circle(30,150)
    self.seth(-10)
    self.circle(500,30)

    self.seth(95)
    self.circle(50,60)
    self.penup()
    self.goto(155.6,-154.1)
    self.pendown()
    self.seth(280)
    self.circle(-50,60)


    # Draws lip
    self.penup()
    self.goto(-20,-185)
    self.pendown()
    self.circle(30,160)
    self.seth(10)
    self.forward(40)
    self.right(105)

    #Draw neck
    self.forward(150)
    self.left(95)
    self.forward(260)
    self.left(85)
    self.forward(255)
    self.end_fill()


def draw_ears(self):
    """
    draw_ears draws the one ear of Bart's face.
    """

    # Draws ear
    self.penup()          # Set the pen up
    self.goto(290,-60)    # Go to x = 290, y = -60
    self.seth(45)         # Rotate the cursor 45 degrees
    self.pendown()        # Put the pen down
    self.fillcolor("#FAE20B")
    self.begin_fill()
    self.circle(-40,245)  # draw 245 degrees of a circle w/radius = -40


    self.penup()     # Set the pen up
    self.forward(20) # Go forward 20
    self.end_fill()
    self.seth(-315)  # rotate the cursor -315 degrees
    self.forward(15) # Go forward 15
    self.pendown()   # Put the pen down
    self.forward(50) # Draw a line 50 coordinates long



def draw_eyes(self):
    """
    draw_eyes draws the uneven eyes and pupils of Bart's face.
    """

    # Draws one eye
    self.fillcolor("white")
    self.seth(-45)  # Rotates the cursor -45 degrees
    self.begin_fill()
    self.goto(5,0)
    self.circle(80) # Draws a circle with radius = 80
    self.end_fill()

    # Draws second eye
    self.seth(-120) # Rotates the cursor to -120
    self.begin_fill()
    self.circle(-70, 280)
    self.end_fill()

    # Redraws the right eye to see the outline between the two eyes
    self.penup()
    self.goto(5,0)
    self.seth(-45)
    self.pendown()
    self.circle(80, 360)

    # Prompt user for a response
    user_input = input("Would you like to see Bart Simpson's funny eyes? Type [yes/no]: ")

    colors = ["#FFEB00", "#FC0019", "#01FF4F", "#FF01D7", "#5600CC", "#00EDF5"]
    positions = [(-60, 30), (60, 50)]  # Eye positions

    if user_input == "yes":
     # Nested loop: outer loop go to positions while inside loop draws hypnotic pupils
        for eye in range(2):
            self.penup()
            self.goto(positions[eye])  # Got to left (-60, 30) then right (60, 50)
            self.pendown()
            for swirl in range(48):
                self.pencolor(colors[swirl % 6])      # Go through trippy colors
                self.circle(swirl, 40)               # Draw half circles with increasing size

    elif user_input == "no":                       # Draws the eye pupils starting with the right eye
                for pupil in range(2):
                    self.penup()                 # Lift the pen up
                    self.goto(positions[pupil]) # Go to (x,y) first iteration, (x,y) second iteration
                    self.pendown()             # Put the pen down
                    self.fillcolor("black")   # Set the fillcolor "black"
                    self.begin_fill()        # Start filling
                    self.circle(10)         # Draw a circle "pupil" with a radius = 10
                    self.end_fill()        # Stop filling
    else:
        print("I guess no eyes for Bart Simpson!")



def draw_nose(self):
    """
    draw_nose draws the nose of Bart's face.
    """

    # Draws a nose
    self.penup()              # Set the pen up
    self.goto(7,-1)          # Go to x =7, y = -1
    self.seth(-145)         # Rotate the cursor -145 degrees
    self.pendown()         # Put the pen down
    self.fillcolor("#FAE20B") # Select golden yellow
    self.begin_fill()    # Start filling
    self.circle(-90,40) # Draw the first part of the nose
    self.forward(25)
    self.circle(40,180)# Draw the rounded part
    self.forward(25)
    self.circle(90,50)# Draw the bottom part of the nose
    self.end_fill()  # Stop filling



def main():
    """
    def_main creates and defines the objects of the Turtle as well as calls functions to draw Bart's face.
    """

    # Creates an instance of the Screen class "window"
    window = turtle.Screen()

    # Sets RGB color wheels;
    window.colormode(255)

    # Set background color to "turquoise blue"
    window.bgcolor(0, 255, 239)
    window.title("Bart Simpson")

    # Create an instance of the Turtle class "eyes"
    eyes = turtle.Turtle()            # This obj will draw the "eyes"
    eyes.hideturtle()                # Hides cursor
    eyes.pencolor("black")          # Sets pen color to "black"
    eyes.pensize(5)                # Sets pen size
    eyes.speed("fastest")

    # Create an instance of the Turtle class "nose"
    nose = turtle.Turtle()
    nose.hideturtle()
    nose.pensize(5)
    nose.speed("fastest")

    # Create an instance of the Turtle class "ears"
    ears = turtle.Turtle()
    ears.hideturtle()
    ears.pensize(5)
    ears.speed("fastest")

    # Create an instance of the Turtle class "head"
    head = turtle.Turtle()
    head.hideturtle()
    head.pensize(5)
    head.speed("fastest")

    # Create an instance of the Turtle class "jaw"
    jaw = turtle.Turtle()
    jaw.hideturtle()
    jaw.pensize(5)
    jaw.speed("fastest")

    # Create an instance of the Turtle class "fill"
    fill = turtle.Turtle()
    fill.hideturtle()
    fill.speed("fastest")

    # Call function & Pass objects as arguments
    fill_spaces(fill)
    draw_head(head)
    draw_jaw(jaw)
    draw_ears(ears)
    draw_eyes(eyes)
    draw_nose(nose)

    window.exitonclick()                  # Keeps window open

main()  # Function call