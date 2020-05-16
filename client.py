#NAME: VIDISHA NARENDRA SHETTY        UTA ID: 1001672826
#Cite 1: https://github.com/suziesu/Computer-Networking/tree/master/assignment1 
#Cite 2: https://www.geeksforgeeks.org/socket-programming-multi-threading-python/
#Cite 3: https://www.bogotobogo.com/python/python_network_programming_server_client_file_transfer.php
from socket import *                  # Import socket module
from urllib.request import localhost
import time

serverSocket = socket(AF_INET,SOCK_STREAM)            # Create a socket object
host = localhost    								# Get local machine name
port = 8080          						          # Reserve a port for your service.

serverSocket.connect(('localhost', 8080))
data = ('GET /Test.html HTTP/1.1')
serverSocket.sendall(data.encode())

while True:
        
        d = serverSocket.recv(1024)
        print('file received=', d)
        if not d:
            break										# write data to a file

print('Received file')
serverSocket.close()
