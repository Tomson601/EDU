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

r=0
g=0
b=0

colours = (r, g, b)


def draw_polygon(x1, y1, x2,y2, x3, y3):
    pygame.draw.polygon(screen, green, [(x1,y1), (x2,y2), (x3,y3)], 2)
starting_pos = (450, 446, 600, 186, 750, 446)

prog_control=True
step = 0
while True:
    pygame.draw.circle(screen, colours, (600, 360), step)
    pygame.display.update()

    r = (random.randint(0, 255))
    g = (random.randint(0, 255))
    b = (random.randint(0, 255))
    colours = (r, g, b)

    screen.fill(black)
    print(step)
    step += 0.5

    if step == 200:
        for minus_step in range(1000):
            r = (random.randint(0, 255))
            g = (random.randint(0, 255))
            b = (random.randint(0, 255))
            colours = (r, g, b)
            pygame.draw.circle(screen, colours, (600, 360), step)
            pygame.display.update()
            screen.fill(black)
            pygame.display.update()
            step -= 0.5

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYUP:
            prog_control = False
