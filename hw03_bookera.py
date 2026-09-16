######################################3
# Author: Andre Booker Jr.
# Username: bookera

import turtle

#b_head = turtle.Turtle()
#b_chest = turtle.Turtle()
#b_legs = turtle.Turtle()
#b_arms = turtle.Turtle
#def b_arms(arms):
#arms.goto(100,100)

def right_side(rs):
    rs.goto(85,-85)
    rs.begin_fill()
    rs.right(45)
    rs.forward(100)
    rs.right(120)
    rs.forward(20)
    rs.right(50)
    rs.forward(90)
    rs.end_fill()
    rs.penup()
    rs.left(80)
    rs.forward(70)
    rs.pendown()
    rs.fillcolor("#13598B")
    rs.begin_fill()
    rs.left(75)
    rs.forward(90)
    rs.left(60)
    rs.forward(20)
    rs.left(120)
    rs.forward(105)
    rs.hideturtle()
    rs.end_fill()

def left_side(ls):
    ls.goto(-85,-85)
    ls.begin_fill()
    ls.right(120)
    ls.forward(100)
    ls.left(120)
    ls.forward(20)
    ls.left(49)
    ls.forward(85)
    ls.end_fill()
    ls.penup()
    ls.right(98)
    ls.forward(65)
    ls.pendown()
    ls.fillcolor("#13598B")
    ls.begin_fill()
    ls.right(80)
    ls.forward(100)
    ls.left(120)
    ls.forward(20)
    ls.left(60)
    ls.forward(93)
    ls.hideturtle()
    ls.end_fill()

def b_chest(chest):
    chest.begin_fill()
    chest.right(45)
    chest.forward(120)
    for i in range(3):
        chest.right(90)
        chest.forward(120)
    chest.hideturtle()
    chest.end_fill()




def b_head(head):
    head.hideturtle()
    head.fillcolor("#8B4513")
    head.begin_fill()
    head.speed(10)
    head.circle(80)
    head.end_fill()

def main():
    wn = turtle.Screen()
    wn.bgcolor("green")
    head = turtle.Turtle()
    chest = turtle.Turtle()
    rs = turtle.Turtle()
    ls = turtle.Turtle()
    b_head(head)
    b_chest(chest)
    right_side(rs)
    left_side(ls)



    wn.exitonclick()
main()