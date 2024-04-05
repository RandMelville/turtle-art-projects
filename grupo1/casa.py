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
    t.color("brown")
    t.begin_fill()
    for _ in range(4):
        t.forward(200)
        t.left(90)
    t.end_fill()

def desenha_telhado(t):
    t.penup()
    t.goto(-100, 150)  
    t.pendown()
    t.color("red")
    t.begin_fill()
    t.goto(0, 250)  
    t.goto(100, 150)  
    t.goto(-100, 150)
    t.end_fill()

def desenha_porta(t):
    t.penup()
    t.goto(-40, -50)  
    t.pendown()
    t.color("black")
    t.begin_fill()
    for _ in range(2):
        t.forward(80)
        t.left(90)
        t.forward(150)
        t.left(90)
    t.end_fill()

def desenha_sol(t):
    t.penup()
    t.goto(150, 150)
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    t.circle(50)
    t.end_fill()

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

        original_heading = t.heading()

        for angle in [0, 120, 240]:
            t.penup()
            t.goto(x, y + 20)
            t.pendown()
            t.setheading(angle)
            t.forward(10)
            t.color("pink")

        t.setheading(original_heading)

def desenha_sapo(t):
    t.penup()
    t.color("green")
    t.shape("turtle") 
    t.shapesize(stretch_len=1, stretch_wid=1)  
    t.setheading(90)  

    t.goto(5, -250)
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
    t.setheading(0) 
    t.goto(-40, -50)
    t.hideturtle()  

t = turtle.Turtle()
t.speed(0)  
screen = turtle.Screen()
screen.bgcolor("lightblue")

grass = turtle.Turtle()
desenha_sol(t)

desenha_gramado(grass)
desenha_flores(t)
desenha_casa(t)
desenha_telhado(t)
desenha_porta(t)
desenha_caminho(t)
desenha_lago(t)
desenha_passarinhos(t)
desenha_sapo(t) 

t.hideturtle()
grass.hideturtle()
screen.mainloop()
