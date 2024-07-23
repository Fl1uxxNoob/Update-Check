# Update-Check

## Overview

This Python script checks for updates for your program by comparing the current version with the latest release version available on GitHub. If an update is available, it prompts the user to upgrade and handles the cloning or pulling of the latest version from the GitHub repository.


## Features

- Checks the latest release version from a specified GitHub repository.
- Compares the current version of the program with the latest release.
- Prompts the user to update the program if a new version is available.
- Clones the repository if it is not already present or pulls the latest changes if it is.

## Prerequisites

- Python 3.x installed on your machine.
- Git installed on your machine.

## Setup

1. **Clone or Download the Script**
    
    Clone or download the script to your local machine. Navigate to the directory where you want to place the script.

2. **Install Required Python Libraries**

    Ensure you have the `requests` library installed. You can install it using pip:
    ```
    pip install requests
    ```

3. **Setup Version**
    
    The version to be compared with should be entered within the TAG of the relese of the repository file on Github (Example: 1.1)

4. **Configure the Script**

    Open the script in your favorite text editor and make the following modifications:

    - **Set the Current Version**
    
        Update the `CURRENT_VERSION` variable to reflect the current version of your program:
        ```
        CURRENT_VERSION = "1.0"  # Replace with the current version of your program
        ```

    - **Set the Repository Details**
        Replace `<repository>` with the name of your repository and `<username>` with your GitHub username:
        ```
        REPO_DIR = "<repository>"
        USER_GIT = "<username>"
        ```
    
    - **Set the GitHub Access Token**
        Replace `<token>` with your GitHub personal access token:
        ```
        GITHUB_TOKEN = "<token>"
        ```

        If you prefer, you can set the token as an environment variable instead
        ```
        GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
        ```

## Usage

1. **Run the Script**

    Execute the script from the command line:
    ```
    python Update-Check.py
    ```

2. **Check for Updates**

    The script will check for the latest release version on GitHub. If a newer version is available, it will prompt you to update. Follow the on-screen instructions to proceed with updating the program.

## Support
If you want to support this project you can make me a small donation ;) 
https://paypal.me/koyzcairs

## License

    This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details