from socket import *
import threading  # Import threading module

def handle_client(connectionSocket):
    """Handles a client request in a separate thread."""
    try:
        # Receive HTTP request
        message = connectionSocket.recv(1024).decode()
        if not message:
            return

        # Extract filename from request
        filename = message.split()[1][1:]  # Remove leading "/"
        if filename == "":
            filename = "index.html"  # Default to index.html

        # Read the requested file
        with open(filename, "r") as f:
            outputdata = f.read()

        # Send HTTP response headers
        connectionSocket.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n".encode())
        connectionSocket.send(outputdata.encode())

    except FileNotFoundError:
        # Send 404 Not Found response
        connectionSocket.send("HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n".encode())
        connectionSocket.send("<html><body><h1>404 Not Found</h1></body></html>\r\n".encode())

    finally:
        connectionSocket.close()  # Close the client connection

# Create a TCP server socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
serverPort = 6789  # Choose an available port
serverSocket.bind(("", serverPort))  # Bind the socket to the port
serverSocket.listen(5)  # Listen for incoming connections (up to 5 clients)

print("Multi-threaded server ready to serve on port", serverPort)

while True:
    # Accept an incoming client connection
    connectionSocket, addr = serverSocket.accept()
    print(f"New connection from {addr}")

    # Create a new thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(connectionSocket,))
    client_thread.start()

# Close the server (this will never reach unless exited manually)
serverSocket.close()
