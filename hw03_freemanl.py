def draw_heart1(turtle,pensize):
    turtle.pensize(pensize)
    turtle.left(125)
    turtle.forward(145)
    for cir in range(85):
        turtle.fd(2)
        turtle.right(2)

def draw_heart2(turtle,pensize):
    turtle.pensize(pensize)
    turtle.left(55)
    turtle.fd(145)
    for cir in range(85):
        turtle.fd(2)
        turtle.left(2)

def main():
    import turtle
    wn = turtle.Screen()
    wn.colormode(255)
    wn.bgcolor(246,0,255)
    tre = turtle.Turtle()
    tre.color(255,255,255)
    ari = turtle.Turtle()
    ari.color(255,255,255)
    draw_heart1(tre,3)
    draw_heart2(ari,3)




    wn.exitonclick()
main()