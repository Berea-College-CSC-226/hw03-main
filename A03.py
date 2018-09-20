#################################################
# Anderson Stettner A03
#################################################
import turtle


def Draw_Home(home):
    """
    Draw the House
    """


    for i in range (4):
        home.forward(300)
        home.right(90)


def Draw_Roof(roof):
    """
    Draw the door for the roof
    """
    for i in range (1):
        roof.left(45)
        roof.forward(213)
        roof.right(90)
        roof.forward(213)


def Draw_Window(window,window2):
    """
    Draw the windows
    """


    for i in range(4):
        window.forward(50)
        window.left(90)

    for i in range (4):
        window2.forward(50)
        window2.left(90)


def Draw_Door(door):
    """
    Draw the door for the house
    """
    for i in range (2):
        door.forward(100)
        door.right(90)
        door.forward(50)
        door.right(90)


def main():
    """
    Draw all of the house functions
    """
    wn = turtle.Screen()                # set up the screen and the background
    wn.bgcolor("green")

    home = turtle.Turtle()                                      # create all the turtles i need
    roof = turtle.Turtle()
    window = turtle.Turtle()
    window2 = turtle.Turtle()
    door = turtle.Turtle()



    window.penup()                                                 # gets window to where I want it to start
    window.forward(50)
    window.right(90)
    window.forward(50)
    window.pendown()

    window2.penup()                                                # gets window2 to where I want it to start
    window2.forward(200)
    window2.right(90)
    window2.forward(200)
    window2.pendown()

    door.penup()                                                    # gets the door to where I want it to start
    door.forward(150)
    door.right(90)
    door.forward(200)
    door.pendown()

    Draw_Door(door)
    Draw_Home(home)
    Draw_Roof(roof)
    Draw_Window(window,window2)

    wn.exitonclick()


main()


