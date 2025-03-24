import threading
import socket
import json
import time

# Store the list of active users
active_users = {}

# Lock to manage access to the active_users dictionary (thread-safe)
active_users_lock = threading.Lock()


# Handle individual client connection
def handle_client(client_sock, addr):
    try:
        print(f"Connection established with {addr}")
        # Receive and process login message
        login_msg = client_sock.recv(1024).decode("utf-8")
        login_data = json.loads(login_msg)

        if login_data["command"] == "login":
            username = login_data["username"]
            # Add the user to active users
            with active_users_lock:
                active_users[username] = client_sock
            print(f"User {username} logged in.")

            # Send active users list to the client
            update_active_users()

            # Listen for messages
            while True:
                message = client_sock.recv(1024).decode("utf-8")
                if message:
                    message_data = json.loads(message)
                    handle_message(message_data, client_sock, username)
                else:
                    break
    except Exception as e:
        print(f"Error handling client {addr}: {e}")
    finally:
        # Remove user from active users on disconnect
        with active_users_lock:
            for username, sock in active_users.items():
                if sock == client_sock:
                    del active_users[username]
                    break
        client_sock.close()
        print(f"Connection closed for {addr}")
        update_active_users()


# Handle received messages
def handle_message(message_data, client_sock, username):
    if message_data["command"] == "PM":
        broadcast_message(message_data, username)
    elif message_data["command"] == "DM":
        send_direct_message(message_data, username)
    elif message_data["command"] == "EX":
        client_sock.close()
    elif message_data["command"] == "WHO":
        send_active_users(client_sock)


# Broadcast message to all clients
def broadcast_message(message_data, from_user):
    message = json.dumps(
        {"type": "broadcast", "from": from_user, "message": message_data["message"]}
    )
    for user, sock in active_users.items():
        if user != from_user:
            sock.send(message.encode("utf-8"))


# Send direct message to a specific user
def send_direct_message(message_data, from_user):
    to_user = message_data["to"]

    # Check if the recipient is active users
    if to_user not in active_users:
        # If the user is not active, send a failure message to the sender
        failure_message = json.dumps(
            {
                "type": "confirmation",
                "message": f"User {to_user} is not currently online.",
            }
        )
        active_users[from_user].send(failure_message.encode("utf-8"))
        return  # Do not proceed with sending the DM

    # If the user is found, send
    message = json.dumps(
        {
            "type": "direct_message",
            "from": from_user,
            "message": message_data["message"],
        }
    )
    active_users[to_user].send(message.encode("utf-8"))

    # Send confirmation to the sender
    confirmation = json.dumps(
        {"type": "confirmation", "message": f"Message sent to {to_user}"}
    )
    active_users[from_user].send(confirmation.encode("utf-8"))


# Update list of active users to all clients
def update_active_users():
    with active_users_lock:
        active_user_list = list(active_users.keys())
    for user, sock in active_users.items():
        active_user_data = json.dumps(
            {"type": "update_users", "users": active_user_list}
        )
        sock.send(active_user_data.encode("utf-8"))


# Send list of active users
def send_active_users(client_sock):
    with active_users_lock:
        active_user_list = list(active_users.keys())
    message = json.dumps({"type": "active_users", "users": active_user_list})
    client_sock.send(message.encode("utf-8"))


# Periodically update the active users list to all clients every 30 seconds
def periodic_active_user_updates():
    while True:
        time.sleep(30)  # Wait for 30 seconds
        update_active_users()  # Send active users list to all clients


# Loop to accept new connections
def run_server(host, port):
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind((host, port))
    server_sock.listen(5)
    print(f"Server listening on {host}:{port}")

    # Start the periodic update thread
    threading.Thread(target=periodic_active_user_updates, daemon=True).start()

    while True:
        client_sock, addr = server_sock.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_sock, addr))
        client_thread.start()


# Start the server, defaults to localhost:12345
if __name__ == "__main__":
    run_server("127.0.0.1", 12345)
