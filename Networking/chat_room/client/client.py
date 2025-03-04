import threading
import sys
from socket import *


def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024).decode()
            if not message:
                break
            print(message)
        except ConnectionError:
            print("Connection lost.")
            break


def send_messages(sock):
    while True:
        message = input()
        if message.lower() == "exit":
            sock.close()
            break
        try:
            sock.send(message.encode())
        except ConnectionError:
            break


def run_client(server_name, server_port):
    client_sock = socket(AF_INET, SOCK_STREAM)
    client_sock.connect((server_name, server_port))

    # Start threads for sending/receiving messages
    threading.Thread(target=receive_messages, args=(client_sock,)).start()
    threading.Thread(target=send_messages, args=(client_sock,)).start()


if __name__ == "__main__":
    server_name = sys.argv[1] if len(sys.argv) > 1 else "localhost"
    server_port = int(sys.argv[2]) if len(sys.argv) > 2 else 12345
    run_client(server_name, server_port)
