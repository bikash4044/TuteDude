import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


HOST_NAME = socket.gethostname()
PORT = 12345

s.bind((HOST_NAME,PORT))
s.listen(4)
client, address = s.accept()
while True:
    messsage = input("Server:")
    client.send(bytes("Hey there, whatsup?","utf-8"))
    print("address")
    
client.close()