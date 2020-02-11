######################################################################
# Author: John Sangarie   TODO: Change this to your name, if modifying
# Username: sangariej        TODO: Change this to your username, if modifying
#
# Assignment: A03:
# Purpose: A Pair of Fully Functional Gitty Psychedelic
######################################################################
# Acknowledgements:
# Original: http://openbookproject.net/thinkcs/python/english3e/hello_little_turtles.html
##GOOGLE DOC https://drive.google.com/file/d/1sWatfcob_xHGro20bxqMUuoCVvJ1kcAI/view?usp=sharing
# Modifications by Dr. Jan Pearce, Dr. Mario Nakazawa, and Dr. Scott Heggen

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.

import turtle

def draw1(draw_car):
    """
    draw the car
    """
    draw_car.penup()
    draw_car.setpos(-273,0)   # set the position of draw_car turtle
    draw_car.pendown()
    draw_car.left(90)
    draw_car.forward(80)
    draw_car.fillcolor("#eb4d55")
    draw_car.begin_fill()
    for i in range(5):
        draw_car.right(90)
        draw_car.forward(100)
    draw_car.end_fill()
    draw_car.color("#fdba9a")
    draw_car.pensize(4)
    draw_car.left(45)
    draw_car.forward(120)
    draw_car.right(45)
    draw_car.forward(200)
    draw_car.right(45)
    draw_car.forward(120)
    draw_car.fillcolor("#eb4d55")    # fill the square
    draw_car.begin_fill()
    draw_car.left(45)
    draw_car.forward(100)
    for i in range (4):      # create the left sqaure
        draw_car.right(90)
        draw_car.forward(100)
    draw_car.end_fill()
    draw_car.right(180)
    draw_car.forward(469)

















def draw2(draw_tire):
    """
    draw the tires of the car
    """
    draw_tire.penup()
    draw_tire.right(90)
    draw_tire.forward(80)
    draw_tire.left(90)
    draw_tire.forward(120)
    draw_tire.pendown()
    draw_tire.pensize(5)
    draw_tire.color("#333333")
    draw_tire.circle(50)
    draw_tire.penup()
    draw_tire.right(90)
    draw_tire.forward(40)
    draw_tire.right(90)
    draw_tire.forward(180)
    draw_tire.right(90)
    draw_tire.forward(130)
    draw_tire.pendown()
    draw_tire.left(90)
    draw_tire.circle(50)
    draw_tire.penup()
    draw_tire.forward(80)
    draw_tire.left(90)
    draw_tire.forward(30)
    draw_tire.right(90)
    draw_tire.forward(36)
    draw_tire.right(180)
    draw_tire.pendown()
    draw_tire.pensize(5)
    draw_tire.forward(70)
    draw_tire.penup()
    draw_tire.forward(100)
    draw_tire.pendown()
    draw_tire.forward(80)
    draw_tire.penup()
    draw_tire.forward(100)
    draw_tire.pendown()
    draw_tire.forward(100)
    draw_tire.penup()
    draw_tire.setpos(280,120)
    draw_tire.write("MY CAR!!!", move = True , align = "center",font=("Arial",30,"normal") )
















def main():
    """
    call the two functions above
    """



    wn= turtle.Screen()
    draw_car = turtle.Turtle()
    draw_tire= turtle.Turtle()
    wn.bgcolor("#4f98ca")
    wn.title("John's Car")



    draw2(draw_tire)
    draw1(draw_car)
    wn.exitonclick()



main()







