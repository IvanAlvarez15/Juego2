# Juego2 comida mov..py
# Ivan Alvarez y Jesus Daniel
# Juego de la Víbora
from turtle import *
from random import randrange
from freegames import square, vector
import random

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


color=random.choice(['Orange', 'green', 'blue', 'black', 'Yellow'])
color2=random.choice(['Orange', 'green', 'blue', 'black', 'Yellow'])
def chqueocolores(color, color2):
    if color==color2:
        color=random.choice(['Orange', 'green', 'blue', 'black', 'Yellow'])
        color2=random.choice(['Orange', 'green', 'blue', 'black', 'Yellow'])
        chqueocolores(color,color2)
        return(color, color2)
    else:
        return(color, color2)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def inside2(food):
    "Return True if food inside boundaries."
    return -200 < food.x < 190 and -200 < food.y < 190
    

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake: #Choca con sigo mismo
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food: #Cuando se come las cosas
        print('Snake:', len(snake))# Imprime el largo de la serpiente

        des=random.choice(["uno", "dos", "tres", "Cuatro"])
        if des=="uno":
            for i in range(5):
                food.x=food.x+i
        elif des=="dos":
            for i in range(5):
                food.x=food.x-i  
        elif des=="tres":
            for i in range(5):
                food.x=food.y-i  
        elif des=="Cuatro":
            for i in range(5):
                food.x=food.y-i 


        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10

       

    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, color)
    square(food.x, food.y, 9, color2)
    update()
    ontimer(move, 100)

    







setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()