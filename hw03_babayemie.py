#################################################################################
# Author: Elijah Babayemi
# Username: babayemie
#
# Assignment:HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Continue practicing creating and using functions, more practice on using the turtle library, learn about how computers represent colors, and learn about source control and Git.
#
# Google Doc Link: https://docs.google.com/document/d/1X9d90s3RxZa3LG8GFm7Y8XtmVSOv1ai_OpNtu0xGtpk/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################


import turtle




def make_house():
   turtle.penup()
   turtle.goto(-50, -50)
   turtle.pendown()


   turtle.fillcolor("#FF3C00")  # red color
   turtle.begin_fill()
   for _ in range(4):
       turtle.forward(100)
       turtle.left(90)
   turtle.end_fill()


   #Draws a door for house
   turtle.penup()
   turtle.fillcolor("#060D04")
   turtle.begin_fill()
   turtle.goto(-15,-50)
   for _ in range(4):
       turtle.forward(30)
       turtle.left(90)
   turtle.end_fill()






   # Draws a roof for the square to make it look like a house.
def draw_roof(shape):
   shape.penup()
   shape.fillcolor("#898685")
   shape.begin_fill()
   shape.goto(50,50)
   shape.pendown()
   shape.goto(0, 100)
   shape.goto(-50, 50)
   shape.goto(50, 50)
   shape.end_fill()
   shape.hideturtle()


#Draws a tree beside the house.
def draw_tree():
   turtle.fillcolor("#4A3209")
   turtle.begin_fill()
   turtle.penup()
   turtle.goto(130, -50)
   turtle.pendown()
   for _ in range(2):
       turtle.forward(20)
       turtle.left(90)
       turtle.forward(40)
       turtle.left(90)
       print(turtle.pos())  #Printing a location so I can find a good place to put the green circle.
   turtle.end_fill()


   #Draws a circle that represents the leaves
   turtle.fillcolor("#2FA118")
   turtle.begin_fill()
   turtle.penup()
   turtle.goto(140,-10) #Putting the circle in a location close to coordinates I got from "print(turtle.pos())" thats in the center of the rectangle.
   turtle.pendown()
   turtle.circle(30)
   turtle.end_fill()














def sun():
   turtle.penup()
   turtle.goto(-150, 100)
   turtle.pendown()


   turtle.fillcolor("#FFDE00")  # Yellow color
   turtle.begin_fill()
   turtle.circle(30)
   turtle.end_fill()








def main():


   shape = turtle.Turtle()


   #Making turtle screen
   wn = turtle.Screen()
   wn.bgcolor("lightblue")




   # Calls Functions
   make_house()
   draw_roof(shape)
   draw_tree()
   sun()




   turtle.hideturtle()


   wn.exitonclick()
main()  # Starts the program!





