from socket import *
import argparse

# Parser for kommandolinjeargumenter
parser = argparse.ArgumentParser(description='Simple HTTP Client')
parser.add_argument('-i', '--ip', required=True, help='Server IP address')
parser.add_argument('-p', '--port', type=int, required=True, help='Server port number')
parser.add_argument('-f', '--file', required=True, help='File to request (e.g., index.html)')
args = parser.parse_args()

# Opprette TCP socket
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((args.ip, args.port))

# Lage og sende HTTP GET-forespørsel
request = f"GET /{args.file} HTTP/1.1\r\nHost: {args.ip}\r\n\r\n"
clientSocket.send(request.encode())

# Motta og vise respons
response = clientSocket.recv(4096)
print("Server response:\n", response.decode())

clientSocket.close()
