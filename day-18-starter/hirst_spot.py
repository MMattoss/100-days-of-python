import colorgram
import turtle as t
import random

# Colorgram things
# extracted_colors = colorgram.extract('hirst spot paiting.jpg', 10)
# colors = []

# for color in extracted_colors:
#     colors.append(color.rgb)
#     print(color.rgb[0])

# Turtle things
t.colormode(255)
pen = t.Turtle()
pen.speed("fastest")

pen.dot(10,(198, 12, 35))
pen.up()
pen.setpos(330, 0)
pen.down()
pen.dot(10,(198, 12, 35))


screen = t.Screen()
screen.screensize(800, 800)
print(screen.screensize())
screen.exitonclick()