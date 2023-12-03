#Create a client to interact with local host server
import socket
HOST="localhost"
PORT=5000
BUFSIZE=1024
ADDRESS=(HOST,PORT)
client = socket.socket()
client.connect(ADDRESS)
print(client.recv(BUFSIZE).decode())

while True:
    #Loop to chat with server
    reply=(client.recv(BUFSIZE)).decode()
    if not reply:
        print("Server disconnected ")
        break
    else:
        print(reply)
    message=input(">")
    client.send(message.encode())

client.close()
