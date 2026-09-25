import subprocess

try :

    output = subprocess.run(["ipconfig"] , shell = True , capture_output = True , text = True )

    print(output.stdout)

except FileNotFoundError :

    print("command Not Found ")