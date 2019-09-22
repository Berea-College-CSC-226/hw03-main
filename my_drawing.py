######################################################################
# Author: Bryar Frank
# Username: frankb
#
# Assignment: A03
#
# Acknowledgements:
#   Background Photo:
#       Url: https://www.needpix.com/photo/897566/coastline-ireland-ocean-coast-sea-irish-water-shore-seascape
#       Author: designaire (pixabay.com)
######################################################################
# Importing turtle library, creating window, and defining two turtles
import turtle
######################################################################


def draw_road(tur, x1, y1, h1, x2, y2, h2):
    """
    draw the bridge road
    :return:
    """

    # Create the slopes for the back and front of the road using x, y coordinates of pillars
    slope1 = float(((y2+h2/5)-(y1+h1/5))/(x2-x1))
    slope2 = float(((y2+7*h2/30)-(y1+7*h1/30))/((x2-h2/5.5)-(x1-h1/5.5)))

    # Set the start and finish positions of y coordinates for the turtle for the road
    ystartposition1 = (y1+h1/5) - (600+x1)*slope1
    yendposition1 = ystartposition1 + slope1*1200
    ystartposition2 = (y1+h1/6) + (600+x1-h1/5.5)*slope2
    yendposition2 = ystartposition2 + slope2*1200

    # Draw the road
    tur.penup()
    tur.pencolor(35, 35, 35)
    tur.fillcolor(30, 30, 30)
    tur.setpos(-600, ystartposition1)
    tur.pendown()
    tur.begin_fill()
    tur.setpos(600, yendposition1)
    tur.setpos(600, yendposition2)
    tur.setpos(-600, ystartposition2)
    tur.setpos(-600, ystartposition1)
    tur.end_fill()


def draw_back_pillar(tur, x, y, h):
    """
    Draws a pillar with a bit of 3D distortion to it to represent the back of the bridge
    :return:
    """
    # Create a new starting point for back pillar
    newx = x - (h/5.5)
    newy = y + (h/30)
    tur.penup()
    tur.setpos(newx, newy)

    # prepare turtle
    tur.seth(90)
    tur.pencolor(185, 30, 30)
    tur.pendown()
    tur.fillcolor(185, 30, 30)
    tur.begin_fill()

    # Begin to draw pillar shape, including support bars across top
    for i in range(5):
        tur.fd(h / 5)
        tur.rt(45)
        tur.fd(h / 150)
        tur.lt(45)

    tur.rt(90)
    tur.fd(h / 50)
    tur.rt(90)

    for i in range(5):
        tur.lt(45)
        tur.fd(h / 150)
        currentx = tur.xcor()
        currenty = tur.ycor()
        tur.setpos(currentx+(h/5.5), currenty-(h/30))
        tur.seth(-90)
        tur.fd(h/15)
        currentx = tur.xcor()
        currenty = tur.ycor()
        tur.setpos(currentx-(h/5.5), currenty+(h/30))
        tur.seth(-90)
        tur.fd((2*h)/15)

    # put turtle back to start and fill shape
    tur.setpos(newx, newy)
    tur.end_fill()
    tur.penup()


def draw_front_pillar(tur, x, y, h):
    """
    Draws the front pillar to cover over the road.
    :return:
    """
    # Set up turtle
    tur.penup()
    tur.setpos(x, y)
    tur.seth(90)
    tur.pencolor(195, 30, 30)
    tur.pendown()
    tur.fillcolor(200, 30, 30)
    tur.begin_fill()

    # Draw pillar
    for i in range(5):
        tur.fd(h / 5)
        tur.rt(45)
        tur.fd(h / 150)
        tur.lt(45)

    tur.rt(90)
    tur.fd(h / 50)
    tur.rt(90)

    for i in range(5):
        tur.lt(45)
        tur.fd(h / 150)
        tur.rt(45)
        tur.fd(h / 5)

    # Finish filling in pillar
    tur.setpos(x, y)
    tur.end_fill()
    tur.penup()


def draw_front_ties(tur, x1, y1, h1, x2, y2, h2):
    """
    draws the road ties connecting the bridge pillars to road
    :return:
    """
    ystart = y1 + 4*h1/5
    xpillar1 = x1 + h1/25
    ypillar1 = y1 + h1*1.02
    xmid = x1 + (2*(x2 - x1)/3)
    ymid = (y1+h1/5) + (2*((y2+h2/5)-(y1+h1/5))/3)
    xpillar2 = x2 + h2/50
    ypillar2 = y2 + h2
    yend = y2 + h2/1.9

    tur.penup()
    tur.pencolor(100, 100, 100)
    tur.pensize(5)
    tur.setpos(-600, ystart)
    tur.pendown()
    tur.setpos(xpillar1, ypillar1)
    tur.pensize(4)
    tur.setpos(xmid, ymid)
    tur.pensize(3)
    tur.setpos(xpillar2, ypillar2)
    tur.pensize(2.5)
    tur.setpos(600, yend)


def draw_back_ties(tur, x1, y1, h1, x2, y2, h2):
    """
    draws the road ties in the back from the pillar to the road
    :return:
    """
    newx1 = x1 - (h1 / 5.5)
    newy1 = y1 + (h1 / 30)
    newx2 = x2 - (h2 / 5.5)
    newy2 = y2 + (h2 / 30)

    ystart = newy1 + 4.5 * h1 / 5
    xpillar1 = newx1 + h1 / 25
    ypillar1 = newy1 + h1 * 1.02
    xmid = newx1 + (2 * (newx2 - newx1) / 3)
    ymid = (newy1 + h1 / 5) + (2 * ((newy2 + h2 / 5) - (newy1 + h1 / 5)) / 3)
    xpillar2 = newx2 + h2 / 50
    ypillar2 = newy2 + h2
    yend = newy2 + h2 /2

    tur.penup()
    tur.pencolor(75, 75, 75)
    tur.pensize(5)
    tur.setpos(-600, ystart)
    tur.pendown()
    tur.setpos(xpillar1, ypillar1)
    tur.pensize(4)
    tur.setpos(xmid, ymid)
    tur.pensize(3)
    tur.setpos(xpillar2, ypillar2)
    tur.pensize(2.5)
    tur.setpos(600, yend)


def main():
    """
    Create Bridge with Background Picture
    :return:
    """
    # Create Screen
    scr = turtle.Screen()
    scr.setup(1200, 768)
    scr.colormode(255)

    # Insert background picture for Screen
    # Credit: https://www.needpix.com/photo/897566/coastline-ireland-ocean-coast-sea-irish-water-shore-seascape
    scr.bgpic("coastline.gif")

    # Create Turtle
    boop = turtle.Turtle()
    boop.speed(9)

    # Define position and size of bridge
    x1 = -400
    y1 = -250
    h1 = 550

    x2 = 475
    y2 = 50
    h2 = 120

    # Draw the back road ties
    draw_back_ties(boop, x1, y1, h1, x2, y2, h2)

    # Draw the back pillars
    boop.pensize(3)
    draw_back_pillar(boop, x1, y1, h1)
    boop.pensize(1)
    draw_back_pillar(boop, x2, y2, h2)

    # Draw the road of the bridge
    draw_road(boop, x1, y1, h1, x2, y2, h2)

    # Draw the front part of the pillars
    boop.pensize(3)
    draw_front_pillar(boop, x1, y1, h1)
    boop.pensize(1)
    draw_front_pillar(boop, x2, y2, h2)

    # Draw the front road ties
    draw_front_ties(boop, x1, y1, h1, x2, y2, h2)

    # screen exit on click
    scr.exitonclick()


main()
