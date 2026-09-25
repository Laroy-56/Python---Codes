import subprocess

try :

    end = subprocess.run(["ifconfg"] , capture_output = True , text = True)

    print(end.stdout)

except FileNotFoundError :

    print("Command Not Found !!!")