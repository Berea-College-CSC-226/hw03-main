######################################################################
# Author: Anna Carrillo
# username: carrilloa
# Link:
#
# Purpose:
#
######################################################################
# Acknowledgements:
#
#
# Licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
######################################################################

def draw_fin2(turt):
    """draws the fin on the top"""
    turt.hideturtle()
    turt.penup()
    turt.setpos(-80, 133)
    turt.left(25)
    turt.pendown()
    turt.begin_fill()
    for i in range(60):
        turt.fd(2)
        turt.right(.25)
    for i in range(7):
        for i in range(30):
            turt.fd(-.5)
            turt.left(6)
        turt.right(190)
        turt.fd(20)
    turt.right(160)
    for i in range(50):
        turt.fd(1)
        turt.left(.5)
    for i in range(35):
        turt.fd(1)
        turt.left(1.5)
    turt.end_fill()


def draw_fin3(turt):
    """draws the fin on the tail"""
    turt.penup()
    turt.hideturtle()
    turt.setpos(41, 70)
    turt.right(55)
    turt.pendown()
    turt.begin_fill()
    turt.fd(30)
    for i in range(80):
        turt.fd(1)
        turt.right(.5)
    turt.fd(10)
    for i in range(80):
        turt.fd(1)
        turt.left(.5)
    turt.right(2)
    turt.fd(2)
    turt.right(130)
    turt.fd(10)
    for i in range(20):
        turt.fd(1)
        turt.right(3)
    for i in range(10):
        turt.fd(1)
        turt.right(1)
    for i in range(40):
        turt.fd(1)
        turt.left(.5)
    for i in range(30):
        turt.fd(1)
        turt.right(1)
    turt.fd(40)
    turt.end_fill()
    turt.begin_fill()
    turt.left(160)
    for i in range(100):
        turt.fd(1)
        turt.left(.5)
    for i in range(50):
        turt.fd(1)
        turt.right(.5)
    turt.right(5)
    turt.fd(40)
    turt.right(160)
    for i in range(100):
        turt.fd(1)
        turt.left(.25)
    for i in range(100):
        turt.fd(1)
        turt.right(.75)
    for i in range(50):
        turt.fd(1)
        turt.left(.25)
    turt.right(45)
    turt.fd(30)
    turt.end_fill()


def draw_fin4(turt):
    """draws the fin underneath"""
    turt.penup()
    turt.hideturtle()
    turt.setpos(-120, 45)
    turt.right(90)
    turt.pendown()
    turt.left(20)
    turt.begin_fill()
    for i in range(50):
        turt.fd(1)
        turt.left(.5)
    for i in range(8):
        for i in range(30):
            turt.fd(.5)
            turt.left(6)
        turt.right(190)
    turt.right(180)
    for i in range(40):
        turt.fd(1)
        turt.left(.75)
    turt.end_fill()


def draw_outerfins(turt1, turt2, turt3):
    """draws all the fins that are outside of the fish"""
    draw_fin2(turt1)
    draw_fin3(turt2)
    draw_fin4(turt3)


# draw outline
def set_starting_point(turt):
    """sets the starting point for the outline"""
    turt.penup()
    turt.left(180)
    turt.forward(200)
    turt.right(90)
    turt.fd(100)
    turt.right(45)
    turt.pendown()


def draw_outline(turt):
    """draws the outline of the fish"""
    turt.hideturtle()
    set_starting_point(turt)
    turt.begin_fill()
    for i in range(90):
        turt.forward(1)
        turt.right(.5)
    for i in range(65):
        turt.right(.05)
        turt.forward(1)
    for i in range(65):
        turt.right(.5)
        turt.forward(1)
    for i in range(55):
        turt.right(1)
        turt.fd(2)
    turt.right(20)
    for i in range(10):
        turt.right(.5)
        turt.fd(.5)
    for i in range(10):
        turt.right(10)
        turt.fd(.5)
    turt.fd(5)
    for i in range(20):
        turt.right(.75)
        turt.fd(1)
    for i in range(55):
        turt.left(1)
        turt.fd(1)
    for i in range(40):
        turt.left(.05)
        turt.fd(.5)
    for i in range(50):
        turt.right(.075)
        turt.fd(1)
    for i in range(131):
        turt.right(.45)
        turt.fd(1)
    turt.right(90)
    turt.fd(2)
    turt.end_fill()


# draw inner fin
def draw_fin1(turt):
    """draws the small fin on the fish's side"""
    turt.penup()
    turt.hideturtle()
    turt.setpos(-110, 70)
    turt.right(45)
    turt.pendown()
    turt.begin_fill()
    for i in range(30):
        turt.fd(1)
        turt.left(.75)
    for i in range(3):
        for i in range(30):
            turt.fd(.5)
            turt.left(6)
        turt.right(170)
    turt.left(170)
    for i in range(25):
        turt.fd(1)
        turt.left(.5)
    turt.end_fill()


# draw eye
def draw_eye(turt):
    """draws the fish's eye"""
    turt.hideturtle()
    turt.penup()
    turt.setpos(-150, 100)
    turt.stamp()


# hide
def hideturtles(turt1, turt2, turt3, turt4, turt5, turt6, turt7):
    """hides all turtles at once"""
    turt1.hideturtle()
    turt2.hideturtle()
    turt3.hideturtle()
    turt4.hideturtle()
    turt5.hideturtle()
    turt6.hideturtle()
    turt7.hideturtle()


# draw bubbles
def bubble(turt):
    """draws the bubbles"""
    turt.hideturtle()
    turt.penup()
    turt.setpos(-200, 150)
    turt.showturtle()
    turt.stamp()
    turt.pensize(80)
    turt.setpos(-237, 210)
    turt.stamp()
    turt.pensize(18)
    turt.setpos(-198, 243)
    turt.stamp()


def main():
    import turtle
    wn = turtle.Screen()
    wn.colormode(255)
    wn.bgcolor((156, 211, 219))

    tera = turtle.Turtle()
    tera.shape("arrow")
    tera.color(0, 128, 128)
    tera.speed(0)

    karen = turtle.Turtle()
    karen.shape("circle")
    karen.color("black")
    karen.speed(0)

    xica = turtle.Turtle()
    xica.shape("arrow")
    xica.color(0, 110, 110)
    xica.speed(0)

    xico = turtle.Turtle()
    xico.shape("arrow")
    xico.color(0, 110, 110)
    xico.speed(0)

    kiki = turtle.Turtle()
    kiki.shape("arrow")
    kiki.color(0, 110, 110)
    kiki.speed(0)

    mahalo = turtle.Turtle()
    mahalo.shape("arrow")
    mahalo.color(0, 110, 110)
    mahalo.speed(0)

    bubbles = turtle.Turtle()
    bubbles.shape("circle")
    bubbles.color(175, 238, 238)
    bubbles.pensize(50)

    hideturtles(tera, karen, xico, xica, kiki, mahalo, bubbles)

    draw_outerfins(xica, xico, kiki)
    draw_outline(tera)
    draw_fin1(mahalo)
    draw_eye(karen)
    bubble(bubbles)

    wn.exitonclick()


main()