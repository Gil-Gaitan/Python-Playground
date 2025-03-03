# Online Chat Room Application

## Objective

Implement the client and server sides of an "online chat room" application. The client will support two main functionalities: public messaging and direct messaging. The server should handle multiple simultaneous client connections using appropriate message formats and multithreading techniques.

## Requirements

- **Language**: Python 3 only.
- **Protocol**: TCP (Transmission Control Protocol).

## Type of Messages

- **Data Message**: Exchanged between clients (public messages or direct messages).
- **Command Message**: Exchanged between a client and the server (login, logout, and messaging commands).

## Message Encoding

You can use either JSON or XML to encode the message format. JSON is recommended for its lightweight, human-readable format and strong support in Python.

### Encoding Messages with JSON (Example)

**Client-to-Server (Command Message Example)**:

```json
{
    "command": "login",
    "username": "alice",
    "password": "securepassword"
}
```

**Server-to-Client (Broadcast Message Example)**:

```json
{
     "type": "broadcast",
     "from": "bob",
     "message": "Hello, everyone!"
}
```

### Encoding and Decoding in Python

**Encoding a Message**:

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

**Decoding a Message**:

```python
received_message = json.loads(encoded_message.decode('utf-8'))
print(received_message['username'])  # Output: alice
```

## Online Chat Room Protocol

### Client Logs In

1. The client connects to the server and sends a login request using the encoded message format.
2. The server checks if the username exists. If it’s a new user, the server prompts for a password and registers the user. Credentials should be stored in a file.
3. Once the client logs in successfully, the server sends the client a list of currently active users.

### Client Sends an Operation Command

After login, the client enters a "prompt user for operation" state and chooses between the following operations:

- **PM**: Public message to all clients.
- **DM**: Direct message to a specific client.
- **EX**: Exit the chat.

### Keeping the Client Updated with Active Users

- **On Login and Logout**: The server sends an updated list of active users to all connected clients whenever a client logs in or logs out.
- **Periodic Updates**: The server could also send an updated list of active users at regular intervals (e.g., every 30 seconds).

## Operations

### PM (Public Message)

1. The client sends a PM operation to broadcast a message to all active clients.
2. The server sends an acknowledgment, receives the message, and broadcasts it to all other clients using the JSON-encoded message format.

### DM (Direct Message)

1. The client sends a DM operation to message a specific client.
2. The server provides a list of active users at login. The client selects a target user and sends the message.
3. The server forwards the message to the target user and sends a confirmation to the sender.

### EX (Exit)

1. The client sends an EX operation to close the connection.
2. The server updates its list of active clients and closes the connection. The server notifies other clients of the updated list of active users.

## Multithreading

- **Server-Side**: The server must use multithreading to handle multiple clients concurrently.
- **Client-Side**: The client must use multithreading to handle both user input and incoming server messages concurrently.

## Technical Instructions

### Client-Side

- The client program should prompt the user for an operation (PM, DM, EX) and handle sending messages to the server.
- Create two threads:
  - One thread for handling user input.
  - Another thread for listening to messages from the server.

### Server-Side

- The server should continuously listen for incoming connections.
- Each client connection must be handled by a separate thread to allow simultaneous communication.
- The server must maintain a list of active clients and forward messages appropriately. When a client logs in, logs out, or when there is any change in the list of active users, the server must notify all connected clients.
