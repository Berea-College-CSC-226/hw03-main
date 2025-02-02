import turtle


w = turtle.Turtle()
s=turtle.Turtle()


def draw_rectangle(t,s):
    for i in range(100):
        t.forward(i)
        t.left(90)


def triangle():
    for i in range(50):
        w.forward(i * 5)
        w.left(120)


def flower():
    t = turtle.Turtle()
    t.speed(8)
    t.color('red', 'blue')
    t.begin_fill()
    for i in range(100):
        t.penup()
        t.forward(100)
        t.left(90)
        t.pendown()
        t.forward(100)
        t.left(169)


def star():
    s.pencolor('orange')
    s.penup()
    s.fd(-100)
    s.left(90)
    s.pendown()
    for i in range(100):

        s.forward(100)
        s.left(169)


def main():
    wn = turtle.Screen()
    wn.bgcolor('blue')
    tess = turtle.Turtle()
    tess.color('green')
    w.pencolor("black")
    w.pensize(1)
    w.penup()
    w.forward(200)
    w.pendown()
    tess.pensize(0)
    w.penup()
    w.bk(200)
    w.pendown()
    draw_rectangle(tess, 50)
    triangle()
    flower()
    star()
    wn.exitonclick()

main()








