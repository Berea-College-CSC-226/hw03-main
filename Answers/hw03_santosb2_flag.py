

#################################################################################
# Author:Bernave Santos
# Username:santosb2
#
# Assignment:HW03
# Purpose:
# Google Doc Link: https://docs.google.com/document/d/1dJwVSxuDfwrbqt-lodUltlvsNYP_PXK_SukVk725Yp8/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################
import turtle
wn = turtle.Screen()
tess = turtle.Turtle()

'''
So I'll be making the brazil flag since one of my brazilain friends gave me the idea. Also i love brazil 
and it very pretty so why not. Also isnt to hard to make unlike the mexican flag.
'''
def make_sqaure():
    tess.penup()
    tess.setposition(-200,-100)
    tess.pendown()
    tess.begin_fill()
    for i in range(2):
        tess.color(0, 156, 59)
        tess.forward(400)
        tess.left(90)
        tess.forward(270)
        tess.left(90)
    tess.end_fill()
'''
So the make_sqaure function helps me create the green flag background and nothing else just wanted the first 
function to be simple.
'''

'''''
The middle_shape is what it sounds like its the middle shapes in the brazil flag. The diffcult part about this was 
the make_weird_sqaure, because you just had to make sure the aligned well with the flag.
'''''
def middle_shape():
    def make_circle():
        tess.left(135)
        tess.begin_fill()
        tess.penup()
        tess.setposition(5,-40)
        tess.pendown()
        tess.color(7, 7, 99)
        tess.circle(70)
        tess.end_fill()
    def make_weird_square():
        tess.begin_fill()
        tess.color("yellow")
        tess.penup()
        tess.setposition(-120,30)
        tess.pendown()
        tess.right(45)
        tess.forward(180)
        tess.left(90)
        tess.forward(180)
        tess.left(90)
        tess.forward(180)
        tess.left(90)
        tess.forward(180)
        tess.end_fill()
    def white_stars():
        def star():
            for i in range(5):
                tess.begin_fill()
                tess.forward(5)
                tess.right(144)
                tess.end_fill()
        tess.color("white")
        tess.penup()
        tess.setposition(0,40)
        tess.pendown()
        star()
        tess.penup()
        tess.setposition(30,45)
        tess.pendown()
        star()
        tess.penup()
        tess.setposition(-20, 45)
        tess.pendown()
        star()


    make_weird_square()
    make_circle()
    white_stars()
"""
The make_circle function was easy just used a setpostion and circle and fill code to make it. Another function i did 
was the star function because the brazil flag has a few and keep in mind i did everything i needed to do in this
assigment so i wasnt going to add a bunch of stars just like three. Again it looks nice having them their. 
"""


def main():
    wn.colormode(255)
    wn.bgcolor(152, 163, 175)
    tess.speed(5)

    # Function calls to function_1 and function_2.
    make_sqaure()            #
    middle_shape()
    wn.exitonclick()
'''
I also used colors from the rbg website 
'''

main()  # Starts the program!