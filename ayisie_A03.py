# Author : Ebenezer Ayisi
# Username: ayisie
# google link : https://docs.google.com/document/d/1EN02kKmUNzDABtUjf3uC-kj8b4T7asFKH69ek9Z7bSg/edit?usp=sharing
# Assignment: T03: Turtles
# Purpose: To very simply demonstrate the turtle library to demo shapes and using images for shapes



import turtle

def draw_eyes(je):
    """ draw eyes of the face"""
    je.begin_fill()
    je.circle(20)
    je.end_fill()
    je.penup()
    je.backward(55)
    je.begin_fill()
    je.circle(20)
    je.end_fill()






def draw_face(je):
    """draw the shape of the face"""
    je.penup()
    je.setpos(-120, -10)
    je.pendown()
    je.left(-90)
    je.circle(90,180)
    je.forward(78)
    je.left(90)
    je.forward(180)
    je.left(90)
    je.forward(82)




def draw_hair(je):
    """draw the hair of the head"""
    je.speed(0)
    je.left(90)
    je.forward(-20)
    je.left(90)
    je.forward(130)

    for i in range(-140,-20, 15):
        je.circle(50,100)
        je.penup()
        je.seth(70)
        je.setpos(i,100)
        je.pendown()

    for i in range(-20,100, 15):
        je.circle(-100,50)
        je.penup()
        je.seth(70)
        je.setpos(i,100)
        je.pendown()
    je.penup()
    je.setpos(70, 100)
    je.pendown()
    je.seth(0)
    je.right(90)
    je.forward(110)
    je.left(90)
    je.forward(-10)
def main():
    """docstring for main"""
    # Create window screen
    wn = turtle.Screen()
    wn.bgcolor("blue")
    je = turtle.Turtle()
    je.pensize(10)

    draw_eyes(je)
    draw_face(je)
    draw_hair(je)
    wn.exitonclick()


main()
