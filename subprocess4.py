import subprocess

targets = ["10.1.0.1" , "192.168.1.1" , "172.16.81.1"]

for target in targets:

    output = subprocess.run(["nmap" , "-sn" , "-sV" , "-sC" , target] , capture_output = True , text = True)

    print(output.stdout)