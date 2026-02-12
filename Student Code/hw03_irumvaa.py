#################################################################################
# Author: Alain Irumva
# Username: irumvaa
#
# Assignment: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Source Control and Git
# Google Doc Link: https://docs.google.com/document/d/1pOIbG65CpjYltCJQEnEJ-lRjg3jt2vX88Tf9P7UaTw0/edit?usp=sharing
import turtle

def main(alain):
    """Initializes the turtle graphics window and starts drawing."""
    turtle.colormode(255)
    wn = turtle.Screen()
    wn.bgcolor('lightgreen')
    turtle.pensize(4)

    build_my_roof(alain)
    draw_wheel(80, 50, alain)
    build_floor(alain)
    wn.exitonclick()

def build_my_roof(alain):
    """Build a roof and paint it brown."""
    alain.color("black", "brown")
    alain.speed(0)
    alain.penup()
    alain.goto(-220, 140)  # Roof position

    alain.begin_fill()
    alain.pendown()
    alain.fd(300)
    alain.left(160)
    alain.fd(200)
    alain.left(50)
    alain.fd(130)
    alain.right(200)
    alain.end_fill()

    alain.penup()
    alain.color("blue")
    alain.fd(60)
    alain.right(100)
    alain.fd(15)
    alain.pendown()
    alain.fd(90)
    alain.left(90)

    for _ in range(80):
        draw_wheel_segment(alain)

    alain.penup()
    alain.right(80)
    alain.fd(150)
    alain.right(80)
    alain.fd(280)
    alain.right(90)
    alain.fd(15)
    alain.pendown()
    alain.color("blue")
    alain.fd(80)


def draw_wheel(x, y, alain):
    """Draw a yellow wheel at the specified position."""
    alain.penup()
    alain.goto(x, y)
    alain.setheading(0)  # reset direction
    alain.pendown()

    for _ in range(80):
        draw_wheel_segment(alain)

    alain.penup()


def draw_wheel_segment(alain):
    """Draw a segment of the wheel."""
    alain.color("black", "yellow")
    alain.begin_fill()
    alain.right(120)  # Wheel rotation angle
    alain.fd(40)  # Wheel size
    alain.left(50)
    alain.fd(40)
    alain.end_fill()


def build_floor(alain):
    """Draw a grey floor under the house."""
    alain.penup()
    alain.goto(-300, -40)  # Floor position
    alain.setheading(0)
    alain.color("black", "grey")
    alain.pendown()

    alain.begin_fill()
    alain.fd(500)  # Floor width
    alain.right(90)
    alain.fd(40)  # Floor height
    alain.right(90)
    alain.fd(500)
    alain.right(90)
    alain.fd(40)
    alain.end_fill()

    alain.penup()
    alain.goto(-130, 200)  # Position of the text
    alain.color("black")
    alain.write("My Moving House", align="center", font=("Arial", 30, "bold"))

if __name__ == "__main__":
    alain = turtle.Turtle()
    main(alain)