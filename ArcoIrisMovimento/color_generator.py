import colorsys
import random


class ColorGenerator:
    """
        Classe utilizada para gerar cores para o arco-íris
    """

    @staticmethod
    def generate_random_color_list(color_count: int) -> list[tuple[float, float, float]]:
        """
            Função que gera uma lista de valores RGB ordenados aleatoriamente.

            :param color_count: Quantidade de cores que serão geradas
        """
        colors = []

        for i in range(color_count):
            hue = i / color_count
            rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
            colors.append((rgb[0], rgb[1], rgb[2]))

        random.shuffle(colors)

        return colors
