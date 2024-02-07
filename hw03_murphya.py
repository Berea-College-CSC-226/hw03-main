import turtle



abby = turtle.Turtle()

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
def main():
    wn = turtle.Screen()
    drawRectangle(abby, 180, 75)
    wn.exitonclick()
main()
