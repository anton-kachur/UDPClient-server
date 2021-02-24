import socket
import sys

serverIP = sys.argv[1]
serverPort = int(sys.argv[2])
bufferSize = 1024


def print_address_and_port():
    print("Client IP address: {}".format(address))


serverSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
serverSocket.bind((serverIP, serverPort))
print("UDPServer is up...")

while True:
    bytesAddressPair = serverSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    print("\nReceived from client: {}".format(message))
    print_address_and_port()

    serverSocket.sendto(str.encode((message.decode()).upper()), address)
