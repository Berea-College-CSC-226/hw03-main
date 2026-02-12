
#################################################################################
# Author: Habiba Sorour
# Username: sorourh
#
# Assignment: HW03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: Create a complex shape
# Google Doc Link: https://docs.google.com/document/d/1rKRNlQN_RK_3qqvULgTdhE_hf_TmtNGvKxBf7tWHUts/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
# https://tr.pinterest.com/pin/96545985755450566/
#
#################################################################################


import turtle

def make_turtle():
    """
    Create all turtles.
    """
    turtle_name = turtle.Turtle()
    turtle_name.pensize(2)
    turtle_name.hideturtle()
    return turtle_name

def move_to(turtle_name, x, y, direction):
    """
    Change the directions of the turtles.
    """
    turtle_name.penup()
    turtle_name.goto(x, y)
    turtle_name.speed(0)
    turtle_name.seth(direction)
    turtle_name.pendown()

def rectangle(t , length,  width):
    """
    Creates a rectangle with the given length and width.
    """
    for i in range(2):
        t.forward(length)
        t.right(90)
        t.forward(width)
        t.right(90)

def guitar_body(radius):
    """
    building the body of the guitar using an ellipse and a circle.
    """
    upper_body = make_turtle()
    upper_body.color((196, 164, 132))
    move_to(upper_body, -radius//2 - radius//4 , -radius*2, -45)
    upper_body.speed(0)
    upper_body.begin_fill()
    for i in range(2):
        # two arcs
        upper_body.circle(radius, 90)
        upper_body.circle(radius // 2, 90)
    upper_body.end_fill()

    move_to(upper_body, - radius//15 , -radius*1.3, 0)
    upper_body.begin_fill()
    upper_body.circle(radius//2)
    upper_body.end_fill()
    return  upper_body.xcor(), upper_body.ycor()

def guitar_neck(current_position, radius):
    """
    building the guitar neck
    """
    neck_body = make_turtle()
    neck_body.color("black")
    neck_body.begin_fill()
    move_to(neck_body, int(current_position[0])- radius//8 ,int(current_position[1])+ radius//2 + radius//3 ,89)
    rectangle(neck_body,radius*2,radius//5 )
    neck_body.end_fill()
    return neck_body.xcor(), neck_body.ycor()

def guitar_details(current_position, radius):
    """
    building the guitar details
    """
    body_details = make_turtle()
    body_details.color("black")
    body_details.begin_fill()

    move_to(body_details, current_position[0] ,current_position[1]- radius//6  ,90)
    rectangle(body_details,radius//10 ,radius// 5)
    body_details.end_fill()

    body_details.begin_fill()
    move_to(body_details, body_details.xcor() ,body_details.ycor()- radius//6  ,90)
    rectangle(body_details, radius//10 ,radius//5)
    body_details.end_fill()

    body_details.begin_fill()
    move_to(body_details, body_details.xcor() ,body_details.ycor()- radius //3 ,90)
    rectangle(body_details, radius // 6 ,radius//5)
    body_details.end_fill()

    body_details.begin_fill()
    move_to(body_details, body_details.xcor() ,body_details.ycor()- 100 ,90)
    rectangle(body_details, radius //3 ,radius//5)
    body_details.end_fill()

def music_notes(radius):
    """
    building the music notes
    """
    notes = make_turtle()
    notes.color("black")
    notes.begin_fill()
    notes.pendown()
    move_to(notes , radius, radius, 90)
    notes.begin_fill()
    notes.circle(5)
    notes.end_fill()
    notes.forward(30)
    notes.right(90)
    notes.forward(30)
    notes.right(90)
    notes.forward(30)
    notes.begin_fill()
    notes.circle(5)
    notes.end_fill()

def display_song(input_song, radius):
    song = make_turtle()
    song.color("black")
    move_to(song , -radius*1.7 , radius*1.7, 0)
    song.write(input_song,False,"Left", font = ("Papyrus", 30, "normal"))

def main():
    """
    Creating a guitar graphic with music note and your favourite song displayed on the screen.
    """
    wn = turtle.Screen()
    wn.colormode(255)
    wn.bgcolor(69, 132, 195)
    fav_song = wn.textinput("Song Recommendation", "Enter your favourite song")

    radius = 150
    current_position = guitar_body(radius)
    current_position = guitar_neck(current_position, radius)
    guitar_details(current_position, radius)
    music_notes(radius-50)
    music_notes(radius)
    music_notes(radius+50)
    music_notes(radius+100)
    display_song(fav_song, radius)



    wn.exitonclick()

main()  # Starts the program!