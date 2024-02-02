import turtle as t
import random

def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return (red, green, blue)

t.colormode(255)
pen = t.Turtle()
pen.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        current_heading = pen.heading()
        pen.circle(100)
        pen.color(random_color())
        pen.setheading(current_heading + size_of_gap)

draw_spirograph(10)




























screen = t.Screen()
screen.exitonclick()