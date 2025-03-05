import threading  # Threading for multiple clients
import json  # JSON for user database
import os  # OS for file operations
import sys  # System for command line arguments
from socket import *  # Socket for networking
import hashlib  # Hash passwords for good practice
import time  # Time for sleep, timestamps

USER_DB_FILE = "users.json"
connected_users = {}  # Tracks active users {username: client_socket}
lock = threading.Lock()  # Prevents race conditions when modifying users


# Load user database
def load_users():
    if os.path.exists(USER_DB_FILE):
        with open(USER_DB_FILE, "r") as f:
            return json.load(f)
    return {}


# Save user database
def save_users(users):
    with open(USER_DB_FILE, "w") as f:
        json.dump(users, f, indent=4)


# Hash password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Send active users list every 5 seconds
def broadcast_user_list():
    while True:
        time.sleep(60)
        with lock:
            if connected_users:
                user_list = (
                    f"\n[Server] Active Users ({len(connected_users)}): "
                    + ", ".join(connected_users.keys())
                )
                for sock in connected_users.values():
                    try:
                        sock.send(user_list.encode())
                    except:
                        pass  # Ignore sending errors


# Handle client login
def handle_login(client_sock):
    users = load_users()

    welcome_message = (
        "\n[Server] Welcome to the chat room!"
        "\n[Server] If you are a returning user, enter your username to log in."
        "\n[Server] If you are a new user, enter a unique username."
        "\n[Server] You can reconnect anytime with the same credentials."
    )
    client_sock.send(welcome_message.encode())

    client_sock.send("\nEnter username: ".encode())
    username = client_sock.recv(1024).decode().strip()

    if username in users:
        client_sock.send("Enter password: ".encode())
        password = client_sock.recv(1024).decode().strip()

        if users[username] == hash_password(password):
            client_sock.send("Login successful! You are now in the chat room.".encode())
            return username
        else:
            client_sock.send("Incorrect password. Connection closed.".encode())
            client_sock.close()
            return None
    else:
        client_sock.send(
            "[Server] You are a new client. Enter a password you can remember: ".encode()
        )
        password = client_sock.recv(1024).decode().strip()
        users[username] = hash_password(password)
        save_users(users)
        client_sock.send(
            "[Server] Registration successful! Welcome to the chat room.".encode()
        )
        return username


# Handle client communication
def handle_client(client_sock, addr):
    print(f"Connection established with {addr}")

    username = handle_login(client_sock)
    if not username:
        return  # End thread if login fails

    with lock:
        connected_users[username] = client_sock

    # Announce new user
    message = f"\n[Server] {username} has joined the chat!"
    with lock:
        for sock in connected_users.values():
            sock.send(message.encode())

    try:
        while True:
            message = client_sock.recv(1024).decode()
            if not message:
                break
            print(f"{username}: {message}")
    except ConnectionError:
        print(f"Connection lost with {username}")
    finally:
        with lock:
            del connected_users[username]

        # Notify others that user left
        message = f"\n[Server] {username} has left the chat."
        with lock:
            for sock in connected_users.values():
                sock.send(message.encode())

        client_sock.close()


# Server setup
def run_server(port_number):
    server_sock = socket(AF_INET, SOCK_STREAM)
    server_sock.bind(("", port_number))
    server_sock.listen(100)
    print(f"Server listening on port {port_number}")

    # Start background thread to broadcast user list
    threading.Thread(target=broadcast_user_list, daemon=True).start()

    while True:
        client_sock, addr = server_sock.accept()
        threading.Thread(target=handle_client, args=(client_sock, addr)).start()


if __name__ == "__main__":
    server_port = int(sys.argv[1]) if len(sys.argv) == 2 else 12345
    run_server(server_port)
