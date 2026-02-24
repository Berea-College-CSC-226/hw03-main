#################################################################################
# Author: Jayden Fleming
# Username: flemingj2
#
# Assignment: HW03
# Purpose: Program that draws a small city.
# Google Doc Link: https://docs.google.com/document/d/10oGGXxGNC6is-CUaaT6OlsmJ6wyXfPPK69GDwuUj9xk/edit?usp=sharing
#
#################################################################################
# Acknowledgements: drawing relies on turtle library
#################################################################################


import turtle


def draw_rect(t, size_x, size_y, pos_x, pos_y):
    """
    Draws a rectangle of a given size centered at a given position.
    """
    start_pos = t.pos()
    t.penup()
    t.goto(pos_x - (size_x//2), pos_y + (size_y//2))
    t.pendown()
    for i in range(4):
        if i % 2 == 0:
            t.fd(size_x)
        else:
            t.fd(size_y)
        t.right(90)
    t.penup()
    t.goto(start_pos)

def draw_building(t, size_x, size_y, pos_x, pos_y):
    """
    Draws a building of a given size centered at a given position.
    """
    building_size_x = size_x
    building_size_y = size_y
    building_pos_x = pos_x
    building_pos_y = pos_y

    # draw building outline
    t.fillcolor(100, 100, 100)
    t.begin_fill()
    draw_rect(t, building_size_x, building_size_y, building_pos_x, building_pos_y)
    t.end_fill()

    # draw windows
    t.fillcolor(0, 0, 255)
    for i in range((building_size_x // 25) + 1):
        for j in range((building_size_y // 25) + 1):
            next_window_pos_x = (building_pos_x + (i * 20)) - (building_size_x // 2) + 10
            next_window_pos_y = (building_pos_y + (j * 20)) - (building_size_y // 2) + 15
            t.begin_fill()
            draw_rect(t, 10, 10, next_window_pos_x, next_window_pos_y)
            t.end_fill()

def main():
    """
    Draws a tiny city on screen using turtle lib.
    """
    wm = turtle.Screen()
    t = turtle.Turtle()

    t.speed(0)
    wm.colormode(255)
    wm.bgcolor(75, 150, 75)
    wm.screensize(500, 500)

    # draw a few buildings scattered about
    for i in range(5):
        if i % 2 == 0:
             draw_building(t, 100, 200, (i * 110) - 200, 0)
        else:
             draw_building(t, 100, 300, (i * 110) - 200, 50)

    wm.exitonclick()

main()