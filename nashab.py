######################################################################################################################
#Abby Nash
#A03
#https://docs.google.com/document/d/1YPYte0A-F_B81MbWRtEEEVA_m-7WIgOkZkXjiEfnV3w/edit?usp=sharing
##################################################################################################################
import turtle

wn=turtle.Screen()
wn.bgcolor('#DDDDDD')
a=turtle.Turtle()
a.hideturtle()

def function_1():

    a= turtle.Turtle()
    a.penup()
    a.goto(5,-50)
    a.pendown()
    a.circle(100,None,None)

    a.penup() #starting to draw eye one
    a.goto(-40,70)
    a.pendown()
    a.begin_fill()
    a.circle(5,None,None) #eye one
    a.color('blue')
    a.end_fill()



    a.penup()
    a.goto(40,70)
    a.pendown()
    a.begin_fill()
    a.circle(5,None,None) #eye two\
    a.color('blue')
    a.end_fill()


    a.penup()
    a.goto(0,0)
    a.pendown()
    a.color('red')
    a.circle(75,45)   #right smile
    a.end_fill()


    a.penup()
    a.setheading(180) # <-- look West I had help with this
    a.goto(0,0)
    a.pendown()
    a.circle(-75,45)

    a.penup()
    a.goto(5,-50)
    a.right(225)
    a.pendown()
    a.color("black")
    a.forward(150)
    a.end_fill()

    a.penup()
    a.goto(5,-50)
    a.right(310)
    a.pendown()
    a.forward(80)

    a.penup()
    a.goto(5,-50)
    a.left(250)
    a.pendown()
    a.forward(80)

    a.penup()
    a.goto(5,-195)
    a.right(310)
    a.pendown()
    a.forward(80)

    a.penup()
    a.goto(5,-195)
    a.left(30)
    a.pendown()
    a.forward(81)
    a.hideturtle()


def main():
    function_1()

main()


wn.exitonclick()
