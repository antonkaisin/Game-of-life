import pygame
from random import randint
from copy import deepcopy

size = (900, 900) 
FPS = 25
width = height = 20
n = size[1] // width  #                       число квадратов

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game of Life")
clock = pygame.time.Clock()

next_status = [[0 for i in range(n)] for i in range(n)] #следущее состояние
current_status = [[randint(0,1) for i in range(n)] for i in range(n)] #текущее состояние


def check_cell(current_status, x, y):       #функция состояния клетки
    count = 0
    for j in range(y - 1, y + 2):               #состояние соседей (количество живых)
        for i in range(x - 1, x + 2):
            if current_status[j % width][i % width] == 1:           # для всего поля current_status[j % width][i % width] == 1
                count +=1

    if current_status[y][x] == 1:        #если клетка жива, то отнимаем единицу из общего количества
        count -= 1
        if count == 2 or count == 3:
            return 1
        return 0
    else:
        if count == 3:
            return 1
        return 0

count = 1
cycle= []

running = True
while running:
    screen.fill(pygame.Color('black'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()    
        
    for i in range(n):
        pygame.draw.line(screen, pygame.Color('white'), (0, (i+1)*width), (size[1], (i+1)*width))
        pygame.draw.line(screen, pygame.Color('white'), ((i+1)*height, 0), ((i+1)*width, size[1]))

    for x in range(n):                                   # для всего поля range(n)
        for y in range(n):                               # для всего поля range(n)
            if current_status[y][x] == 1:
                pygame.draw.rect(screen, pygame.Color('pink'), (x*height+2, y*height+2, height-2, height-2))        #рисуем живые клетки
            next_status[y][x] = check_cell(current_status, x, y)   

    
    current_status = deepcopy(next_status)
    
    if (count%2) == 0:
        if current_status == cycle:
            print("GAME OVER")
            running = False

    if (count%2) == 0:
        cycle = current_status
    count += 1
    
    pygame.display.flip()
    clock.tick(FPS)