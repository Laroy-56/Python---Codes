import subprocess


ip = input("Enter IP address:   ")


output = subprocess.run(["nmap" ,"-sn" ,  "-sV" , "-sC" ,  ip] , capture_output = True , text = True )


print(output.stdout)