




def draw_petal(petal1):
    #this function draws the petals for the flower
    petal1.color("red")
    # finding position of the stem
    # m.goto(60, 100)
    petal1.circle(10, 150)
    petal1.left(120)


def draw_flower(x, petal1):
    for i in range(x):
       draw_petal(petal1)
       petal1.right(360/x)



def main():

    import turtle
    wn = turtle.Screen()
    wn.bgcolor("lightblue")
    petal1 = turtle.Turtle()
    petal1.pendown
    ### first stem
    petal1.speed(0)
    petal1.color("green")
    petal1.left(90)
    petal1.forward(100)
    petal1.right(180)
    petal1.forward(50)
    ### second stem
    petal1.right(-45)
    petal1.forward(-20)
    petal1.right(180)
    petal1.forward(50)
    ### third stem
    petal1.right(180)
    petal1.forward(70)
    petal1.left(90)
    petal1.forward(70)

    """
    Draws a flower
    :param: sides: the number of sides of a polygon
    :param: petal1: a turtle object to draw the flower with
    """

    #middle flower drawing
    petal1.penup()
    petal1.goto(0, 100)
    petal1.pendown()

    draw_flower(20,petal1)

#right flower drawing
    petal1.penup()
    petal1.goto(60, 100)
    petal1.pendown()

    draw_flower(20,petal1)
    # left flower drawing
    petal1.penup()
    petal1.goto(-60, 100)
    petal1.pendown()
    draw_flower(20,petal1)
    petal1.hideturtle()


    wn.exitonclick()

main()  # Starts the program!

'''
 I got help from Javier Soto he helped me understand my red squiggle line errors. 
'''

