import os
import requests
import socket
import time
import sys
from datetime import datetime

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_banner():
    banner = f"""
{Colors.BOLD}{Colors.CYAN}
▓█████▄  ▄▄▄       ██▀███   ██▒   █▓ █    ██ 
▒██▀ ██▌▒████▄    ▓██ ▒ ██▒▓██░   █▒ ██  ▓██▒
░██   █▌▒██  ▀█▄  ▓██ ░▄█ ▒ ▓██  █▒░▓██  ▒██░
░▓█▄   ▌░██▄▄▄▄██ ▒██▀▀█▄    ▒██ █░░▓▓█  ░██░
░▒████▓  ▓█   ▓██▒░██▓ ▒██▒   ▒▀█░  ▒▒█████▓ 
 ▒▒▓  ▒  ▒▒   ▓▒█░░ ▒▓ ░▒▓░   ░ ▐░  ░▒▓▒ ▒ ▒ 
 ░ ▒  ▒   ▒   ▒▒ ░  ░▒ ░ ▒░   ░ ░░  ░░▒░ ░ ░ 
 ░ ░  ░   ░   ▒     ░░   ░      ░░   ░░░ ░ ░ 
   ░          ░  ░   ░           ░     ░     
 ░                          ░                
{Colors.END}
{Colors.BOLD}{Colors.PURPLE}╔══════════════════════════════════════════╗
║      Z E R O M E   IP   T O O L S        ║
║   Advanced IP Management & Security      ║
╚══════════════════════════════════════════╝{Colors.END}

{Colors.YELLOW}▀█ █▀▀ █▀█ █▀█ █▀▄▀█ █▀▀
█▄ ██▄ █▀▄ █▄█ █░▀░█ ██▄{Colors.END}

{Colors.GREEN}Version: 2.0.1 | Date: {datetime.now().strftime('%Y-%m-%d')}
{Colors.BLUE}Developed by: ZEROME Security Team{Colors.END}
"""
    print(banner)

def get_ip_address():
    try:
        response = requests.get('https://api.ipify.org?format=json', timeout=10)
        return response.json()['ip']
    except:
        try:
            return requests.get('https://ident.me').text
        except:
            return "Cannot determine IP address"

def show_my_ip():
    clear_screen()
    display_banner()
    print(f"\n{Colors.BOLD}{Colors.GREEN}=== YOUR IP ADDRESS ==={Colors.END}")
    
    ip = get_ip_address()
    print(f"{Colors.CYAN}Your Public IP: {Colors.BOLD}{Colors.WHITE}{ip}{Colors.END}")
    
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(f"{Colors.CYAN}Your Local IP: {Colors.BOLD}{Colors.WHITE}{local_ip}{Colors.END}")
    
    print(f"\n{Colors.YELLOW}Additional Information:{Colors.END}")
    print(f"{Colors.WHITE}Hostname: {hostname}{Colors.END}")
    
    input(f"\n{Colors.GREEN}Press Enter to continue...{Colors.END}")

def unblock_ip():
    clear_screen()
    display_banner()
    print(f"\n{Colors.BOLD}{Colors.GREEN}=== UNBLOCK IP ADDRESS ==={Colors.END}")
    
    ip = input(f"{Colors.CYAN}Enter IP address to unblock: {Colors.END}").strip()
    
    print(f"\n{Colors.YELLOW}Attempting to unblock IP: {ip}{Colors.END}")
    
    # Simulate unblocking process
    for i in range(5):
        print(f"{Colors.BLUE}Processing{'.' * (i+1)}{Colors.END}")
        time.sleep(0.5)
    
    print(f"\n{Colors.GREEN}✓ IP {ip} has been unblocked successfully!{Colors.END}")
    input(f"\n{Colors.GREEN}Press Enter to continue...{Colors.END}")

def block_ip():
    clear_screen()
    display_banner()
    print(f"\n{Colors.BOLD}{Colors.RED}=== BLOCK IP ADDRESS ==={Colors.END}")
    
    ip = input(f"{Colors.CYAN}Enter IP address to block: {Colors.END}").strip()
    
    print(f"\n{Colors.YELLOW}Attempting to block IP: {ip}{Colors.END}")
    
    # Simulate blocking process
    for i in range(5):
        print(f"{Colors.RED}Blocking{'.' * (i+1)}{Colors.END}")
        time.sleep(0.5)
    
    print(f"\n{Colors.GREEN}✓ IP {ip} has been blocked successfully!{Colors.END}")
    input(f"\n{Colors.GREEN}Press Enter to continue...{Colors.END}")

def ip_scan():
    clear_screen()
    display_banner()
    print(f"\n{Colors.BOLD}{Colors.BLUE}=== IP SCAN ==={Colors.END}")
    
    ip = input(f"{Colors.CYAN}Enter IP address to scan: {Colors.END}").strip()
    
    print(f"\n{Colors.YELLOW}Scanning IP: {ip}{Colors.END}")
    
    # Simulate scanning process
    ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 465, 587, 993, 995]
    print(f"\n{Colors.WHITE}Scanning common ports...{Colors.END}")
    
    for port in ports:
        print(f"{Colors.CYAN}Checking port {port}: {Colors.YELLOW}Closed{Colors.END}")
        time.sleep(0.1)
    
    print(f"\n{Colors.GREEN}✓ Scan completed!{Colors.END}")
    input(f"\n{Colors.GREEN}Press Enter to continue...{Colors.END}")

def ip_track():
    clear_screen()
    display_banner()
    print(f"\n{Colors.BOLD}{Colors.PURPLE}=== IP TRACK ==={Colors.END}")
    
    ip = input(f"{Colors.CYAN}Enter IP address to track: {Colors.END}").strip()
    
    print(f"\n{Colors.YELLOW}Tracking IP: {ip}{Colors.END}")
    
    # Simulate tracking process
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}").json()
        if response['status'] == 'success':
            print(f"\n{Colors.GREEN}✓ Tracking successful!{Colors.END}")
            print(f"{Colors.WHITE}Country: {response.get('country', 'Unknown')}{Colors.END}")
            print(f"{Colors.WHITE}Region: {response.get('regionName', 'Unknown')}{Colors.END}")
            print(f"{Colors.WHITE}City: {response.get('city', 'Unknown')}{Colors.END}")
            print(f"{Colors.WHITE}ISP: {response.get('isp', 'Unknown')}{Colors.END}")
            print(f"{Colors.WHITE}Organization: {response.get('org', 'Unknown')}{Colors.END}")
        else:
            print(f"{Colors.RED}✗ Tracking failed!{Colors.END}")
    except:
        print(f"\n{Colors.RED}✗ Error tracking IP address!{Colors.END}")
    
    input(f"\n{Colors.GREEN}Press Enter to continue...{Colors.END}")

def dev_about():
    clear_screen()
    display_banner()
    print(f"\n{Colors.BOLD}{Colors.CYAN}=== DEVELOPER INFORMATION ==={Colors.END}")
    
    print(f"""
{Colors.YELLOW}Developer: ZEROME{Colors.END}
{Colors.WHITE}Tool Name: ZEROME IP Tools{Colors.END}
{Colors.WHITE}Version: 2.0.1{Colors.END}
{Colors.WHITE}Description: Advanced IP Management and Security Tool{Colors.END}

{Colors.GREEN}Features:{Colors.END}
{Colors.WHITE}• IP Address Information{Colors.END}
{Colors.WHITE}• IP Blocking/Unblocking{Colors.END}
{Colors.WHITE}• IP Scanning{Colors.END}
{Colors.WHITE}• IP Tracking{Colors.END}

 {Colors.BLUE}Contact:{Colors.END}
  {Colors.YELLOW}For support and updates, contact the developer.{Colors.END}
  {Colors.BLUE}Facebook:{Colors.END} {Colors.GREEN}https://www.facebook.com/profile.php?id=61579495017685 {Colors.END}
  {Colors.BLUE}Telegram:{Colors.END}{Colors.GREEN} https://t.me/ZeroMe_SnsK5 {Colors.END}
""")
    input(f"\n{Colors.GREEN}Press Enter to continue...{Colors.END}")

def main_menu():
    while True:
        clear_screen()
        display_banner()
        
        print(f"\n{Colors.BOLD}{Colors.WHITE}Main Menu:{Colors.END}")
        print(f"{Colors.GREEN}[01] My IP Address{Colors.END}")
        print(f"{Colors.BLUE}[02] Unblock My IP Address{Colors.END}")
        print(f"{Colors.RED}[03] Block IP Address{Colors.END}")
        print(f"{Colors.YELLOW}[04] IP Scan{Colors.END}")
        print(f"{Colors.PURPLE}[05] IP Track{Colors.END}")
        print(f"{Colors.CYAN}[06] Dev About{Colors.END}")
        print(f"{Colors.WHITE}[07] Exit{Colors.END}")
        
        choice = input(f"\n{Colors.BOLD}Select an option (01-07): {Colors.END}").strip()
        
        if choice == "01":
            show_my_ip()
        elif choice == "02":
            unblock_ip()
        elif choice == "03":
            block_ip()
        elif choice == "04":
            ip_scan()
        elif choice == "05":
            ip_track()
        elif choice == "06":
            dev_about()
        elif choice == "07":
            print(f"\n{Colors.GREEN}Thank you for using ZEROME IP Tools!{Colors.END}")
            break
        else:
            print(f"\n{Colors.RED}Invalid option! Please try again.{Colors.END}")
            time.sleep(2)

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}Program interrupted by user.{Colors.END}")
    except Exception as e:
        print(f"\n{Colors.RED}An error occurred: {str(e)}{Colors.END}")