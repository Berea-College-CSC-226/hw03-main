# Author: Darius Morton
# Username: mortond
# Google doc link: https://docs.google.com/document/d/1LCaK7xrjIaCi4lZffVT7LUmrYVyYUXjz15eXhzyeMmI/edit?usp=sharing

# Assignment: A03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: To learn about how computers use colors using rgb values and using source and git.


import turtle



def main_house(house):
    '''Draws the house
    Paramater name:None
    Return Value(None)'''
    turtle.colormode(255)
    house.pencolor(2, 22, 200)
    for i in range(4):
        house.pensize(14)
        house.forward(240)
        house.left(90)


def windows(win):
    '''Draws the windows to the house
    Parameter name(win)
    Return value:none'''
    turtle.colormode(255)
    win.pencolor(2, 4, 222)
    win.goto(0, 120)
    for i in range(4):
        win.forward(120)
        win.left(90)
    win.forward(60)
    win.circle(0, 90)
    win.forward(120)
    win.circle(0, 90)
    win.forward(60)
    win.circle(0, 90)
    win.forward(90)
    win.forward(1)
    win.left(90)
    win.forward(120)
    win.speed()


def makedoor(door):
    '''This draws the door to the house
    Parameter name(door)
    Return value: none'''
    turtle.colormode(255)
    door.pencolor(2, 4, 222)
    door.goto(120, 0)
    for i in range(4):
        door.forward(60)
        door.left(90)
    door.penup()
    door.goto(120, 26)
    door.pendown()
    door.left(-40)
    door.circle(7)


def main():
    '''Executes functions and calls the names to the definitons'''
    wn = turtle.Screen()
    wn.title("hello")
    wn.bgcolor("green")
    house = turtle.Turtle()
    win = turtle.Turtle()
    door = turtle.Turtle()
    main_house(house)    #funtion call to main_house
    makedoor(door)  # function call to makedoor
    windows(win)  # function call to windows
    wn.exitonclick()


main()
#Credit to Concepta and Darian