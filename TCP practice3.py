import socket

targets = ["192.168.1.1" , "10.1.0.1" , "172.16.50.1"]

ports = [80 , 443 , 21 , 22 , 139 , 3589 ]

for target in targets:

    for port in ports :

        try :

            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

            sock.connect((target , port))

            print(f"TCP connection succeeded for target {target} on port {port}")

        except :

            print(f"TCP connection rejected for target {target} on port {port}")