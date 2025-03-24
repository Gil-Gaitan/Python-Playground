# **Client README**

## **How to Run**

1. Ensure the **server** is running. You cannot run the client without the server.
2. Clone or download the project files.
3. Navigate to the directory containing the `client.py` file in your terminal or command prompt.
4. Run the client with the following command:

   ```bash
   python3 client.py
   ```

## **How to Use the Chat Room Program**

Once the client program starts, follow the on-screen instructions to interact with the chat room:

1. **Login**:
   - Upon starting the client, you'll be prompted to enter a **username** and **password**.
   - If you are logging in for the first time, the server will register you. If your username already exists, you will be authenticated.

2. **Select Command**: After logging in, you'll be prompted to select an action by entering a command:

   - **PM (Public Message)**:
     - Type **PM** to send a message to all active users.
     - You'll be prompted to enter the message, and it will be broadcast to everyone connected to the chat room.

   - **DM (Direct Message)**:
     - Type **DM** to send a private message to a specific user.
     - You'll be prompted to enter the recipient’s username and the message to send to them.

   - **WHO (Active Users)**:
     - Type **WHO** to request the list of active users currently connected to the server.
     - The server will respond with a list of usernames.

   - **EX (Exit)**:
     - Type **EX** to disconnect from the server and close the connection.
     - The server will be notified, and the client will terminate.

3. **Receiving Messages**:
   - While you are using the client, incoming messages (public or direct messages) from other users will be displayed in real-time.
   - The client automatically handles incoming messages and updates, so you can focus on sending messages without worrying about incoming data.

4. **Logout**:
   - Once you choose to exit by typing **EX**, you will be logged out, and the client will disconnect from the server.

## **Example Interaction**

- **Login Prompt**:

  ```bash
  Enter your username: hannah
  Enter your password: securepassword
  ```

- **Command Prompt**:

  ```bash
  Choose command (PM/DM/EX/WHO): PM
  Enter message to send to everyone: Hello, everyone!
  ```

- **Active Users**:

  ```bash
  Choose command (PM/DM/EX/WHO): WHO
  Current active users on the server: hannah, jerry, alex
  ```

- **Exit**:

  ```bash
  Choose command (PM/DM/EX/WHO): EX
  ```

## **Troubleshooting**

- Ensure the **server** is running and accessible. If the client cannot connect, check the server logs for issues.
- If you encounter any issues with the client, make sure the correct host and port are being used for the connection.

Sure! Here is the section on **Instructions on testing multiple clients** that you can add to your README:

---

## Instructions on Testing Multiple Clients

To test the functionality of the chat room application with multiple clients, follow these steps:

### 1. Start the Server

- Open a terminal and navigate to the directory where the server file is located.
- Run the server by executing the following command:

```bash
python server.py
```

- The server will start listening on the specified IP address and port (default: `127.0.0.1:12345`).

### 2. Start Multiple Clients

- Open multiple terminal windows (or tabs) to simulate multiple clients.
- In each terminal window, run the client script by executing the following command:

```bash
python client.py
```

- The client will prompt for a username and password. Enter a different username in each terminal window to simulate different users.
  
### 3. Perform Operations

Once the clients are running and connected to the server, you can perform various operations:

- **Public Messaging (PM)**: One client can send a public message to all connected clients. All clients will see the message.
- **Direct Messaging (DM)**: A client can send a direct message (DM) to another specific client by providing their username.
- **Who (WHO)**: A client can check the list of active users in the chat room by typing `WHO`. This will display the usernames of all clients currently logged in.
- **Exit (EX)**: A client can exit the chat by typing `EX`. This will close their connection, and the server will update other clients with the list of active users.

### 4. Testing Error Handling

- **Disconnected Clients**: Simulate network issues by closing one of the client terminals or disconnecting a client. The other clients should receive a message indicating that the client has disconnected.
- **Invalid Commands**: Try sending invalid commands such as a direct message to a user that is not online. The client should receive an error message indicating that the recipient is not available.
- **Server Shutdown**: Test server crash recovery by stopping the server (Ctrl + C) and attempting to send messages from any connected client. The client should display an error indicating the server is no longer available.
