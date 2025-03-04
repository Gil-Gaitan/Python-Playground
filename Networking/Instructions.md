# Online Chat Room Project Instructions

## Objective

Implement an "online chat room" application consisting of both client and server components. The client supports public and direct messaging, while the server manages multiple simultaneous connections. The communication between the client and server will use TCP and an appropriate message format (JSON or XML). Multithreading will be required to handle concurrent tasks efficiently.

## Requirements

### Language

- Python 3 only.

### Protocol

- TCP (Transmission Control Protocol).

### Message Types

1. **Data Messages**: Exchanged between clients (public and direct messages).
2. **Command Messages**: Exchanged between a client and the server (e.g., login, logout, and messaging commands).

### Message Encoding (JSON Recommended)

#### Client-to-Server Command Example

```json
{
  "command": "login",
  "username": "alice",
  "password": "securepassword"
}
```

#### Server-to-Client Broadcast Example

```json
{
   "type": "broadcast",
   "from": "bob",
   "message": "Hello, everyone!"
}
```

### Encoding and Decoding JSON in Python

#### Encoding a Message

```python
import json
message = {
    "type": "command",
    "command": "login",
    "username": "alice",
    "password": "securepassword"
}
encoded_message = json.dumps(message).encode('utf-8')
```

#### Decoding a Message

```python
received_message = json.loads(encoded_message.decode('utf-8'))
print(received_message['username'])  # Output: alice
```

## Online Chat Room Protocol

### Client Logs In

- The client connects to the server and sends a login request.
- The server checks if the username exists. If not, it prompts for a password and registers the user.
- Credentials are stored in a file.
- The server responds with a list of currently active users.

### Client Operations

1. **PM (Public Message)**: Broadcasts a message to all active users.
2. **DM (Direct Message)**: Sends a private message to a specific user.
3. **EX (Exit)**: Logs the user out and updates the list of active users.

### Keeping Clients Updated

- On login and logout, the server sends an updated list of active users.
- Optionally, periodic updates (e.g., every 30 seconds) can be sent to ensure an up-to-date list.

## Multithreading

### Server-Side Multithreading

- The server must handle multiple clients concurrently.
- Each client connection runs on a separate thread.

#### Example

```python
import threading
import sys
from socket import *

def handle_client(client_sock, addr):
    print(f"Connection established with {addr}")
    try:
        while True:
            message = client_sock.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Received from {addr}: {message}")
            client_sock.send(f"Echo: {message}".encode())
    except ConnectionError:
        pass
    finally:
        print(f"Closing connection to {addr}")
        client_sock.close()

def run_server(port_number):
    server_sock = socket(AF_INET, SOCK_STREAM)
    server_sock.bind(('', port_number))
    server_sock.listen(100)
    print(f"Server listening on port {port_number}")

    while True:
        client_sock, addr = server_sock.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_sock, addr))
        client_thread.start()
        print(f"Started thread for {addr}")
```

### Client-Side Multithreading

- The client must handle both user input and incoming server messages concurrently.
- Two threads:
  1. **Receiving messages** from the server.
  2. **Sending user input** to the server.

Example

```python
import threading
import sys
from socket import *

def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024).decode('utf-8')
            if message:
                print(f"Message from server: {message}")
            else:
                break
        except ConnectionError:
            break

def send_messages(sock):
    while True:
        message = input("Enter message: ")
        if message.lower() == 'exit':
            sock.close()
            break
        try:
            sock.send(message.encode())
        except ConnectionError:
            break

def run_client(server_name, server_port):
    client_sock = socket(AF_INET, SOCK_STREAM)
    client_sock.connect((server_name, server_port))
    
    receive_thread = threading.Thread(target=receive_messages, args=(client_sock,))
    send_thread = threading.Thread(target=send_messages, args=(client_sock,))
    
    receive_thread.start()
    send_thread.start()
    
    receive_thread.join()
    send_thread.join()
    
    print("Client connection closed.")
```

## Submission Requirements

### Directory Structure

- `client/` (contains client code and `README.txt`)
- `server/` (contains server code and `README.txt`)

### README.txt Requirements

- How to install dependencies (`requirements.txt` encouraged).
- Instructions to run the server and client.
- How to test multiple clients.

## Evaluation Criteria (100 Points)

1. **Server Implementation (30 points)**: Proper handling of multiple clients using multithreading.
2. **Client Implementation (30 points)**: Handles user input and incoming messages using multithreading.
3. **Chat Protocol (20 points)**: Correct implementation of PM, DM, and EX operations.
4. **Error Handling (10 points)**: Handles disconnected clients and invalid input.
5. **Documentation (10 points)**: Clear README.txt and well-commented code.

## Conclusion

By following these instructions, you will implement a robust online chat room with client-server communication using TCP and multithreading. Proper handling of concurrent connections ensures a responsive and scalable application.
