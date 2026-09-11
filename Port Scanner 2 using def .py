def port_scanner_code():

    import socket # socket module enables the connections

    ip = input("Enter ip address:  ")

    ports = [80, 443, 22, 21]

    for port in ports:

        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        sock.settimeout(0.5)

        result = sock.connect_ex((ip ,  port))

        if result == 0:

            print (f" port {port} is open")

        else:

            print(f"port {port} is closed")

    sock.close

port_scanner_code()
