import pygame
import random

pygame.init()

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30

cols = SCREEN_WIDTH // BLOCK_SIZE
rows = SCREEN_HEIGHT // BLOCK_SIZE

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
COLORS = [
    (0, 255, 255), 
    (0, 0, 255),     
    (255, 165, 
    (255, 255, 0),   
    (0, 255, 0),     
    (128, 0, 128),  
    (255, 0, 0)      
]

SHAPES = [
    [
        [[1, 1, 1, 1]],
        [[1],
         [1],
         [1],
         [1]]
    ],
    [
        [[2, 0, 0],
         [2, 2, 2]],
        [[2, 2],
         [2, 0],
         [2, 0]],
        [[2, 2, 2],
         [0, 0, 2]],
        [[0, 2],
         [0, 2],
         [2, 2]]
    ],
    [
        [[0, 0, 3],
         [3, 3, 3]],
        [[3, 0],
         [3, 0],
         [3, 3]],
        [[3, 3, 3],
         [3, 0, 0]],
        [[3, 3],
         [0, 3],
         [0, 3]]
    ],
    [
        [[4, 4],
         [4, 4]]
    ],
    # S shape
    [
        [[0, 5, 5],
         [5, 5, 0]],
        [[5, 0],
         [5, 5],
         [0, 5]]
    ],
    [
        [[0, 6, 0],
         [6, 6, 6]],
        [[6, 0],
         [6, 6],
         [6, 0]],
        [[6, 6, 6],
         [0, 6, 0]],
        [[0, 6],
         [6, 6],
         [0, 6]]
    ],
    [
        [[7, 7, 0],
         [0, 7, 7]],
        [[0, 7],
         [7, 7],
         [7, 0]]
    ]
]

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

def create_grid(locked_positions={}):
    grid = [[0 for _ in range(cols)] for _ in range(rows)]
    for y in range(rows):
        for x in range(cols):
            if (x, y) in locked_positions:
                grid[y][x] = locked_positions[(x, y)]
    return grid

def draw_grid(surface, grid):
    for y in range(rows):
        for x in range(cols):
            pygame.draw.rect(surface, GRAY, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

def draw_window(surface, grid, score=0):
    surface.fill(BLACK)
    for y in range(rows):
        for x in range(cols):
            if grid[y][x]:
                pygame.draw.rect(surface, COLORS[grid[y][x] - 1],
                                 (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
    draw_grid(surface, grid)
    font = pygame.font.SysFont('Arial', 30)
    label = font.render(f'Score: {score}', True, WHITE)
    surface.blit(label, (10, 10))

class Piece:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = SHAPES.index(shape) + 1
        self.rotation = 0

    def image(self):
        return self.shape[self.rotation % len(self.shape)]

def convert_shape_format(piece):
    positions = []
    format = piece.image()
    for i, row in enumerate(format):
        for j, column in enumerate(row):
            if column != 0:
                positions.append((piece.x + j, piece.y + i))
    return positions

def valid_space(piece, grid):
    accepted_positions = [[(x, y) for x in range(cols) if grid[y][x] == 0] for y in range(rows)]
    accepted_positions = [pos for row in accepted_positions for pos in row]
    formatted = convert_shape_format(piece)
    for pos in formatted:
        if pos not in accepted_positions:
            if pos[1] >= 0:
                return False
    return True

def check_lost(locked_positions):
    for pos in locked_positions:
        x, y = pos
        if y < 1:
            return True
    return False

def get_shape():
    return Piece(3, 0, random.choice(SHAPES))

def clear_rows(grid, locked):
    cleared = 0
    for y in range(rows - 1, -1, -1):
        if 0 not in grid[y]:
            cleared += 1
            for x in range(cols):
                try:
                    del locked[(x, y)]
                except:
                    continue
    if cleared > 0:
        # Shift down
        for key in sorted(list(locked), key=lambda k: k[1])[::-1]:
            x, y = key
            if y < rows:
                newKey = (x, y + cleared)
                locked[newKey] = locked.pop(key)
    return cleared

def main():
    locked_positions = {}
    grid = create_grid(locked_positions)
    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock_speed = 0.5
    fall_time = 0
    score = 0

    while run:
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time / 1000 > clock_speed:
            fall_time = 0
            current_piece.y += 1
            if not valid_space(current_piece, grid) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not valid_space(current_piece, grid):
                        current_piece.x += 1
                if event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not valid_space(current_piece, grid):
                        current_piece.x -= 1
                if event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not valid_space(current_piece, grid):
                        current_piece.y -= 1
                if event.key == pygame.K_UP:
                    current_piece.rotation = (current_piece.rotation + 1) % len(current_piece.shape)
                    if not valid_space(current_piece, grid):
                        current_piece.rotation = (current_piece.rotation - 1) % len(current_piece.shape)

        shape_pos = convert_shape_format(current_piece)
        for pos in shape_pos:
            x, y = pos
            if y >= 0:
                grid[y][x] = current_piece.color

        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False
            cleared = clear_rows(grid, locked_positions)
            if cleared > 0:
                score += cleared * 10

        draw_window(screen, grid, score)
        pygame.display.update()

        if check_lost(locked_positions):
            run = False

    pygame.time.delay(2000)

main()
