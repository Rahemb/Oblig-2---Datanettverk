from socket import *

serverName = "10.0.0.2"  
serverPort = 6789  # Same port as the web server

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))  # Connect to server

request = "GET /index.html HTTP/1.1\r\nHost: localhost\r\n\r\n"
clientSocket.send(request.encode())  # Send request

response = clientSocket.recv(4096)  # Receive response
print("Server response:\n", response.decode())  # Print response

clientSocket.close()  # Close connection
