import pygame

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Fish Destroyer Simulator")
running = True

surf = pygame.Surface((100,200))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.fill('cadetblue4')
    display_surface.blit(surf, (100,150))
    pygame.display.update()

pygame.quit()