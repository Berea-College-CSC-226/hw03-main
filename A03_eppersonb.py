import turtle
wn = turtle.Screen()
wn.title("Ambulance")
wn.bgcolor("blue")
wn.colormode(255)
bryan = turtle.Turtle()
w1 = turtle.Turtle()
w2 = turtle.Turtle()
medic = turtle.Turtle()
bryan.pensize(5)
w1.pensize(7)
w2.pensize(7)
medic.pensize(5)
medic.pencolor(255, 0, 0)
wn.colormode(255)


def drawambulance():
    """This draws an ambulance!!!

    return:None
    """
    bryan.fillcolor(255,255,255)
    bryan.begin_fill()
    for i in range(1):
        bryan.forward(90)
        bryan.right(90)
        bryan.forward(50)
        bryan.right(-90)
        bryan.forward(50)
        bryan.right(25)
        bryan.forward(50)
        bryan.right(65)
        bryan.forward(50)
        bryan.right(90)
        bryan.forward(250)
        bryan.right(90)
        bryan.forward(120)
        bryan.right(90)
        bryan.forward(65)
    bryan.end_fill()

def drawwheel():
    """This draws the first wheel

    return:None
    """

    w1.fillcolor(0,0,0)
    w1.penup()
    w1.right(90)
    w1.forward(90) #moves the pen
    w1.right(-90)
    w1.pendown()
    w1.begin_fill()
    for i in range(20):
        w1.right(25)
        w1.forward(13) #draws the wheel
    w1.penup()
    w1.end_fill()








def drawwheel2():
    """This draws the second wheel

    return:None
    """
    w1.fillcolor(0,0,0)
    w2.penup()
    w2.forward(110)
    w2.right(90)
    w2.forward(90)
    w2.right(-90)
    w2.pendown()
    w2.begin_fill()
    for i in range(20):
        w2.right(25)
        w2.forward(12.15) #draws the second wheel
    w2.end_fill()
def drawcross():
    """This draws a medical cross on the ambulance

    return:None
    """
    medic.fillcolor(255,0,0)
    medic.penup()
    medic.right(90)
    medic.forward(80)
    medic.right(90)
    medic.pendown()
    medic.begin_fill()
    for i in range(2):
        medic.forward(15)   #This line of code makes a cross!
        medic.right(90)
        medic.forward(25)
        medic.right(-90)
        medic.forward(25)
        medic.right(90)
        medic.forward(25)
        medic.right(90)
        medic.forward(25)
        medic.right(-90)
        medic.forward(25)
        medic.right(90)
        medic.forward(15)
    medic.end_fill()







def main():
    '''
    The main function of the program, where all things begin.

    :return: None
    '''
    drawambulance()
    drawwheel()
    drawwheel2()
    drawcross()


main()

wn.mainloop()
