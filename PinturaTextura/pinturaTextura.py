import turtle
import random
from PIL import Image

image_path = "PinturaTextura/Terra.jpg"
image = Image.open(image_path)
image.save("terra.gif")

background_image_path = "PinturaTextura/estrela.png"
background_image = Image.open(background_image_path)
background_image.save("space.gif")

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Planeta Terra com Estrelas")

t = turtle.Turtle()
t.speed(0)

screen.addshape("terra.gif")
screen.addshape("space.gif")
t.shape("terra.gif")

t.penup()
t.goto(0, 0)
t.pendown()

def draw_star(size):
    turtle.shape('space.gif')
    turtle.stamp()

turtle.penup()
turtle.color("white")
turtle.hideturtle()

num_stars = 15
for _ in range(num_stars):
    x = random.randint(-screen.window_width() // 2, screen.window_width() // 2)
    y = random.randint(-screen.window_height() // 2, screen.window_height() // 2)
    size = random.randint(5, 20)
    turtle.goto(x, y)
    turtle.begin_fill()
    draw_star(size)
    turtle.end_fill()

t.penup()
t.color("white")

turtle.mainloop()
