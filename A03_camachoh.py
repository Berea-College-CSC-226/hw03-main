#############################
# Name: Henry Camacho
# Username: camachoh

# assignment: A03 A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
# Google Doc: https://docs.google.com/document/d/1Q498kj0SC1jqCYIzW5itAKzHmZA9jXYs2dJ_xtgM71A/edit?usp=sharing
############################################

import turtle

wn= turtle.Screen()
wn.bgpic("michael3.gif")
wn.bgcolor('black')

text = turtle.Turtle()
turtle.color("white")
style = ( 'courier', 10, 'bold')
turtle.write ("When Professor Scott asks \n if we're ready for the quiz", font=style, align='center')
turtle.hideturtle()

def funny_face():
    circle = turtle.Turtle()
    circle.speed(10)
    circle.setpos(0, -100)
    circle.fillcolor("yellow")
    circle.begin_fill()
    for face in range(75):
        circle.forward(10)
        circle.right(5)
    circle.end_fill()

    eyes = turtle.Turtle()
    eyes.speed(10)

    eyes.penup()
    eyes.setpos(50,-150)
    eyes.shape ("triangle")
    eyes.stamp()
    eyes.setpos(-50, -150)
    mouth = turtle.Turtle ()
    mouth.speed(10)
    mouth.penup ()
    mouth.setpos(50, -250)
    mouth.pendown()
    mouth.left(90)
    for smile in range(30):
        mouth.forward(5)
        mouth.left(5)
    mouth.hideturtle()



funny_face()










        


wn.exitonclick()