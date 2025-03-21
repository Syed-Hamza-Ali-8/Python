import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game by Hamza")

clock = pygame.time.Clock()

class Snake:
    def __init__(self):
        self.body = [[100, 50], [80, 50], [60, 50]]
        self.direction = 'RIGHT'
        self.change_to = self.direction

    def change_dir(self, dir):
        # Prevent reverse movement
        if dir == 'UP' and not self.direction == 'DOWN':
            self.direction = 'UP'
        if dir == 'DOWN' and not self.direction == 'UP':
            self.direction = 'DOWN'
        if dir == 'LEFT' and not self.direction == 'RIGHT':
            self.direction = 'LEFT'
        if dir == 'RIGHT' and not self.direction == 'LEFT':
            self.direction = 'RIGHT'

    def move(self):
        head = self.body[0][:]
        if self.direction == 'UP':
            head[1] -= CELL_SIZE
        if self.direction == 'DOWN':
            head[1] += CELL_SIZE
        if self.direction == 'LEFT':
            head[0] -= CELL_SIZE
        if self.direction == 'RIGHT':
            head[0] += CELL_SIZE

        self.body = [head] + self.body[:-1]

    def grow(self):
        tail = self.body[-1][:]
        self.body.append(tail)

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], CELL_SIZE, CELL_SIZE))


class Food:
    def __init__(self):
        self.position = [random.randrange(0, WIDTH, CELL_SIZE),
                         random.randrange(0, HEIGHT, CELL_SIZE)]

    def respawn(self):
        self.position = [random.randrange(0, WIDTH, CELL_SIZE),
                         random.randrange(0, HEIGHT, CELL_SIZE)]

    def draw(self):
        pygame.draw.rect(screen, RED, pygame.Rect(self.position[0], self.position[1], CELL_SIZE, CELL_SIZE))


def game_over():
    font = pygame.font.SysFont('times new roman', 50)
    go_surf = font.render('GAME OVER', True, RED)
    screen.blit(go_surf, [WIDTH // 3, HEIGHT // 3])
    pygame.display.flip()
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()

def main():
    snake = Snake()
    food = Food()
    score = 0

    while True:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Key controls: Using W, A, S, D keys
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    snake.change_dir('UP')
                elif event.key == pygame.K_s:
                    snake.change_dir('DOWN')
                elif event.key == pygame.K_a:
                    snake.change_dir('LEFT')
                elif event.key == pygame.K_d:
                    snake.change_dir('RIGHT')

        snake.move()

        snake_head_rect = pygame.Rect(snake.body[0][0], snake.body[0][1], CELL_SIZE, CELL_SIZE)
        food_rect = pygame.Rect(food.position[0], food.position[1], CELL_SIZE, CELL_SIZE)

        if snake_head_rect.colliderect(food_rect):
            food.respawn()
            snake.grow()
            score += 10
        snake.draw()
        food.draw()

        if (snake.body[0][0] < 0 or snake.body[0][0] >= WIDTH or
                snake.body[0][1] < 0 or snake.body[0][1] >= HEIGHT):
            game_over()

        for block in snake.body[1:]:
            if snake.body[0] == block:
                game_over()

        font = pygame.font.SysFont('times new roman', 20)
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, [10, 10])

        pygame.display.update()
        clock.tick(15)


if __name__ == "__main__":
    main()
