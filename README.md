# argus-dvr-traversal

# Argus Surveillance DVR 4.0.0.0 - Directory Traversal Exploit

## Description
This script exploits a directory traversal vulnerability in Argus Surveillance DVR 4.0.0.0. The vulnerability allows an attacker to access arbitrary files on the server by manipulating the URL.

## Requirements
- Python 3.x
- `requests` library

## Installation
1. **Clone the repository or download the script:**

    ```sh
    git clone https://github.com/yourusername/argus-dvr-traversal.git
    cd argus-dvr-traversal
    ```

2. **Install the `requests` library if not already installed:**

    ```sh
    pip install requests
    ```

## Usage
1. **Run the script with the following command:**

    ```sh
    python3 test.py <TARGET_IP> <TARGET_PORT> <TARGET_FILE>
    ```

    - `<TARGET_IP>`: The IP address of the target DVR.
    - `<TARGET_PORT>`: The port on which the DVR's web interface is running (typically 80 or 8080).
    - `<TARGET_FILE>`: The file you want to access on the target system.

2. **Example:**

    ```sh
    python3 test.py 192.168.1.100 8080 /etc/passwd
    ```

    This command attempts to retrieve the `/etc/passwd` file from the DVR at `192.168.1.100` on port `80`.

## How It Works
The script constructs a URL with the directory traversal payload and sends an HTTP GET request to the target DVR. If the request is successful, the content of the targeted file is displayed.
