# Author: Tobore Takpor
# Username: takport
#
# Assignment:  HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: To continue practicing creating and using functions. More practice on using the turtle library. Learn about how computers represent colors. Learn about source control and Git.

# Google Doc Link: https://docs.google.com/document/d/1iM0_w1wRQGrA8l-tM-broe1hVOoxkpgx4ORivJB3Z8Y/edit?usp=sharing
#
#################################################################################


import turtle


def draw_flower():
    """
    Draws a flower with petals using an unnamed RGB color.
    """
    turtle.colormode(255)  # Set the color mode to RGB
    turtle.color(172, 115, 57)  # Custom brownish-orange color for the flower petals
    turtle.begin_fill()
    for _ in range(36):  # Draw 36 petals
        turtle.circle(50, steps=4)
        turtle.left(10)
    turtle.end_fill()


def draw_stem():
    """
    Draws the stem of the flower.
    """
    turtle.color("green")
    turtle.right(90)
    turtle.forward(200)


def draw_leaf():
    """
    Draws a single leaf attached to the stem.
    """
    turtle.penup()
    turtle.left(90)
    turtle.forward(50)
    turtle.right(45)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(30, 180)  # Half-circle for the leaf
    turtle.left(90)
    turtle.circle(30, 180)
    turtle.end_fill()


def draw_tree():
    """
    Draws a simple tree next to the flower.
    """
    turtle.penup()
    turtle.goto(-200, -100)
    turtle.pendown()
    turtle.color("brown")
    turtle.begin_fill()
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(60)
    turtle.end_fill()

    turtle.color("green")
    turtle.penup()
    turtle.goto(-210, -40)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(50)  # Draw the foliage
    turtle.end_fill()

def write_text():
    """
    Writes a custom message below the drawing.
    """
    turtle.penup()
    turtle.goto(-100, -250)
    turtle.pendown()
    turtle.color("blue")
    turtle.write("Nature's Beauty", font=("Arial", 24, "bold"))


def main():
    """
    Main function to orchestrate the drawing of the flower, stem, leaves, and additional details.
    """
    turtle.speed(8)  # Set the turtle's speed
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()

    # Drawing flower and its components
    draw_flower()
    draw_stem()
    draw_leaf()

    # Drawing additional details: tree and flower
    draw_tree()
    draw_flower()

    # Write a custom message
    write_text()

    turtle.hideturtle()  # Hides the turtle after drawing is complete
    turtle.done()


# Run the main function/starts the program
main()
