######################################################################
# Authors: Jakob Bister
# Username: bisterj
# Doc link: https://docs.google.com/document/d/14SaoPnirHLAimFZClApE9LVONUtrSzHRP1WLj_0BRqU/edit?usp=sharing
# Assignment: A03
######################################################################
import turtle


def move(turt, x, y):
    turt.penup()
    turt.setpos(x, y)
    turt.pendown()


def draw_line(turt, x1, y1, x2, y2):
    move(turt, x1, y1)
    turt.setpos(x2, y2)


def draw_stickman(turt, sz, x, y):
    move(turt, x, y)
    turt.circle(sz/2)
    head_x = turt.xcor()
    head_y = turt.ycor()
    draw_line(turt, head_x, head_y, head_x, head_y - sz)
    tail_x = turt.xcor()
    tail_y = turt.ycor()
    draw_line(turt, tail_x, tail_y, tail_x - sz / 2, tail_y - sz / 2)
    draw_line(turt, tail_x, tail_y, tail_x + sz/2, tail_y - sz/2)
    draw_line(turt, head_x - sz/2, head_y - sz/2, head_x + sz/2, head_y - sz/2)


def draw_rect(turt, x, y, w, h):
    move(turt, x, y)
    for i in range(2):
        turt.forward(w)
        turt.right(90)
        turt.forward(h)
        turt.rt(90)


def draw_dog(turt, sz, x, y):
    # body
    draw_rect(turt, x, y, sz, sz/2)
    # tail
    draw_line(turt, x, y, x - sz/8, y + sz/8)
    # head
    draw_rect(turt, x + sz, y + sz/4, sz/3, sz/4)
    # ears
    draw_line(turt, x + sz, y + sz/4, x + sz + sz/24, y + sz/3)
    draw_line(turt, x + sz + sz/24, y + sz/3, x + sz + sz/12, y + sz/4)
    draw_line(turt, x + sz + sz/12, y + sz/4, x + sz + sz * 3/24, y + sz/3)
    draw_line(turt, x + sz + sz * 3/24, y + sz/3, x + sz + sz/6, y + sz/4)
    # draws legs
    draw_line(turt, x + sz / 4, y - sz / 2, x + sz / 16, y - sz * 3 / 4)
    draw_line(turt, x + sz / 4, y - sz / 2, x + sz*3 / 16 + sz/4, y - sz * 3 / 4)
    draw_line(turt, x + sz * 3 / 4, y - sz / 2, x + sz / 16 + sz / 2, y - sz * 3 / 4)
    draw_line(turt, x + sz * 3 / 4, y - sz / 2, x + sz*3 / 16 + sz/4 + sz / 2, y - sz * 3 / 4)


def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    wn.colormode(255)
    tess = turtle.Turtle()
    tess.speed(7)
    tess.color(125, 175, 50)
    draw_line(tess, -320, -100, 320, -100)
    tess.color("brown")
    draw_dog(tess, 50, 0, -62)
    tess.color(197, 140, 133)
    draw_stickman(tess, 50, -100, -25)
    draw_stickman(tess, 37, 100, -45)
    move(tess, 0, 200)
    tess.penup()
    tess.color("blue")
    tess.write("A man's best friend", True,  align= "center", font=("Arial", 20, "normal"))
    wn.exitonclick()


main()
