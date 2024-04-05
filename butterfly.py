import turtle  # Importa a biblioteca turtle para gráficos
import random  # Importa a biblioteca random para geração de números aleatórios

# Configuração da tela
screen = turtle.Screen()  # Cria uma tela de turtle
screen.setup(width=800, height=600)  # Configura o tamanho da tela
screen.bgcolor("lightblue")  # Define a cor de fundo da tela como azul claro

# Registrar a imagem de borboleta
screen.addshape("butterfly.gif")  # Registra uma imagem de borboleta chamada "butterfly.gif"

# Lista de cores para as borboletas
cores = ["red", "orange", "yellow", "green", "blue", "purple"]  # Lista de cores para as borboletas

# Função para criar uma borboleta
def criar_borboleta():
    borboleta = turtle.Turtle()  # Cria uma tartaruga para representar uma borboleta
    borboleta.shape("butterfly.gif")  # Define a forma da tartaruga como a imagem de borboleta
    borboleta.color(random.choice(cores))  # Escolhe uma cor aleatória para a borboleta
    borboleta.speed(0)  # Define a velocidade da tartaruga como a mais rápida possível
    borboleta.penup()  # Levanta a caneta para que a tartaruga não desenhe ao se mover
    borboleta.setpos(random.randint(-400, 400), random.randint(-250, 250))  # Define a posição inicial da tartaruga de forma aleatória
    borboleta.setheading(random.randint(0, 360))  # Define a direção inicial da tartaruga de forma aleatória
    return borboleta  # Retorna a tartaruga criada representando a borboleta

# Lista de borboletas
borboletas = []  # Cria uma lista para armazenar as tartarugas que representam as borboletas

# Criar várias borboletas
for _ in range(10):  # Loop para criar 10 borboletas
    borboleta = criar_borboleta()  # Chama a função criar_borboleta para criar uma borboleta
    borboletas.append(borboleta)  # Adiciona a borboleta à lista de borboletas

# Loop principal
while True:  # Loop principal para movimentar as borboletas continuamente
    for borboleta in borboletas:  # Loop para percorrer todas as borboletas na lista
        borboleta.forward(random.randint(1, 5))  # Move a borboleta para frente com uma distância aleatória entre 1 e 5
        if borboleta.xcor() > 400 or borboleta.xcor() < -400 or borboleta.ycor() > 250 or borboleta.ycor() < -250:
            # Verifica se a borboleta saiu dos limites da tela
            borboleta.setpos(random.randint(-400, 400), random.randint(-250, 250))  # Reposiciona a borboleta de forma aleatória
            borboleta.setheading(random.randint(0, 360))  # Define uma nova direção aleatória para a borboleta
