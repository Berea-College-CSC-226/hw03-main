#################################################################################
# Author: Arohasina Ravoahanginiaina
# Username: arohasina
#
# Assignment:HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: to draw something complex using turtle module
#################################################################################
# Acknowledgements:
#window image credits: <a href="https://www.flaticon.com/free-icons/window" title="window icons">Window icons created by Freepik - Flaticon</a>
#sun image credits: <a href="https://www.flaticon.com/free-icons/sun" title="sun icons">Sun icons created by Freepik - Flaticon</a>
#wn_background image credits: Arohasina Ravoahanginiaina
#
#link to my google doc: https://docs.google.com/document/d/1yOOY5LJFnBw-4Owlrxvn8j0_EiagiBsDbx_5uxkbKYk/edit
#################################################################################
import turtle

def draw_main_house(t):
    """
    draws the main house rectangle

    :param t: a Turtle object
    :return: None
    """
    t.hideturtle()
    t.penup()
    t.setposition(-210,-225)
    t.pendown()
    t.color(255,255,204)
    t.begin_fill()
    for i in range (2):
        t.forward(140)
        t.left(90)
        t.forward(210)
        t.left(90)
    t.end_fill()


def draw_window(wn,t):
    """
    import the window gif

    :param t: a Turtle object
    :param wn: a Screen object
    :return: None
    """
    wn.register_shape("window.gif")
    t.hideturtle()
    t.penup()
    t.setposition(-140,-70)
    t.pendown()
    t.shape("window.gif")
    t.stamp()


def draw_roof(t):
    """
    draw the roof on top of the main house

    :param t: a Turtle object
    :return: None
    """
    t.hideturtle()
    t.penup()
    t.setposition(-210,-15)
    t.pendown()
    t.color("firebrick4")
    t.begin_fill()
    for i in range(3):
        t.forward(140)
        t.left(120)
    t.end_fill()


def draw_sun(wn,t):
    """
    import the sun gif

    :param t: a Turtle object
    :param wn: a Screen object
    :return: None
    """
    wn.register_shape("sunny.gif")
    t.hideturtle()
    t.penup()
    t.setposition(110,120)
    t.pendown()
    t.shape("sunny.gif")
    t.stamp()


def draw_person(t):
    """
    draw a person next to the house

    :param t: a Turtle object
    :return: None
    """
    #draw the face of the person
    t.hideturtle()
    t.penup()
    t.setposition(40,-90)
    t.pendown()
    t.pencolor("black")
    t.fillcolor("#D8B279")
    t.begin_fill()
    t.circle(30)
    t.end_fill()

    #draw the dress of the person
    t.penup()
    t.setposition(40,-90)
    t.pendown()
    t.fillcolor("#FF66CC")
    t.begin_fill()
    t.right(120)
    t.forward(140)
    for i in range(2):
        t.left(120)
        t.forward(140)
    t.end_fill()

    # draw the eyes of the person
    x=27
    for i in range(2):
        if i == 1:  # Second iteration
            x = 27 + 15
        t.penup()
        t.setposition(x, -50)
        t.pendown()
        t.dot(8, "black")

    # draw the smile of the person
    t.penup()
    t.setposition(32, -76)
    t.pendown()
    t.setheading(-30)
    t.circle(15, 130)

    # draw left arm of the person
    t.penup()
    t.setposition(32, -100)
    t.pendown()
    t.pensize(5)
    t.left(45)
    t.forward(40)

    # draw right arm of the person
    t.penup()
    t.setposition(79, -75)
    t.pendown()
    t.left(75)
    t.forward(40)

    # draw left leg of the person
    t.penup()
    t.setposition(20, -225)
    t.pendown()
    t.right(129)
    t.forward(12.5)

    # draw right leg of the person
    t.penup()
    t.setposition(60, -212.5)
    t.pendown()
    t.right(180)
    t.forward(14)


def write_text(t, arg):
    """
    Writes text to the screen.
    :param t: a Turtle object
    :param arg: the text to be written
    :return: None
    """
    t.color("#FFFEBA")
    t.penup()
    t.setpos(-110, 170)
    t.pendown()
    t.write(arg, move=False, align='center', font=("Comic Sans MS", 25, ("bold", "italic")))


def main():
    """
    Draws a house at x, y on the screen.
    Add an image of sun
    Draws a person next to the house
    Add text at the top of the screen

    :return: None
    """
    turtle.colormode(255)

    wn = turtle.Screen()
    wn.setup(width=700, height=550)
    wn.bgpic("my_background.gif")
    wn.title("Aro's Perfect Day")

    t=turtle.Turtle()

    draw_main_house(t)
    draw_roof(t)
    draw_window(wn, t)
    draw_sun(wn,t)
    draw_person(t)
    write_text(t, "Aro's Perfect Day :)")

    wn.exitonclick()

main()