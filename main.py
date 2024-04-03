import turtle 

def main():
    first_circle()
    second_circle()
    third_circle()

def first_circle():
    animation = turtle.Turtle()
    # cria um objeto turtle, que é o objeto que será usado para desenhar a animação

    animation.speed(0.5)
    # determina a velocidade do desenho.

    animation.hideturtle() 
    # Esconde o simbolo do objeto Turtle na tela.

    animation.getscreen().bgcolor("black") 
    # Define a cor de fundo da tela como preta.

    animation.color("red") 
    # Define a cor do objeto Turtle como vermelha.
    
    for i in range(300):
        # Faz com que o loop se repita  300 vezes.
        animation.circle(i) 
        # Desenha um círculo com raio igual à variável "i".
        animation._rotate(10)
        # Rotaciona o Turtle para esquerda em 10 graus.

    animation.clear()

def second_circle():
    # Configuração da tela
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.color("white")

    # Função para desenhar círculos concêntricos
    def draw_concentric_circles(num_circles, initial_radius, distance_between_circles):
        radius = initial_radius
        for _ in range(num_circles):
            t.goto(0, -radius)      # Mova para a posição inicial do círculo
            t.pendown()             # Comece a desenhar
            t.circle(radius)        # Desenhe o círculo
            t.penup()               # Pare de desenhar
            radius += distance_between_circles  # Aumente o raio para o próximo círculo

    num_circles = 20 # Altere aqui pra desenhar mais círculos.
    initial_radius = 10
    distance_between_circles = 20
    angle = 1

    for i in range(6):
        t.clear()
        draw_concentric_circles(num_circles, initial_radius, distance_between_circles)
        t.right(angle)
        screen.update()

    t.clear()

def third_circle():
    sc = turtle.Screen()
    sc.bgcolor('black')

    pen = turtle.Turtle()
    pen.width(4)

    def circle(col, rad, val):
        pen.color(col)
        pen.circle(rad)
        pen.up()
        
        pen.setpos(0, val)
        pen.down()

    # Aumente o número do for para aumentar a quantidade de círculos
    for i in range(7):
        circle("white", -20*(i+1), 20*(i+1))


if __name__ == '__main__':
    main()