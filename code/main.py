import pygame

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Fish Destroyer Simulator")
running = True

surf = pygame.Surface((100,200))
surf.fill('orange')
player_surf = pygame.image.load('../images/diver.png').convert_alpha()
player = pygame.transform.scale_by(player_surf, 0.5)
player_rect = player.get_frect(midbottom = ((WINDOW_WIDTH / 2),WINDOW_HEIGHT - 5))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.fill('cadetblue4')
    display_surface.blit(player, player_rect)
    pygame.display.update()

pygame.quit()