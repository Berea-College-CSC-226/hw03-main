#################################################################################
# Author: Yoseph Alemu
# Username: alemuy
#
# Assignment: Draw something complex, like a house, animal, or person.
# Purpose: Bird Drawing
# Google Doc Link: https://docs.google.com/document/d/1ktJ999pabXorwqER5-J3XWQSuS0ylfjCTjnTAChYcew/edit?tab=t.0#heading=h.j4414z2ufr72
#
#################################################################################
# Acknowledgements:
#  - Based on hw03 stubs structure
#  - Yoseph’s own modifications
#################################################################################

import turtle

turtle.colormode(255)
WIDTH, HEIGHT = 900, 700


def move_to(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def draw_circle(t, r, fill_color=None, outline_color=None):
    if outline_color:
        t.pencolor(outline_color)
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    t.circle(r)
    if fill_color:
        t.end_fill()


def draw_branch_leaf(t, x, y, w):
    wood = (140, 95, 70)
    t.pensize(6)
    t.pencolor(wood)
    move_to(t, x, y)
    t.setheading(0)
    t.forward(w)

    # Front leaf
    leaf = (60, 160, 90)
    t.pencolor(leaf)
    t.fillcolor(leaf)
    move_to(t, x + w - 40, y + 15)
    t.begin_fill()
    t.circle(12)
    t.end_fill()


def draw_cloud(t, x, y, scale=1.0):
    cloud = (250, 250, 255)
    t.fillcolor(cloud)
    t.pencolor((210, 210, 220))
    for dx, r in [(-25, 18), (0, 24), (25, 18)]:
        move_to(t, x + dx*scale, y)
        t.begin_fill()
        t.circle(r*scale)
        t.end_fill()


def draw_bird(t, x, y, scale=1.0):
    body_rgb = (80, 150, 210)
    wing_rgb = (50, 110, 170)
    head_rgb = (95, 160, 220)
    beak_hex = "#D99A2B"
    outline = (40, 60, 90)

    # Body
    move_to(t, x, y)
    t.pencolor(outline)
    t.fillcolor(body_rgb)
    t.begin_fill()
    for _ in range(2):
        t.circle(60*scale, 90)
        t.circle(30*scale, 90)
    t.end_fill()

    # Wing
    move_to(t, x + 10*scale, y - 5*scale)
    t.fillcolor(wing_rgb)
    t.begin_fill()
    for _ in range(2):
        t.circle(35*scale, 90)
        t.circle(18*scale, 90)
    t.end_fill()

    # Head
    move_to(t, x + 70*scale, y + 35*scale)
    t.fillcolor(head_rgb)
    t.begin_fill()
    t.circle(28*scale)
    t.end_fill()

    # Eye with highlight
    move_to(t, x + 83*scale, y + 48*scale)
    t.fillcolor((20, 25, 30))
    t.begin_fill()
    t.circle(5*scale)
    t.end_fill()
    move_to(t, x + 85*scale, y + 50*scale)
    t.fillcolor((255, 255, 255))
    t.begin_fill()
    t.circle(2*scale)
    t.end_fill()

    # Beak
    move_to(t, x + 98*scale, y + 40*scale)
    t.setheading(0)
    t.fillcolor(beak_hex)
    t.begin_fill()
    t.forward(20*scale)
    t.left(120)
    t.forward(12*scale)
    t.left(120)
    t.forward(12*scale)
    t.end_fill()

    # Tail
    move_to(t, x - 65*scale, y + 5*scale)
    t.setheading(200)
    t.fillcolor((60, 110, 165))
    t.begin_fill()
    t.forward(28*scale)
    t.left(105)
    t.forward(18*scale)
    t.left(75)
    t.forward(16*scale)
    t.end_fill()

    # Legs + claws
    t.pensize(3)
    t.pencolor((100, 60, 30))
    for offset in [15, 35]:
        move_to(t, x + offset*scale, y - 45*scale)
        t.setheading(270)
        t.forward(22*scale)
        t.pensize(2)
        for ang in (220, 270, 320):
            move_to(t, x + offset*scale, y - 67*scale)
            t.setheading(ang)
            t.forward(10*scale)
        t.pensize(3)


def draw_label(t, text, x, y, size=20):
    t.hideturtle()
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color((20, 20, 35))
    t.write(text, align="center", font=("Arial", size, "bold"))


def setup_background(screen):
    screen.bgcolor((185, 210, 245))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Bird")

    setup_background(screen)

    t = turtle.Turtle()
    t.speed(0)

    # Clouds
    draw_cloud(t, -200, 200, scale=1.2)
    draw_cloud(t, 150, 180, scale=0.9)

    # Branch + front leaf
    draw_branch_leaf(t, x=-150, y=-120, w=320)

    # Bird
    draw_bird(t, x=-20, y=-60, scale=1.0)

    # Label
    draw_label(t, "Bird", x=0, y=-260, size=22)

    screen.mainloop()


main()  # Starts the program!
