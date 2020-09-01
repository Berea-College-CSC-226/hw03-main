########################################################
# Author: Matthew Trigg
# Username: triggm

# Assignment: A03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Create something creative
####################################################
import turtle

wn = turtle.Screen()  # Set up the window and its attributes
wn.title("Good Looking Stop Sign")
wn.bgcolor("#9085FF")

johnna = turtle.Turtle()  # turtle to make the print
johnna.color('white')
johnna.hideturtle()


halt = turtle.Turtle()  # turtle that makes the octagon and fills it in
halt.color('red')

def draw_stopsign():  # makes red octagon
   """
   Draws octagon with a WHITE border and RED background
   """
   halt.penup()
   halt.goto(-100, -150)
   halt.pendown()  # Sets the turtle in the center of the screen

   halt.begin_fill()
   for i in range(8):
       halt.fd(160)
       halt.left(45)
   halt.end_fill()
   halt.hideturtle()


def write_text():   # writes the text "STOP"
   """
   Writes text to the screen.
   """
   johnna.penup()
   johnna.goto(-165, -40)
   johnna.pendown()

   johnna.write("STOP", font=('Impact', 110))
   johnna.hideturtle()


def main():
   """
   Makes the full stop sign
   """

   draw_stopsign()  # Calls draw_stopsign function

   write_text()     # Calls write_text function


main()

wn.exitonclick()
