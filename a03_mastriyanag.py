######################################################################
# Author: Vidya Mastriyana
# Username: mastriyanag
#
# Assignment: A03: A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
#
# Purpose:      Grow to appreciate pair programming a little more.
#               Continue practicing creating and using functions.
#               More practice on using the turtle library.
#               Learn about how computers represent colors.
#               Learn about source control and git.
#
# Google Doc Link: https://docs.google.com/document/d/13aT6B1HIOXcdvxoDP0TMXywOI2_qTq7BGoAx1ZcacPI/edit?usp=sharing
######################################################################
# Acknowledgements:
# Gazebo image: https://secure.img1-fg.wfcdn.com/im/77678980/compr-r85/4010/40109781/default_name.jpg
#################################################################################
import turtle

# Gazebo Time!

def build_roof(shape):
    """
    Draws a solid, gray, triangular roof
    """
    shape.penup()
    shape.setpos(-100, 100)
    shape.color('gray')
    shape.begin_fill()
    for side in range(3):
        shape.pendown
        shape.forward(200)
        shape.left(120)

    shape.end_fill()

def build_gazebo(wn, shape):
    """
    The main gazebo area, illustrated via a .gif
    """
    # ...
    wn.register_shape("1gazebo.gif")
    shape.penup()
    shape.setpos(0, -70)
    shape.pendown()
    shape.shape("1gazebo.gif")               # Sets the shape to an image in the library (above)
    shape.stamp()

def draw_sun(shape):
    """
    Draws a sun in the top right corner
    """
    shape.penup()
    shape.setpos(-100, 175)
    shape.color("yellow")
    shape.pendown()
    shape.begin_fill()
    shape.circle(35)
    shape.end_fill()

def draw_shadow(shape):
    """
    Draws the gazebo's shadow, in relation to the sun.
    """
    shape.penup()
    shape.setpos(0, -245)
    shape.color("black")
    shape.pendown()
    shape.begin_fill()
    for side in range(2):                   # Shape is a parallelogram (I think that's what it's called...)
        shape.forward(100)
        shape.right(60)
        shape.forward(100)
        shape.right(120)
        shape.forward(100)
    shape.end_fill()

def title(shape):
    """
    Titles my beautiful work.

       """
    shape.color("#FF00FF")              # Color: Magenta (Hex)
    shape.penup()
    shape.setpos(200, 100)
    shape.write(".gif Gazebo", align='center', font=("Arial", 30, ("bold", "normal")))

def main():
    """
    Docstring for main. Calls all functions sequentially.
    """
    wn = turtle.Screen()
    wn.colormode(255)
    wn.bgcolor((102,255,102))           # Window background color, a light green (in RGB)
    shape = turtle.Turtle()
    shape.hideturtle()

    # FUNCTION CALLS:
    build_roof(shape)               # Function call to build_roof
    build_gazebo(wn,shape)          # Function call to build_gazebo
    draw_sun(shape)                 # Function call to draw_sun
    draw_shadow(shape)              # Function call to draw_shadow
    title(shape)                    # Function call to title

    wn.exitonclick()                # Exits window on click



main()
