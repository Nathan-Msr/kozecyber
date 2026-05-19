import os
import sys
import time
import app

# Colors
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
CYAN = "\033[1;36m"
WHITE = "\033[1;37m"
RESET = "\033[0m"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_banner():
    # ASCII Art
    ascii_art = f"""{GREEN}
  __  __         _______          _     
 |  \/  |       |__   __|        | |    
 | \  / |_   _     | | ___   ___ | |___ 
 | |\/| | | | |    | |/ _ \ / _ \| / __|
 | |  | | |_| |    | | (_) | (_) | \__ \\
 |_|  |_|\__, |    |_|\___/ \___/|_|___/
          __/ |                         
         |___/                          
{WHITE}               Version 1.0
{RESET}"""
    print(ascii_art)
    print(f"{GREEN}[+] Tool Created by n4than the dz{RESET}\n")

def draw_menu():
    print(f"{CYAN}  .:. Select an option from the menu .:.{RESET}\n")
    
    # 3-column layout similar to the image
    print(f"  {RED}[01]{YELLOW} IP Scanner       {RED}[11]{YELLOW} Tool 11          {RED}[21]{YELLOW} Tool 21")
    print(f"  {RED}[02]{YELLOW} Tool 2           {RED}[12]{YELLOW} Tool 12          {RED}[22]{YELLOW} Tool 22")
    print(f"  {RED}[03]{YELLOW} Tool 3           {RED}[13]{YELLOW} Tool 13          {RED}[23]{YELLOW} Tool 23")
    print(f"  {RED}[04]{YELLOW} Tool 4           {RED}[14]{YELLOW} Tool 14          {RED}[24]{YELLOW} Tool 24")
    print(f"  {RED}[05]{YELLOW} Tool 5           {RED}[15]{YELLOW} Tool 15          {RED}[25]{YELLOW} Tool 25")
    print(f"  {RED}[06]{YELLOW} Tool 6           {RED}[16]{YELLOW} Tool 16          {RED}[26]{YELLOW} Tool 26")
    print(f"  {RED}[07]{YELLOW} Tool 7           {RED}[17]{YELLOW} Tool 17          {RED}[27]{YELLOW} Tool 27")
    print(f"  {RED}[08]{YELLOW} Tool 8           {RED}[18]{YELLOW} Tool 18          {RED}[28]{YELLOW} Tool 28")
    print(f"  {RED}[09]{YELLOW} Tool 9           {RED}[19]{YELLOW} Tool 19          {RED}[29]{YELLOW} Tool 29")
    print(f"  {RED}[10]{YELLOW} Tool 10          {RED}[20]{YELLOW} Tool 20          {RED}[x]{YELLOW} Exit\n")

def main():
    if sys.platform == "win32":
        os.system("") # Enable ANSI colors in Windows terminal
        os.system("title My Tools Menu")
        
    while True:
        clear_screen()
        draw_banner()
        draw_menu()
        
        choice = input(f"{GREEN} manso@terminal-dz {WHITE}~$ {RESET}")
        
        if choice in ['1', '01']:
            clear_screen()
            print(f"{GREEN}[+] Launching IP Scanner...{RESET}\n")
            # Run the IP scanner app directly from the module
            app.main()
        elif choice.lower() == 'x':
            print(f"\n{RED}[!] Exiting...{RESET}")
            break
        else:
            print(f"\n{RED}[!] Invalid option or Tool not implemented yet.{RESET}")
            time.sleep(1.5)

if __name__ == "__main__":
    main()
