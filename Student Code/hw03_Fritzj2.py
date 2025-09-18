


#################################################################################
# Author: Julius Fritz
# Username: Fritzj2
#
# Assignment: hw03
# Purpose: Learn to use git and gitHub to push and pull branches, get feedback, and get more practice with turtle
# Google Doc Link: https://docs.google.com/document/d/11-bhBE_z4YSAgW-Wrwi5ediloF5m-LBPOzNu8RYMyJ0/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################


import turtle
import random

def Trunk_Draw():
    trunk = turtle.Turtle()
    trunk.shape("square")
    trunk.color("brown")
    trunk.speed(0) #TODO Change this off of 0
    trunk.teleport(450, 150)
    trunk.begin_fill()
    trunk.right(90)
    trunk.circle(50,100)
    trunk.left(350-180)
    trunk.forward(300)
    trunk.right(180)
    trunk.circle(50,89.95)
    #This is the code for the base of the trunk with the curves
    trunk.right(10)
    trunk.fd(300)
    trunk.right(80)
    trunk.forward(95)
    trunk.end_fill()
    trunk.pensize(1)
    trunk.teleport(-250,0)


    #Draws the trunk of the tree
    pass

def Trunk_texture():
    texture = turtle.Turtle()
    texture.color(0.44,0.09,0.04)
    texture.speed(0)
    texture.pensize(2)
    texture.right(90)
    for i in range(15):
        texture.teleport(random.randint(315, 400),random.randint(400,425))
        texture.forward(random.randint(175, 300))
    #this makes a random texture pattern on the tree
    texture.teleport(-250, 0)


    pass
def Trunk_Hole():
    hole = turtle.Turtle()
    hole.color('black')
    hole.speed(0)
    hole.teleport(325, 250)
    hole.begin_fill()
    hole.circle(25)
    hole.end_fill()
    hole.teleport(-250,0)
    #Creates the hole on the tree
def Leaves():
    leaves = turtle.Turtle()
    leaves.color(1, 0.121,0.4)
    leaves.shape('square')
    leaves.speed(0)
    leaves.penup()
    for i in range(150):
        leaves.teleport(random.randint(200,600),random.randint(350,500))
        leaves.stamp()
        leaves.color(1,random.randint(5,65)/255,random.randint(70,155)/255)
    #center leaves

    for i in range(150):
        leaves.teleport(random.randint(100 ,700), random.randint(300, 600))
        leaves.stamp()
        leaves.color(1, random.randint(5, 65) / 255, random.randint(70, 155) / 255)
    #Spread top leaves

    for i in range(100):
        leaves.teleport(random.randint(175 ,650), random.randint(450, 600))
        leaves.stamp()
        leaves.color(1, random.randint(85, 135) / 255, random.randint(135, 245) / 255)
    #For the Leaves up top

    for i in range(100):
        leaves.teleport(random.randint(50 ,750), random.randint(25, 100))
        leaves.stamp()
        leaves.color(random.randint(200, 255)/255
                     , random.randint(5, 65) / 255
                     , random.randint(70, 155) / 255)

    for i in range(50):
        leaves.teleport(random.randint(50 ,250), random.randint(75, 125))
        leaves.stamp()
        leaves.color(random.randint(200,255)/255
                     , random.randint(5, 65) / 255
                     , random.randint(70, 155) / 255)

    for i in range(50):
        leaves.teleport(random.randint(450 ,750), random.randint(75, 125))
        leaves.stamp()
        leaves.color(random.randint(200,255)/255
                     , random.randint(5, 65) / 255
                     , random.randint(70, 155) / 255)


    wn = turtle.Screen()
    wn.exitonclick()

def main():
    wn = turtle.Screen()
    turtle.setworldcoordinates(0, 0, 800, 600)
    wn.bgcolor("pink")


    # Function calls to function_1 and function_2.
    Trunk_Draw()
    Trunk_texture()
    Trunk_Hole()
    Leaves()
    #TODO Add the final function with the leaves
    # Now progreess done after making the pull from the main
main()  # Starts the program!