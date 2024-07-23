import requests
import subprocess
import os

# Current version of the program
CURRENT_VERSION = "1.0"  # Replace with the current version of your program

# Name of the repository directory
REPO_DIR = "<repository>"

# Username of the repository
USER_GIT = "<username>"

# Specifies the URL of the GitHub API to get the releases
GITHUB_API_URL = f"https://api.github.com/repos/{USER_GIT}/{REPO_DIR}/releases/latest"


# Specifies the Access Token
GITHUB_TOKEN = "<token>"

# If you prefer to put the token in system variables you can use this string
# GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

def get_latest_release():
    try:
        headers = {'Authorization': f'token {GITHUB_TOKEN}'} if GITHUB_TOKEN else {}
        response = requests.get(GITHUB_API_URL, headers=headers)
        response.raise_for_status() 
        latest_release = response.json()
        latest_version = latest_release["tag_name"].strip('v') 
        return latest_version
    except requests.RequestException as e:
        print(f"Error when checking version: {e}")
        return None

def prompt_for_update():
    response = input("A new version of the program is available. Do you want to upgrade? (y/n): ")
    return response.lower() == 'y'

def clone_or_pull_repo():
    try:
        if GITHUB_TOKEN:
            # Constructs the URL for the private repository with authentication
            repo_url = f"https://{GITHUB_TOKEN}:x-oauth-basic@github.com/{USER_GIT}/{REPO_DIR}.git"
        else:
            # Use public URL if token is not set
            repo_url = f"https://github.com/{USER_GIT}/{REPO_DIR}.git"
        
        if os.path.isdir(REPO_DIR):
            subprocess.run(["git", "-C", REPO_DIR, "pull", repo_url, "main"], check=True)
        else:
            subprocess.run(["git", "clone", repo_url], check=True)
        
        print("The updated version has been installed in the directory of this file!")
    except subprocess.CalledProcessError as e:
        print(f"Error while updating the program: {e}")

def main():
    latest_version = get_latest_release()
    if latest_version:
        if CURRENT_VERSION < latest_version:
            print(f"A new version is available: {latest_version}. Your current version is: {CURRENT_VERSION}.")
            if prompt_for_update():
                clone_or_pull_repo()
                return
        else:
            print("The program version is updated.")
    else:
        print("Unable to determine the latest version available.")

    # Enter the rest of your program below
    print("Program execution...")

if __name__ == "__main__":
    main()
