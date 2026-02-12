# Author: Mildred Catalina Gonzalez Molina
# Username: gonzalezmolinam
# Assignment: HW03:Fully functional gitty psychedelic robotic rules
# Purpose: I need to do a complex drawing
# Google Doc Link:https://docs.google.com/document/d/1J7UK_kEodkuLCn28hBy6PLai8v5HrK3YIafSBGknWus/edit?usp=sharing
#Extra help I used:
#https://www.geeksforgeeks.org/python/turtle-setpos-and-turtle-goto-functions-in-python/
#https://realpython.com/beginners-guide-python-turtle/#drawing-a-shape

'This program draws a cute white puppy face'
import turtle



'draws the puppy face, it is a circle'

def draw_face(bob):
    bob.penup()
    bob.goto(0, -50)
    bob.pendown()
    bob.color(217, 218, 219)
    bob.begin_fill()
    bob.circle(100)
    bob.end_fill()

'it draws the puppy ears'
def draw_ears(bob):
    bob.color(217, 218, 219)
    bob.penup()
    bob.goto(-70, 70)
    bob.pendown()
    bob.begin_fill()
    bob.circle(40)
    bob.end_fill()

'it draws the right ear with a circle'
def right_ear(bob):
    bob.penup()
    bob.goto(70, 70)
    bob.pendown()
    bob.begin_fill()
    bob.circle(40)
    bob.end_fill()

'It draws black eyes for the puppy'
def draw_eyes(bob):
    'it draws the left eye with a circle'
    bob.color("black")
    bob.penup()
    bob.goto(-35, 20)
    bob.pendown()
    bob.begin_fill()
    bob.circle(10)
    bob.end_fill()

    'it draws the left eye with a circle'
    bob.penup()
    bob.goto(35, 20)
    bob.pendown()
    bob.begin_fill()
    bob.circle(10)
    bob.end_fill()


'It draws a black nose for the puppy'
def draw_nose(bob):
    bob.penup()
    bob.goto(0, -10)
    bob.pendown()
    bob.color("black")
    bob.begin_fill()
    bob.circle(8)
    bob.end_fill()


'It draws a pink tongue for the puppy'
def draw_tongue(bob):
    bob.penup()
    bob.goto(0, -25)
    bob.pendown()
    bob.color("pink")
    bob.begin_fill()
    bob.circle(4)
    bob.end_fill()
'it draws everything at the end'
def main():
    bob = turtle.Turtle()
    wn = turtle.Screen()

    wn.colormode(255)
    wn.bgcolor(139, 182, 255)
    bob.speed(0)

    draw_ears(bob)
    right_ear(bob)
    draw_face(bob)
    draw_eyes(bob)
    draw_nose(bob)
    draw_tongue(bob)

    bob.hideturtle()
    wn.exitonclick()

main()

