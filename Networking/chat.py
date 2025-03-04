# Online Chat Room
# Includes client and server sides
# Main functions: Public Messages and DMs
# Server handles multiple simultaneous client connections
# Use appropriate message message formats, multi-threading, and error handling

# Protocol: TCP

# Types of messages: Data or Commands
# Data: Messages sent between clients - public or direct
# Command Messages: Client to Server
#   - /login <username> : login to the chat server
#   - /logout : logout from the chat server
#   - /msgall <message> : send a message to all users
#   - /msg <username> <message> : send a direct message to a user
#   - /names : list all users currently logged in
#   - /help : list all available commands
#   - /quit : quit the chat server

# Messages are sent in JSON format. Examples in documentation.
