import os
import requests
from github import Github

# Initialize GitHub API with your personal access token
token = 'token'  # Replace with your GitHub personal access token
g = Github(token)

# Path to your local template README file
readme_file_path = '/mnt/c/Users/barro/GitHub/danielbarroso/README.md'  # Replace with the correct path to your template README file

# Get the content of your template README
with open(readme_file_path, 'r') as file:
    template_readme = file.read()

# Get the user object for the 'barroso2223' GitHub account
user = g.get_user('barroso2223')

# Iterate through all your repositories and update the README
for repo in user.get_repos():
    try:
        # Check if the repository already has a README
        contents = repo.get_contents("README.md")
        # Update the README
        repo.update_file(contents.path, "Update README", template_readme, contents.sha)
        print(f"Updated README in {repo.name}")
    except Exception as e:
        # If the repository doesn't have a README, create one
        repo.create_file("README.md", "Add README", template_readme)
        print(f"Created README in {repo.name}")
