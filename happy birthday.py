#################################################################################
# Author:
# Username: AbdulBaseer Mahmood
#
# Assignment: a-o3
# Purpose: to create happy birthday cake
# Google Doc Link: https://docs.google.com/document/d/1vqxaWs54B0K_AzsEIOlyF96Hx13iN_ehCspy9zxjzgM/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################
import turtle


def rect(t, leng):
    """

    :param t:       "t" is our turtle that draws the three block of cake
    :param leng:     the length is the parameters for the sides of the block of cake
    :return:            It draws the blocks of cake
    """


    t.forward(leng)
    t.right(90)
    t.forward(100)
    t.right(90)


def move(t):
    t.fd(50)
    t.left(90)
    t.fd(100)
    t.right(90)


def lamp(t, l, w):                        # this function draw our candles on top of our cake
    for g in range(3):
        t.forward(l)
        t.right(90)
        t.forward(w)
        t.right(90)
        t.forward(l)
        t.left(90)
        t.forward(w)                             # t.forward(w)
        t.left(90)


def baloons(tess):                             # This function draws our balloons
    tess.left(150)
    tess.forward(100)






def flatoval(r, tess):                           # this draws our oval shaped baloons
    tess.fillcolor("#8B4513")
    tess.begin_fill()                                            # Horizontal Oval
    tess.right(45)
    for loop in range(2):
        tess.circle(r,90)
        tess.circle(r%3,90)
    tess.end_fill()
    tess.right(60)
    tess.begin_fill()
    tess.fillcolor("pink")
    tess.begin_fill()
    for great in range(2):
     tess.circle(r, 90)
     tess.circle(r%3,90)
    tess.end_fill()
    tess.left(120)
    tess.fillcolor("red")
    tess.begin_fill()
    for mob in range(2):
        tess.circle(r, 90)
        tess.circle(r%2, 90)
    tess.end_fill()




#talloval(50)


#
def write(tess):                          # this function writes the text "happy birthday"
    tess.penup()
    tess.setpos(-300, -200)
    tess.pendown()
    tess.left(90)
    tess.write("HAPPY BIRTHDAY ABDUL ", move=False, align='center', font=("Arial", 40, ("bold", "normal")))


def main():
    """
    This main function contain some part of my rectangle function.
    :return:
    """

    hassan = turtle.Turtle()

    hassan.pensize(10)

    tess = turtle.Turtle()
    tess.pensize(10)
    tess.color("blue")

    mouse = turtle.Turtle()

    wn = turtle.Screen()

    wn.bgcolor("#d4ddb7")
    hassan.color("white")
    hassan.color("red")

    hassan.speed(20)
    tess.speed(20)

    hassan.fillcolor("#8B4513")
    #hassan.begin_fill()

    for i in [300, 200, 100]:             # This loop repeats our three layers of cake.

        for v in range(2):
            rect(hassan, i)

        if i == 100:
            break

        move(hassan)
    #hassan.end_fill()


    hassan.forward(30)
    hassan.left(90)

    baloons(tess)

    lamp(hassan, 50, 10)
    flatoval(100, tess)

    write(tess)
    wn.exitonclick()

main()













































































