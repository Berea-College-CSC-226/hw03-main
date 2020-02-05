######################################################################
# Author: Axel Quintanar            TODO: Change this to your name, if modifying
# Username: quintanarpenaa                     TODO: Change this to your username, if modifying
#
# Assignment: A03:  Turtles
# Purpose: To create houses
######################################################################
# Acknowledgements:
#Gdoc:https://docs.google.com/document/d/1WBEFX7bGdiuXyeJ3jShev8kx0OTde1xSXx8s-FoY-eY/edit?usp=sharing
# originally created by me
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
######################################################################
import turtle


def smokey(n):
    """creates smoke"""
    n.left(-10)
    n.circle(20, extent=-180)
    n.right(180)


def rep(bd):
    """moves the turtle back into position"""
    bd.penup()
    bd.right(90)
    bd.fd(320)
    bd.right(90)
    bd.fd(285)
    bd.left(180)
    bd.pendown()


def smoke(mn):
    """creates smoke"""
    mn.left(-10)
    mn.circle(20, extent=-180)
    mn.right(180)




def chimmeny(ui):
    ui.color('black')
    ui.begin_fill()
    ui.right(30)
    ui.fd(20)
    ui.left(30)
    ui.fd(40)
    ui.left(90)
    ui.fd(10)
    ui.left(90)
    ui.fd(56)
    ui.left(180)
    ui.fd(56)
    ui.end_fill()


def reposss(ht):
    ht.penup()
    ht.left(90)
    ht.fd(373)
    ht.pendown()


def reposs(yu):
    """Positions the turtle to make a door"""
    yu.penup()
    yu.fd(25)
    yu.right(90)
    yu.fd(200)
    yu.left(90)
    yu.fd(75)
    yu.pendown()


def door(rt):
    """makes a door"""
    rt.color("red")
    rt.begin_fill()
    rt.fd(50)
    rt.left(90)
    rt.fd(70)
    rt.left(90)
    rt.fd(50)
    rt.left(90)
    rt.fd(70)
    rt.end_fill()
    rt.color("blue")
    rt.penup()
    rt.backward(25)
    rt.left(90)
    rt.fd(10)
    rt.pendown()
    rt.begin_fill()
    rt.circle(5)
    rt.end_fill()
    rt.penup()
    rt.backward(10)
    rt.right(90)
    rt.fd(25)
    rt.left(90)
    rt.pendown()


def repos(er):
    """repositions the turtle again for the roof"""
    er.penup()
    er.backward(260)
    er.left(90)
    er.fd(100)
    er.right(90)
    er.fd(25)
    er.pendown()


def repo(op):
    """makes the turtle go in position to make windows"""
    op.left(90)
    op.fd(100)
    op.right(90)


def roof(ro):
    """makes a roof"""
    ro.color("blue")
    ro.begin_fill()
    ro.backward(50)
    ro.left(60)
    ro.fd(250)
    ro.right(120)
    ro.fd(250)
    ro.left(60)
    ro.backward(250)
    ro.end_fill()


def reposition(qw):
    """repositions the turtle on the bottom left of the screen"""
    qw.penup()
    qw.right(135)
    qw.fd(350)
    qw.right(-135)
    qw.pendown()


def house(wt):
    """Makes the frame of the house"""
    wt.color("black")
    wt.begin_fill()
    wt.fd(200)
    wt.left(90)
    wt.fd(200)
    wt.left(90)
    wt.fd(200)
    wt.left(90)
    wt.fd(200)
    wt.left(90)
    wt.end_fill()



def windows(nt):
    """This makes windows """
    nt.color("yellow")
    nt.begin_fill()
    nt.fd(70)
    nt.left(90)
    nt.fd(70)
    nt.left(90)
    nt.fd(70)
    nt.left(90)
    nt.fd(70)
    nt.end_fill()
    nt.left(180)
    nt.fd(35)
    nt.right(90)
    nt.color("black")
    nt.fd(70)
    nt.backward(35)
    nt.left(90)
    nt.fd(35)
    nt.backward(70)
    nt.right(90)
    nt.penup()
    nt.backward(35)
    nt.fd(130)
    nt.pendown()


def main():
    roe = turtle.Turtle()
    roe.speed(0)
    wn = turtle.Screen()
    wn.bgcolor("#738678")
    roe.pensize(2)
    reposition(roe)
    house(roe)
    repo(roe)
    for i in range(2):
        windows(roe)
    repos(roe)
    roof(roe)
    reposs(roe)
    door(roe)
    reposss(roe)
    chimmeny(roe)
    for i in range(5):
        smoke(roe)
    roe.left(-180)
    for i in range(5):
        roe.penup()
        smoke(roe)
        roe.pendown()
    rep(roe)
    for i in range(7):
        smokey(roe)
    wn.exitonclick()


main()

# turtle.color ("#738678") #this code makes a circle the color xanadu
# turtle.begin_fill()
# turtle.circle(60)
# turtle.end_fill()

