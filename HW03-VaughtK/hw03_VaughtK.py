
#################################################################################
# Author: Kai Vaught
# Username: VaughtK
# Assignment: Homework 3
# Purpose: To learn how branches work.
# Google Doc Link: https://docs.google.com/document/d/1OvsmR456y61n3UzwBlIlVE13IBz0tF39Vyv10F24ZGI/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################




def draw_house(t):
    """
    Draws green lines in the shape of a house.
    """
def main(t):
    t.setpos(0,-100)
    t.color("green")
    t.width(4)
    t.speed(0)  # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
    t.screen.bgcolor("black")
    t.left(60)
    t.forward(90)
    t.left(30)
    t.forward(90)
    t.left(85)
    t.forward(90)
    t.left(55)
    t.forward(90)
    t.left(35)
    t.forward(90)
    t.forward(-90)
    t.left(90)
    t.forward(90)
    t.left(55)
    t.forward(90)
    t.forward(-90)
    t.left(35)
    t.forward(-90)
    t.left(-90)

def draw_detail(t):
    t.color("red")
    t.forward(120)
    t.left(-100)
    t.forward(-80)
    t.left(-80)
    t.forward(80)
    t.left(70)
    t.forward(90)
    t.right(70)
    t.color("green")
    t.forward(40)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(25)
    t.right(90)
    t.forward(60)
    t.forward(-210)
    t.color("red")
    t.right(90)
    t.forward(20)
    t.forward(-20)
    t.right(-90)
    t.forward(115)
    t.color("green")
    t.forward(100)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.penup()
    t.forward(15)
    t.pendown()
    t.color("white")
    t.forward(30)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.penup()
    t.setpos(150,150)
    t.pendown()


def draw_stars(turtle2):
    """
    Draws white lines in the shape of the moon and stars.
    """

    turtle2.color("white")
    turtle2.penup()
    turtle2.setpos(150,150)
    turtle2.speed(0)
    turtle2.pendown()
    turtle2.pensize(25)
    turtle2.pencolor("white")
    turtle2.right(30)
    turtle2.forward(5)
    turtle2.right(30)
    turtle2.forward(5)
    turtle2.right(30)
    turtle2.forward(5)
    turtle2.right(30)
    turtle2.forward(5)
    turtle2.right(30)
    turtle2.forward(5)
    turtle2.right(30)
    turtle2.forward(5)
    turtle2.right(30)
    turtle2.forward(5)
    turtle2.right(30)
    turtle2.forward(5)
    turtle2.right(30)
    turtle2.forward(5)
    turtle2.right(30)
    turtle2.forward(5)
    turtle2.right(30)
    turtle2.forward(5)
    turtle2.right(30)
    turtle2.forward(5)

    turtle2.pensize(5)

    turtle2.penup()
    turtle2.setpos(-150,150)
    turtle2.pendown()
    turtle2.forward(5)

    turtle2.penup()
    turtle2.setpos(-130,170)
    turtle2.pendown()
    turtle2.forward(5)

    turtle2.penup()
    turtle2.setpos(10,210)
    turtle2.pendown()
    turtle2.forward(5)

    turtle2.penup()
    turtle2.setpos(-210,130)
    turtle2.pendown()
    turtle2.forward(5)

    turtle2.penup()
    turtle2.setpos(220,190)
    turtle2.pendown()
    turtle2.forward(5)

    turtle2.penup()
    turtle2.setpos(210,130)
    turtle2.pendown()
    turtle2.forward(5)

    turtle2.penup()
    turtle2.setpos(140,210)

    turtle2.exitonclick()


def main():
    import turtle

    t = turtle.Turtle()

    turtle2 = turtle.Turtle()

    """
    Main channel
    """

    draw_house(t)
    """
    Draws green lines in the shape of a house.
    """

    draw_detail(t)
    """
    Draws multicolored building elements: the white window and red lot.
    """

    draw_stars(turtle2)
    """
    Draws white lines in the shape of the moon and stars.
    """

main()