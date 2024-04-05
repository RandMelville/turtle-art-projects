import turtle

# Configuração inicial da tela e da caneta
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.width(2)

# Função para desenhar a espiral
def draw_spiral(num_turns, turn_angle, initial_length, length_increment):
    length = initial_length
    for _ in range(num_turns):
        pen.forward(length)
        pen.left(turn_angle)
        length += length_increment

# Desenhando a espiral
pen.penup()
pen.goto(-100, 0)
pen.pendown()
draw_spiral(500, 15, 1, 0.1)

# Esconder a caneta e finalizar
pen.hideturtle()
screen.mainloop()
