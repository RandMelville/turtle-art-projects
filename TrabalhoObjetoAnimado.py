import turtle
import math

#Inicialização do programa
screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor('white')

#Objeto principal
objeto_principal = turtle.Turtle()
objeto_principal.shape('circle')
objeto_principal.color('grey')
objeto_principal.shapesize(6, 6)
objeto_principal.penup()

#Sombra
sombra = turtle.Turtle()
sombra.shape('circle')
sombra.color('black')
sombra.shapesize(5, 5)
sombra.penup()

#Iluminação(sol)
sol = turtle.Turtle()
sol.shape('circle')
sol.color('yellow')
sol.shapesize(3, 3)
sol.penup()

# Ângulos iniciais dos objetos
angulo_sombra = 0
angulo_sol = 180  #Cria o sol do lado oposto da sombra
angulo_objeto = 0

#Função para mover a sombra e o objeto principal
def mover_sombra():
    global angulo_sombra, angulo_objeto
    raio = 50
    x = raio * math.cos(math.radians(angulo_sombra))
    y = raio * math.sin(math.radians(angulo_sombra))
    sombra.setpos(objeto_principal.xcor() + x, objeto_principal.ycor() + y)
    angulo_sombra += 1.2
    angulo_objeto += 0.2  # Ajuste a velocidade do objeto principal aqui
    x = raio * math.cos(math.radians(angulo_objeto))
    y = raio * math.sin(math.radians(angulo_objeto))
    objeto_principal.setpos(x, y)
    screen.ontimer(mover_sombra, 50)

#Função para mover o sol em uma trajetória circular
def mover_sol():
    global angulo_sol
    raio = 200
    x = raio * math.cos(math.radians(angulo_sol))
    y = raio * math.sin(math.radians(angulo_sol))
    sol.setpos(objeto_principal.xcor() + x, objeto_principal.ycor() + y)
    angulo_sol += 1  # Ajuste a velocidade do sol aqui
    screen.ontimer(mover_sol, 50)

#Chamada dos métodos para iniciar a animação
mover_sombra()
mover_sol()

#Encerra o programa quando clicar na tela
screen.mainloop()
