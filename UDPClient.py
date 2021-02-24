import socket
import sys
# -*- coding: UTF-8 -*-

serverIP = sys.argv[1]
serverPort = int(sys.argv[2])
bufferSize = 1024
choice = ''

serverAddressPort = (serverIP, serverPort)
print("Hello", '\U0001F600')
print("UDP Server IP address: ", serverIP)
print("UDP Server port number: ", serverPort)
clientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

while choice != 'y':
    msg = input("Enter the statement: ")
    bytesToSend = str.encode(msg)

    clientSocket.sendto(bytesToSend, serverAddressPort)
    msgFromServer = clientSocket.recvfrom(bufferSize)

    print("\nReceived from server: {}".format(msgFromServer[0]))
    choice = input("Do you want to exit (y/n)? ")

print("Bye", '\U0001F44B')
clientSocket.close()