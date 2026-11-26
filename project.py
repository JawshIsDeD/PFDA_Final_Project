import pygame

pygame.init()

SCREEN_Length = 600
SCREEN_Width = 600
screen = pygame.display.set_mode((SCREEN_Length, SCREEN_Width))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()
FPS = 60

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()