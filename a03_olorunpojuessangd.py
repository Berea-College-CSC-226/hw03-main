# Author: David Olorunpoju-Essang
# Username: olorunpojuessangd

# Assignment: A03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Draws a fractal tree
#Reference : https://www.youtube.com/watch?v=RWtNQ8RQkO8
#Google doc link: https://docs.google.com/document/d/1AVxiZuugCxoRw1HFxaOiRBXjW_VQFrHNXVA4CwW8-qU/edit?usp=sharing

import turtle

def draw_tree(i): #the parameter i defines when we call the function
    if i<10: #Once a value of 10 is achieved the turtle reverses
        return
    else:
        david.fd(i)
        david.left(30)
        draw_tree(3*i/4) #The equation determines the extensiveness and length of the branch patterns
        david.right(60)
        draw_tree(3*i/4)
        david.left(30)
        david.backward(i)

def main():
    wn = turtle.Screen()
    turtle.bgcolor("skyblue")
    wn.title("Here is a tree")
    global david
    david = turtle.Turtle()
    david.color("blue")
    david.shape("turtle")
    david.pensize(7)
    david.pencolor("green")
    david.penup()
    david.setpos(0,-200) #lowers the turtle's placment in the screen
    david.left(90)
    david.speed(0)
    david.pendown()
    draw_tree(100)
    draw_tree()
    turtle.done() #Keeps the window open until the turtle has completed executing the function


main()
