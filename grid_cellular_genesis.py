import pygame
import random

# --- Constants ---
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
CELL_SIZE = 20
FPS = 10
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Calculate Grid Dimensions
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# --- Game Logic ---
def initialize_grid(blank=False):
    if blank:
       return [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    else:
        grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        #add random cells at start
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                if random.random() < 0.2:
                    grid[y][x] = 1
        return grid

def count_neighbors(grid, x, y):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            neighbor_x = x + j
            neighbor_y = y + i
            if 0 <= neighbor_x < GRID_WIDTH and 0 <= neighbor_y < GRID_HEIGHT:
                count += grid[neighbor_y][neighbor_x]
    return count

def update_grid(grid):
    new_grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            neighbors = count_neighbors(grid, x, y)
            if grid[y][x] == 1: # Cell is alive
                if neighbors < 2 or neighbors > 3:
                    new_grid[y][x] = 0 # Loneliness or Overcrowding
                else:
                    new_grid[y][x] = 1 # Survival
            else:  # Cell is dead
                if neighbors == 3:
                    new_grid[y][x] = 1  # Reproduction
    return new_grid

# --- Pygame Setup ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cellular Genesis")
clock = pygame.time.Clock()

# --- Game Variables ---
grid = initialize_grid(blank=True)
running = True
paused = True  # Start paused

# --- Game Loop ---
while running:
    # --- Event Handling ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
               paused = not paused  # Toggle pause/play
            if event.key == pygame.K_r:
                grid = initialize_grid(blank=True) # Reset Grid
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            grid_x = mouse_x // GRID_SIZE
            grid_y = mouse_y // GRID_SIZE
            if 0 <= grid_x < GRID_WIDTH and 0 <= grid_y < GRID_HEIGHT:
                grid[grid_y][grid_x] = 1 if grid[grid_y][grid_x] == 0 else 0 # Toggle cell on click

    # --- Game Logic ---
    if not paused:
      grid = update_grid(grid)

    # --- Drawing ---
    screen.fill(BLACK)
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if grid[y][x] == 1:
                rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, BLUE, rect)
            else: # Draw the grid
                rect = pygame.Rect(x*GRID_SIZE, y*GRID_SIZE,CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, WHITE, rect, 1)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
