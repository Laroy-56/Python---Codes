import socket

ip = input("Enter ip address:  ")

ports = [80, 443, 22, 21, 3589, 53]

for port in ports :

    try :

        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        sock.connect((ip , port ))

        print("TCP connection succeeded on port {port} for ip address {ip} ")

    except:

        print(f"TCP connection rejected on port {port} for ip address {ip} ")

        