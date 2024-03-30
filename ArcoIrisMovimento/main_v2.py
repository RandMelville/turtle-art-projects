import colorsys
import random
import turtle


def desenha_semi_circulo(caneta, cor, raio, valor):
    caneta.color(cor)
    caneta.circle(raio, -180)
    caneta.up()
    caneta.setpos(valor, 0)
    caneta.down()
    caneta.right(180)


def main():
    tela = turtle.Screen()
    tela.setup(600, 600)
    tela.bgcolor('black')

    while True:
        cores = []

        for i in range(360):
            hue = i / 360
            rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
            cores.append((rgb[0], rgb[1], rgb[2]))

        random.shuffle(cores)

        caneta = turtle.Turtle()
        caneta.right(90)
        caneta.width(10)
        caneta.speed(0)
        turtle.tracer(0, 0)

        for i in range(7):
            desenha_semi_circulo(caneta, cores[i], 10 * (i + 8), -10 * (i + 1))

        turtle.update()


if __name__ == "__main__":
    main()
