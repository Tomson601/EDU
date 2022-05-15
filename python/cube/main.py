import pygame
import math

pygame.init()
pygame.display.set_caption("3D Cube")

WIDTH=1200
HEIGHT=720

screen=pygame.display.set_mode((WIDTH, HEIGHT))

white=(255, 255, 255)
black=(0, 0, 0)
green=(0,255,0)

x_offset=WIDTH/2
y_offset=HEIGHT/2


def draw(x, y):
    pygame.draw.circle(screen, green, (x+x_offset, y+y_offset), 1)

x = -720
rads = 0

while True:
    for rads in range(360):
        pygame.display.update()
        draw(x, 10*math.sin(math.radians(rads)))
        rads+=5
        draw(x, 15*math.sin(math.radians(rads)))
        rads+=10
        draw(x, 20*math.sin(math.radians(rads)))
        x+=0.5
        rads+=15

    #pygame.display.update()
    for event in pygame.event.get():    # Quit loop
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
