import threading
import socket
import json


# Handle receiving messages from the server
def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024).decode("utf-8")
            if message:
                message_data = json.loads(message)
                if message_data["type"] == "broadcast":
                    print(f"\n{message_data['from']} says: {message_data['message']}")
                elif message_data["type"] == "direct_message":
                    print(
                        f"\nDirect message from {message_data['from']}: {message_data['message']}"
                    )
                elif message_data["type"] == "update_users":
                    # Print the active users on a new line and then bring back the input prompt
                    print(f"\nActive users: {', '.join(message_data['users'])}")
                    print("Choose command (PM/DM/EX/WHO): ", end="", flush=True)
                elif message_data["type"] == "confirmation":
                    print(f"\n{message_data['message']}")
                elif message_data["type"] == "active_users":
                    # Print the active users list with a proper line break
                    print(
                        f"\nCurrent active users on the server: {', '.join(message_data['users'])}"
                    )
                    print("Choose command (PM/DM/EX/WHO): ", end="", flush=True)
            else:
                break
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

    # Exit the client after disconnection
    exit(0)


# Handle sending messages from user input to server
def send_messages(sock):
    while True:
        try:
            # Get the command
            command = input("Choose command (PM/DM/EX/WHO): ").strip().upper()

            # Handle different commands
            if command == "PM":
                message = input("Enter message to send to everyone: ")
                msg_data = {"command": "PM", "message": message}
                sock.send(json.dumps(msg_data).encode("utf-8"))
            elif command == "DM":
                to_user = input("Enter the username to send a message to: ")
                message = input("Enter your message: ")
                msg_data = {"command": "DM", "to": to_user, "message": message}
                sock.send(json.dumps(msg_data).encode("utf-8"))
            elif command == "EX":
                msg_data = {"command": "EX"}
                sock.send(json.dumps(msg_data).encode("utf-8"))
                break
            elif command == "WHO":
                msg_data = {"command": "WHO"}
                sock.send(json.dumps(msg_data).encode("utf-8"))
        # Handle exceptions
        except Exception as e:
            print(f"Error sending message: {e}")
            print("Server may have disconnected. Exiting client...")
            break

    # Exit client after disconnection
    exit(0)


# Running the client
def run_client(server_ip, server_port):
    try:
        # Create and connect the socket
        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_sock.connect((server_ip, server_port))
    except (socket.error, ConnectionRefusedError) as e:
        print(f"Unable to connect to the server at {server_ip}:{server_port}.")
        print(f"Error: {e}")
        return

    # Login prompt for client
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    login_data = {"command": "login", "username": username, "password": password}
    try:
        client_sock.send(json.dumps(login_data).encode("utf-8"))
    except Exception as e:
        print(f"Error sending login data: {e}")
        return

    # Start threads for receiving and sending
    receive_thread = threading.Thread(target=receive_messages, args=(client_sock,))
    send_thread = threading.Thread(target=send_messages, args=(client_sock,))

    receive_thread.start()
    send_thread.start()

    receive_thread.join()
    send_thread.join()


# Run the client, default is localhost:12345
if __name__ == "__main__":
    run_client("127.0.0.1", 12345)
