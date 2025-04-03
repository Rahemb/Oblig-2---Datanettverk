import argparse
from socket import *

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Simple HTTP Client")
parser.add_argument("-i", "--ip", required=True, help="Server IP address")
parser.add_argument("-p", "--port", type=int, required=True, help="Server port")
parser.add_argument("-f", "--file", required=True, help="File to request from the server")
args = parser.parse_args()

# Create a TCP socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# Connect to the server using the provided IP and port
clientSocket.connect((args.ip, args.port))

# Send an HTTP GET request for the specified file
request = f"GET /{args.file} HTTP/1.1\r\nHost: {args.ip}\r\n\r\n"
clientSocket.send(request.encode())

# Receive and print the response from the server
response = clientSocket.recv(4096)
print("Server response:\n", response.decode())

# Close the connection
clientSocket.close()
