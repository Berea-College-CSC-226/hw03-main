#################################################################################
# Author: Aaron Whitaker
# Username: whitakera2
#
# Assignment: hw03
# Purpose: Draws a rainbow of variable size following user input
# Google Doc Link: https://docs.google.com/document/d/1b6Vpxv6G5OTl73SmNrhtsZfo4ngtvti9DMaX8iCwIPc/edit?tab=t.0#heading=h.j4414z2ufr72
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle as t

def draw_rainbow(y, size):
    """
    draws a rainbow in the middle of the screen with a variable size
    """
    y.setpos(-size, -size/2)                    ### move turtle into position
    y.left(90)
    colors1 = ["purple", "green", "orange"]     ### pick colors for rainbow
    colors2 = ["blue", "yellow", "red"]         ###

    for i in range(3):                          ### draws the lines of the rainbow using semi circles
                                                ### draws 2 lines and then loops
        y.pendown()
        y.color(colors1[i % len(colors1)])      ### color change
        y.pensize(11)
        y.circle(-size, 180, 200)               ### line 1 semi circle
        y.penup()
        y.left(90)
        y.forward(10)
        y.left(90)
        y.pendown()
        y.color(colors2[i % len(colors2)])      ### color change
        y.circle(size+10, 180, 200)             ### line 2 semi circle
        y.penup()
        size = size + 20
        y.right(90)
        y.forward(10)
        y.right(90)


def write_text(y, size):
    """
    writes text in the screen with variable size and position related to variable size
    """
    size = size / 1.5 + 80                                                      ### use size of rainbow to adjust
    y.setpos(0, size)                                                           ### placement of writing
    y.color("black")
    y.write("Promise", align="center", font=("aptos", int(size/6) , "bold"))    ### write using size variable to determine size of writing



def main():
    """
    main function
    """
    size = int(input("what size rainbow 1-5?"))   ### user picks size of rainbow picture
    size = size * 60                              ### set input to a usable value
    wn = t.Screen()                               ###
    y = t.Turtle()                                ### set up turtle
    y.speed(0)                                    ###
    t.setup(700, 700)                ###
    y.penup()
    wn.colormode(255)                             ### change background color
    wn.bgcolor(149, 223, 223)                     ###
    wn.colormode(1)                               ### revert back to standard color mode

    draw_rainbow(y, size)                         ### call functions
    write_text(y, size)                           ###

    wn.exitonclick()                              ### program ends when window is closed

main()