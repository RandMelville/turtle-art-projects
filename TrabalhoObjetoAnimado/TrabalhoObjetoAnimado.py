'''
Obs: 
-adicionado objeto "Lua" (linha 44)
-adicionado texturas para todos os objetos (Objeto Principal, Sol, Lua e Sombra)
-adicionado função "mover_lua" (linha 85)
-adicionado função register_shape nos objetos (Objeto Principal, Sol, Lua)
-adicionado fundo para a tela (linha 16)
'''

import turtle
import math

#Inicialização do programa

screen = turtle.Screen()
screen.bgpic("espaço.png")

#Objeto principal
objeto_principal = turtle.Turtle()
turtle.register_shape("terra.gif")  # Registra a imagem da Terra
objeto_principal.shape("terra.gif")  # Define a textura da Terra
objeto_principal.color("grey")
objeto_principal.shapesize(6, 6)
objeto_principal.penup()

#Sombra
sombra = turtle.Turtle()
#turtle.register_shape('sombra.gif')
#sombra.shape('sombra.gif')
sombra.shape('circle')
sombra.color('black')
sombra.shapesize(0.8, 0.8)
sombra.penup()

#Iluminação(sol)
sol = turtle.Turtle()
turtle.register_shape('sol.gif')  # Registra a imagem do sol
sol.shape('sol.gif')              # Define a textura do sol
sol.color('yellow')
sol.shapesize(3, 3)
sol.penup()

#Lua
lua = turtle.Turtle()
turtle.register_shape('lua.gif')  # Registra a imagem da lua
lua .shape('lua.gif')              # Define a textura da lua
lua .color('white')
lua .shapesize(1, 1)
lua .penup()

# Ângulos iniciais dos objetos
angulo_sombra = 0
angulo_sol = 180  #Cria o sol do lado oposto da sombra
angulo_objeto = 0
angulo_lua = 180

#Função para mover a sombra e o objeto principal
def mover_sombra():
    global angulo_sombra, angulo_objeto
    raio = 30
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
    raio = 300
    x = raio * math.cos(math.radians(angulo_sol))
    y = raio * math.sin(math.radians(angulo_sol))
    sol.setpos(objeto_principal.xcor() + x, objeto_principal.ycor() + y)
    angulo_sol += 1  # Ajuste a velocidade do sol aqui
    screen.ontimer(mover_sol, 50)

    

def mover_lua():
    global angulo_lua
    raio = 120
    x = raio * math.cos(math.radians(angulo_lua))
    y = raio * math.sin(math.radians(angulo_lua))
    lua.setpos(objeto_principal.xcor() + x, objeto_principal.ycor() + y)
    angulo_lua += 1  # Ajuste a velocidade da lua aqui
    screen.ontimer(mover_lua, 50)  

    
#Chamada dos métodos para iniciar a animação
mover_sombra()
mover_sol()
mover_lua()

#Encerra o programa quando clicar na tela
screen.mainloop()


