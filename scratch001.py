import turtle

wn = turtle.Screen()
t = turtle.Turtle()


# wn.colormode(255)
# t.pencolor("black")
# # t.color(115, 134, 120)
# # t.fd(100)
# wn.colormode(255)
# t.color(115, 134, 120)   # xanadu
# # t.fillcolor(115, 134, 120)
#
# # draw your shape here
# t.circle(50)
# t.fillcolor(115, 134, 120)
# # t.end_fill()
turtle.colormode(255)

# t.pencolor("black")        # outline color
t.fillcolor(115, 134, 120) # xanadu
t.circle(50)
t.begin_fill()
# t.circle(50)
t.end_fill()


wn.exitonclick()