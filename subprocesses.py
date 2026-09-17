import subprocess

result = subprocess.run(["ipconfig"] , capture_output = True , text = True)

print(result.stdout)