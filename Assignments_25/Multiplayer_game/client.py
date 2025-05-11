import pygame
import socket
import pickle
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 40
MOVEMENT_SPEED = 5
FPS = 60

SERVER = "127.0.0.1"
PORT = 5555

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Multiplayer Game")
clock = pygame.time.Clock()

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = SERVER
        self.port = PORT
        self.addr = (self.server, self.port)
        self.player_id = None
        self.all_players = {}
        self.connect()

    def connect(self):
        try:
            self.client.connect(self.addr)
            initial_data = self.receive_data()
            self.player_id = initial_data["id"]
            self.all_players = initial_data["game_state"]
            return True
        except socket.error as e:
            print(f"Connection error: {e}")
            return False

    def send_data(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return self.receive_data()
        except socket.error as e:
            print(f"Error sending data: {e}")
            return None

    def receive_data(self):
        try:
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(f"Error receiving data: {e}")
            return None

    def disconnect(self):
        try:
            self.client.close()
        except:
            pass

class Player:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.rect = pygame.Rect(x, y, size, size)

    def draw(self, screen):
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 2)

    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy

        if 0 <= new_x <= WIDTH - self.size:
            self.x = new_x
        if 0 <= new_y <= HEIGHT - self.size:
            self.y = new_y

def main():
    network = Network()
    if not network.player_id:
        print("Failed to connect to server")
        return

    print(f"Connected to server as Player {network.player_id}")

    my_player = Player(
        network.all_players[network.player_id]["x"],
        network.all_players[network.player_id]["y"],
        PLAYER_SIZE,
        network.all_players[network.player_id]["color"]
    )
    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_LEFT]:
            dx = -MOVEMENT_SPEED
        if keys[pygame.K_RIGHT]:
            dx = MOVEMENT_SPEED
        if keys[pygame.K_UP]:
            dy = -MOVEMENT_SPEED
        if keys[pygame.K_DOWN]:
            dy = MOVEMENT_SPEED

        if dx != 0 or dy != 0:
            my_player.move(dx, dy)

            player_data = {"x": my_player.x, "y": my_player.y}
            game_state = network.send_data(player_data)

            if game_state:
                if isinstance(game_state, dict) and "ping" not in game_state:
                    network.all_players = game_state
            else:
                print("Lost connection to server")
                running = False

        screen.fill(GRAY)

        for x in range(0, WIDTH, 50):
            pygame.draw.line(screen, WHITE, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, 50):
            pygame.draw.line(screen, WHITE, (0, y), (WIDTH, y))

        for pid, p_data in network.all_players.items():
            if pid == network.player_id:
                my_player.draw(screen)
            else:
                other_player = Player(p_data["x"], p_data["y"], PLAYER_SIZE, p_data["color"])
                other_player.draw(screen)

                font = pygame.font.SysFont("arial", 15)
                id_text = font.render(f"P{pid}", True, BLACK)
                screen.blit(id_text, (p_data["x"] + PLAYER_SIZE//2 - 10, p_data["y"] - 20))

        font = pygame.font.SysFont("arial", 20)
        player_count_text = font.render(f"Players: {len(network.all_players)}", True, BLACK)
        screen.blit(player_count_text, (10, 10))

        my_player_text = font.render(f"You: Player {network.player_id}", True, BLACK)
        screen.blit(my_player_text, (10, 40))

        pygame.display.flip()

    network.disconnect()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()