
#################################################################################
# Author: Joyce Mukalamusi
# Username: mukalamusij
#
# Assignment: HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose:
# Google Doc Link: https://docs.google.com/document/d/16yXRh2zAV79Lqzp0jjNsU5dQf5AVqUKSO7DxrRJjoeo/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################


import turtle as h

def draw_square(side_length):
    for i in range(4):
        house.forward(side_length)
        house.left(90)


# function to draw triangle

def draw_triangle(base_length):
    for i in range(3):
        # house.width(15)
        house.forward(base_length)
        house.left(120)


# function to draw door

def draw_door():
    """
    draws door
    """
    house.penup()
    house.goto(-20, -100)
    house.pendown()
    house.begin_fill()
    house.color("brown")
    draw_square(40)
    house.end_fill()
    house.penup()
    house.goto(0, -100)
    house.pendown()



# func to draw the roof
def draw_roof():
    """
    attributes/draws the roof
    """
    house.width(100)
    house.penup()
    house.goto(-50, 100)
    house.pendown()
    house.begin_fill()
    house.color("red")
    draw_triangle(120)
    house.end_fill()
    house.penup()
    house.goto(0, 0)
    house.pendown()

def draw_sun():
    """
    yellow sun in corner
    """
    h.penup()
    h.goto(-335, 200)  # coordinates to position sun
    h.pendown()
    h.color("yellow")
    h.begin_fill()
    h.circle(150)
    h.end_fill()
    h.pendown()
    h.hideturtle()


# main function
def main():
    # code for text
    house.penup()
    house.goto(0, -200)  # coordinates

    text = "Joyce's little simple house"
    font = ("Arial", 16, "normal")
    color = "blue"

    house.color(color)
    house.write(text, font=font, align="center")

# sets up the screen
h.bgcolor("skyblue")

# creates turtle object
house = h.Turtle()

house.penup()
house.speed(5) # drawing speed
house.setpos(-100, -100)
house.pensize(7)
house.pendown()
draw_square(200)  # draw the house base

draw_door()  # draw the door
draw_roof()  # draw the roof
draw_sun()   # my sun


house.hideturtle() # hides turtle crusor
h.done()

h.speed(5)

# house.penup()
# house.goto(0, -200)  # coordinates
#
# text = "Joyce's little simple house"
# font = ("Arial", 16, "normal")
# color = "blue"
#
# house.color(color)
# house.write(text, font=font, align="center")

main()
