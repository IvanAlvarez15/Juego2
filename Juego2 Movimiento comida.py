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

colors  = ["green","blue","orange","purple","black"] #Generamos una lista con 5 posibles colores
color_snake = random.choice(colors) #Seleccion aleatoria de un color de la lista mediante random.choice
colors.remove(color_snake) #Quitamos el color seleccionado para la serpiete para evitar que sea el mismo para la comida
color_food = random.choice(colors) #Seleccion aleatoria de un color de la lista mediante random.choice


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

        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)
    clear()


    for body in snake:
        square(body.x, body.y, 9, color_snake)
    square(food.x, food.y, 9, color_food)
    update()
    ontimer(move, 100)


def movefood():
    n=random.choice((1,2,3,4))
    if n==1:
        food.x= food.x+10
    elif n==2:
        food.x= food.x-10
    elif n==3:
        food.y= food.x+10
    elif n==4:
        food.y= food.x-10
    ontimer(movefood,200)






setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
movefood()
done()