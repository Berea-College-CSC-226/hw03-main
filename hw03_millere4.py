########################################################################################################################
# Author: Liz Miller
# Username: millere4
# Assignment: HW03:Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Practice using functions and turtle library, learn about computer coloring, and learn about source control and git.
# Google Doc Link: https://docs.google.com/document/d/1UjeAgNqt2sr6U5eQ6sAq0yWgOL2Su_GQgJ_tg0iqL-o/edit?usp=sharing
########################################################################################################################
#Acknowledgements:
#Thread for learning how to add music into script from chatGPT https://chatgpt.com/share/67a01c5c-7b34-800b-8f00-c6f6b55c6526
#Google Doc for HWO3
#Python turtle-Turtle Graphics https://docs.python.org/3/library/turtle.html#compound-shapes
#Turtle senseis of note- Dr.Ballou, Dr.Scudder-Davis, Dr.Heggen
########################################################################################################################
########################################################################################################################

import turtle

"""
    imports turtle library
"""
########################################################################################################################
####################################################-extra imports-#####################################################
########################################################################################################################
import pygame               #attaching chatgpt thread I used to learn how to add this and threading into the script to incorporate music. https://chatgpt.com/share/67a01c5c-7b34-800b-8f00-c6f6b55c6526
"""                         
    imports pygame library. 
"""
import threading
"""
    imports threading library.
"""
####turtle fact no.1, turtles have a limiting membrane around their lungs that is attached via muscles to their fore and hind limbs. Walking/swimming, movement of legs, assists their breathing.
########################################################################################################################
####################################################-serious brows-#####################################################
########################################################################################################################
def angry_brow():
    turtle.Turtle()
    turtle.hideturtle()
    turtle.left(180)
    turtle.backward(22)
    turtle.stamp()
########################################################################################################################
###################################################-plays the best music-###############################################
########################################################################################################################
def protect_ya_neck():
    pygame.init()
    """
    initializes pygame mixer
    """
    pygame.mixer.music.load("Protect ya neck.mp3")
    """
    song path/loads this specific song
    """
    pygame.mixer.music.play(-1)
    """
    plays music on an indefinite loop
    """
wu_tang_magic=threading.Thread(target=protect_ya_neck)
"""
    creates thread for protect ya neck, attaches variable to it.
"""
wu_tang_magic.daemon=True
"""
makes the mp3 a daemon thread, so it will only terminate when the main thread terminates.
"""
wu_tang_magic.start()
"""
starts music thread
"""

########################################################################################################################
#### turtle fact no.2, turtles have temperature dependent sex determination. temperature fluctuations during incubation can result in only one sex turtle hatching from a clutch.
########################################################################################################################
#############################################-Text at top of screen-####################################################
########################################################################################################################
def long_neck_body_turtle():
    turtle.Turtle()
    """
    defines the_answer as a turtle object
    """
    turtle.hideturtle()
    """
    hides turtle shape
    """
    turtle.color((116, 201, 32))
    turtle.setpos(0, 230)
    """
    sets turtle position
    """
    turtle.write("Side neck turts gotta, ", move=False, align='center', font=("Bold", 45, ("bold")))
    """
    writes answer on turtle screen
    """
    #This creates the wording at the top of the picture, "side neck turts gotta,"

########################################################################################################################
#################################################-second line of words-#################################################
########################################################################################################################
def pleurodira_playlist():
    turtle.Turtle()
    """
    defines pleurodira as a turtle object
    """
    turtle.hideturtle()
    """
    hides turtle shape
    """
    turtle.color((87,112,92))
    """
    sets turtle color to a dark green
    """
    turtle.setpos(40, 158)
    """
    sets position of text
    """
    turtle.write("Protect ya neck!", move=False, align='center', font=("Bold", 37, ("bold")))
    """
    turtle displays text on screen
    """
    # This creates the wording above the picture, "Protect ya neck!"
########################################################################################################################
##################################################-turtle stamp frame-##################################################
########################################################################################################################
def traveling_turt_named_burt(): #first frame
    burt=turtle.Turtle()
    burt.color(2,154,68)
    burt.speed(2)
    burt.pensize(40)
    burt.hideturtle()
    burt.penup()
    burt.setpos(-255, -150)
    burt.shape("turtle")
    """
    sets turtle position
    """
    width = 17
    """
    width in number of turtles
    """
    height = 10
    """
    height in number of turtles
    """
    for _ in range(width): #starting from left corner of the picture, turtle moves right while stamping first side of frame
        burt.stamp()
        """
        Stamps turtle print
        """
        burt.tilt(15)  #neat, saw this in the python turtle graphics manual
        """
        tilts turtle, but keeps direction
        """
        burt.forward(30)
        """
        Move forward by 30 units before stamping
        """
        #The turtle moves thirty pixels before stamping and repeating that 17 times(width=17). burt.tilt tilts the turtle 15 degrees after each stamp
    burt.left(90)
    """
    Turn left by 90 degrees to go up
    """
    for _ in range(height): #right side, up while stamping
        burt.stamp()
        burt.tilt(15)
        """
        tilts turtle, but keeps direction
        """
        burt.forward(30)
        """
        move up by 30 pixels
        """
    burt.left(90) ###gotta be a way to repeat this instead of writing code out again for the second set of sides. Tried and could not make it fit in time, but it is possible and would be better.
    """
    turn left by 90 degrees
    """
    for _ in range(width): #move left across top while stamping
        burt.stamp()
        burt.tilt(15)
        burt.forward(30)
    burt.left(90)
    for _ in range(height):# Left side (move down) while stamping
        burt.stamp()
        burt.tilt(15)
        burt.forward(30)
    """
    results in turtle stamp frame around picture
    """
    # The creates the turtle frame. setpos is used to set the turtle at the corner, then width and height are provided and multiple loops are created to make the stamp repeatedly stamp across the screen before turning 90 degrees to do another side. After completing the side the turtle turns 90 degrees and does it again.
    ####################################################################################################################
    ##########################################-Second turtle stamp frame-###############################################
    ####################################################################################################################
def not_a_tiger(): #second frame
    tiger = turtle.Turtle()
    tiger.shape("turtle")
    tiger.color(255, 128, 0)
    tiger.speed(3)
    tiger.pensize(40)
    tiger.hideturtle()
    tiger.penup()
    tiger.left(180)
    tiger.setpos(285, -200)


    width =19
    """
    sets width of rectangle in turtles
    """
    height=14
    """
    sets height of rectangle in turtles
    """

    for i in range (width): # i and _ used interchangeably??
        tiger.stamp()
        tiger.tilt(20)
        tiger.forward(30)
    tiger.right(90)

    for _ in range(height):  # right side, going up
        tiger.stamp()
        tiger.tilt(20)
        tiger.forward(30)
        """
        move up by 30 pixels
        """
    tiger.right(90)
    """
    turn right by 90 degrees
    """
    for i in range(width):  # move across, toward left side
        tiger.stamp()
        tiger.tilt(20)
        tiger.forward(30)

    tiger.right(90)  # Turn left by 90 degrees to go down to start position

    # Left side (move down)
    for i in range(height):
        tiger.stamp()
        tiger.tilt(20)
        tiger.forward(30)
########################################################################################################################
####################################-Write "Wu Tang Forever with turtle "wu"-###########################################
########################################################################################################################
def wu_tang_for_life(): #this is my turtle spelling chaos, turtle moves about, lifting and dropping pen to write "Wu Tang Forever"
    turtle.Turtle()
    wu=turtle.Turtle()
    wu.color((255, 222, 0))
    wu.speed(8)
    wu.pensize(4)
    wu.hideturtle()
    wu.penup()
    wu.setpos(-140, -250)
    wu.pendown()
    wu.left(90)
    wu.forward(20)
    wu.backward(20)
    wu.right(90)
    wu.forward(10)
    wu.left(90)
    wu.forward(10)
    wu.backward(10)
    wu.right(90)
    wu.forward(10)
    wu.left(90)
    wu.forward(20)
    wu.backward(20)
    wu.right(90)
    #forms W
    wu.penup()
    """
    picks up pen 
    """
    wu.forward(8)
    wu.pendown()
    """
    puts pen down
    """
    #no line between letters
    wu.pendown()

    wu.left(90)
    wu.forward(10)
    wu.backward(10)
    wu.right(90)
    wu.forward(10)
    wu.left(90)
    wu.forward(10)
    wu.backward(10)
    wu.right(90)
    #forms u

    wu.penup()
    wu.forward(18)
    wu.pendown()
    """
    moves pen to next location
    """
    wu.left(90)
    wu.forward(20)
    wu.left(90)
    wu.forward(8)
    wu.backward(16)
    wu.forward(8)
    wu.left(90)
    wu.forward(20)
    wu.left(90) #->
    #forms T

    wu.penup()
    wu.forward(10)
    wu.pendown()
    """
    moves pen to next location
    """
    wu.left(90)
    wu.forward(10)
    wu.right(90)
    wu.forward(10)
    wu.right(90)
    wu.backward(2)
    wu.forward(12)
    wu.right(90)
    wu.forward(10)
    wu.left(180)
    wu.forward(10)#->
    #forms a
    wu.penup()
    wu.forward(10)
    wu.pendown()
    """
    moves pen to next location
    """
    wu.left(90)
    wu.forward(12)
    wu.backward(2)
    wu.right(90)
    wu.forward(10)
    wu.right(90)
    wu.forward(10)
    wu.left(90)
    #forms n
    wu.penup()
    wu.forward(10)
    wu.pendown()
    """
    moves pen to next location
    """
    wu.forward(10)
    wu.backward(10)
    wu.left(90)
    wu.forward(10)
    wu.right(90)
    wu.forward(10)
    wu.right(90)
    wu.forward(20)
    wu.right(90)
    wu.forward(10)
    wu.left(180)
    wu.forward(10)
    wu.left(90)
    wu.forward(10)
    wu.right(90) #->
    #forms g
    wu.penup()
    wu.forward(20)
    wu.pendown()
    """
    moves pen to next location
    """

    wu.left(90)
    wu.forward(20)
    wu.right(90)
    wu.forward(12)
    wu.backward(12)
    wu.right(90)
    wu.forward(10)
    wu.left(90)
    wu.forward(10)
    wu.backward(10)
    wu.right(90)
    wu.forward(10)
    wu.left(90)
    wu.penup()
    wu.forward(20)#-> and set at start of new number
    #makes F
    wu.pendown()

    wu.forward(10)
    wu.left(90)
    wu.forward(10)
    wu.left(90)
    wu.forward(10)
    wu.left(90)
    wu.forward(10)
    wu.left(90)
    wu.forward(8)
    #makes o
    wu.penup()
    wu.forward(10)
    wu.pendown()
    """
    moves pen to next location
    """
    wu.left(90)
    wu.forward(12)
    wu.backward(2)
    wu.right(90)
    wu.forward(10)
    wu.right(90)
    wu.forward(2)
    wu.penup()
    wu.forward(8)
    wu.left(90)#-> and pen up. I set myself up at where I would have ended on characters that have right sides.
    #makes r
    wu.forward(10)
    wu.pendown()


    wu.left(90)
    wu.forward(10)
    wu.right(90)
    wu.forward(10)
    wu.right(90)
    wu.forward(5)
    wu.right(90)
    wu.forward(10)
    wu.left(90)
    wu.forward(5)
    wu.left(90)
    wu.forward(10)
    #forms e
    wu.penup()
    wu.forward(15)
    wu.pendown()

    wu.left(125)
    wu.forward(14)
    wu.backward(14)
    wu.right(70)
    wu.forward(14)
    wu.backward(14)
    wu.right(55)  # ->
    # forms v

    wu.penup()
    wu.forward(15)
    wu.pendown()
    """
    moves pen to next location
    """
    wu.left(90)
    wu.forward(10)
    wu.right(90)
    wu.forward(10)
    wu.right(90)
    wu.forward(5)
    wu.right(90)
    wu.forward(10)
    wu.left(90)
    wu.forward(5)
    wu.left(90)
    wu.forward(10)
    # forms e
    wu.penup()
    wu.forward(10)
    wu.pendown()
    """
    moves pen to next location
    """
    wu.left(90)
    wu.forward(12)
    wu.backward(2)
    wu.right(90)
    wu.forward(10)
    wu.right(90)
    wu.forward(2)
    wu.penup()
    wu.forward(8)
    wu.left(90)  # -> and pen up
    # makes r
    #yay, tiger turtle with the words
########################################################################################################################
######################################################-spirals-#########################################################
########################################################################################################################
def create_spiral(x, y): #heck yeah, fancy spirals thingies.  Like spiracles, elasmobranch external opening of the otic capsule represent
    spiraclez = turtle.Turtle()
    spiraclez.pensize(3)
    spiraclez.color(118, 255, 242)
    spiraclez.penup()
    spiraclez.hideturtle()
    spiraclez.setpos(x, y)
    spiraclez.pendown()
    spiraclez.speed(0)

    distance = 1
    """
    starting distance turtle will move before turning
    """
    angle = 137.5 #apparently this is the golden angel for spirals
    """
    angle turtle turns after each move
    """
    num_steps = 150
    """
    total number of steps the turtle will take
    """

    for i in range(num_steps):
        """
        runs the loop for what ever number "num_steps" is set to
        """
        spiraclez.forward(distance)
        spiraclez.color(20,100,200)
        spiraclez.right(angle)
        spiraclez.forward(distance)
        spiraclez.color(200, 100, 20)
        spiraclez.right(angle)
        spiraclez.forward(distance)
        spiraclez.color(118, 255, 242)
        spiraclez.right(angle)
        """
        angle at which the turtle moves after each movement
        """
        distance += 1
        """
        increasing turtle movement distance for each step
        """

def main():
    wn = turtle.Screen()
    """
    Creates screen and assigns it the variable wn
    """
    wn.setup(800,600)
    """ 
    sets up the screen size
    """
    wn.bgcolor("Black")
    wn.bgpic("Wave Swimming GIF by Roger Williams Park Zoo.gif")
    """
    Sets background image
    """
    turtle.hideturtle()
    """
    hides turtle shape
    """
    turtle.colormode(255)
    """
    sets RGB color mode
    """
    turtle.penup()  #keep so floating turtles aren't seen leaving the origin
    """
    lifts turtle pen at origin
    """

    angry_brow()
    protect_ya_neck()
    long_neck_body_turtle()
    pleurodira_playlist()
    traveling_turt_named_burt()
    not_a_tiger()
    wu_tang_for_life()
    create_spiral(-380,-150)
    create_spiral(380,150)
    create_spiral(-380,0)
    create_spiral(380, 0)
    create_spiral(-380,150)
    create_spiral(380,-150)
    """
    create spirals at these locations
    """
    # 6 spiracles is always better than 1, in my opinion.

    wn = turtle.Screen()
    wn.exitonclick()
    turtle.done()
if __name__ == "__main__":
    main() # Starts the program
