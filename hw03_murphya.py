import turtle

wn = turtle.Screen()
abby = turtle.Screen()
abby.bgpic('starry.gif')

abby = turtle.Turtle()
aaliyah = turtle.Turtle()

#This code makes the horizon line and makes the water blue.
abby.color("#3A3C8E", "#3A3C8E")
abby.begin_fill()
abby.penup()
abby.right(90)
abby.forward(65)
abby.pendown()
abby.left(90)
abby.forward(375)
abby.left(180)
abby.forward(700)
abby.left(90)
abby.forward(200)
abby.left(90)
abby.forward(700)
abby.left(90)
abby.forward(200)
abby.left(90)
abby.end_fill()

abby.penup()
abby.goto(-40, -65)
abby.pendown()
#This code makes the ship dock
abby.forward(250)
abby.left(90)
abby.color("#8E5B3A", "#8E5B3A")
def drawRectangle(t, w, h):
    for i in range(2):
        abby.begin_fill()
        abby.forward(w)
        abby.left(90)
        abby.forward(h)
        abby.left(90)
        abby.end_fill()

#worked on the boat
aaliyah.penup()
aaliyah.goto(-90,-160)
aaliyah.pendown()
aaliyah.color("#8E5B3A", "#8E5B3A")
aaliyah.begin_fill()
aaliyah.right(90)
aaliyah.circle(100,180)
aaliyah.left(90)
aaliyah.forward(200)
aaliyah.end_fill()
aaliyah.backward(100)
aaliyah.right(90)
aaliyah.forward(100)
def drawFlag(t, sz):

    for i in range(4):
        t.forward(sz)
        t.left(90)

def main():
    drawRectangle(abby, 180, 75)
    drawFlag(aaliyah, 50)
    wn.exitonclick()
main()
