from turtle import Turtle, Screen
pen = Turtle()
pen.shape("turtle")

colors = ["AliceBlue", "bisque", "BlueViolet", "firebrick", "gold", "khaki", "lavender", "light coral", "magenta", "olive drab"]
angles = [120, 90, 72, 60, 51.42, 45, 40, 36]
turns = 10

for x in range(len(angles)):

    for y in range(turns):
        pen.right(angles[x])
        pen.forward(100)
    
    turns += 1
    pen.color(colors[x])










screen = Screen()
screen.exitonclick()
