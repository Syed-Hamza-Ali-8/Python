import socket
import pygame
import threading

server = "127.0.0.1"
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((server, port))
s.listen(2)

print("Server started, waiting for players...")

players = [[50, 50], [400, 400]]  # Initial positions for 2 players
connections = []

def handle_client(conn, player_id):
    conn.send(str.encode(f"{players[player_id][0]},{players[player_id][1]}"))
    while True:
        try:
            data = conn.recv(2048).decode()
            if not data:
                break
            x, y = map(int, data.split(","))
            players[player_id] = [x, y]
            other_player = 1 - player_id
            reply = f"{players[other_player][0]},{players[other_player][1]}"
            conn.sendall(str.encode(reply))
        except:
            break
    print(f"Player {player_id + 1} disconnected.")
    conn.close()

def server_thread():
    player_id = 0
    while player_id < 2:
        conn, addr = s.accept()
        print(f"Player {player_id + 1} connected from {addr}")
        connections.append(conn)
        threading.Thread(target=handle_client, args=(conn, player_id)).start()
        player_id += 1

threading.Thread(target=server_thread, daemon=True).start()

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = server
        self.port = port
        self.addr = (self.server, self.port)
        self.pos = self.connect()

    def connect(self):
        try:
            self.client.connect(self.addr)
            data = self.client.recv(2048).decode()
            x, y = map(int, data.split(","))
            return [x, y]
        except:
            print("Unable to connect to server.")
            return [0, 0]

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            reply = self.client.recv(2048).decode()
            x, y = map(int, reply.split(","))
            return [x, y]
        except socket.error as e:
            print(e)
            return [0, 0]

pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Online Multiplayer Game")

def redraw_window(win, player, opponent):
    win.fill((255, 255, 255))
    pygame.draw.rect(win, (255, 0, 0), (player[0], player[1], 50, 50))
    pygame.draw.rect(win, (0, 0, 255), (opponent[0], opponent[1], 50, 50))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    n = Network()
    player = n.pos
    opponent = [0, 0]

    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player[0] -= 5
        if keys[pygame.K_RIGHT]:
            player[0] += 5
        if keys[pygame.K_UP]:
            player[1] -= 5
        if keys[pygame.K_DOWN]:
            player[1] += 5

        opponent = n.send(f"{player[0]},{player[1]}")
        redraw_window(win, player, opponent)

    pygame.quit()

main()
