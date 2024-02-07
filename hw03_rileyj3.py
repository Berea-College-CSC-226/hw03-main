######################################################################
# Author: Bryce Riley
# Username: rileyj3
#
# Assignment: HW03 : Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: To create something complex and learn about GitHub.
# Link to Document: https://docs.google.com/document/d/1EzPApStfIckqskXxnh8CNhMuNgis_GTE2FZZHHZvji4/edit?usp=sharing
#####################################################################


import turtle


def build_house(bryce):
    """
    Have turtle build me a nice house.
    """
    bryce.speed(0)
    bryce.pu()
    bryce.setpos(50, 0)
    bryce.pd()
    bryce.color('hot pink')
    bryce.begin_fill()
    for i in range(4):
        bryce.forward(150)
        bryce.left(90)
    bryce.end_fill()


def edit_house(bryce):
    """
    Have my turtle build me some nice windows into my house
    """
    bryce.color('black')
    bryce.pu()
    bryce.setpos(100, 80)
    bryce.pd()
    bryce.begin_fill()
    for i in range(4):
        bryce.left(90)
        bryce.forward(25)
    bryce.end_fill()
    bryce.pu()
    bryce.setpos(150, 80)
    bryce.pd()
    bryce.begin_fill()
    for i in range(4):
        bryce.forward(25)
        bryce.left(90)
    bryce.end_fill()
    bryce.pu()
    bryce.setpos(112.5, 0)
    bryce.pd()
    bryce.begin_fill()
    for i in range(2):
        bryce.forward(25)
        bryce.left(90)
        bryce.forward(50)
        bryce.left(90)
    bryce.end_fill()


def add_roof(bryce):
    """
    have my turtle add a roof onto my house
    """
    bryce.color('blue')
    bryce.pu()
    bryce.setpos(45, 150)
    bryce.pd()
    bryce.begin_fill()
    for i in range(1):
        bryce.forward(160)
        bryce.left(135)
        bryce.forward(115)
        bryce.left(90)
        bryce.forward(115)
    bryce.end_fill()
    bryce.pu()
    bryce.setpos(-50, 0)


def add_words(bryce):
    """
    Have my turtle write 'My Lovely Complex House' on the screen
    """
    bryce.setpos(-10, -100)
    bryce.hideturtle()
    bryce.color('yellow')
    bryce.write("My Lovely Complex House", move=False, align='center', font=("Arial", 45, ("bold", "normal")))


def main():
    """
    Builds a nice house with a roof and some  nice windows
    """
    bryce = turtle.Turtle()

    build_house(bryce)

    edit_house(bryce)

    add_roof(bryce)

    add_words(bryce)

    wn = turtle.Screen()
    wn.bgcolor('teal')
    bryce.speed(0)

    wn.exitonclick()


main()
