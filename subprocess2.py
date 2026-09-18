import subprocess

ip = input("Enter IP address:   ")

output = subprocess.run(["ping" , ip] , capture_output = True , text = True )

print(output.stdout)