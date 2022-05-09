import pygame
import math

pygame.init()

WIDTH=1280
HEIGHT=720

screen=pygame.display.set_mode((WIDTH, HEIGHT))

white=(255, 255, 255)
black=(0, 0, 0)

x_offset=WIDTH/2
y_offset=HEIGHT/2


def draw(x, y):
    pygame.draw.circle(screen, white, (x+x_offset, y+y_offset), 1)
