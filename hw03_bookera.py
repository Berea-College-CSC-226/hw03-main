######################################3
# Author: Andre Booker Jr.
# Username: bookera

import turtle

#b_head = turtle.Turtle()
#b_chest = turtle.Turtle()
#b_legs = turtle.Turtle()
#b_arms = turtle.Turtle
#def b_arms(arms):
    #arms.goto(100,100)

def b_legs(legs):
    legs.goto(85,-85)
    legs.right(45)
    legs.forward(100)
    legs.right(120)
    legs.forward(20)
    legs.right(45)
    legs.forward(90)


def b_arms(arms):
    arms.goto(-85,-85)
    arms.right(120)
    arms.forward(100)
    arms.left(120)
    arms.forward(20)
    arms.left(49)
    arms.forward(80)



def b_chest(chest):
    chest.right(45)
    chest.forward(120)
    for i in range(3):
        chest.right(90)
        chest.forward(120)




def b_head(head):
    head.circle(100)


def main():
    wn = turtle.Screen()
    head = turtle.Turtle()
    chest = turtle.Turtle()
    arms = turtle.Turtle()
    legs = turtle.Turtle()
    b_head(head)
    b_chest(chest)
    b_arms(arms)
    b_legs(legs)



    wn.exitonclick()
main()