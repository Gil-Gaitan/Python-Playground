# Chat Room Application

## Objective

Implement the client and server sides of a chat room application. The client will support functionalities: public messaging (PM) and direct messaging (DM). The server will handle multiple simultaneous client connections using appropriate message formats and multithreading techniques.

## Requirements

- **Language**: Python 3 only.
- **Protocol**: TCP (Transmission Control Protocol).
- **Libraries**: `socket`, `threading`, `json`

## Types of Messages

- **Data/Text Message**: Exchanged between clients (public messages or direct messages).
- **Command Message**: Exchanged between a client and the server.

## Message Encoding

JSON is used to encode the message.

### Encoding Messages with JSON (Example)

**Client-to-Server (Command Message Example)**:

```json
{
    "command": "login",
    "username": "jerry",
    "password": "apassword"
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

message = {...}
encoded_message = json.dumps(message).encode('utf-8')
```

**Decoding a Message**:

```python
received_message = json.loads(encoded_message.decode('utf-8'))
print(received_message['username'])
```

## Chat Protocol

### Client Log In

1. The client connects to the server and sends a login request.
2. The server checks if the username exists. If it’s a new user, the server prompts for a password and registers the user. User data is stored in memory for persistence.
3. Once the client logs in successfully, the server sends the client a list of currently active users.

### Client Sends an Operation Command

After login, the client enters a "prompt user for operation" state and can choose between the following operations:

- **PM**: Public message to all clients.
- **DM**: Direct message to a specific client.
- **EX**: Exit the chat.
- **WHO**: Display users in the room

### Keeping the Client Updated with Active Users

- **On Login and Logout**: The server sends an updated list of active users when a client logs in or out.

## Operations

### PM (Public Message)

1. The client sends a **PM** operation to broadcast a message to all active clients.
2. The server sends an acknowledgment, receives the message, and broadcasts it to all other clients using the JSON-encoded message format.

### DM (Direct Message)

1. The client sends a **DM** operation to message a specific client.
2. The server provides a list of active users at login. The client selects a target user and sends the message.
3. The server forwards the message to the target user and sends a confirmation to the sender.

### EX (Exit)

1. The client sends an **EX** operation to close the connection.
2. The server updates its list of active clients and closes the connection. The server notifies other clients of the updated list of active users.

### WHO (Who's On)

1. The client sends a **WHO** operation to request the list of currently active users.
2. The server responds with a JSON-encoded message containing the list of active users.
3. The client displays the list of active users to the user.

## Multithreading

- **Server-Side**: Server uses multithreading to handle multiple clients concurrently. Each client connection is managed by a separate thread.
- **Client-Side**: Client uses multithreading to handle both user input (PM, DM, EX) and incoming server messages concurrently.

## Technical Instructions

### Client-Side

- The client prompts the user for an operation (PM, DM, EX, WHO) and handles sending messages to the server.
- Two threads are created:
  - **Input Handling Thread**: Handles user input to send messages.
  - **Listening Thread**: Listens for incoming messages from the server, including broadcast messages, direct messages, and updates on active users.

### Server-Side

- The server listens for incoming connections and assigns each client connection to a separate thread for handling communication.
- The server maintains a list of active clients and forwards messages appropriately. When a client logs in or out, the server updates all connected clients with the current list of active users.

---

### Key Functionalities

- **Login**: After the client connects, they can log in by providing a username and password. The server checks for the username and either registers or authenticates the user.
- **Public Messaging**: After logging in, the client can send a message that is broadcast to all other connected clients.
- **Direct Messaging**: The client can send a direct message to another specific user by selecting a recipient from the list of active users.
- **Exit**: Clients can send an exit command to disconnect. When a client exits, the server updates the list of active users and notifies all other clients.
- **Who**: The client can request a list of currently active users in the chat room. This operation helps the user identify who is available for communication.
- **Error Handling**: The server and client handle errors for situations such as network issues, invalid user inputs such as a DM to a user not in the room, and connection problems. If the server goes down, users are notified and it doesn't crash the client.
