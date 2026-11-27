import pygame
import random

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
colors = [(0, 255, 255), (0, 0, 255), (255, 165, 0), (255, 255, 0), (0, 255, 0), (128, 0, 128), (255, 0, 0)]
shapes = [
    [[1,1,1,1]],
    [[1,0,0],[1,1,1]],
    [[0,0,1],[1,1,1]],
    [[1,1],[1,1]],
    [[0,1,1],[1,1,0]],
    [[0,1,0],[1,1,1]],
    [[1,1,0],[0,1,1]]
]

class Tetrimino:
    def __init__(self, x, y, shape, color):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color

    def draw(self):
        for row_idx, row in enumerate(self.shape):
            for col_idx, val in enumerate(row):
                if val:
                    pygame.draw.rect(screen, self.color, ((self.x + col_idx) * Cell_size, (self.y + row_idx) * Cell_size, Cell_size, Cell_size))
                    pygame.draw.rect(screen, Background, ((self.x + col_idx) * Cell_size, (self.y + row_idx) * Cell_size, Cell_size, Cell_size), 1)

def draw_grid():
    for y in range(Rows):
        for x in range(Columns):
            pygame.draw.rect(screen, grid_color, (x * Cell_size, y * Cell_size, Cell_size, Cell_size))
            pygame.draw.rect(screen, Background, (x * Cell_size, y * Cell_size, Cell_size, Cell_size), 1)

running = True
current = Tetrimino(3, 0, random.choice(shapes), random.choice(colors))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(Background)
    draw_grid()
    current.draw()
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()