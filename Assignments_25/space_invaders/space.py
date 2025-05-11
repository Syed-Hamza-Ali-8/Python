import pygame
import random

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Define colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Player settings
player_width = 50
player_height = 50
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10
player_velocity = 5

# Bullet settings
bullet_width = 5
bullet_height = 10
bullet_velocity = 7
bullet_state = "ready"  # "ready" means the bullet is ready to be fired, "fire" means it is moving

# Alien settings
alien_width = 50
alien_height = 50
alien_velocity = 1
alien_count = 5
alien_x = [random.randint(0, WIDTH - alien_width) for _ in range(alien_count)]
alien_y = [random.randint(50, 150) for _ in range(alien_count)]
alien_direction = [1 for _ in range(alien_count)]  # 1 means moving right, -1 means moving left

# Set up font
font = pygame.font.SysFont("Arial", 24)

# Function to display the player's score
def show_score(score):
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

# Function to draw the player
def draw_player(x, y):
    pygame.draw.rect(screen, GREEN, (x, y, player_width, player_height))

# Function to draw the bullet
def draw_bullet(x, y):
    pygame.draw.rect(screen, WHITE, (x, y, bullet_width, bullet_height))

# Function to draw aliens
def draw_aliens(x, y):
    pygame.draw.rect(screen, RED, (x, y, alien_width, alien_height))

# Main game loop
def game_loop():
    global player_x, player_y, bullet_state, bullet_x, bullet_y, alien_x, alien_y, alien_direction
    running = True
    score = 0

    while running:
        screen.fill(BLACK)

        # Check for events (key presses, quitting, etc.)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get key presses
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_velocity
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
            player_x += player_velocity
        if keys[pygame.K_SPACE] and bullet_state == "ready":
            bullet_x = player_x + player_width // 2 - bullet_width // 2
            bullet_y = player_y
            bullet_state = "fire"

        # Move the bullet
        if bullet_state == "fire":
            bullet_y -= bullet_velocity
            if bullet_y < 0:
                bullet_state = "ready"

        # Move the aliens
        for i in range(alien_count):
            alien_x[i] += alien_velocity * alien_direction[i]
            if alien_x[i] <= 0 or alien_x[i] >= WIDTH - alien_width:
                alien_direction[i] *= -1
                alien_y[i] += alien_height

            # Check for collision with bullet
            if bullet_state == "fire" and alien_x[i] < bullet_x < alien_x[i] + alien_width and alien_y[i] < bullet_y < alien_y[i] + alien_height:
                alien_x[i] = random.randint(0, WIDTH - alien_width)
                alien_y[i] = random.randint(50, 150)
                bullet_state = "ready"
                score += 1

            # Draw alien
            draw_aliens(alien_x[i], alien_y[i])

        # Check for collision with player
        for i in range(alien_count):
            if alien_x[i] < player_x < alien_x[i] + alien_width and alien_y[i] < player_y < alien_y[i] + alien_height:
                running = False

        # Draw player and bullet
        draw_player(player_x, player_y)
        if bullet_state == "fire":
            draw_bullet(bullet_x, bullet_y)

        # Display score
        show_score(score)

        # Update the display
        pygame.display.update()

        # Control the frame rate
        pygame.time.Clock().tick(60)

    pygame.quit()

if __name__ == "__main__":
    game_loop()
