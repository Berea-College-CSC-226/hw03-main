######################################################################
# Author: Collins kandongwe
# Username: kandongwec
# Assignment: A03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Continue practicing creating and using functions.
# More practice on using the turtle library.
# Learn about how computers represent colors.
# Learn about source control and git.
######################################################################
# Acknowledgements:
# color combinations used came from https://www.wolframalpha.com/widgets/gallery/view.jsp?id=c0abe9808671bca189c7e6a560739ae4
# use the turtle libray specified by https://docs.python.org/3/library/turtle.html#turtle.heading for specific turtle movements
######################################################################
import turtle

wn = turtle.Screen()
wn.colormode(255)
wn.bgcolor("gray")
ed = turtle.Turtle()              # creating new turtles and turtle screen
dj = turtle.Turtle()
ed.ht()
dj.hideturtle()
ed.speed(0)
dj.speed(0)


def draw_rectangle(col, x, y, l, w):
    """
    Draws rectangle on position x, y with length of l and width of w
    """
    ed.fillcolor(col)                              # begin filling the shape drew with specified color
    ed.up()
    ed.goto(x, y)
    ed.down()
    ed.begin_fill()
    for i in range(2):
        ed.fd(l)
        ed.left(90)
        ed.fd(w)
        ed.left(90)

    ed.end_fill()                                           # stop filling shape


def draw_triangle():
    """
    Draws a triangle
    """
    ed.fillcolor((139, 69, 19))
    ed.up()
    ed.begin_fill()
    ed.goto(-225, 5)
    ed.goto(20, 110)
    ed.goto(275, 5)
    ed.goto(-225, 5)
    ed.end_fill()


def draw_square(x, y):
    """
    Draws a square beginning  at position x , y
    """
    dj.up()
    dj.setheading(0)                                  # set the direction of the turtle instance to north
    dj.fillcolor(255, 255, 255)
    dj.begin_fill()
    dj.goto(x, y)
    for i in range(4):
        dj.fd(95)
        dj.left(90)

    dj.end_fill()
    dj.down()
    dj.seth(0)
    dj.fd(47.5)
    dj.left(90)
    dj.fd(95)
    dj.rt(90)
    dj.fd(47.5)
    dj.rt(90)
    dj.fd(47.5)
    dj.rt(90)
    dj.fd(95)


def draw_moon():
    """
    Draws a moon
    """
    ed.up()
    ed.goto(-234, 180)
    ed.fillcolor((225, 255, 255))
    ed.begin_fill()
    ed.circle(50)
    ed.end_fill()
    ed.goto(-260, 220)                          # move turtle instance to the centre of the circle
    ed.pencolor(0, 0, 0)
    ed.pensize(8)
    ed.write("FULL MOON")                        # Writes full moon inside the circle


def write_something():
    """
    Writes something on the turtle graphics canvas
    """
    ed.up()
    ed.setpos(0, 85)
    ed.write("May not be much", move=True, align="center", font=["chiller", 40, "bold"])
    ed.setpos(0, 0)
    ed.write("But, I call this Home!!", move=True, align="center", font=["chiller", 40, "bold"])


def main():
    """Calls all the other functions"""
    draw_rectangle((0, 0, 128), -225, -225, 500, 230)    # draws the body of the house with specified color, position
    draw_rectangle((0, 0, 0), -20, -225, 90, 120)        # draws the door of th house
    draw_triangle()                                      # draws the roof of the house
    draw_square(-180, -125)                              # draws the left side window
    draw_square(130, -125)                                # draws the right side window
    draw_rectangle((139, 69, 19), 275, 5, -20, 50)        # Draws a Chimney
    draw_moon()                                          # Draws a moon
    write_something()                                     # writes words on the screen
    wn.mainloop()


main()

