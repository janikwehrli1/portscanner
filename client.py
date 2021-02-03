import socket

SRV_ADDR = input("Server IP Addresse: ")
SRV_PORT = int(input("Server Port: "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SRV_ADDR, SRV_PORT))

data = input("Nachricht: ")

s.sendall(data.encode())