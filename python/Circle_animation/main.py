import time
import pygame
import math
import random


pygame.init()
pygame.display.set_caption("Circle animation")

WIDTH=1200
HEIGHT=720

screen=pygame.display.set_mode((WIDTH, HEIGHT))

x_offset=WIDTH/2
y_offset=HEIGHT/2

black = (0, 0, 0)
green=(0, 255, 0)

r=(random.randint(0, 255))
g=(random.randint(0, 255))
b=(random.randint(0, 255))

colours = (r, g, b)


def draw_polygon(x1, y1, x2,y2, x3, y3):
    pygame.draw.polygon(screen, green, [(x1,y1), (x2,y2), (x3,y3)], 2)
starting_pos = (450, 446, 600, 186, 750, 446)

prog_control=True
step = 1
while True:
    pygame.draw.circle(screen, colours, (600, 360), step)
    pygame.display.update()

    r = (random.randint(0, 255))
    g = (random.randint(0, 255))
    b = (random.randint(0, 255))
    
    print(r,g,b)
    time.sleep(0.05)
    screen.fill(black)

    step += 1

    if step == 200:
        i = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYUP:
            prog_control = False
