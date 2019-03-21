import socket

client = socket.socket()
client.connect(('localhost', 9000))
client.send("Hello server!".encode())

data_from_server = client.recv(1024)
client.close()

print(data_from_server)