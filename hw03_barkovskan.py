#################################################################################
# Author: Nadia Barkovska
# Username: barkovskan
#
# Assignment: to create a creative project using functions, turtles, loops and etc.
# Purpose: to practice what I have learned
# Google Doc Link: https://docs.google.com/document/d/1D4g2xz0JzRCXfvOkGUlMte5aEAw4f--9gXS_3KenPJY/edit?usp=sharing
#
# ################################################################################
# Acknowledgements:
# https://colorspire.com/rgb-color-wheel/   (used to find the numbers for the color)
# https://cs111.wellesley.edu/archive/cs111_spring21T4/public_html/reference/turtle (to set my position in a list form"
# https://stackoverflow.com/questions/21717206/trying-to-draw-a-checkerboard-using-turtle-in-python-how-do-i-fill-in-every-ot
# (used it as an example code)
#################################################################################

import turtle


def drawsquare(bubbles, size):
    """Draw a square using turtle."""
    for i in range(4):
        bubbles.forward(size)
        bubbles.left(90)


def draw_row(bubbles, color1, color2):
    """Draw a row of squares with alternating colors."""
    for i in range(8):
        if i % 2 == 0:
            bubbles.fillcolor(color1)
        else:
            bubbles.fillcolor(color2)
        bubbles.begin_fill()
        drawsquare(bubbles, 60)
        bubbles.forward(60)
        bubbles.end_fill()


def main():
    """Main function to set up turtle and draw the pattern."""
    wn = turtle.Screen()
    wn.bgcolor("black")
    bubbles = turtle.Turtle()
    bubbles.speed(0)

    positions = [100, 40, -20, -80, -140, -200]
    colors1 = ["pink", (0.165, 0.42, 0.42), "orange", (0.80, 0.203, 0.118), "yellow", (0.143, 0.188, 0.143)]
    colors2 = [(0.245, 0.245, 0.220), "white", (0.237, 0.145, 0.33), "blue", (0.85, 0.107, 0.47), "purple"]

    for pos, color1, color2 in zip(positions, colors1, colors2):
        bubbles.penup()
        bubbles.setpos(-220, pos)
        bubbles.pendown()
        draw_row(bubbles, color1, color2)

    wn.exitonclick()


if __name__ == "__main__":
    main()
