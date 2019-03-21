import socket

server = socket.socket()
server.bind(('localhost', 9000))
server.listen(10)

client_sock, client_inet_addr = server.accept()


#print("client is joined, his inet address is: ",  client_inet_addr)

while True:
    data_from_client = client_sock.recv(1024)
    if not data_from_client:
        break
    client_sock.send("Joined to server...".encode())

server.close()