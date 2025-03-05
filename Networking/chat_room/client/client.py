import threading
import sys
from socket import *


def receive_messages(sock):
    """Continuously receives messages from the server."""
    while True:
        try:
            message = sock.recv(1024).decode()
            if not message:
                break
            print(message)
        except (ConnectionError, OSError):
            print("\n[Client] Connection lost. Exiting...")
            break
    sock.close()  # Ensure socket is closed when the receiving thread exits
    sys.exit(0)  # Exit the program


def send_messages(sock):
    """Continuously sends user input messages to the server."""
    while True:
        try:
            message = input()
            if message.lower() == "exit":
                sock.send("/exit".encode())  # Notify server
                break
            sock.send(message.encode())
        except (ConnectionError, OSError):
            break
    sock.close()
    sys.exit(0)  # Ensure the program exits cleanly


def run_client(server_name, server_port):
    """Connects to the server and starts send/receive threads."""
    try:
        client_sock = socket(AF_INET, SOCK_STREAM)
        client_sock.connect((server_name, server_port))
    except (ConnectionError, OSError):
        print("[Client] Unable to connect to the server.")
        sys.exit(1)

    # Start threads for sending/receiving messages
    threading.Thread(target=receive_messages, args=(client_sock,), daemon=True).start()
    send_messages(client_sock)  # Runs in the main thread


if __name__ == "__main__":
    server_name = sys.argv[1] if len(sys.argv) > 1 else "localhost"
    server_port = int(sys.argv[2]) if len(sys.argv) > 2 else 12345
    run_client(server_name, server_port)
