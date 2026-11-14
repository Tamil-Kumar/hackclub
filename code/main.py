import pygame

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Fish Destroyer Simulator")
clock = pygame.time.Clock()
running = True

surf = pygame.Surface((100,200))
surf.fill('orange')
player_surf = pygame.image.load('../images/diver.png').convert_alpha()
player = pygame.transform.scale_by(player_surf, 0.5)
player_rect = player.get_frect(midbottom = ((WINDOW_WIDTH / 2),WINDOW_HEIGHT - 5))

while running:
    dt = clock.tick(60) / 1000
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if keys[pygame.K_LEFT]:
        player_rect.centerx -= 300 * dt
    if keys[pygame.K_RIGHT]:
        player_rect.centerx += 300 * dt

    display_surface.fill('cadetblue4')
    display_surface.blit(player, player_rect)
    pygame.display.update()

pygame.quit()