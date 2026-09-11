import socket

try :

    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    sock.connect(("192.168.1.1" , 80))

    print("Connected!!")

except :

    print("Host seems down!")