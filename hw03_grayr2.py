#################################################################################
# Author: Relly Gray
# Username: grayr2
#
# Assignment:
# Purpose:
# Google Doc Link: https://docs.google.com/document/d/1UVBNWf08HXY_rivdGX1H_HSzcBGa33XGG7AeElADZLg/edit?usp=sharing
#
#################################################################################
# Acknowledgements: ChatGpt
# I asked chatgpt how it may be possible to turn my shape into a skyscraper and it gave me back this: rell.setpos(-100, 100 - (floor + 1) * floor_height)  # Adjust position for the next floor
# I asked chatgpt how I may be able to loop my windows but to no avail.
# Update the y value for the next window
#         y -= 60
#
#         # After drawing the third window in a column, reset y and shift x
#         if (i + 1) % 3 == 0:
#             y = 190  # Reset y to the top of the column
#             x += 60  # Move x to the next column
#################################################################################


import turtle


def draw_skyscraper(rell):
    """
    This function will create the basis to my skyscraper and fill those shapes in.
    """
    pass
    rell.color("grey")
    rell.penup()
    rell.setpos(-100, 200)
    rell.pendown()
    rell.pensize(5)
    floor = 10
    floor_height = 50
    rell.begin_fill()
    for floor in range(4):
        rell.fd(200)
        rell.right(90)
    rell.penup()
    rell.setpos(-100, 200 - (floor + 1) * floor_height)  # Adjust position for the next floor
    rell.pendown()
    for floor in range (4):
        rell.fd(300)
        rell.right(90)
    rell.end_fill()
def draw_square(rell):
    for windows in range(9):
        rell.fd(40)
        rell.right(90)

def draw_rectangle(rell):
    for windows in range(3):
        rell.fd(280)
        rell.right(90)
        rell.fd(70)
        rell.right(90)

def draw_window(rell):
    """
    This function will draw multiple windows on my building as well as adding in a door.
    """
    pass
    rell.pensize(1)
    rell.color("lightblue")
    x = -90
    y = 190

    for i in range(9):
        rell.penup()
        rell.setpos(x, y)
        rell.pendown()
        draw_square(rell)

        # Update the y value for the next window
        y -= 60

        # After drawing the third window in a column, reset y and shift x
        if (i + 1) % 3 == 0:
            y = 190  # Reset y to the top of the column
            x += 60  # Move x to the next column

    # the bottom layer of windows starts here (includes door and text)
    rell.penup()
    rell.setpos(-90, -10)
    rell.pendown()
    draw_rectangle(rell)

    rell.penup()
    rell.setpos(-90, -90)
    rell.pendown()
    draw_rectangle(rell)

    rell.penup()
    rell.setpos(-90, -170)
    rell.pendown()
    draw_rectangle(rell)
# the door
    rell.penup()
    rell.setpos(0, -270)
    rell.pendown()
    rell.color("white")
    for windows in range(2):
        rell.fd(50)
        rell.right(90)
        rell.fd(30)
        rell.right(90)
    rell.penup()
    rell.setpos(-90, 230)
    rell.pendown()
    rell.color(0, 0, 0)
    rell.hideturtle()
    rell.write("Welcome to Turtle Inc.", (30))

def main():
    """
    Docstring for main. Should describe the main functionality of this file.
    """
    rell = turtle.Turtle()
    rell.speed(10)
    wn = turtle.Screen()
    wn.bgcolor("#8BF2FD")
    # Function calls to function_1 and function_2.
    draw_skyscraper(rell)
    draw_window(rell)

    wn.exitonclick()

main()  # Starts the program!