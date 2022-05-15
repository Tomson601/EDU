import pygame
import math

pygame.init()

WIDTH=360
HEIGHT=360

screen=pygame.display.set_mode((WIDTH, HEIGHT))

white=(255, 255, 255)
black=(0, 0, 0)

x_offset=WIDTH/2
y_offset=HEIGHT/2


def draw(x, y):
    pygame.draw.circle(screen, white, (x+x_offset, y+y_offset), 1)

while True:
    for i in range(1000):
        draw(0, i)
        pygame.display.update()

