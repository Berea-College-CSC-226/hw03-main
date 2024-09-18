# Author: Tobore Takpor
# Username: takport
#
# Assignment:  HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: To continue practicing creating and using functions. More practice on using the turtle library. Learn about how computers represent colors. Learn about source control and Git.

# Google Doc Link: https://docs.google.com/document/d/1iM0_w1wRQGrA8l-tM-broe1hVOoxkpgx4ORivJB3Z8Y/edit?usp=sharing
#
#################################################################################


import turtle


def draw_flower(t):
    """
    Draws a flower with petals using an unnamed RGB color.
    """
    t.color(172, 115, 57)  # Custom brownish-orange color for the flower petals
    t.begin_fill()
    for _ in range(36):  # Draw 36 petals
        t.circle(50, steps=4)
        t.left(10)
    t.end_fill()


def draw_stem(t):
    """
    Draws the stem of the flower.
    """
    t.color("green")
    t.right(90)
    t.forward(200)


def draw_leaf(t):
    """
    Draws a single leaf attached to the stem.
    """
    t.penup()
    t.left(90)
    t.forward(50)
    t.right(45)
    t.pendown()
    t.begin_fill()
    t.circle(30, 180)  # Half-circle for the leaf
    t.left(90)
    t.circle(30, 180)
    t.end_fill()


def draw_tree(t):
    """
    Draws a simple tree next to the flower.
    """
    t.penup()
    t.goto(-200, -100)
    t.pendown()
    t.color("brown")
    t.begin_fill()
    t.forward(20)
    t.right(90)
    t.forward(60)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(60)
    t.end_fill()

    t.color("green")
    t.penup()
    t.goto(-210, -40)
    t.pendown()
    t.begin_fill()
    t.circle(50)  # Draw the foliage
    t.end_fill()


def write_text(t):
    """
    Writes a custom message below the drawing.
    """
    t.penup()
    t.goto(-100, -250)
    t.pendown()
    t.color("blue")
    t.write("What a waste of Beauty", font=("Arial", 24, "bold"))


def main():
    """
    Main function to orchestrate the drawing of the flower, stem, leaves, and additional details.
    """
    wn = turtle.Screen()
    wn.colormode(255)  # Set the color mode to RGB (screen-wide)
    wn.bgcolor("yellow")  # Set the background color to yellow

    t = turtle.Turtle()
    t.speed(9)  # Set the turtle's speed
    t.penup()
    t.goto(0, 0)
    t.pendown()

    # Drawing flower and its components
    draw_flower(t)
    draw_stem(t)
    draw_leaf(t)

    # Drawing additional details: tree and second flower
    draw_tree(t)
    t.penup()
    t.goto(200, 0)  # Move to a new location for the second flower
    t.pendown()
    draw_flower(t)


    write_text(t)   # Writing the text

    wn.exitonclick()


# Run the main function/starts the program
main()

