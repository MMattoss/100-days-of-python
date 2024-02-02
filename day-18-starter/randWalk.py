import turtle as t
import random


directions = [0, 90, 180, 270]

t.colormode(255)
pen = t.Turtle()
pen.width(10)
pen.speed("fast")

def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return (red, green, blue)

while True:
    pen.color(random_color())
    pen.setheading(random.choice(directions))
    pen.forward(30)


















screen = t.Screen()
screen.exitonclick()