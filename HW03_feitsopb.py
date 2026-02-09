import turtle

# Screen setup
screen = turtle.Screen()
screen.bgcolor("skyblue")

t = turtle.Turtle()
t.speed(3)
t.width(2)

# ---------- LAWN ----------
t.penup()
t.goto(-300, -200)
t.pendown()
t.color("green")
t.begin_fill()

for _ in range(2):
    t.forward(600)
    t.left(90)
    t.forward(120)
    t.left(90)

t.end_fill()

# ---------- HOUSE BASE ----------
t.penup()
t.goto(-100, -80)   # just above the lawn
t.pendown()
t.color("black", "burlywood")
t.begin_fill()

for _ in range(2):
    t.forward(200)
    t.left(90)
    t.forward(140)
    t.left(90)

t.end_fill()

# ---------- ROOF (TRIANGLE) ----------
t.penup()
t.goto(-100, 60)
t.pendown()
t.color("black", "brown")
t.begin_fill()

t.forward(200)
t.left(135)
t.forward(140)
t.left(90)
t.forward(140)
t.left(135)

t.end_fill()

# ---------- WINDOWS ----------
t.color("black", "lightyellow")

# Left window
t.penup()
t.goto(-70, -20)
t.pendown()
t.begin_fill()
for _ in range(4):
    t.forward(40)
    t.left(90)
t.end_fill()

# Right window
t.penup()
t.goto(30, -20)
t.pendown()
t.begin_fill()
for _ in range(4):
    t.forward(40)
    t.left(90)
t.end_fill()

# ---------- DOOR ----------
t.penup()
t.goto(-15, -80)   # centered at bottom of house
t.pendown()
t.color("black", "saddlebrown")
t.begin_fill()

for _ in range(2):
    t.forward(30)
    t.left(90)
    t.forward(70)
    t.left(90)

t.end_fill()

# Door knob
t.penup()
t.goto(10, -45)
t.pendown()
t.color("gold")
t.begin_fill()
#t.circle(3)
t.end_fill()

# ---------- SUN ----------
t.penup()
t.goto(180, 140)
t.pendown()
t.color("orange", "yellow")
t.begin_fill()
t.circle(35)
t.end_fill()

# Sun rays
for _ in range(12):
    t.penup()
    t.goto(180, 175)
    t.setheading(_ * 30)
    t.forward(35)
    t.pendown()
    t.forward(15)

t.hideturtle()
screen.exitonclick()
