################################################
# Author: Lauren Redmon
# Username: redmonl
#
# Assignment: A03: A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: to create an image with turtles
################################################



import turtle
wn = turtle.Screen()                                         # creates the screen
wn.bgcolor('pink')
bud = turtle.Turtle()                                        # creates the first turtle
bud.hideturtle()
petal = turtle.Turtle()                                      # creates the second turtle
petal.hideturtle()

petal.up()
petal.goto(17,25)                                           # puts the second turtle into position

bud.fillcolor('yellow')                                     # creates the center of the flower
bud.begin_fill()
bud.circle(20)
bud.end_fill()
def draw_petal():                                          # the parameters for the petal
    petal.fillcolor('#CC0000')
    petal.begin_fill()
    petal.circle(100,70)
    petal.left(110)
    petal.circle(100,70)
    petal.end_fill()

def main():                                                # draws the flower
    draw_petal()
    petal.goto(8,2)
    draw_petal()
    petal.goto(-20,20)
    draw_petal()
    petal.goto(17,30)
    draw_petal()
    petal.goto(10,4)
    draw_petal()
    petal.goto(-20,18)
    draw_petal()
    petal.goto(0,40)
    draw_petal()
    petal.goto(17,10)
    draw_petal()
    petal.goto(-10,5)
    draw_petal()
    petal.goto(-10,35)
    draw_petal()
    petal.goto(17,12)
    draw_petal()
    petal.goto(0,0)
    draw_petal()
    petal.goto(-17,30)
    draw_petal()

main()


wn.mainloop()

