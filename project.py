import pygame

pygame.init()

Cell_size = 30
Rows = 20
Columns = 10
SCREEN_Width = Cell_size * Rows
SCREEN_Length = Cell_size * Columns

screen = pygame.display.set_mode((SCREEN_Length, SCREEN_Width))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()
FPS = 60

Background = (50, 50, 50) #black
grid_color = (0, 0, 0) #grey

def draw_grid():
    for y in range(Rows):
        for x in range(Columns):
            pygame.draw.rect(screen, grid_color, (x * Cell_size, y * Cell_size, Cell_size, Cell_size))
            pygame.draw.rect(screen, Background, (x * Cell_size, y * Cell_size, Cell_size, Cell_size), 1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(Background)
    draw_grid()
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()