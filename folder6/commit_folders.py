import os
import shutil
import subprocess

# Specify GitHub repository URL
repo_url = "https://github.com/kushwaha-pankaj/LeetCodePush.git"  # Replace with your GitHub repository URL

# Specify local directory where repository will be cloned
local_dir = os.path.dirname(os.path.abspath(__file__))  # Replace with your local directory

# Specify the path to the directory containing 20 folders
folder_dir = os.path.join(local_dir, "LeetCodePush2/")  # Replace with your folder directory

# Clone GitHub repository to local computer
if not os.path.exists(local_dir):
    os.makedirs(local_dir)
os.chdir(local_dir)
subprocess.run(["git", "clone", repo_url])
print("Repository cloned successfully.")

# Get list of folders to push
folders_to_push = [folder for folder in os.listdir(folder_dir) if os.path.isdir(os.path.join(folder_dir, folder))]

# Specify local directory of cloned repository
local_repo_dir = os.path.join(local_dir, "LeetCodePush/")  # Replace with your local repository directory

# Change directory to the cloned repository
os.chdir(local_repo_dir)

# Git commands to add, commit, and push all folders to GitHub
for folder in folders_to_push:
    folder_path = os.path.join(local_repo_dir, folder)
    shutil.copytree(os.path.join(folder_dir, folder), folder_path)
    subprocess.run(["git", "add", folder])
subprocess.run(["git", "commit", "-m", "Add all folders"])
subprocess.run(["git", "push", "origin", "main"])

print("All folders pushed to GitHub successfully.")
