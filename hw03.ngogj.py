#############################################################################
# Author:Jack Ngog ,
# Username: ngogj
# Google Doc: https://docs.google.com/document/d/1zy874rTuubuXPNoopAg9RF0OKdJx9nts4yEyMIRV8Sg/edit?usp=sharing
#Assignment : HW03
#############################################################################
import turtle
import random


def draw_sky(t):
    """Draws the background for the sky using the turtle `t`."""
    t.penup()
    t.goto(-400, 300)  # Start at the top-left corner
    t.pendown()
    t.color("midnightblue")
    t.begin_fill()
    for _ in range(2):
        t.forward(800)  # Width of the sky
        t.right(90)
        t.forward(600)  # Height of the sky
        t.right(90)
    t.end_fill()


def draw_sun(t):
    """Draws the sun in the sky using the turtle `t`."""
    t.penup()
    t.goto(-200, 100)  # Position of the sun
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    t.circle(50)  # Sun's radius
    t.end_fill()



def draw_moon(t):
    """Draws a crescent moon in the sky using the turtle `t`."""
    t.penup()
    t.goto(200, 150)  # Position of the moon
    t.pendown()
    t.color("lightgray")
    t.begin_fill()
    t.circle(50)  # Full moon shape
    t.end_fill()

    # Draw the 'shadow' part of the moon to create a crescent effect
    t.penup()
    t.goto(220, 170)
    t.pendown()
    t.color("midnightblue")
    t.begin_fill()
    t.circle(40)  # Smaller circle to create crescent
    t.end_fill()


def draw_star(t, x, y, size):
    """Draws a single star at the given (x, y) coordinates using turtle `t`."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("white")
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)  # Angle for star
    t.end_fill()


def scatter_stars(t):
    """Scatters multiple stars randomly across the sky using turtle `t`."""
    for _ in range(20):  # Draw 20 stars
        x = random.randint(-380, 380)  # Random x-coordinate
        y = random.randint(0, 280)  # Random y-coordinate
        size = random.randint(10, 20)  # Random star size
        draw_star(t, x, y, size)


def main():
    """Main function to draw the entire scene of the sun, moon, and stars."""
    wn = turtle.Screen()  # Create a window for drawing
    wn.bgcolor("black")  # Black background to simulate night

    t = turtle.Turtle()  # Create a turtle for drawing
    t.speed(6)

    draw_sky(t)  # Draw the background sky
    draw_sun(t)  # Draw the sun
    draw_moon(t)  # Draw the moon
    scatter_stars(t)  # Scatter stars in the sky

    t.hideturtle()  # Hide the turtle after drawing
    wn.exitonclick()  # Wait for user to click to close the window


# Call the main function
if __name__ == "__main__":
    main()
