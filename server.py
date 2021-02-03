import socket

SRV_ADDR = input("Server IP Addresse: ")
SRV_PORT = int(input("Server Port: "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SRV_ADDR, SRV_PORT))
s.listen(1)

connection, address = s.accept()

while 1:
    data = connection.recv(1024)
    if not data: break
    connection.sendall(b"message received")
    print(data.decode("utf-8"))
connection.close()