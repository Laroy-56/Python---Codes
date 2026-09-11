def port_scanner(): 

        import socket

        ip = input("Enter ip address:  ")

        ports = [80, 443, 22, 21, 3589, 53]

        for port in ports :

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            sock.settimeout(0.5)

            result = sock.connect_ex((ip , port ))

            if result == 0 :

                print(f"port {port} is open for ip address {ip} ")

            else:

                print(f"port {port} is closed for ip address {ip} ")

        sock.close()

port_scanner()