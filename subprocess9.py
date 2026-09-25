import subprocess

command = input("Enter Command:    ")

try :

    output = subprocess.run([command] , shell = True , capture_output = True , text = True)

    print("Output")

    print(output.stdout)

    print("returncode")

    print(output.returncode)

except FileNotFoundError:

    print("Command Not Found !!!")