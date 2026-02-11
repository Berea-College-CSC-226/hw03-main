import turtle


def draw_background():
    screen = turtle.Screen()
    screen.bgcolor("#87CEEB")  # RGB sky blue
    return screen


def draw_house(Beni, beni,):
    t = turtle.Turtle()
    t.speed(10)
    t.penup()
    t.goto(Beni,beni)
    t.pendown()

    # House base
    t.fillcolor("#B22222")  # firebrick red
    t.begin_fill()
    for _ in range(4):
        t.forward(200)
        t.left(90)
    t.end_fill()

    # Roof
    t.fillcolor("#8B4513")  # brown
    t.begin_fill()
    t.left(45)
    for _ in range(2):
        t.forward(200 / (2 ** 0.5))
        t.left(90)
    t.end_fill()


def draw_door(B, S):
    t = turtle.Turtle()
    t.speed(10)
    t.penup()
    t.goto(B, S)
    t.pendown()

    t.fillcolor("#654321")  # dark brown
    t.begin_fill()
    for _ in range(2):
        t.forward(50)
        t.left(90)
        t.forward(100)
        t.left(90)
    t.end_fill()


def draw_window(x, y):
    t = turtle.Turtle()
    t.speed(10)
    t.penup()
    t.goto(x, y)
    t.pendown()

    t.fillcolor("#FFFF99")  # light yellow
    t.begin_fill()
    for _ in range(4):
        t.forward(50)
        t.left(90)
    t.end_fill()

    # Window panes
    t.forward(25)
    t.left(90)
    t.forward(50)
    t.backward(25)
    t.left(90)
    t.forward(25)
    t.backward(50)


def draw_tree(x, y):
    t = turtle.Turtle()
    t.speed(10)
    t.penup()
    t.goto(x, y)
    t.pendown()

    # Trunk
    t.fillcolor("#8B4513")
    t.begin_fill()
    for _ in range(2):
        t.forward(40)
        t.left(90)
        t.forward(100)
        t.left(90)
    t.end_fill()

    # Leaves
    t.penup()
    t.goto(x - 60, y + 100)
    t.pendown()
    t.fillcolor("green")
    t.begin_fill()
    t.circle(80)
    t.end_fill()


def draw_sun(x, y):
    t = turtle.Turtle()
    t.speed(10)
    t.penup()
    t.goto(x, y)
    t.pendown()

    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(50)
    t.end_fill()


def main():
    screen = draw_background()

    draw_house(-100, -100)
    draw_door(-25, -100)
    draw_window(-80, -30)
    draw_window(20, -30)
    draw_tree(200, -100)
    draw_sun(-250, 200)

    screen.exitonclick()  # keeps window open


main()
