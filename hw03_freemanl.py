def draw_heart1(turtle,pensize):
    turtle.pensize(pensize)
    turtle.left(125)
    turtle.forward(145)
    for cir in range(82):
        turtle.fd(2)
        turtle.right(2)

def draw_heart2(turtle,pensize):
    turtle.pensize(pensize)
    turtle.left(55)
    turtle.fd(145)
    for cir in range(82):
        turtle.fd(2)
        turtle.left(2)

def break_heart(turtle,pensize):
    turtle.pensize(pensize)
    turtle.left(90)
    turtle.penup()
    turtle.fd(200)
    turtle.pendown()
    turtle.left(180)
    turtle.fd(20)
    turtle.right(45)
    turtle.fd(30)
    turtle.left(100)
    turtle.fd(45)
    turtle.right(90)
    turtle.fd(45)


def main():
    import turtle
    wn = turtle.Screen()
    wn.colormode(255)
    wn.bgcolor(246,0,255)
    tre = turtle.Turtle()
    tre.color(255,255,255)
    ari = turtle.Turtle()
    ari.color(255,255,255)
    ty = turtle.Turtle()
    ty.color(0, 0, 0)
    ty.speed(1)
    ari.speed(0)
    tre.speed(0)
    draw_heart1(tre,3)
    draw_heart2(ari,3)
    break_heart(ty,7)
    ari.hideturtle()
    tre.hideturtle()
    ty.hideturtle()

    wn.exitonclick()
main()