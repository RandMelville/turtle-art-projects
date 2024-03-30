import turtle
import colorsys


def desenhar_arco(posicao_x, posicao_y, raio, tamanho_caneta, cor):
    turtle.up()
    turtle.goto(posicao_x + raio, posicao_y)
    turtle.down()
    turtle.seth(90)
    turtle.pensize(tamanho_caneta)
    turtle.pencolor(cor)
    turtle.circle(raio, 180)


turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor('black')
turtle.title('49-Color Rainbow')
turtle.setup(700, 700)
quantidade_cores = 49

raio = 300
tamanho_caneta = 20 * 7 / quantidade_cores
matiz = 0

for i in range(quantidade_cores):
    (r, g, b) = colorsys.hsv_to_rgb(matiz, 1, 1)

    desenhar_arco(posicao_x=0,
                  posicao_y=-100,
                  raio=raio,
                  tamanho_caneta=tamanho_caneta,
                  cor=(r, g, b))

    raio -= (tamanho_caneta - 1)
    matiz += 0.9 / quantidade_cores
