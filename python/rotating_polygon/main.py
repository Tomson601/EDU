import pygame
import math

pygame.init()
pygame.display.set_caption("Rotating Polygon")

WIDTH=1200
HEIGHT=720

screen=pygame.display.set_mode((WIDTH, HEIGHT))


x_offset=WIDTH/2
y_offset=HEIGHT/2

green=(0, 255, 0)

def draw(x, y):
    pygame.draw.circle(screen, green, (x+x_offset, y+y_offset), 1)
def draw_polygon(x1, y1, x2,y2, x3, y3):
    pygame.draw.polygon(screen, green, [(x1,y1), (x2,y2), (x3,y3)], 1)

while True:

    
    draw_polygon(550, 330, 600, 270, 650, 330)
    pygame.display.update()

    for event in pygame.event.get():                                    # Quit loop
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
