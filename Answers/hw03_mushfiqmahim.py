import turtle

def setup_screen():
    """Create window with non-white background and enable RGB colors."""
    wn = turtle.Screen()
    wn.title("HW03 – Fully Functional Gitty Psychedelic Robotic Turtles")
    wn.setup(900, 650)
    wn.bgcolor("#eaf6ff")       # non-white background (HEX)
    turtle.colormode(255)
    return wn

def make_pen():
    """Return a configured turtle (hidden, fast)."""
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.pensize(2)
    return t

def draw_ground(t):
    t.up(); t.goto(-460, -200); t.setheading(0); t.down()
    t.color((110, 170, 110))
    t.begin_fill()
    for _ in range(2):
        t.forward(920); t.right(90); t.forward(200); t.right(90)
    t.end_fill()

def draw_house(t, x=-180, y=-200, w=300, h=200):
    """Minimal house: body, roof, door, one window."""
    t.up(); t.goto(x, y); t.setheading(0); t.down()
    t.color("#c9b79c", "#c9b79c")  # body (HEX)
    t.begin_fill()
    for _ in range(2):
        t.forward(w); t.left(90); t.forward(h); t.left(90)
    t.end_fill()

    # roof (triangle)
    t.color("#5a4636", "#5a4636")
    t.up(); t.goto(x, y + h); t.down()
    t.begin_fill()
    t.forward(w)
    t.left(135); t.forward(w * 0.35)
    t.left(90);  t.forward(w * 0.35)
    t.left(135)
    t.end_fill()

    # door
    dw, dh = w * 0.18, h * 0.48
    dx = x + w * 0.15; dy = y
    t.color("#7d5a50", "#7d5a50")
    t.up(); t.goto(dx, dy); t.setheading(0); t.down()
    t.begin_fill()
    for _ in range(2):
        t.forward(dw); t.left(90); t.forward(dh); t.left(90)
    t.end_fill()

    # window (single)
    ww, wh = w * 0.22, h * 0.22
    wx = x + w * 0.62; wy = y + h * 0.55
    t.color("#8ecae6", "#8ecae6")
    t.up(); t.goto(wx, wy); t.down()
    t.begin_fill()
    for _ in range(2):
        t.forward(ww); t.left(90); t.forward(wh); t.left(90)
    t.end_fill()

    t.color("#2b2d42"); t.up(); t.goto(wx + ww/2, wy); t.setheading(90); t.down(); t.forward(wh)
    t.up(); t.goto(wx, wy + wh/2); t.setheading(0); t.down(); t.forward(ww)

def write_label(t, text="Home", x=0, y=240):
    """Top label."""
    t.up(); t.goto(x, y); t.color("#264653")
    t.write(text, align="center", font=("Arial", 18, "bold"))


def main():
    wn = setup_screen()
    pen = make_pen()


    draw_ground(pen)
    draw_house(pen)          # single complex object with a small detail (window)
    write_label(pen, "Blue Ridge House")

    wn.mainloop()

main()
