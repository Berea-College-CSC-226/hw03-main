#############################################################################
# Author:Jack Ngog ,
# Username: ngogj
# Google Doc: https://docs.google.com/document/d/1zy874rTuubuXPNoopAg9RF0OKdJx9nts4yEyMIRV8Sg/edit?usp=sharing
#Assignment : HW03
#############################################################################
import turtle
import random

def draw_sky():
    """Draws the night sky background."""
    turtle.penup()
    turtle.goto(-400, -300)  # Bottom-left corner
    turtle.pendown()
    turtle.color("midnightblue")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(800)  # Width of the sky
        turtle.left(90)
        turtle.forward(600)  # Height of the sky
        turtle.left(90)
    turtle.end_fill()

def draw_sun():
    """Draws the sun at the top-left corner of the screen."""
    turtle.penup()
    turtle.goto(-250, 150)  # Position of the sun
    turtle.pendown()
    turtle.color("yellow")
    turtle.begin_fill()
    turtle.circle(50)  # Radius of the sun
    turtle.end_fill()



def draw_moon():
    """Draws a crescent moon at the top-right of the screen."""
    # Draw the full moon first (in white)
    turtle.penup()
    turtle.goto(200, 100)
    turtle.pendown()
    turtle.color("white")
    turtle.begin_fill()
    turtle.circle(50)  # Full moon
    turtle.end_fill()

    # Overlay part of the moon to create a crescent shape
    turtle.penup()
    turtle.goto(230, 120)  # Move to the right slightly for the overlay
    turtle.pendown()
    turtle.color("midnightblue")
    turtle.begin_fill()
    turtle.circle(50)  # Overlay to create crescent shape
    turtle.end_fill()

def draw_star(x, y, size):
    """Draws a single star at the given coordinates with the given size."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("white")

    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)  # Star points angle
    turtle.end_fill()

def draw_random_stars(num_stars):
    """Draws a given number of stars randomly scattered across the sky."""
    for _ in range(num_stars):
        x = random.randint(-350, 350)
        y = random.randint(0, 250)  # Stars appear in the upper half of the screen
        size = random.randint(10, 20)
        draw_star(x, y, size)
# Used to chatgpt to help me find out how to spread out the stars at random
def main():
    """Main function to show the drawing of the sun, moon, stars, and background."""
    turtle.speed(3)
    turtle.hideturtle()

    draw_sky()           # Draw the night sky background
    draw_sun()           # Draw the sun
    draw_moon()          # Draw the crescent moon
    draw_random_stars(15)  # Draw 15 randomly scattered stars

    turtle.done()

# Call the main function
if __name__ == "__main__":
    main()
# Ran into a problem in my code with calling the code back with main