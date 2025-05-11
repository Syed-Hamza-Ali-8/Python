import socket
import threading
import pickle
import time

SERVER = "0.0.0.0"
PORT = 5555
ADDR = (SERVER, PORT)
MAX_PLAYERS = 10
UPDATE_RATE = 0.03

players = {}
player_id_counter = 0
game_running = True

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    server_socket.bind(ADDR)
except socket.error as e:
    print(f"Socket binding error: {e}")

server_socket.listen(MAX_PLAYERS)
print(f"[SERVER] Started on {SERVER}:{PORT}, waiting for connections...")

def generate_color(player_id):
    colors = [
        (255, 0, 0),    # Red
        (0, 255, 0),    # Green
        (0, 0, 255),    # Blue
        (255, 255, 0),  # Yellow
        (255, 0, 255),  # Purple
        (0, 255, 255),  # Cyan
        (255, 128, 0),  # Orange
        (128, 0, 255),  # Violet
        (255, 0, 128),  # Pink
        (0, 128, 0),    # Dark Green
    ]
    return colors[player_id % len(colors)]

def threaded_client(conn, player_id):
    global players

    start_x, start_y = 100 + (player_id * 20), 100
    player_color = generate_color(player_id)
    players[player_id] = {"x": start_x, "y": start_y, "color": player_color}

    initial_data = {"id": player_id, "game_state": players}
    conn.send(pickle.dumps(initial_data))

    try:
        while game_running:
            try:
                conn.settimeout(5.0)
                data = conn.recv(2048)

                if not data:
                    break

                player_data = pickle.loads(data)
                players[player_id]["x"] = player_data["x"]
                players[player_id]["y"] = player_data["y"]

                conn.send(pickle.dumps(players))

            except socket.timeout:
                conn.send(pickle.dumps({"ping": True}))
            except Exception as e:
                print(f"Error handling client {player_id}: {e}")
                break
    finally:
        print(f"[SERVER] Connection closed for Player {player_id}")
        if player_id in players:
            del players[player_id]
        conn.close()

def broadcast_game_state():
    while game_running:
        time.sleep(UPDATE_RATE)

broadcast_thread = threading.Thread(target=broadcast_game_state)
broadcast_thread.daemon = True
broadcast_thread.start()

try:
    while game_running:
        conn, addr = server_socket.accept()
        print(f"[SERVER] Connected to: {addr}")

        client_thread = threading.Thread(target=threaded_client, args=(conn, player_id_counter))
        client_thread.daemon = True
        client_thread.start()

        player_id_counter += 1
        print(f"[SERVER] Active connections: {threading.active_count() - 2}")

except KeyboardInterrupt:
    print("[SERVER] Server shutting down...")
    game_running = False
finally:
    server_socket.close()