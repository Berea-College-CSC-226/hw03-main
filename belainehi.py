# Created by: Immanuela Belaineh Username: belainehi
# drive: https://docs.google.com/document/d/1vT5qt0KlIlf5vfc0n5OG5T-hB03guzDR9IC3iWU3B1Y/edit?usp=sharing

import turtle

#def draw_backcircle(a, angel):
#    a.speed(10)
 #   for i in range(angel):
#        a.backward(1)
 #       a.right(1)


def drawrecta(a):
    "'This function's main purpose is to draw a rectangle around the options. It draws a cool stamp of arrows into a rectangle. '"
    for i in range(2):
        a.stamp()
        a.penup()
        for i in range(100):
            a.stamp()
            a.forward(1)
        a.left(90)
        for i in range(50):
            a.stamp()
            a.forward(1)
        a.left(90)


#def bubble(a):
 #   a.begin_fill()
  #  a.speed(0)
    # wn.bgpic("Brain 1.gif")
   # for i in range(360):
        # a.speed(10)
    #    a.stamp()
     #   a.backward(1)
      #  a.right(1)
    #a.end_fill()


def drawflower(f):
    "'This function draws a flower made of lines angeled 220 degrees inbetween.'"
    f.begin_fill()
    f.speed(0)
    for i in range(30):
        f.stamp()
        f.forward(200)
        f.left(220)
    f.end_fill()

def drawthickflower(f):
    "'This function does wat drawflower does but with a bigger pen size. '"
    f.pensize(20)
    drawflower(f)

def main():
    wn = turtle.Screen()
    wn.bgpic(picname="Brain 1.png")
    wn.colormode()

    d = turtle.Turtle() #This turtle writes the prompt
    d.speed(0)
    d.penup()
    d.setpos(200, -200)
    d.pendown()
    d.color("red", "white")
    d.write("\nWhat's really\n on my mind?", move=False, font=("Times", 20, ("bold", "normal")))
    print("d is:", d.position())

    a = turtle.Turtle() #This turtle provides one of the options
    a.color("red")
    a.speed(0)
    a.penup()
    a.setposition(-200, -50)
    a.write("   Family", move=False, font=("Times", 15, ("bold", "normal")))
    # ("Arial", 30, ("bold", "normal")))
    a.pendown()
    drawrecta(a)
    print("a is:", a.position())
    # bubble(a)

    b = turtle.Turtle() #This turtle provides one of the options
    b.speed(0)
    b.penup()
    b.setpos(-400, -100)
    b.color("green")
    b.write("   Friends", move=False, font=("Times", 15, ("bold", "normal")))
    b.pendown()
    drawrecta(b)
    b.penup()
    print("b is:", b.position())
    # bubble(b)

    c = turtle.Turtle() #This turtle provides one of the options
    c.speed(0)
    c.penup()
    c.setpos(0, 0)
    c.pendown()
    c.color("blue")
    c.write("   Future", move=False, font=("Times", 15, ("bold", "normal")))
    drawrecta(c)
    print("c is:", c.position())

    f = turtle.Turtle() #This turtle provides one of the options
    f.speed(0)
    f.penup()
    f.setpos(200, -50)
    f.color("red")
    f.write("   Self-Care", move=False, font=("Times", 15, ("bold", "normal")))
    f.pendown()
    drawrecta(f)
    print("f is:", f.position())

    e = turtle.Turtle() #This turtle draws one of the flowers
    e.speed(0)
    e.penup()
    e.setposition(-500,200)
    e.pendown()
    e.color("red","white")
    drawthickflower(e)
    e.penup()

    g = turtle.Turtle() #This turtle draws one of the flowers
    g.penup()
    g.setpos(150, 200)
    g.pendown()
    g.color("blue","white")
    drawflower(g)

    h = turtle.Turtle() #This turtle draws one of the flowers
    h.penup()
    h.setpos(-150, 200)
    h.pendown()
    drawflower(h)
    h.penup()


    wn.exitonclick()


main()
