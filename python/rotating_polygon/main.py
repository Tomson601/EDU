import pygame
import math

pygame.init()
pygame.display.set_caption("Rotating Polygon")

WIDTH=1200
HEIGHT=720

screen=pygame.display.set_mode((WIDTH, HEIGHT))

x_offset=WIDTH/2
y_offset=HEIGHT/2

black = (0, 0, 0)
green=(0, 255, 0)

def draw(x, y):
    pygame.draw.circle(screen, green, (x+x_offset, y+y_offset), 1)


def draw_polygon(x1, y1, x2,y2, x3, y3):
    pygame.draw.polygon(screen, green, [(x1,y1), (x2,y2), (x3,y3)], 1)

y1=187 #-->447
y2=447 #-->187
y3=187 #-->447

while True:
    #draw_polygon(450, 447, 600, 187, 750, 447)      #DOWN
    #draw_polygon(450, 187, 600, 447, 750, 187)      #UP

    #TODO: draw_polygon(450, 187, 600, 447, 750, 187) --->  draw_polygon(450, 447, 600, 187, 750, 447)
    for i in range(260):
        screen.fill(black)
        pygame.display.update()
        draw_polygon(450, i+y1, 600, y2-i, 750, i+y3)
        i+=1
        pygame.display.update()
        if i == 259:
            for i in range(260):
                screen.fill(black)
                pygame.display.update()
                draw_polygon(450, y2-i, 600, y2+i, 750, y3-i)
                i+=1
                if i == 259:
                    i=0
                    continue
    
    for event in pygame.event.get():                                    # Quit loop
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
