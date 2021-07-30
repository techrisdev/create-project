import os
import subprocess
from github import Github

print("What kind of Project do you want to create?")
print("0: Empty (default)")
print("1: Flutter")
print("2: Rust")
kind = input("Number: ")

if not kind == '1' and not kind == '2':
    # Create an empty project by default
    kind = '0'

project_name = input("Name of your Project: ")
projects_directory = "$HOME/dev/Projects/"
directory = projects_directory + project_name

if kind == '0':
    # Create the directory in $HOME/dev/Projects
    os.system("mkdir -p " + directory + "/src")
elif kind == "1":
    # Run flutter create
    os.system("cd " + projects_directory + "; flutter create " + project_name)
elif kind == "2":
    # Run cargo new
    os.system("cd " + projects_directory + "; cargo new " + project_name)
    
# Create a README file
os.system("touch " + directory + "/README.md")

# Create the remote repository on Github
# Get the access token
file = open(os.getenv("HOME") + "/.bin/create-project_access_token.txt")
token = file.read()[:-1]

private = input("Should the Github Repository be private (0 yes, default): ")
if private == 1:
    private = False
else:
    private = True

github = Github(token)
github.get_user().create_repo(project_name, private=private)

# Create a local git repository and push to the remote repository
username = github.get_user().login
os.system("cd " + directory + "; git init; git branch -M main; git add .; git commit -m 'Initial Commit'; git remote add origin https://github.com/" + username + "/" + project_name + ".git; git push -u origin main")
