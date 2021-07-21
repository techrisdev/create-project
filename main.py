import os

print("What kind of Project do you want to create?")
print("0: Empty (default)")
print("1: Flutter")
kind = input("Number: ")

if not kind == '1':
    # Create an empty project by default
    kind = '0'

project_name = input("Name of your Project: ")

# Create a directory in $HOME/dev/Projects
directory = "$HOME/dev/Projects/" + project_name
os.system("mkdir -p " + directory + "/src")

# Create a local git repository
os.system("cd " + directory + "; git init; git add .; git commit -m 'Initial Commit'")

