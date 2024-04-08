import turtle
import random

def desenha_gramado(t):
    t.shape("square")
    t.color("green")
    t.shapesize(stretch_wid=20, stretch_len=40)
    t.penup()
    t.goto(0, -200)
    t.stamp()

def desenha_casa(t):
    t.penup()
    t.goto(-100, -50)  
    t.pendown()
    t.color("lightgray") 
    t.begin_fill()
    for i in range(2):
        t.forward(200)
        t.left(90)
        t.forward(150)
        t.left(90)
    t.end_fill()

def desenha_porta(t):
    t.penup()
    t.goto(-30, -50)
    t.pendown()
    t.color("saddlebrown")
    t.begin_fill()
    for _ in range(2):
        t.forward(60)
        t.left(90)
        t.forward(100)
        t.left(90)
    t.end_fill()

    t.penup()
    t.goto(-15, 0)
    t.pendown()
    t.color("gray")
    t.begin_fill()
    t.shape("circle")
    t.shapesize(stretch_wid=0.4, stretch_len=0.4)  
    t.stamp()  
    t.end_fill()

def desenha_janelas(t):
    t.penup()
    posicoes_janelas = [(-85, 0), (45, 0)] 
    for posicao in posicoes_janelas:
        t.goto(posicao)
        t.pendown()
        t.color("black")
        t.begin_fill()
        for _ in range(4):
            t.forward(40)
            t.left(90)
        t.end_fill()
        t.penup()
        
        t.goto(posicao[0] + 5, posicao[1] + 5)
        t.pendown()
        t.color("lightblue")
        t.begin_fill()
        for _ in range(4):
            t.forward(30)
            t.left(90)
        t.end_fill()
        t.penup()

def desenha_telhado(t):
    t.penup()
    t.goto(-100, 100)  
    t.pendown()
    t.color("red")
    t.begin_fill()
    t.goto(0, 250)  
    t.goto(100, 100)  
    t.goto(-100, 100)
    t.end_fill()

def desenha_sol(t):
    t.penup()
    t.goto(150, 150)
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    t.circle(50)
    t.end_fill()

def desenha_raios_sol(t):
    t.penup()
    t.goto(150, 200)
    t.color("yellow")
    t.pensize(2)
    t.pendown()
    for _ in range(12):
        t.forward(100)
        t.backward(100)
        t.left(30)
    t.pensize(1)

def desenha_caminho(t):
    t.penup()
    t.goto(-40, -50)  
    t.pendown()
    t.color("gray")
    t.begin_fill()
    t.forward(80)  
    t.goto(50, -250)  
    t.goto(-50, -250)  
    t.goto(-40, -50)  
    t.end_fill()

def desenha_lago(t):
    t.penup()
    t.goto(200, -100)  
    t.pendown()
    t.color("blue")
    t.begin_fill()
    t.shape("circle")
    t.shapesize(stretch_wid=6, stretch_len=12)  
    t.stamp()  
    t.end_fill()

def desenha_peixe(t):
    t.penup()
    t.goto(220, -120)
    t.pendown()
    t.color("orange")
    t.begin_fill()
    t.shape("circle")
    t.shapesize(stretch_wid=1, stretch_len=2)
    t.stamp()  
    t.end_fill()
    
    t.penup()
    t.goto(240, -120)
    t.setheading(0)
    t.pendown()
    t.begin_fill()
    t.goto(260, -130)
    t.goto(260, -110)
    t.goto(240, -120)
    t.end_fill()

    t.goto(212, -114)
    t.color("black")
    t.begin_fill()
    t.shape("circle")
    t.shapesize(stretch_wid=0.2, stretch_len=0.2)
    t.stamp()
    t.end_fill()

def desenha_passarinhos(t):
    t.color("black")
    for _ in range(5):
        x = random.randint(-200, 200)
        y = random.randint(0, 200)
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.goto(x+10, y+10)
        t.goto(x+20, y)
        t.penup()

def desenha_flores(t):
    for _ in range(10):
        x = random.randint(-300, -100)
        y = random.randint(-180, -50)
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.color("brown")
        t.goto(x, y + 20)

        t.color("pink")

        for _ in range(6):
            t.penup()
            t.goto(x, y + 20)
            t.pendown()
            t.begin_fill()
            t.shape("circle")
            t.shapesize(stretch_wid=0.4, stretch_len=0.4)  
            t.stamp()
            t.end_fill()
            t.right(60)

def desenha_tartaruga(t):
    t.penup()
    t.color("green")
    t.shape("turtle")
    t.shapesize(stretch_len=1, stretch_wid=1)
    t.setheading(90)

    t.goto(-5, -250)
    t.speed(1)

    while t.ycor() < -50:
        for _ in range(5):
            t.forward(2)
            t.left(10)
        
        t.setheading(90)
        t.forward(10)

        for _ in range(5):
            t.right(10)
            t.forward(2)
        
        t.setheading(90)
        
        if -30 <= t.xcor() <= 30 and t.ycor() >= -50:
            break
    
    t.hideturtle()

t = turtle.Turtle()
t.speed("fastest")  
screen = turtle.Screen()
screen.bgcolor("lightblue")

grass = turtle.Turtle()
desenha_sol(t)
desenha_raios_sol(t)
desenha_gramado(grass)
desenha_flores(t)
desenha_casa(t)
desenha_telhado(t)
desenha_porta(t)
desenha_janelas(t)
desenha_caminho(t)
desenha_lago(t)
desenha_peixe(t)
desenha_passarinhos(t)
desenha_tartaruga(t) 

t.hideturtle()
grass.hideturtle()
screen.mainloop()
