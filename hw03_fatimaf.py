

#################################################################################
# Author: Faryal Fatima
# Username: fatimaf
#
# Assignment: Psychedelic Turtles
# Purpose: work on functions
# Google Doc Link:https://docs.google.com/document/d/1ajqtgMAZudl5i-qPUVEiolbzbEEewsNVbwFdmq1Xykk/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################

#setting the background and size for the turtle
import turtle
wn = turtle.Screen()
turtle.colormode(255)  # Enable RGB color mode
wn.bgcolor(173, 216, 230)# Set to light blue
turtle.pensize(4)


#funtion to draw the square for the house
def draw_square(size, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)
    turtle.end_fill()


#funtion to draw the triangle for the house
def draw_triangle(size, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(size)
        turtle.left(120)
    turtle.end_fill()

#funtion to draw the window for the house
def draw_circle(radius,color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

#function to draw the door for the house
def draw_rectangle(width, height, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
    turtle.end_fill()


# funtion to put all the functions for the componets of the house together to draw the house
def draw_house():

    draw_square(100, "red")
    # changing the position of the turtle after drawing the suare
    turtle.penup()
    turtle.goto(-90, 30)
    turtle.pendown()
    #calling the function to draw the triangle
    draw_triangle(100, "brown")
    # changing the position of the turtle after drawing the square
    turtle.penup()
    turtle.goto(-15, -20)
    turtle.pendown()
    #calling the function to draw the circle
    draw_circle(15,"yellow")
    # changing the position of the turtle after drawing the square
    turtle.penup()
    turtle.goto(-20, -70)
    turtle.pendown()
    # calling the function to draw the circle
    draw_rectangle(1, 40, "brown")
    turtle.penup()

# Function to draw the cloud using multiple circles
def draw_cloud():
    # Drawing the cloud by stamping circles
    cloud_positions = [(-10, 120), (-0, 130), (30, 120), (-20, 140), (5, 150),(10,130)]  # Positions for the cloud circles
    for pos in cloud_positions:
        turtle.penup()
        turtle.goto(pos)  # Move to each position in the cloud list
        turtle.pendown()
        draw_circle(15, "white")  # Draw each small circle for the cloud
#main funtion

def main():
    #adjusting the starting position for the turtle
    turtle.penup()
    turtle.goto(-90,-70)
    turtle.pendown()
    turtle.speed(0)

    draw_house() #calling the draw_house function
    draw_cloud() #calling the draw_cloud function


main()  # Starts the program!
wn.exitonclick()