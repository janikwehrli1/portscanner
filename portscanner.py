import socket

target_ip = input("Ziel IP Adresse: ")
portrange = input("Portbereich der gescannt werden soll(zb 1-1024): ")

low_port = int(portrange.split("-")[0])
high_port = int(portrange.split("-")[1])
open_ports = []

print(f"Scanne Ziel Host {target_ip} im Port Bereich {low_port} bis {high_port}")

for i in range(low_port, high_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.1)
    status = s.connect_ex((target_ip, i))
    if status == 0:
        print(f"Port {i}  --- OFFEN")
        open_ports.append(i)
    else:
        print(f"Port {i}  --- GESCHLOSSEN")
s.close()