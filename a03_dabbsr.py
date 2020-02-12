Robert Dabbs
dabbsr
https://docs.google.com/document/d/1NYZeAN_fGb0iTEdF8upy8mrT_fNUva248VOr3c7x7pY/edit#

import turtle
wn = turtle.Screen()
wn.colormode(255)

wn.bgcolor(5,160,170)
luigi = turtle.Turtle()
def red_shape():
    """
    
    first 
    """
    luigi.color("Red")
    luigi.begin_fill()
    luigi.speed(0)
    luigi.left(15)
    luigi.forward(45)
    print(luigi.pos())
    luigi.left(60)
    luigi.forward(45)
    luigi.left(40)
    luigi.forward(132)
    print(luigi.pos())
    luigi.setpos(0,0)
    luigi.end_fill()
def yellow_shape():
    """
    
    second 
    """
    luigi.color("Yellow")
    luigi.begin_fill()
    luigi.forward(70)
    print(luigi.pos())
    luigi.setpos(-0.67,174.75)
    luigi.setpos(0,0)
    luigi.end_fill()
def og_shape():
    """
    
    third 
    """
    luigi.color("Orange")
    luigi.setheading(180)
    luigi.begin_fill()
    luigi.forward(200)
    luigi.setpos(-29.58,63.44)
    luigi.setpos(0,0)
    luigi.end_fill()
def green_shape():
    """
    
    fourth 
    """
    luigi.color("Green")
    luigi.setheading(180)
    luigi.begin_fill()
    luigi.forward(200)
    luigi.setpos(-29.58,-63.44)
    luigi.setpos(0,0)
    luigi.end_fill()
def wt_shape():
    """
    
    fifth
    """
    luigi.color("White")
    luigi.begin_fill()
    luigi.setpos(-29.58,-63.44)
    print(luigi.pos())
    luigi.setpos(-0.67,-174.75)
    luigi.setpos(0,0)
    luigi.end_fill()
def pnk_shape():
    """
    
    final 
    """
    luigi.color("Pink")
    luigi.setheading(0)
    luigi.begin_fill()
    luigi.left(-15)
    luigi.forward(45)
    print(luigi.pos())
    luigi.left(-60)
    luigi.forward(45)
    luigi.left(-40)
    luigi.forward(132)
    print(luigi.pos())
    luigi.setpos(0,0)
    luigi.end_fill()
def main():
    """
    
    puts all sections together of the pop art
    """
    red_shape()
    yellow_shape()
    og_shape()
    green_shape()
    wt_shape()
    pnk_shape()
    wn.title("Pop Art")
    wn.exitonclick()
main()