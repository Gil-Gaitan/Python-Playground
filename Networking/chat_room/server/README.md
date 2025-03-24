# **Server README**

## **Objective**

The server program listens for incoming client connections and handles multiple clients concurrently using multithreading. It manages user logins, broadcasts public messages, handles direct messages, and updates clients with the current list of active users.

## **Features**

- Handle multiple client connections simultaneously
- Manage user logins and registration
- Broadcast public messages (PM) to all clients
- Forward direct messages (DM) to the target client
- Update clients with a list of active users
- Handle client disconnections and exit commands (EX)

## **How to Run**

1. Ensure Python 3 is installed.
2. Clone or download the project files.
3. Navigate to the directory containing the `server.py` file in your terminal or command prompt.
4. Run the server with the following command:

   ```bash
   python3 server.py
   ```

5. The server will start listening for incoming client connections on the default host (`127.0.0.1`) and port (`12345`).

## **How to Designate a Specific Port**

By default, the server listens on port `12345`, but if you'd like to designate a different port for the server, you can easily change this by modifying the code.

1. Open the `server.py` file.
2. Find the following line of code where the server is set to listen on a specific port:

   ```python
   run_server("127.0.0.1", 12345)
   ```

3. Change `12345` to any port number you want. For example, if you want the server to listen on port `8080`, modify it like so:

   ```python
   run_server("127.0.0.1", 8080)
   ```

4. Save the changes and run the server again:

   ```bash
   python server.py
   ```

This will start the server on the newly designated port. Ensure that the client is also configured to connect to the same port.

## **Troubleshooting**

1. **Cannot Connect to the Server**:
   - **Issue**: The client cannot connect to the server.
   - **Solution**: Make sure the server is running. If it is running on a non-default port, verify that the client is trying to connect to the correct port. You can update the client's connection settings by modifying the `server_ip` and `server_port` in the `client.py` file.

2. **Port Already in Use**:
   - **Issue**: When trying to run the server, you receive an error like "Address already in use."
   - **Solution**: Choose a different port by following the instructions above to change the port in `server.py`.
