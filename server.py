#NAME: VIDISHA NARENDRA SHETTY        UTA ID: 1001672826
#Cite 1: https://github.com/suziesu/Computer-Networking/tree/master/assignment1 
#Cite 2: https://www.geeksforgeeks.org/socket-programming-multi-threading-python/
#Cite 3: https://www.bogotobogo.com/python/python_network_programming_server_client_file_transfer.php
#import socket module
from socket import *
import random
from urllib.request import localhost
import _thread
import webbrowser
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('localhost', 8080))
serverSocket.listen(10)
def serverclient(connectionSocket):
    serverSock2 = socket(AF_INET,SOCK_STREAM)
    port = random.randint(7500,8000)                    # Reserve a port for your service.             
    serverSock2.bind(('localhost', port))
    print('Port used for Multi threading is',port)

#Prepare a sever socket
#Fill in start
#Fill in end
    try:
        message=connectionSocket.recv(1024).decode()        #Message received from client
        print ('Message received: %s' %message)
		#Fill in start #Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()                               
        print('Output data: %s' %outputdata)                #HTML code 
		#Send one HTTP header line into socket
        connectionSocket.send(('HTTP/1.1 200 OK Content-Type: text/html').encode('utf-8'))          #If the file exists
        b = outputdata.encode('utf-8')
        connectionSocket.send(b)
 		#Fill in start
 		#Fill in end
 		#Send the content of the requested file to the client
        #for i in range(0, len(outputdata)):
        #  connectionSocket.send(outputdata[i])
        connectionSocket.close()
        serverSock2.close()
    except IOError:
        #Send response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found Content-Type: text/html")                     #If the file does not exist
 		#Fill in start
 		#Fill in end
 		#Close client socket
        connectionSocket.close()
        serverSock2.close()
 		#Fill in start
 		#Fill in end 
while True:
    #Establish the connection
    print ('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()                                                  #Accepting incoming connections
    print("%s:%s has connected." % addr)
    _thread.start_new_thread(serverclient, (connectionSocket, ))
    #Fill in start #Fill in end
serverSocket.close()
