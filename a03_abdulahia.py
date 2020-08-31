# Author : Ahmed Abdulahi
# username: Abdulahia

#  assigment: A03
# google doc link : https://docs.google.com/document/d/1u5OhWOtjtqerYXssSf1M2EpTn7kqaPuRVyn4C5St9HA/edit#

import turtle
ahmed = turtle.Turtle()
ahmed.shape("turtle")
ahmed.color("yellow")
ahmed.speed(7)
ahmed.pensize(5)


def house(house, color):
    """
    creating a house
    :return:
    """
    # creating the house turtle
    house.fillcolor("purple")
    house.begin_fill()
    ahmed.penup()
    ahmed.goto(-210, -150)
    ahmed.pendown()
    for i in range(2):
        house.forward(450)
        house.left(90)
        house.forward(225)
        house.left(90)
    house.end_fill()
# creating the door


def door(door, color):
    ahmed.pendown()
    ahmed.goto(0, -150)
    door.fillcolor("blue")
    door.begin_fill()
    for i in range(2):
        door.forward(50)
        door.left(90)
        door.forward(100)
        door.left(90)
    door.end_fill()
# creating the windows


def window1(window1, color):
    ahmed.penup()
    ahmed.goto(-150, 0)
    ahmed.pendown()
    window1.fillcolor("pink")
    window1.begin_fill()

    for i in range(2):
        window1.forward(50)
        window1.left(90)
        window1.forward(30)
        window1.left(90)
    window1.end_fill()


def window2(window2, color):
    ahmed.penup()
    ahmed.goto(130, 0)
    ahmed.pendown()
    window2.fillcolor("pink")
    window2.begin_fill()

    for i in range(2):
        window2.forward(50)
        window2.left(90)
        window2.forward(30)
        window2.left(90)
    window2.end_fill()

# creating the roof


def roof(roof, color):
    ahmed.penup()
    ahmed.goto(-210, 75)
    ahmed.pendown()
    roof.fillcolor("red")
    roof.begin_fill()
    roof.left(40)
    roof.forward(300)
    roof.right(81)
    roof.forward(290)
    roof.end_fill()
# creating the sun


def sun(sun, color):
    ahmed.penup()
    ahmed.goto(150, 200)
    ahmed.pendown()
    sun.fillcolor("yellow")
    sun.begin_fill()
    sun.circle(180)
    sun.end_fill()


def main():
    wn = turtle.Screen()
    wn.bgcolor("light blue")
    wn.title("house and sun")


    # calls to functions
    house(ahmed, "yellow")
    door(ahmed, "blue")
    window1(ahmed, "yellow")
    window2(ahmed, "yellow")
    roof(ahmed, "red")
    sun(ahmed, "yellow")
    wn.exitonclick()


main()