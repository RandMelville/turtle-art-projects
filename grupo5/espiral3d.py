import turtle
import math
import colorsys

# Configuração inicial da tela e da caneta
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")

pen = turtle.Turtle()
pen.speed(0)
colorNum = 60
color = colorsys.hsv_to_rgb(0.5, 0.5, 0.4)
pen.color(color)
pen.width(2)

# Função para desenhar a espiral
def draw_spiral(num_turns, turn_angle, initial_length, length_increment):
    colorNum = 0 
    width = 2
    length = initial_length
    for _ in range(num_turns):
        colorNum += 10 / num_turns  
        color = colorsys.hsv_to_rgb(colorNum, 1, 1)
        print(color)
        pen.color(color)
        width += 0.05
        pen.width(width)
        pen.forward(length)
        pen.left(turn_angle)
        length += length_increment

# Desenhando a espiral
pen.penup()
pen.goto(0, 0)
pen.pendown()
draw_spiral(335, 15, 1, 0.4)

# Esconder a caneta e finalizar
pen.hideturtle()
screen.mainloop()
