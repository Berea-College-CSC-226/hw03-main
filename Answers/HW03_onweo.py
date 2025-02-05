#Author: Ositadimma Onwe
#username: onweo
#Assignment: HW03: Drawing a house using turtle module
#####################################################################################

import turtle

def draw_rectangle(x, y, width, height, color=None):
    if color:
        turtle.fillcolor(color)
        turtle.begin_fill()

    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)

    if color:
        turtle.end_fill()


def draw_hut():
    screen = turtle.Screen()
    screen.bgcolor("lightblue")

    turtle.speed(3)

    # Draw the hut body
    draw_rectangle(-100, 0, 200, 150, "brown")

    # Draw the roof
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(-120, 0)
    turtle.pendown()
    turtle.goto(0, 100)
    turtle.goto(120, 0)
    turtle.goto(-120, 0)
    turtle.end_fill()

    # Draw door
    draw_rectangle(-30, -100, 60, 100, "black")

    # Draw windows
    draw_rectangle(-80, -20, 40, 40, "white")
    draw_rectangle(40, -20, 40, 40, "white")

    turtle.hideturtle()
    screen.mainloop()
def main():
    wn = turtle.Screen()
    wn.bgcolor("blue")
    draw_hut()

    draw_rectangle(10, 10, 15, 20, )

    wn.exitonclick()

main()
