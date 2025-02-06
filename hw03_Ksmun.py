

#################################################################################
# Author: Naod Ksmu
# Username: Ksmun
#
# Assignment:CSC 226 - HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose:
 #Google Doc Link:https://docs.google.com/document/d/1wlV5ufYtq_pLxl3pC2goho9RFRjxMk1HN4RcPo24w3w/edit?usp=sharing
#
#################################################################################
# Acknowledgements: I used ChatGPT, an AI by OpenAI, for guidance on structuring my code and debugging.
# All final coding decisions were my own.
#  Citation: OpenAI. (2025). ChatGPT [AI model]. https://openai.com
#
#
#################################################################################
import turtle

def setup_screen():
    screen = turtle.Screen()
    screen.colormode(255)
    screen.bgcolor((115, 134, 120))

def setup_turtle():
    t = turtle.Turtle()
    t.speed(3)
    return t

def draw_house(t):
    """Draws a house with a square base and a triangular roof."""

    # Move turtle to start position.
    t.penup()
    t.goto(-100,-100)
    t.pendown()

    # Draw the square base
    t.fillcolor((165, 42, 42))  # Brown Color
    t.begin_fill()
    for _ in range(4):
        t.forward(200)
        t.left(90)
    t.end_fill()

    t.penup()
    t.goto(-100, 100)
    t.pendown()

    # Draw the roof
    t.fillcolor((129, 0, 12))
    t.begin_fill()
    t.goto(0, 200)  # Top of the roof
    t.goto(100, 100)
    t.goto(-100, 100)
    t.end_fill()

def main():
    setup_screen()
    t = setup_turtle()
    draw_house(t)
    t.hideturtle()
    turtle.exitonclick()

if __name__ == "__main__":
    main()


