# Exercise 1: Using os.system
import subprocess
import os

print("ls")
os.system("ls")

# os.system("clear")
# print("ls -ltr")
# os.system("ls -ltr")

# Exercise 2: Using subprocess.run
subprocess.run("clear")
print("the ls in subprocess method")
subprocess.run(["ls"])


# Exercise 3: Using subprocess.run with two arguments
subprocess.run("clear")
subprocess.run(["ls", "-l"])


# Exercise 4: Using subprocess.run with three arguments
subprocess.run("clear")
subprocess.run(["ls", "-l", "README.md"])


# Exercise 5: Retrieving system information
subprocess.run("clear")
command = "uname"
commandArgument = "-a"
print(
    f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command, commandArgument])


# Exercise 6: Retrieving information about disk space
subprocess.run("clear")
command = "ps"
commandArgument = "-x"
print(
    f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command, commandArgument])
