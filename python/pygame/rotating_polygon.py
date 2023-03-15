import pygame
import time
import math


pygame.init()
screen_size = [1280, 720]
mid_x = screen_size[0]/2
mid_y = screen_size[1]/2
screen = pygame.display.set_mode((screen_size[0], screen_size[1]))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    ######CORDS######
    x1 = 390
    y1 = 110

    x2 = 890
    y2 = 110

    x3 = 890
    y3 = 610

    x4 = 390
    y4 = 610
    ################
    for i in range(360):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if running == False:
            break
        ###################MATHS##################
        angle = math.radians(i)
        cx = 640
        cy = 360
        # Rotate x1, y2
        u_x1 = ((x1-cx)*math.cos(angle)+(y1-cy)*math.sin(angle))+cx
        u_y1 = (-(x1-cx)*math.sin(angle)+(y1-cy)*math.cos(angle))+cy

        u_x2 = ((x2-cx)*math.cos(angle)+(y2-cy)*math.sin(angle))+cx
        u_y2 = (-(x2-cx)*math.sin(angle)+(y2-cy)*math.cos(angle))+cy

        u_x3 = ((x3-cx)*math.cos(angle)+(y3-cy)*math.sin(angle))+cx
        u_y3 = (-(x3-cx)*math.sin(angle)+(y3-cy)*math.cos(angle))+cy

        u_x4 = ((x4-cx)*math.cos(angle)+(y4-cy)*math.sin(angle))+cx
        u_y4 = (-(x4-cx)*math.sin(angle)+(y4-cy)*math.cos(angle))+cy
        ##########################################
        pygame.draw.polygon(screen, (255, 255, 0), [(u_x1, u_y1), (u_x2, u_y2), (u_x3, u_y3), (u_x4, u_y4)])
        pygame.display.flip()
        time.sleep(0.02)
    
        screen.fill((0, 0, 0))
        pygame.display.flip()

pygame.quit()
print("soft shutdown")
