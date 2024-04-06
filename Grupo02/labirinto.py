import turtle

screen = turtle.Screen()
screen.title("Labirinto com Turtle")
screen.setup(600, 600)
screen.setworldcoordinates(0, 0, 600, 600)

class Block(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)

def draw_maze():
    maze = [
        "XXXXXXXXXXXXXXXXXXXXXXX",
        "X   X                 X",
        "X X XXXXXXX  XXXXXXX  XXXXXXXX",
        "X X   X   X X       X        X",      
        "X XXX X X X X XXX X XXXXXX   X",
        "X X   X X X X X   X X    X  X",
        "X X XXX XXX X XXXXX X    X X",
        "X X   X   X X       X",
        "X XXXXXXXXX XXXXXXX X",
        "X                   X",
        "XXXXXXXXXXXXXXXXXXXXX"
    ]

    start_x, start_y = None, None

    for y in range(len(maze)):
        for x in range(len(maze[y])):
            char = maze[y][x]
            screen_x = -280 + (x * 20)
            screen_y = 280 - (y * 20)

            if char == "X":
                block = Block()
                block.goto(screen_x, screen_y)
            elif char == " ":
                if start_x is None:
                    start_x, start_y = screen_x, screen_y
                block = Block()
                block.color("white")
                block.goto(screen_x, screen_y)

    return start_x, start_y

start_x, start_y = draw_maze()

player = turtle.Turtle()
player.shape("turtle")
player.color("red")
player.penup()
player.goto(start_x, start_y)

def go_up():
    x = player.xcor()
    y = player.ycor() + 20
    if (x, y) not in walls:
        player.pendown()
        player.goto(x, y)

def go_down():
    x = player.xcor()
    y = player.ycor() - 20
    if (x, y) not in walls:
        player.pendown()
        player.goto(x, y)

def go_left():
    x = player.xcor() - 20
    y = player.ycor()
    if (x, y) not in walls:
        player.pendown()
        player.goto(x, y)

def go_right():
    x = player.xcor() + 20
    y = player.ycor()
    if (x, y) not in walls:
        player.pendown()
        player.goto(x, y)

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

walls = set()
for block in screen.turtles():
    if block.color()[0] == "black":
        walls.add((round(block.xcor()), round(block.ycor())))

turtle.done()
