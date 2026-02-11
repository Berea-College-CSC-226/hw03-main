#################################################################################
# Author: Alain Irumva
# Username: irumvaa
#
# Assignment: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Source Control and Git
# Google Doc Link: https://docs.google.com/document/d/1pOIbG65CpjYltCJQEnEJ-lRjg3jt2vX88Tf9P7UaTw0/edit?usp=sharing

def main():
    """Initializes the turtle graphics window"""
    import turtle
    alain = turtle.Turtle()
    turtle.colormode(255)
    wn = turtle.Screen()
    wn.bgcolor('lightgreen')
    turtle.pensize(4)

    def build_my_roof():
        """ Build a roof and paint it with Brown"""
        alain.color("black", "brown")
        alain.speed(0)
        alain.penup()
        alain.goto(-220, 140)
        for i in range(1):
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
            for i in range(80):
                alain.color("black", "yellow")
                alain.begin_fill()
                alain.right(120)
                alain.fd(40)
                alain.left(50)
                alain.fd(40)
                alain.end_fill()
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
    def draw_wheel_2(x,y):
        """Draw another yellow wheel"""
        alain.penup()
        alain.goto(x, y)
        alain.setheading(0)  # reset direction
        alain.pendown()
        for i in range(80): #set it back two 80 after testing
            alain.color("black", "yellow")
            alain.begin_fill()
            alain.right(120)
            alain.fd(40)
            alain.left(50)
            alain.fd(40)
            alain.end_fill()

        alain.penup()
    def build_floor():
        """A grey floor under the house"""
        alain.penup()
        alain.goto(-300, -40)
        alain.setheading(0)
        alain.color("black", "grey")
        alain.pendown()
        alain.begin_fill()
        alain.fd(500)
        alain.right(90)
        alain.fd(40)
        alain.right(90)
        alain.fd(500)
        alain.right(90)
        alain.fd(40)
        alain.end_fill()
        alain.penup()
        alain.penup()
        alain.goto(-130, 200)  # position of the text (top center area)
        alain.color("black")
        alain.write("My Moving House", align="center", font=("Arial", 30, "bold"))

    build_my_roof()
    draw_wheel_2(80,50)
    build_floor()

    wn.exitonclick()
main()

