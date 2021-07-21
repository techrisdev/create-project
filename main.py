import os
from github import Github

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

# Create a README file
os.system("touch " + directory + "/README.md")

# Create the remote repository on Github
# Get the access token
file = open("access_token.txt")
token = file.read()[:-1]

github = Github(token)
github.get_user().create_repo(project_name)

# Create a local git repository and push to the remote repository
username = github.get_user().login
os.system("cd " + directory + "; git init; git branch -M main; git add .; git commit -m 'Initial Commit'; git remote add origin https://github.com/" + username + "/" + project_name + ".git; git push -u origin main")
