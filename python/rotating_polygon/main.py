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
    pygame.draw.polygon(screen, green, [(x1,y1), (x2,y2), (x3,y3)], 2)
starting_pos = (450, 446, 600, 186, 750, 446)

x1=450
y1=446
x2=600
y2=186
x3=750
y3=446

prog_control=True

while True:
    #draw_polygon(450, 446, 600, 186, 750, 446)      #UP
    #draw_polygon(686, 510, 426, 360, 686, 210)      #LEFT
    if prog_control == True:
        for i in range(174):
            screen.fill(black)
            pygame.display.update()
            x1+=1.35632183908046
            y1+=0.367816091954023
            x2-=1
            y2+=1
            x3-=0.367816091954023
            y3-=1.35632183908046
            draw_polygon(x1, y1 ,x2 ,y2, x3, y3)
            pygame.display.update()
    if prog_control == True:
        for i in range(174):
            screen.fill(black)
            pygame.display.update()
            x1+=1.35632183908046
            y1-=0.367816091954023
            x2+=1
            y2+=1
            x3-=0.367816091954023
            y3+=1.35632183908046
            draw_polygon(x1, y1 ,x2 ,y2, x3, y3)
            pygame.display.update()
    if prog_control == True:
        for i in range(174):
            screen.fill(black)
            pygame.display.update()
            x1-=1.35632183908046
            y1-=0.367816091954023
            x2+=1
            y2-=1
            x3+=0.367816091954023
            y3-=1.35632183908046
            draw_polygon(x1, y1 ,x2 ,y2, x3, y3)
            pygame.display.update()


    x1=450
    y1=446
    x2=600
    y2=186
    x3=750
    y3=446
    # for i in range(260):
    #     screen.fill(black)
    #     pygame.display.update()
    #     draw_polygon(450, i+y1, 600, y2-i, 750, i+y3)
    #     pygame.display.update()
    #     if i == 259:
    #         for i in range(260):
    #             screen.fill(black)
    #             pygame.display.update()
    #             draw_polygon(450, y2-i, 600, y2+i, 750, y3-i)
    #             if i == 259:
    #                 i=0
    #                 continue
    for event in pygame.event.get():                                    # Quit loop
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYUP:
            prog_control = False
