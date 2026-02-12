#https://www.geeksforgeeks.org/python/turtle-setpos-and-turtle-goto-functions-in-python/
#https://realpython.com/beginners-guide-python-turtle/#drawing-a-shape
import turtle


def setup_screen():

    screen = turtle.Screen()
    screen.colormode(255)
    screen.bgcolor(139, 182, 255)


def draw_face():

    turtle.penup()
    turtle.goto(0, -50)
    turtle.pendown()
    turtle.colormode(255)
    turtle.color(217, 218, 219)
    turtle.begin_fill()
    turtle.circle(100)
    turtle.end_fill()


def draw_ears():
    turtle.colormode(255)
    turtle.color(217, 218, 219)

    # Left ear
    turtle.penup()
    turtle.goto(-70, 70)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(40)
    turtle.end_fill()

    # Right ear
    turtle.penup()
    turtle.forward(100)
    turtle.goto(70, 70)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(40)
    turtle.end_fill()


def draw_eyes():

    turtle.color("black", "black")

    # Left eye
    turtle.penup()
    turtle.goto(-35, 20)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()

    # Right eye
    turtle.penup()
    turtle.goto(35, 20)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()


def draw_nose():

    turtle.penup()
    turtle.goto(0, -10)
    turtle.pendown()
    turtle.color("black", "black")
    turtle.begin_fill()
    turtle.circle(8)
    turtle.circle(-2)
    turtle.circle(2)
    turtle.end_fill()


def draw_tongue():

    turtle.penup()
    turtle.goto(0, -25)
    turtle.pendown()
    turtle.color("black", "pink")
    turtle.begin_fill()
    turtle.circle(4)
    turtle.end_fill()
def draw_collar():
    turtle.penup()
    turtle.goto(-50, -500)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.color("red")
    turtle.forward(100)

    turtle.begin_fill()
    turtle.end_fill()

    turtle.color("red")

def main():

    turtle.speed(0)
    setup_screen()

    draw_ears()
    draw_face()
    draw_eyes()
    draw_nose()
    draw_tongue()

    turtle.hideturtle()
    turtle.done()


main()
