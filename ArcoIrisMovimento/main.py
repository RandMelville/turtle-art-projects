import turtle

tela = turtle.Screen()

caneta = turtle.Turtle()


def desenha_semi_circulo(cor, raio, valor):
    caneta.color(cor)
    caneta.circle(raio, -180)
    caneta.up()
    caneta.setpos(valor, 0)
    caneta.down()
    caneta.right(180)


cores = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']

tela.setup(600, 600)

tela.bgcolor('black')

caneta.right(90)
caneta.width(10)
caneta.speed(7)

for i in range(7):
    desenha_semi_circulo(cores[i], 10 * (i + 8), -10 * (i + 1))
caneta.hideturtle()
