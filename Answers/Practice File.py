# COMMENT BLOCK - ANTONIO KORNRUMPF | KORNRUMPFA
# GOOGLE DOC: https://docs.google.com/document/d/1fC6ElCTtnF5QXUl4j6HjAupjVTARlsWqTyTIoTfCp9c/edit?usp=sharing



import turtle

def make_And_Modify_Turtle(A):
    #for steps in range(4):
     #   turtle.forward(50)
      #  turtle.left(90)
       # turtle.left(90)
        # turtle.fillcolor("blue")
    # Attempted to define: instance creation, movement, and attribute here, but failed.
    # Tried using the .fillcolor() method to fill up the created shaped, but failed.
    turtle.color('blue') #This line makes the pen color, and the outline of the turtle blue.
    turtle.fillcolor("#738678") #This will fill the inside of the turtle object with Xanadu.
    # Block 34 - 40 does not actually fill a shape.
    turtle.begin_fill()
  #  for steps in range(5):
   #   for c in ('blue', 'red', 'green'):
    #        turtle.color(c)
     #       turtle.forward(steps)
      #      turtle.right(30)
#    turtle.end_fill()
# The for loop in combination with line 34, and 46 will draw a square and color it Xanadu
# however, this does not explicitly fill within the boundaries of the square. Though, after
# changing the starting background color, the program doesn't seem to flow correctly.

    for i in range(4):
        turtle.forward(100)
        turtle.left(90)

    turtle.end_fill()

def main():
    wn=turtle.Screen()
    wn.bgcolor("blue")
    #- Attempted to pass hexidecimal input to the method, but failed
    # bad color argument: wn.bgcolor(#738678). Also attempted to pass string input, but
    # this also failed. wn.bgcolor("xanadux"). I also attempted to follow the documentation
    # about this and used wn.bgcolor("#738678"), but this too failed. For some reason,
    # wn.bgcolor("red") also failed!? Assuming there was a cache related error, I restarted the application
    # and my system, only to realize the problem was related to the position of the method.
    # It needed to be IN-FRONT-OF the exitonclick() eventHandler.
    A = turtle.Turtle
    #A.color("red") #This line errored out. Why don't I need to call the object I made in line
    #14?
    turtle.color("red") # This line did what I wanted line 15 to do.
    turtle.shape("arrow")
    make_And_Modify_Turtle(A)
    #turtle.shape("turtle")

    #turtle.fillcolor()
    wn.exitonclick()


main()