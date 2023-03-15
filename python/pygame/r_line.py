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

    # Fill the background with black
    screen.fill((0, 0, 0))

    x1 = 390
    y1 = 110+250

    x2 = 890
    y2 = 110+250

    # Draw origin rect
    print((x1, y1, x2, y2))
    pygame.draw.line(screen, (255, 0, 0), (x1, y1), (x2, y2))
    pygame.display.flip()
    time.sleep(0.5)

    screen.fill((0, 0, 0))
    pygame.display.flip()
    time.sleep(0.5)
    
    ###################MATHS##################
    angle = math.radians(90)   # 45 degrees
    # Calculate center
    cx = (x1 + x2) / 2
    cy = (y1 + y2) / 2
    # Rotate x1, y2
    u_x1 = ((x1-cx)*math.cos(angle)+(y1-cy)*math.sin(angle))+cx
    u_y1 = (-(x1-cx)*math.sin(angle)+(y1-cy)*math.cos(angle))+cy

    u_x2 = ((x2-cx)*math.cos(angle)+(y2-cy)*math.sin(angle))+cx
    u_y2 = (-(x2-cx)*math.sin(angle)+(y2-cy)*math.cos(angle))+cy
    ##########################################
    # Draw rotated rect by pi/4 rads
    #pygame.draw.line(screen, (255, 0, 0), (u_x1, u_y1), (u_x2, u_y2))
    pygame.display.flip()
    time.sleep(0.5)

    screen.fill((0, 0, 0))
    pygame.display.flip()

    for i in range(180):
        angle = math.radians(i)   # 45 degrees
        # Calculate center
        cx = (x1 + x2) / 2
        cy = (y1 + y2) / 2
        cx = 640
        yx = 360
        # Rotate x1, y2
        u_x1 = ((x1-cx)*math.cos(angle)+(y1-cy)*math.sin(angle))+cx
        u_y1 = (-(x1-cx)*math.sin(angle)+(y1-cy)*math.cos(angle))+cy

        u_x2 = ((x2-cx)*math.cos(angle)+(y2-cy)*math.sin(angle))+cx
        u_y2 = (-(x2-cx)*math.sin(angle)+(y2-cy)*math.cos(angle))+cy

        pygame.draw.line(screen, (255, 0, 0), (u_x1, u_y1), (u_x2, u_y2))
        pygame.display.flip()
        time.sleep(0.005)
    
        screen.fill((0, 0, 0))
        pygame.display.flip()


pygame.quit()
print("soft shutdown")
