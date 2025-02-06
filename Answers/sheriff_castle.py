
# CSC 226 Assignment: Fantasy Castle Drawing
# Name: Fatma Sherif
# Username: sheriff
# Google Doc Link: https://docs.google.com/document/d/1y5Ww_WQB-PeRvBXi40IsiTtWS2d_xn8giiXkpMOIwek/edit?tab=t.0
import turtle
turtle.bgcolor((135 / 255, 206 / 255, 235 / 255))

# Main function
def main():
    turtle.speed(0) #for maximum turtle speed
    draw_castle()
    draw_details()


# Function to draw a rectangle
def draw_rectangle(x, y, width, height, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()


def draw_tower(x, y):
    draw_rectangle(x, y, 50, 150, (128/255, 128/255, 128/255))  # Tower base
    draw_rectangle(x + 10, y + 150, 30, 30, (169/255, 169/255, 169/255))  # Tower top
    draw_flag(x + 25, y + 180)


def draw_castle():
    draw_rectangle(-100, -100, 200, 100, (190/255, 190/255, 190/255))
    draw_tower(-125, -100)  # Left tower
    draw_tower(75, -100)  # Right tower
    draw_rectangle(-30, -100, 60, 60, (139/255, 69/255, 19/255))


def draw_flag(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor((255/255, 0, 0))
    turtle.begin_fill()
    turtle.goto(x + 20, y - 10)
    turtle.goto(x, y - 20)
    turtle.goto(x, y)
    turtle.end_fill()


def draw_details():
    draw_tree(-200, -100)
    draw_tree(200, -100)


def draw_tree(x, y):
    draw_rectangle(x, y, 20, 60, (139/255, 69/255, 19/255))  # Trunk using RGB
    turtle.penup()
    turtle.goto(x + 10 , y + 60)
    turtle.pendown()
    turtle.fillcolor((34/255, 139/255, 34/255))  # Green leaves using RGB
    turtle.begin_fill()
    turtle.circle(40)
    turtle.end_fill()

# Call the main function
main()

turtle.exitonclick()
