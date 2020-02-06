
import turtle


def rect(t, leng):
    t.forward(leng)
    t.right(90)
    t.forward(100)
    t.right(90)


def move(t):
    t.fd(50)
    t.left(90)
    t.fd(100)
    t.right(90)


def lamp(t, l, w):
    for g in range(3):
        t.forward(l)
        t.right(90)
        t.forward(w)
        t.right(90)
        t.forward(l)
        t.left(90)
        t.forward(w)                             # t.forward(w)
        t.left(90)


def baloons(tess):
    tess.left(150)
    tess.forward(100)
    #tess.penup()
    #tess.setposition(-300, -100)
    #tess.pendown()
    #tess.forward(100)




#def talloval(r):               # Verticle Oval
 #   hassan.left(45)
  #  for loop in range(5):      # Draws 2 halves of ellipse
   #     hassan.circle(r,90)    # Long curved part
    #    hassan.circle(r/2,90)  # Short curved part

def flatoval(r, tess):
    tess.fillcolor("#8B4513")
    tess.begin_fill()                                            # Horizontal Oval
    tess.right(45)
    for loop in range(2):
        tess.circle(r,90)
        tess.circle(r%3,90)
    tess.end_fill()
    tess.right(60)
    tess.begin_fill()
    tess.fillcolor("pink")
    tess.begin_fill()
    for great in range(2):
     tess.circle(r, 90)
     tess.circle(r%3,90)
    tess.end_fill()
    tess.left(120)
    tess.fillcolor("red")
    tess.begin_fill()
    for mob in range(2):
        tess.circle(r, 90)
        tess.circle(r%2, 90)
    tess.end_fill()




#talloval(50)


#
def write(tess):
    tess.penup()
    tess.setpos(-300, -200)
    tess.pendown()
    tess.left(90)
    tess.write("HAPPY BIRTHDAY ABDUL ", move=False, align='center', font=("Arial", 40, ("bold", "normal")))


def main():
    hassan = turtle.Turtle()
    hassan.pensize(10)

    tess = turtle.Turtle()
    tess.pensize(10)
    tess.color("blue")

    mouse = turtle.Turtle()

    wn = turtle.Screen()
    wn.bgcolor("white")
    hassan.color("white")
    hassan.color("red")

    hassan.speed(20)
    tess.speed(20)

    hassan.fillcolor("#8B4513")
    hassan.begin_fill()

    for i in [300, 200, 100]:

        for v in range(2):
            rect(hassan, i)

        if i == 100:
            break

        move(hassan)
    hassan.end_fill()


    hassan.forward(30)
    hassan.left(90)

    baloons(tess)

    lamp(hassan, 50, 10)
    flatoval(100, tess)

    write(tess)
    wn.exitonclick()

main()

















































"""def rectangle(t, l):
    for i in range (2):
        t.forward(l)
        t.left(90)
        t.forward(100)
        t.left(90)

def first_block_of_cake(color,):
    hassan.penup()
    hassan.setpos(-300, -200)
    hassan.pendown()
    #for i in range(2):
    rectangle(hassan, 300)
    hassan.penup()
    hassan.goto(-280, -100)
    hassan.right(90)
    hassan.pendown()
def second_block_of_cake():
      #hassan.begin_fill()
      rectangle(hassan, 200)
      #hassan.end_fill()
      hassan.penup()
      hassan.goto(-260, 0)
      hassan.left(90)
      hassan.left(90)
      hassan.pendown()
def third_block_of_cake():
    rectangle(hassan, 100)










first_block_of_cake("red")

second_block_of_cake()
third_block_of_cake()"""






















