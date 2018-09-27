######################################################################
# Author: Morgan Benningfield
# Username: benningfieldm
#
# Assignment: A03: A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
#
# Purpose: Draws some triangles and supposed to look pretty. Totally not a reference to a Nintendo franchise.
#
# https://docs.google.com/document/d/1gZcK3zgjuXRP_axcvjqHHNq6AYC5Y-zop1d9dtkubIg/edit?usp=sharing
######################################################################
# Acknowledgements:
# You two for making the header outline.
# Rebekah Whitford for reexplaining some of the terms to me and referencing older assignments to look at.
# http://www.wolframalpha.com/widgets/gallery/view.jsp?id=c0abe9808671bca189c7e6a560739ae4 To find hex codes
# https://en.wikipedia.org/wiki/Equilateral_triangle Because I'm bad at geometry.
# https://cdn.shopify.com/s/files/1/0941/8552/products/Legend_of_Zelda_-_Triforce.jpg?v=1530023743 Okay fine I *really did*
# make something from a game
# Lovell's branch for reference on how to make words
####################################################################################

import turtle


def triangles(x, y):
   """
   Draws some triangles. HYAH!
   :param x: x coordinate of starting point
   :param y: same as x but y
   :return: None
   """
   hyah = turtle.Turtle()
   hyah.hideturtle()
   hyah.color("#C8B400")  # A golden color. Or mustard. Whelp.
   hyah.penup()
   hyah.setposition(x, y)
   hyah.pendown()
   hyah.begin_fill()
   for side in range(3):
       hyah.forward(200)
       hyah.left(120)
   hyah.end_fill()


def text(t, w):
   """
   Uses a turtle to write some words.
   :param t: Turtle used
   :param w: Words
   """
   t.goto(-20, -200)
   t.pendown()
   t.write(w, move=False, align='center', font=("Courier New", 29))


def main():
   """
   The main function. Sets the background color and also chooses where these triangles go.
   """
   window = turtle.Screen()
   window.bgcolor("green")  # Green is not a creative color
   triangles(25, -100)  # First triangle
   triangles(-175, -100)  # Second triangle
   triangles(-75, 75)  # THIRD TRIANGLE
   # PLOT TWIST: THERE'S AN INVISIBLE FORTH TRIANGLE. WHOOOAAA
   tortoise = turtle.Turtle()  # Not at turtle but a turtle. Tortoise. You shall write words.
   tortoise.hideturtle()
   tortoise.penup()
   words = "This is the TRIBORCE"  # Not the Triforce. The Triborce. Obviously better than the "original"
   text(tortoise, words)
   window.exitonclick()  # Makes it so I can exit on command rather than it trying to kick us out.


main()  # CALL THAT MAIN
