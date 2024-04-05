import turtle
import random
from PIL import Image

image_path = "Terra.jpg"
image = Image.open(image_path)
image.save("terra.gif")

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Planeta Terra com Estrelas")

t = turtle.Turtle()
t.speed(0)  

screen.addshape("terra.gif")  
t.shape("terra.gif")

t.penup()
t.goto(0, 0)
t.pendown()

def draw_star(size):
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)

screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.bgcolor("black")
turtle.speed(0)  
turtle.hideturtle()  
turtle.penup()  

num_stars = 60
for _ in range(num_stars):
    x = random.randint(-screen.window_width() // 2, screen.window_width() // 2)
    y = random.randint(-screen.window_height() // 2, screen.window_height() // 2)
    size = random.randint(5, 20)
    turtle.goto(x, y)
    turtle.color("white")
    turtle.begin_fill()
    draw_star(size)
    turtle.end_fill()

t.penup()
t.color("white")

turtle.mainloop()