import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# MUST match the Server's IP and Port
HOST_NAME = '127.0.0.1'
PORT = 12345

s.connect((HOST_NAME,PORT))
while(True):
    message = s.recv(50)
    print(message.decode('utf-8'))

    message_to_sender = input("Client:")
    s.send(bytes(message_to_sender,"utf-8"))

s.close()