import time
import turtle

from color_generator import ColorGenerator


class Drawer:
    """
        Classe responsável por desenhar o arco-íris
    """

    def __init__(self, screen_width, screen_height):
        """
            :param screen_width: Largura da tela
            :param screen_height: Altura da tela
        """
        self.screen = turtle.Screen()
        self.screen.setup(screen_width, screen_height)
        self.screen.bgcolor('black')

        self.pen = self.__config_pen()

    def draw_rainbow(self, rainbow_lines_number: int):
        """
            Função que faz o desenho do arco-íris com um número específico de linhas,
            onde cada linha terá uma cor.

            :param rainbow_lines_number: Número de linhas que o arco-íris terá.
        """
        colors = ColorGenerator.generate_random_color_list(rainbow_lines_number)

        for i in range(rainbow_lines_number):
            self.__draw_rainbow_line(color=colors[i], radius=10 * (i + 8), position_x=-10 * (i + 1))

        turtle.update()
        time.sleep(0.2)

    def reconfigure_pen(self):
        """
            Função que permite reconfigurar a caneta.
        """
        self.pen = self.__config_pen()

    def __draw_rainbow_line(self, color, radius, position_x):
        """
            Função responsável por desenhar a linha do arco-íris.

            :param color: Cor da linha
            :param radius: Raio usado para desenhar a linha com uma curvatura
            :param position_x: Posição do eixo X para posicionar a caneta
        """
        self.pen.color(color)
        self.pen.circle(radius, -180)
        self.pen.up()
        self.pen.setpos(x=position_x, y=0)
        self.pen.down()
        self.pen.right(180)

    def __config_pen(self) -> turtle.Turtle:
        """
            Função para configurar a caneta.
        """
        pen = turtle.Turtle()
        pen.right(90)
        pen.width(10)
        pen.speed(0)

        turtle.tracer(0, 0)

        return pen
