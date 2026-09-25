import turtle
import math
import random
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Animated Heart")
heart = turtle.Turtle()
heart.speed(0)
heart.pensize(5)
colors = ["red", "pink", "purple", "orange", "magenta"]
for i in range(50):
    heart.color(random.choice(colors))
    heart.penup()
    heart.goto(0, 0)
    heart.pendown()
    heart.setheading(i * 7)
    for t in range(360):
        angle = math.radians(t)
        x = 16 * math.sin(angle) ** 3
        y = (13 * math.cos(angle)
            - 5 * math.cos(2 * angle)
            - 2 * math.cos(3 * angle)
            - math.cos(4 * angle))
        heart.goto(x * 10, y * 10)
turtle.done()