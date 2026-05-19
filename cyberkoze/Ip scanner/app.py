import socket
import os
import sys

# ASCII color codes
GREEN = "\033[1;32m"
BLUE = "\033[1;34m"
RESET = "\033[0m"

def portScanner(target, port):
    try:
        theSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        theSocket.settimeout(1)
        result = theSocket.connect_ex((target, port))

        if result == 0:
            print(f"Port {port}: {GREEN}open{RESET}.")
        else:
            print(f"Port {port}: {RESET}not open.")
        theSocket.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

def main():
    # Set console title
    os.system("title Linux Terminal - Port Scanner")
    
    # Simple Linux-like prompt header
    user = "manso"
    hostname = "terminal-dz"
    cwd = "~/projet"
    
    print(f"{GREEN}Welcome to Linux Terminal Emulator v1.0{RESET}")
    print("Initializing environment...")
    print(f"{user}@{hostname}:{cwd}$ python3 port_scanner.py")
    print("-" * 40)

    target = input(f"{BLUE}Please enter an IP address to scan: {RESET}")

    print(f"\n{GREEN}[+] Scanning target: {target}{RESET}")
    
    for ports in [21, 22, 80, 443]:
        portScanner(target, ports)
    
    print("-" * 40)
    print(f"{GREEN}Scan complete.{RESET}")
    input(f"\n{GREEN}{user}@{hostname}:{cwd}${RESET} ")

if __name__ == "__main__":
    # Enable ANSI escape sequences on Windows
    if sys.platform == "win32":
        os.system("") 
    main()