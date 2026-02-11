import turtle

ws = turtle.Screen()
ws.bgcolor("white")

turt = turtle.Turtle()

ws.exitonclick()

def pattern (thickness, interval, times):
    for i in range(times):
        turt.forward(interval)
        turt.left((times % 2 * 2 - 1) * 90)
        print((times % 2 * 2 - 1) * 90)
        turt.forward(thickness)
        turt.left((times % 2 * 2 - 1) * 90)
pattern(100,10,5)