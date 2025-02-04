#this is where i am coding
import turtle
kh1 = turtle.Turtle
wn = turtle.Screen()
wn.bgcolor('lightblue')

kh1.penup()
kh1.setposition(200,100)
kh1.pendown()
kh1.color('yellow')
kh1.pensize(100)
kh1.circle(5)

def person():
    """
    Example docstring for function_1. function_1 is not a good function name and should be changed.
    """
    pass

    # ....


def ground():
    """
    Example docstring for function_2. function_2 is not a good function name and should be changed.
    """
    pass
    # ...


def main():
    """
    Docstring for main. Should describe the main functionality of this file.
    """

    # Function calls to function_1 and function_2.
    #function_1()
   # function_2()

#main()  #
wn.exitonclick()