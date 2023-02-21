import pygame


def hello_world():
    return "Hello world"

def init(res=[1280, 720]):
    # initialize the pygame module
    x = res[0]
    y = res[1]

    pygame.init()

    pygame.display.set_caption("minimal program")
     
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((x, y))
     
    # define a variable to control the main loop
    running = True

    surf_center = (
        (x-screen.get_width())/2,
        (y-screen.get_height())/2
    )

    image = pygame.image.load("xina.jpeg")
    screen.blit(image, surf_center)
    pygame.display.flip()

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():                                    # Quit loop
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
